# Define note frequency 
NOTES_FREQ = {
				'C0': '16.35',
				'C#0': '17.32',
				'Db0': '17.32',
				'D0': '18.35',
				'D#0': '19.45',
				'Eb0': '19.45',
				'E0': '20.60',
				'F0': '21.83',
				'F#0': '23.12',
				'Gb0': '23.12',
				'G0': '24.50',
				'G#0': '25.96',
				'Ab0': '25.96',
				'A0': '27.50',
				'A#0': '29.14',
				'Bb0': '29.14',
				'B0': '30.87',
				'C1': '32.70',
				'C#1': '34.65',
				'Db1': '34.65',
				'D1': '36.71',
				'D#1': '38.89',
				'Eb1': '38.89',
				'E1': '41.20',
				'F1': '43.65',
				'F#1': '46.25',
				'Gb1': '46.25',
				'G1': '49.00',
				'G#1': '51.91',
				'Ab1': '51.91',
				'A1': '55.00',
				'A#1': '58.27',
				'Bb1': '58.27',
				'B1': '61.74',
				'C2': '65.41',
				'C#2': '69.30',
				'Db2': '69.30',
				'D2': '73.42',
				'D#2': '77.78',
				'Eb2': '77.78',
				'E2': '82.41',
				'F2': '87.31',
				'F#2': '92.50',
				'Gb2': '92.50',
				'G2': '98.00',
				'G#2': '103.83',
				'Ab2': '103.83',
				'A2': '110.00',
				'A#2': '116.54',
				'Bb2': '116.54',
				'B2': '123.47',
				'C3': '130.81',
				'C#3': '138.59',
				'Db3': '138.59',
				'D3': '146.83',
				'D#3': '155.56',
				'Eb3': '155.56',
				'E3': '164.81',
				'F3': '174.61',
				'F#3': '185.00',
				'Gb3': '185.00',
				'G3': '196.00',
				'G#3': '207.65',
				'Ab3': '207.65',
				'A3': '220.00',
				'A#3': '233.08',
				'Bb3': '233.08',
				'B3': '246.94',
				'C4': '261.63',
				'C#4': '277.18',
				'Db4': '277.18',
				'D4': '293.66',
				'D#4': '311.13',
				'Eb4': '311.13',
				'E4': '329.63',
				'F4': '349.23',
				'F#4': '369.99',
				'Gb4': '369.99',
				'G4': '392.00',
				'G#4': '415.30',
				'Ab4': '415.30',
				'A4': '440.00',
				'A#4': '466.16',
				'Bb4': '466.16',
				'B4': '493.88',
				'C5': '523.25',
				'C#5': '554.37',
				'Db5': '554.37',
				'D5': '587.33',
				'D#5': '622.25',
				'Eb5': '622.25',
				'E5': '659.25',
				'F5': '698.46',
				'F#5': '739.99',
				'Gb5': '739.99',
				'G5': '783.99',
				'G#5': '830.61',
				'Ab5': '830.61',
				'A5': '880.00',
				'A#5': '932.33',
				'Bb5': '932.33',
				'B5': '987.77',
				'C6': '1046.50',
				'C#6': '1108.73',
				'Db6': '1108.73',
				'D6': '1174.66',
				'D#6': '1244.51',
				'Eb6': '1244.51',
				'E6': '1318.51',
				'F6': '1396.91',
				'F#6': '1479.98',
				'Gb6': '1479.98',
				'G6': '1567.98',
				'G#6': '1661.22',
				'Ab6': '1661.22',
				'A6': '1760.00',
				'A#6': '1864.66',
				'Bb6': '1864.66',
				'B6': '1975.53',
				'C7': '2093.00',
				'C#7': '2217.46',
				'Db7': '2217.46',
				'D7': '2349.32',
				'D#7': '2489.02',
				'Eb7': '2489.02',
				'E7': '2637.02',
				'F7': '2793.83',
				'F#7': '2959.96',
				'Gb7': '2959.96',
				'G7': '3135.96',
				'G#7': '3322.44',
				'Ab7': '3322.44',
				'A7': '3520.00',
				'A#7': '3729.31',
				'Bb7': '3729.31',
				'B7': '3951.07',
				'C8': '4186.01',
				'C#8': '4434.92',
				'Db8': '4434.92',
				'D8': '4698.63',
				'D#8': '4978.03',
				'Eb8': '4978.03',
				'E8': '5274.04',
				'F8': '5587.65',
				'F#8': '5919.91',
				'Gb8': '5919.91',
				'G8': '6271.93',
				'G#8': '6644.88',
				'Ab8': '6644.88',
				'A8': '7040.00',
				'A#8': '7458.62',
				'Bb8': '7458.62',
				'B8': '7902.13',
				'N0': '0'
}

MIDI_NOTE_TO_FREQ = {
					'21': '27.5',
					'22': '29.1',
					'23': '30.9',
					'24': '32.7',
					'25': '34.6',
					'26': '36.7',
					'27': '38.9',
					'28': '41.2',
					'29': '43.7',
					'30': '46.2',
					'31': '49.0',
					'32': '51.9',
					'33': '55.0',
					'34': '58.3',
					'35': '61.7',
					'36': '65.4',
					'37': '69.3',
					'38': '73.4',
					'39': '77.8',
					'40': '82.4',
					'41': '87.3',
					'42': '92.5',
					'43': '98.0',
					'44': '103.8',
					'45': '110.0',
					'46': '116.5',
					'47': '123.5',
					'48': '130.8',
					'49': '138.6',
					'50': '146.8',
					'51': '155.6',
					'52': '164.8',
					'53': '174.6',
					'54': '185.0',
					'55': '196.0',
					'56': '207.7',
					'57': '220.0',
					'58': '233.1',
					'59': '246.9',
					'60': '261.6',
					'61': '277.2',
					'62': '293.7',
					'63': '311.1',
					'64': '329.6',
					'65': '349.2',
					'66': '370.0',
					'67': '392.0',
					'68': '415.3',
					'69': '440.0',
					'70': '466.2',
					'71': '493.9',
					'72': '523.3',
					'73': '554.4',
					'74': '587.3',
					'75': '622.3',
					'76': '659.3',
					'77': '698.5',
					'78': '740.0',
					'79': '784.0',
					'80': '830.6',
					'81': '880.0',
					'82': '932.3',
					'83': '987.8',
					'84': '1046.5',
					'85': '1108.7',
					'86': '1174.7',
					'87': '1244.5',
					'88': '1318.5',
					'89': '1396.9',
					'90': '1480.0',
					'91': '1568.0',
					'92': '1661.2',
					'93': '1760.0',
					'94': '1864.7',
					'95': '1975.5',
					'96': '2093.0',
					'97': '2217.5',
					'98': '2349.3',
					'99': '2489.0',
					'100': '2637.0',
					'101': '2793.8',
					'102': '2960.0',
					'103': '3136.0',
					'104': '3322.4',
					'105': '3520.0',
					'106': '3729.3',
					'107': '3951.1',
					'108': '4186.0'
					}