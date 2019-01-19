import dwf
import time
import sys
from mido import MidiFile
from musicConstants import NOTES_FREQ
from midi2Cmd import MidiFileParser

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


OUTPUT_NODE_TYPE = dwf.DwfAnalogOut.NODE.CARRIER  # Output node type

# Connect to device
print("Connecting to first device found...")
dwf_ao = dwf.DwfAnalogOut()
print("Device connected")

mid = MidiFile(midiFileName)
print("Playing: %s" % mid.filename)
loader = MidiFileParser(mid)

for cmd in loader.play():
	"""
	yield {
			'channel': waveChannel,
			'amplitude': waveAmplitude,
			'waveFunc': waveFunc,
			'frequency': noteFrequency,
			'output': noteOutput
		}
	"""
	# TODO Set output function
	# cmd['waveFunc']

	dwf_ao.nodeEnableSet(cmd['channel'], OUTPUT_NODE_TYPE, True)				  				# Enable channel note
	dwf_ao.nodeFunctionSet(cmd['channel'], OUTPUT_NODE_TYPE, dwf.DwfAnalogOut.FUNC.RAMP_UP)   	# Set output function
	dwf_ao.nodeAmplitudeSet(cmd['channel'], OUTPUT_NODE_TYPE, cmd['amplitude'])  				# Set amplitude: cmd['amplitude']
	dwf_ao.nodeFrequencySet(cmd['channel'], OUTPUT_NODE_TYPE, eval(cmd['frequency']))
	dwf_ao.configure(cmd['channel'], cmd['output'])


# Release
dwf_ao.close()
