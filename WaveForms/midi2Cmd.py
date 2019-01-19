import logging
from mido import MetaMessage
from time import sleep

# TODO Better way to import constants, right now use relative path
from musicConstants import MIDI_NOTE_TO_FREQ

##
# @description Load an external midi file and turn it into frequency series
# 
# @author William
#
##

class MidiFileParser():
	def __init__(self, midiFileObject):
		self.fmido = midiFileObject;
		fmido = self.fmido

		# Initialiize logger with filename as reference
		self.logger = logging.getLogger(fmido.filename.split('.')[0])
		self.logger.setLevel(logging.INFO)
		self.logger.info("Loaded file: %s" % fmido.filename)
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
		self.logger.info("Tempo: %d ms/beat or %d beats/min" % (int(self.meta.get("tempo", 0) / 1e3), int(60 / (self.meta.get("tempo", 0) / 1e6))))
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

			if msg.type == 'note_on':
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



