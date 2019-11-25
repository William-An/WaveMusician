import logging
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from mido import MetaMessage
from time import sleep
from math import pi

# TODO Better way to import constants, right now use relative path
from musicConstants import MIDI_NOTE_TO_FREQ

##
# @description Load an external midi file and turn it into frequency series
# 
# @author William
#
##

class MidiFileParser():
	"""
	Parse midi file into generic dictionary objects for wave generator
	"""

	def __init__(self, midiFileObject, logLevel="INFO"):
		self.fmido = midiFileObject;
		fmido = self.fmido

		# Initialiize logger with filename as reference
		self.logger = logging.getLogger(fmido.filename.split('.')[-2])
		self.logger.setLevel(logging.DEBUG)

		# Initialize logging handler and formatter
		ch = logging.StreamHandler()
		formatter = logging.Formatter('%(levelname)s - %(message)s')

		ch.setFormatter(formatter)
		ch.setLevel(getattr(logging, logLevel))

		self.logger.addHandler(ch)
		self.logger.info("Loaded file: %s", fmido.filename)
		self.logger.info("MIDI File format: Format %d" % fmido.type)
		self.logger.info("Total length (s): %d" % fmido.length)
		self.logger.info("Total tracks: %d" % len(fmido.tracks))

		# Read meta info
		headerChunk = fmido.tracks[0]
		self.meta = {}
		for msg in headerChunk:
			self.meta.update(msg.dict())
		# Print out Track info
		self.logger.info("Header Track Name: %s" % headerChunk.name)
		self.logger.info("Music Meter: %d/%d" % (self.meta.get("numerator", 0), self.meta.get("denumerator", 0)))
		self.logger.info("Tempo: %d ms/beat or %d beats/min" % (int(self.meta.get("tempo", 500000) / 1e3), int(60 / (self.meta.get("tempo", 500000) / 1e6))))
		self.logger.debug("Frame_rate: %d" % self.meta.get("Frame_rate",0))
		self.logger.debug("Full meta info: %s" % str(self.meta))

	def play(self):
		# For Format 0 and Format 1 Midi file
		# Initialize wave vars
		waveAmplitude = 1
		waveFunc = 'SINE'
		waveChannel = 0
		noteOutput = True
		noteFrequency = 440

		# For identify whether one note is playing
		# Use note num for identifier
		lastNote = 0

		for msg in self.fmido:
			# Iterate through messages in MidiFile, msg.time is in seconds (adjusted automatically according to beats and ticks)  
			sleep(msg.time)
			# if isinstance(msg, MetaMessage):
			# 	# Skip meta msg
			#	continue
			#else:

			##
			# Meta Message control: end_of_track
			##
			if isinstance(msg, MetaMessage):
				if msg.type == 'end_of_track':
					noteOutput = False

					# Short circuit
					yield {
						'channel': waveChannel,
						'amplitude': waveAmplitude,
						'waveFunc': waveFunc,
						'frequency': noteFrequency,
						'output': noteOutput
					}
					continue
				else:
					continue
				
			# Turn msg into waveform settings
			if msg.channel < 2:
				waveChannel = msg.channel
			else:
				# Channel 3 to 16 are ignored
				continue
			##
			# Configure according to Control msg
			# Only volume is implemented
			#
			# TODO Map instrument to wave functions
			##

			if msg.type == 'control_change' and msg.control == 7:
				# Control 7 is volume control, use amplitude to control volume
				# Message value in range(0, 128)
				waveAmplitude = msg.value / 127
				continue

			##
			# Note control
			#
			# TODO Wave superpostion for more than two notes at the same time
			##

			# TODO Support multiple notes play in the future
			if msg.type == 'note_off' and msg.note == lastNote:
					noteOutput = False
					# TODO Better solution?
					# To save time from query frequency
					yield {
						'channel': waveChannel,
						'amplitude': waveAmplitude,
						'waveFunc': waveFunc,
						'frequency': noteFrequency,
						'output': noteOutput
					}
					continue

			# TODO Add control for velocity
			if msg.type == 'note_on' and msg.velocity != "0":
				noteOutput = True
				# Set note output and frequency
				noteFrequency = MIDI_NOTE_TO_FREQ.get(str(msg.note), 0)

				# Signal occupied wave generator
				lastNote = msg.note

				yield {
					'channel': waveChannel,
					'amplitude': waveAmplitude,
					'waveFunc': waveFunc,
					'frequency': noteFrequency,
					'output': noteOutput
				}

	def playMultiNote(self, initialFrequency=1):
		"""
		Preprocess input file for complex notes
		"""

		# TODO Better loader compatiability

		# Pre-defined Constants
		# TODO Better program design needed
		numOfIntvals = 4096 * 1
		waveAmplitude = 1
		waveFunc = 'CUSTOM'
		waveChannel = 0
		noteOutput = True
		noteFrequency = 440
		noteData = np.zeros(numOfIntvals)
		initialFrequency = initialFrequency
		initialPeriod = 1 / initialFrequency

		# Generate 4096 samples, for AD 2, prototyping purpose
		# Over 4096, data might be corrupted
		timeInterval = np.linspace(0, initialPeriod, numOfIntvals)

		# TODO Better phase track method
		phaseRec = {}

		# Change wave function
		wavefunc = np.sin

		# Noise Cancelling
		NOISE_CANCELLING_DECIMAL = 3
		waveSum = 0



		# The rest is copied from play method for prototyping only
		# TODO Consider merging two methods
		for msg in self.fmido:
			# Iterate through messages in MidiFile, msg.time is in seconds (adjusted automatically according to beats and ticks)  
			self.logger.debug(msg)
			sleep(msg.time)
			# if isinstance(msg, MetaMessage):
			# 	# Skip meta msg
			#	continue
			#else:

			##
			# Meta Message control: end_of_track
			##
			if isinstance(msg, MetaMessage):
				if msg.type == 'end_of_track':
					noteOutput = False
					# Short circuit
					yield {
						'channel': waveChannel,
						'amplitude': waveAmplitude,
						'waveFunc': waveFunc,
						'frequency': initialFrequency,
						'output': noteOutput,
						'data': noteData.tolist(),
						'intval': timeInterval,
						'waveSum': waveSum
					}
					continue
				else:
					continue
				
			# Turn msg into waveform settings
			"""
			if msg.channel < 5:
				waveChannel = msg.channel
			else:
				# Channel 3 to 16 are ignored
				continue
			"""
			##
			# Configure according to Control msg
			# Only volume is implemented
			#
			# TODO Map instrument to wave functions
			##

			if msg.type == 'control_change' and msg.control == 7:
				# Control 7 is volume control, use amplitude to control volume
				# Message value in range(0, 128)
				waveAmplitude = msg.value / 127
				continue

			##
			# Note control
			#
			# NOTE Modified from "play" method
			# 
			# TODO Wave superpostion for more than two notes at the same time
			##


			# Turn off note, set note velocity to 0
			# TODO Phase problem
			if msg.type == 'note_off' or (msg.type == "note_on" and msg.velocity == 0):
				noteOutput = True
				# TODO Better solution?
				# To save time from query frequency

				# Know which note to remove
				# initialFrequency as scaling factor
				noteFrequency = eval(MIDI_NOTE_TO_FREQ.get(str(msg.note), 0))
				phase = phaseRec.pop(msg.note, 0)
				waveRm = wavefunc(2 * pi * noteFrequency * timeInterval - phase)
				waveRm.round(NOISE_CANCELLING_DECIMAL)

				noteData = np.subtract(noteData, waveRm)

				# Simple noise cancelling
				noteData = np.round(noteData, NOISE_CANCELLING_DECIMAL) 
				# noteData = signal.medfilt(noteData, 1)

				waveSum = np.sum(noteData)
				self.logger.debug("Wave Sum: %f", waveSum)

				yield {
					'channel': waveChannel,
					'amplitude': waveAmplitude,
					'waveFunc': waveFunc,
					'frequency': initialFrequency,
					'output': noteOutput,
					'data': noteData.tolist(),
					'intval': timeInterval,
					'waveSum': waveSum
				}
				continue

			if msg.type == 'note_on' and msg.velocity != 0:
				noteOutput = True
				# Set note output and frequency
				# initialFrequency as scaling factor
				noteFrequency = eval(MIDI_NOTE_TO_FREQ.get(str(msg.note), 0))
				deltaTime = msg.time % (1 / noteFrequency)	# The difference of x axis, deltaTime > 0
				
				# phase = round(2 * pi * deltaTime, 3)
				phase = 2 * pi * deltaTime
				# phase = 0 

				phaseRec[msg.note] =  phase

				# NOTE Use sine for prototyping purpose, add instrutment wave in the FUTURE
				wave = wavefunc(2 * pi * noteFrequency * timeInterval - phase)
				wave.round(NOISE_CANCELLING_DECIMAL)

				# Superimpose waves
				noteData = np.add(noteData, wave)
				
				# Simple noise cancelling
				noteData.round(NOISE_CANCELLING_DECIMAL) 
				# noteData = signal.medfilt(noteData, 1)

				# Logging
				waveSum = np.sum(noteData)
				self.logger.debug("Wave Sum: %f", waveSum)

				yield {
					'channel': waveChannel,
					'amplitude': waveAmplitude,
					'waveFunc': waveFunc,
					'frequency': initialFrequency,
					'output': noteOutput,
					'data': noteData.tolist(),
					'intval': timeInterval,
					'waveSum': waveSum
				}

	class WaveFunction():
		"""
		Create custom wave functions
		"""
		def __init__(self):
			self.funcDict = {}

		def addFunc(self, func):
			self.funcList[func.__hash__()] = func

		def call(self, inputs):
			# Tarverse each function
			for func in self.funcList.values():
				results += func(inputs)
			return results

	def playMultiNoteFunction(self, initialFrequency=1):
		"""
		Represent each note play as numpy functions

		"""

		# TODO Better loader compatiability

		# Pre-defined Constants
		# TODO Better program design needed
		waveAmplitude = 1
		waveFunc = 'CUSTOM'
		waveChannel = 0
		noteOutput = True
		noteFrequency = 440
		noteData = np.zeros(4096)
		initialFrequency = initialFrequency
		initialPeriod = 1 / initialFrequency

		playFunction = WaveFunction()

		# Generate 4096 samples, for AD 2, prototyping purpose
		timeInterval = np.linspace(0, initialPeriod, 4096)

		# TODO Better phase track method
		phaseRec = {}



		# The rest is copied from play method for prototyping only
		# TODO Consider merging two methods
		for msg in self.fmido:
			# Iterate through messages in MidiFile, msg.time is in seconds (adjusted automatically according to beats and ticks)  
			sleep(msg.time)
			# if isinstance(msg, MetaMessage):
			# 	# Skip meta msg
			#	continue
			#else:

			##
			# Meta Message control: end_of_track
			##
			if isinstance(msg, MetaMessage):
				if msg.type == 'end_of_track':
					noteOutput = False

					# Short circuit
					yield {
						'channel': waveChannel,
						'amplitude': waveAmplitude,
						'waveFunc': waveFunc,
						'frequency': initialFrequency,
						'output': noteOutput,
						'data': noteData.tolist(),
						'intval': timeInterval
					}
					continue
				else:
					continue
				
			# Turn msg into waveform settings
			if msg.channel < 2:
				waveChannel = msg.channel
			else:
				# Channel 3 to 16 are ignored
				continue
			##
			# Configure according to Control msg
			# Only volume is implemented
			#
			# TODO Map instrument to wave functions
			##

			if msg.type == 'control_change' and msg.control == 7:
				# Control 7 is volume control, use amplitude to control volume
				# Message value in range(0, 128)
				waveAmplitude = msg.value / 127
				continue

			##
			# Note control
			#
			# NOTE Modified from "play" method
			# 
			# TODO Wave superpostion for more than two notes at the same time
			##


			# Turn off note, set note velocity to 0
			# TODO Phase problem
			if msg.type == 'note_off' or (msg.type == "note_on" and msg.velocity == 0):
				noteOutput = True
				# TODO Better solution?
				# To save time from query frequency

				# Know which note to remove
				# initialFrequency as scaling factor

				noteFrequency = eval(MIDI_NOTE_TO_FREQ.get(str(msg.note), 0)) / initialFrequency
				phase = phaseRec.pop(msg.note, 0)
				waveRm = np.sin(2 * pi * noteFrequency * timeInterval - phase)
				waveRm = np.round(waveRm * 100) / 100  # Simple noise cancelling
				noteData = np.subtract(noteData, waveRm)
				noteData = np.round(noteData * 100) / 100  # Simple noise cancelling

				yield {
					'channel': waveChannel,
					'amplitude': waveAmplitude,
					'waveFunc': waveFunc,
					'frequency': initialFrequency,
					'output': noteOutput,
					'data': noteData.tolist(),
					'intval': timeInterval
				}
				continue

			if msg.type == 'note_on' and msg.velocity != 0:
				noteOutput = True
				# Set note output and frequency
				# initialFrequency as scaling factor
				noteFrequency = eval(MIDI_NOTE_TO_FREQ.get(str(msg.note), 0)) / initialFrequency
				deltaTime = msg.time % (1 / noteFrequency)	# The difference of x axis, deltaTime > 0
				
				phase = 2 * pi * noteFrequency
				# phase = 0 

				phaseRec[msg.note] =  phase

				# NOTE Use sine for prototyping purpose, add instrutment wave in the FUTURE
				wave = np.sin(2 * pi * noteFrequency * timeInterval - phase)
				wave = np.round(wave * 100) / 100  # Simple noise cancelling

				# Superimpose waves
				noteData = np.add(noteData, wave)
				noteData = np.round(noteData * 100) / 100  # Simple noise cancelling

				yield {
					'channel': waveChannel,
					'amplitude': waveAmplitude,
					'waveFunc': waveFunc,
					'frequency': initialFrequency,
					'output': noteOutput,
					'data': noteData.tolist(),
					'intval': timeInterval
				}



