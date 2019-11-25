import dwf
import time
import sys
import random
from mido import MidiFile
from musicConstants import NOTES_FREQ
from midi2Cmd import MidiFileParser
import numpy as np
import matplotlib.pyplot as plt

##
# 
# @description MusicWave for Analog Discovery Device 2, using WaveForm SDK
#
# @author William
# @email china_aisa@live.com
#
# @version 01/17/2019
#
##

# TODO Support more cmdline args for config
midiFileName = sys.argv[1]
logLevel = sys.argv[2].upper() if len(sys.argv) > 2 else 'INFO'


OUTPUT_NODE_TYPE = dwf.DwfAnalogOut.NODE.CARRIER  # Output node type

# Connect to device
print("Connecting to first device found...")
dwf_ao = dwf.DwfAnalogOut()
print("Device connected")

mid = MidiFile(midiFileName)
loader = MidiFileParser(mid, logLevel)

print("Playing: %s" % mid.filename)

"""
# One note
for cmd in loader.play():
	# TODO Set output function
	# cmd['waveFunc']

	dwf_ao.nodeEnableSet(cmd['channel'], OUTPUT_NODE_TYPE, True)				  				# Enable channel note
	dwf_ao.nodeFunctionSet(cmd['channel'], OUTPUT_NODE_TYPE, dwf.DwfAnalogOut.FUNC.SINE)   	# Set output function
	dwf_ao.nodeAmplitudeSet(cmd['channel'], OUTPUT_NODE_TYPE, cmd['amplitude'])  				# Set amplitude: cmd['amplitude']
	dwf_ao.nodeFrequencySet(cmd['channel'], OUTPUT_NODE_TYPE, eval(cmd['frequency']))
	dwf_ao.configure(cmd['channel'], cmd['output'])

"""
waveSum = []
waveData = []
count = 0
# Multi Notes
for cmd in loader.playMultiNote(initialFrequency=1):
	count += 1
	if cmd['channel'] > 2:
		cmd['channel'] = random.randint(0, 1)
	dwf_ao.nodeEnableSet(cmd['channel'], OUTPUT_NODE_TYPE, True)	
	dwf_ao.nodeFunctionSet(cmd['channel'], OUTPUT_NODE_TYPE, dwf.DwfAnalogOut.FUNC.CUSTOM)		# Set output function
	dwf_ao.nodeAmplitudeSet(cmd['channel'], OUTPUT_NODE_TYPE, cmd['amplitude'] * 0.5)  				# Set amplitude: cmd['amplitude']
	dwf_ao.nodeFrequencySet(cmd['channel'], OUTPUT_NODE_TYPE, cmd['frequency'])
	dwf_ao.nodeDataSet(cmd['channel'], OUTPUT_NODE_TYPE, cmd['data'])
	dwf_ao.configure(cmd['channel'], cmd['output'])
	waveSum.append(cmd['waveSum'])
	waveData = cmd['data']
	if logLevel == 'DEBUG' and count % 100 == 0:
		plt.plot(waveData[8192//2 - 1000 : 8192//2 + 1000])
		plt.show()

if logLevel == 'DEBUG':
	plt.plot(waveData)
	plt.show()

# Release
dwf_ao.close()

