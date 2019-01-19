# Music Wave
- Use wave generators to play music
- Currently only support WaveForms devices
- Tested on analog discovery 2

## ~~SCPI~~
For function generators supporting SCPI commands

## WaveForms
For Analog Discovery 2

### How to (Prototype)
1. Download [WaveForms SDK](https://store.digilentinc.com/waveforms-previously-waveforms-2015/)
1. Clone this repo
1. Get some [midi files!](https://musescore.com)
1. Go to repo directory and install required packages `pip install -r requirements.txt`
1. `cd WaveForms/`
1. `python WaveForms/main.py DIR_TO_MIDI_FILES`

## TODO
1. [ ] Package design / Directory Structure
	- Make this a package
	- WaveMusician 
		- resources
			- MIDI Files
			- MusicXML Files
			- MP3 Files
			- Other music format
		- src
			- Loader
				- Abstract Loader
				- MIDI File Loader
				- MusicXML Loader
				- MP3 Loader
				- KeyboardInput Loader
					- Play from keyboard
			- WaveGenerator 
				- Abstract WaveGenerator
					- Unified interface for wave generator
				- (Different kinds of wave generator that implement the api interface, i.e. transform loader info into generator commands)
				- SCPI Devices
				- WaveForms
				- Other wave generator
		- examples
			- Sample code
		- setup.py
		- and other package installation files
1. [ ] Unified note message data structure design
	1. Track message for wave generator
		1. Wave Channel
		1. Wave Function
			1. Wave data, for custom wave
		1. Wave Amplitude
		1. Wave Frequency
		1. Wave Phase
		1. Wave Offset
1. [ ] Multiple Notes Support
	1. Preprocess input track? to calculate custom waves
	1. Real-time solution
		1. Superposition
1. [ ] Instrument Style
	1. Generator waves similar to instrument indicated in music files
1. [ ] Better Command Line Tools
	1. Configuration
	1. File dir

## info
- WaveForms
	- [Python API Wrapper](https://github.com/amuramatsu/dwf)
	- [WaveForms SDK Reference Manual](https://s3-us-west-2.amazonaws.com/digilent/resources/instrumentation/waveforms/waveforms_sdk_rm.pdf)
	- [WaveForms Reference Website](https://reference.digilentinc.com/reference/software/waveforms/waveforms-3/startmu)
- MIDI Python
	- [Mido](https://mido.readthedocs.io/en/latest/message_types.html)
- MIDI Message & File Format 
	- [Message Summary](https://www.midi.org/specifications-old/item/table-1-summary-of-midi-message)
	- [Control Message](https://www.midi.org/specifications-old/item/table-3-control-change-messages-data-bytes-2)
	- [MIDI File Format](https://www.csie.ntu.edu.tw/~r92092/ref/midi/)