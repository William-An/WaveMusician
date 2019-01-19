# Music Wave
Use wave generators to play music

## SCPI
For function generators supporting SCPI commands

## WaveForms
For Analog Discovery 2

### How to (Prototype)
1. Download [WaveForms SDK](https://store.digilentinc.com/waveforms-previously-waveforms-2015/)
1. Clone this repo
1. Go to repo directory and install required packages `pip install -r requirements.txt`
1. `cd WaveForms/`
1. `python WaveForms/main.py DIR_TO_MIDI_FILES`

## TODO
1. [x] Tick support
1. [ ] MIDI support
	1. [x] MIDI File load
		1. Load midi file using mido
		1. Identify [file format](https://www.csie.ntu.edu.tw/~r92092/ref/midi/)
			1. Format 0
			1. Format 1
				If there are more than 2 tracks (one header chunk and one music tracks), prompt warning
			1. Format 2
		1. Parse header
			1. Tick info
			1. Beat info
			1. tempo info
			1. time signature
			1. etc.
		1. Parse music track
			1. Instrument to wave form
			1. Volume control
			1. Note to frequency
			1. Tick to time
	1. [x] Complie waveform from loader
	1. [x] "Run" Music 
		1. Set timer triggers?
		1. Or send real-time  
	1. [ ] Concurrence problem
		1. SuperPosition
	1. Instrument 
		1. Ramp is like trumpet
1. [ ] SCPI support
1. [ ] Command line configuration
1. [x] Load music sheet from files
1. [ ] Create unified interface for WaveForms and SCPI, wrapping the lower level command
	1. [x] MIDI Loader
1. [ ] Package cmd tools
	1. Play from cmd

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