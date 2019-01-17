import dwf
import time
from musicConstants import NOTES_FREQ

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

# TODO Support cmdline args for config
CHANNEL = 0  									  # Wavegenerator output port, default to be ch 1
OUTPUT_WAVE_FUNC = dwf.DwfAnalogOut.FUNC.SINE     # Output wave form, see dwf python wrapper api code for details # https://github.com/amuramatsu/dwf/blob/master/dwf/api.py
OUTPUT_AMPLITUDE = 5  							  # Output wave amplitude, for raising or lowering volume (-5 ~ 5v)
OUTPUT_NODE_TYPE = dwf.DwfAnalogOut.NODE.CARRIER  # Output node type

# Connect to device
print("Connecting to first device found...")
dwf_ao = dwf.DwfAnalogOut()
print("Device connected")

# Initial Configuration of device
dwf_ao.nodeEnableSet(CHANNEL, OUTPUT_NODE_TYPE, True)				  # Enable channel note
dwf_ao.nodeFunctionSet(CHANNEL, OUTPUT_NODE_TYPE, OUTPUT_WAVE_FUNC)   # Set output function
dwf_ao.nodeAmplitudeSet(CHANNEL, OUTPUT_NODE_TYPE, OUTPUT_AMPLITUDE)  # Set amplitude
print("Initial configuration complete")

# Here comes the music part
# TODO Support timing
# TODO Support loading music file
print("Here comes the music part")
musicSheet = [("A4", 1), ("A4", 1), ("E5", 1), ("E5", 1), ("F5", 1), ("F5", 1), ("E5", 2), ("D5", 1), ("D5", 1), ("C5", 1), ("C5", 1), ("B4", 1), ("B4", 1), ("A4", 1)]

for note, step in musicSheet:
	freq = NOTES_FREQ[note]
	dwf_ao.nodeFrequencySet(CHANNEL, OUTPUT_NODE_TYPE, eval(freq))
	dwf_ao.configure(CHANNEL, True)
	# 0.5s
	time.sleep(0.5 * step)

# Release
dwf_ao.close()
