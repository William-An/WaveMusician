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
1. `python WaveForms/main.py`

### info
- [Python API Wrapper](https://github.com/amuramatsu/dwf)
- [WaveForms SDK Reference Manual](https://s3-us-west-2.amazonaws.com/digilent/resources/instrumentation/waveforms/waveforms_sdk_rm.pdf)
- [WaveForms Reference Website](https://reference.digilentinc.com/reference/software/waveforms/waveforms-3/startmu)

## TODO
1. [x] Tick support
1. [ ] SCPI support
1. [ ] Command line configuration
1. [ ] Load music sheet from files
1. [ ] Create unified interface for WaveForms and SCPI, wrapping the lower level command
1. [ ] MIDI support?
1. [ ] Package cmd tools
	1. Play from cmd