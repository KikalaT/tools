# -*- coding: utf-8 -*-

import re
import itertools

tone_flat = ['C','F','Bb','Eb','Ab','Db','Gb','Cb']
tone_sharp = ['G','D','A','E','B','F_','C_']
pitch_flat = ['Ab','A','Bb','Cb','C','Db','D','Eb','E','F','Gb','G']   
pitch_sharp = ['G_','A','A_','B','C','C_','D','D_','E','F','F_','G']
chord_type = ['6','7','M7','dim7','m6','m7','m7b5','mM7']

C = {}
F = {}
Bb = {}
Eb = {}
Ab = {}
Db = {}
Gb = {}
Cb = {}
G = {}
D = {}
A = {}
E = {}
B = {}
F_ = {}
C_ = {}


C['M7'] = [
	['C3','B3','E4','G4'],
	['C3','G3','B3','E4'],
	['C3','G3','E4','B4'],
	['C3','E3','B3','E4'],
	['E3','B3','C4','G4'],
	['E3','C4','G4','B4'],
	['E3','G3','C4','B4'],
	['G3','C4','E4','B4'],
	['G3','B3','C4','E4'],
	['C4','E4','G4','B4'],
]

C['6'] = [
	['C3','A3','E4','G4'],
	['C3','G3','A3','E4'],
	['C3','G3','E4','A4'],
	['C3','E3','A3','E4'],
	['E3','A3','C4','G4'],
	['E3','G3','C4','A4'],
	['G3','A3','C4','E4'],
	['E3','G3','A3','C4'],
	['C4','E4','G4','A4'],
]

C['m7b5'] = [
	['C3','Bb3','Eb4','Gb4'],
	['C3','Eb3','Bb3','Gb4'],
	['C3','Gb3','Bb3','Eb4'],
	['C3','Gb3','Eb4','Bb4'],
	['C3','Eb4','Gb4','Bb4'],
	['Eb3','Bb3','Gb4','C4'],
	['Eb3','Bb3','C4','Gb4'],
	['Eb3','Gb3','C4','Bb4'],
	['Eb3','C4','Gb4','Bb4'],
	['Gb3','C4','Eb4','Bb4'],
	['Bb2','Gb3','Eb4','C5'],
	['C4','Eb4','Gb4','Bb4'],
	['Bb3','C4','Eb4','Gb4'],
	['Gb3','Bb3','C4','Eb4'],
	['Eb3','Gb3','Bb3','C4'],
]

C['dim7'] = [
	['C3','A3','Eb4','Gb4'],
	['C3','Gb3','Eb4','A4'],
	['C3','Gb3','A3','Eb4'],
	['C3','Eb3','A4','Gb4'],
	['Eb3','C4','Gb4','A4'],
	['Eb3','A4','C4','Gb4'],
	['Eb3','A4','Gb4','C5'],
	['Eb3','A4','C4','Gb4'],
	['Gb3','C4','Eb4','A4'],
	['Gb3','Eb4','A4','C5'],
	['A2','Eb3','C4','Gb4'],
	['A2','Eb3','Gb3','C4'],
	['A4','Gb3','Eb4','C5'],
	['A4','Gb3','C4','Eb4'],
	['C4','Eb4','Gb4','A4'],
	['A4','C4','Eb4','Gb4'],
	['Gb3','A4','C4','Eb4'],
	['Eb3','Gb3','A4','C4'],
]

C['mM7'] = [
	['C3','B3','Eb4','G4'],
	['C3','G3','B3','Eb4'],
	['C3','G3','Eb4','B4'],
	['Eb3','B3','C4','G4'],
	['Eb3','G3','C4','B4'],
	['Eb3','C4','G4','B4'],
	['G3','C4','Eb4','B4'],
	['C4','Eb4','G4','B4'],
	['B3','C4','Eb4','G4'],
	['G3','B3','C4','Eb4'],
]

C['m7'] = [
	['C3','Bb3','Eb4','G4'],
	['C3','G3','Bb3','Eb4'],
	['C3','G3','Eb4','Bb4'],
	['C3','Eb3','Bb3','G4'],
	['Eb3','Bb3','G4','C5'],
	['Eb3','Bb3','C4','Bb3'],
	['Eb3','G3','C4','Bb4'],
	['Eb3','C4','G4','Bb4'],
	['G3','C4','Eb4','Bb4'],
	['Bb3','Eb4','G4','C5'],
	['Bb2','G3','Eb4','C5'],
	['C4','Eb4','G4','Bb4'],
	['Bb3','C4','Eb4','G4'],
	['G3','Bb3','C4','Eb4'],
	['Eb3','G3','Bb3','C4'],
]

C['m6'] = [
	['C3','A3','Eb4','G4'],
	['C3','G3','A3','Eb4'],
	['C3','G3','Eb4','A4'],
	['C3','Eb3','A3','G4'],
	['Eb3','C4','G4','A4'],
	['G3','C4','Eb4','A4'],
	['A2','G3','C4','Eb4'],
	['C4','Eb4','G4','A4'],
	['A3','C4','Eb4','G4'],
	['G3','A3','C4','Eb4'],
	['Eb3','G3','A3','C4'],
]

C['7'] = [
	['C3','Bb3','E4','G4'],
	['C3','G3','Bb3','E4'],
	['C3','G3','E4','Bb4'],
	['C3','E3','Bb3','G4'],
	['E3','Bb3','G4','C5'],
	['E3','Bb3','C4','G4'],
	['E3','G3','C4','Bb4'],
	['E3','C4','G4','Bb4'],
	['G3','C4','E4','Bb4'],
	['Bb3','C4','G4','C5'],
	['Bb2','G3','E4','C4'],
]
	
def transpose(chord,initkey,finalkey):

	note_to_midi_flat = {
	'A0':'21','Bb0':'22','B0':'23','C1':'24','Db1':'25','D1':'26','Eb1':'27','E1':'28','F1':'29','Gb1':'30','G1':'31','Ab1':'32','A1':'33','Bb1':'34','B1':'35','C2':'36','Db2':'37','D2':'38','Eb2':'39','E2':'40','F2':'41','Gb2':'42','G2':'43','Ab2':'44','A2':'45','Bb2':'46','B2':'47','C3':'48','Db3':'49','D3':'50','Eb3':'51','E3':'52','F3':'53','Gb3':'54','G3':'55','Ab3':'56','A3':'57','Bb3':'58','B3':'59','C4':'60','Db4':'61','D4':'62','Eb4':'63','E4':'64','F4':'65','Gb4':'66','G4':'67','Ab4':'68','A4':'69','Bb4':'70','B4':'71','C5':'72','Db5':'73','D5':'74','Eb5':'75','E5':'76','F5':'77','Gb5':'78','G5':'79','Ab5':'80','A5':'81','Bb5':'82','B5':'83','C6':'84','Db6':'85','D6':'86','Eb6':'87','E6':'88','F6':'89','Gb6':'90','G6':'91','Ab6':'92','A6':'93','Bb6':'94','B6':'95','C7':'96','Db7':'97','D7':'98','Eb7':'99','E7':'100','F7':'101','Gb7':'102','G7':'103','Ab7':'104','A7':'105','Bb7':'106','B7':'107','C8':'108',
	}
	midi_to_note_flat = {v:k for k,v in note_to_midi_flat.items()}
	
	note_to_midi_sharp = {
	'A0':'21','A#0':'22','B0':'23','C1':'24','C#1':'25','D1':'26','D#1':'27','E1':'28','F1':'29','F#1':'30','G1':'31','G#1':'32','A1':'33','A#1':'34','B1':'35','C2':'36','C#2':'37','D2':'38','D#2':'39','E2':'40','F2':'41','F#2':'42','G2':'43','G#2':'44','A2':'45','A#2':'46','B2':'47','C3':'48','C#3':'49','D3':'50','D#3':'51','E3':'52','F3':'53','F#3':'54','G3':'55','G#3':'56','A3':'57','A#3':'58','B3':'59','C4':'60','C#4':'61','D4':'62','D#4':'63','E4':'64','F4':'65','F#4':'66','G4':'67','G#4':'68','A4':'69','A#4':'70','B4':'71','C5':'72','C#5':'73','D5':'74','D#5':'75','E5':'76','F5':'77','F#5':'78','G5':'79','G#5':'80','A5':'81','A#5':'82','B5':'83','C6':'84','C#6':'85','D6':'86','D#6':'87','E6':'88','F6':'89','F#6':'90','G6':'91','G#6':'92','A6':'93','A#6':'94','B6':'95','C7':'96','C#7':'97','D7':'98','D#7':'99','E7':'100','F7':'101','F#7':'102','G7':'103','G#7':'104','A7':'105','A#7':'106','B7':'107','C8':'108',
	}
	midi_to_note_sharp = {v:k for k,v in note_to_midi_sharp.items()}
	
	if initkey in tone_flat:
		init = pitch_flat.index(initkey)
	else: 
		init = pitch_sharp.index(initkey)	
	
	if finalkey in tone_flat:
		final = pitch_flat.index(finalkey)
	else:
		final = pitch_sharp.index(finalkey)

	diff = final - init
	
	try:
		if finalkey in tone_flat:
			chord_index = note_to_midi_flat[chord]
		else:
			chord_index = note_to_midi_sharp[chord]
	except KeyError:
		chord_index = note_to_midi_flat[chord]
	
	chord_transposed_index = int(chord_index) + diff
	
	if finalkey in tone_flat:
		chord_transposed = midi_to_note_flat[str(chord_transposed_index)]
	else:
		chord_transposed = midi_to_note_sharp[str(chord_transposed_index)]

	return chord_transposed

#generate all chords
k = ''
for i,j in itertools.product(tone_flat,chord_type):
	k = i
	i = {j:''}
	i[j] = [[transpose(x,'C',k) for x in chord] for chord in C[j]]
	exec(k+'[\''+j+'\']'+'='+str(i[j]))
	
for i,j in itertools.product(tone_sharp,chord_type):
	k = i
	i = {j:''}
	i[j] = [[transpose(x,'C',k) for x in chord] for chord in C[j]]
	exec(k+'[\''+j+'\']'+'='+str(i[j]))

#create input loop, search, display and print results

output = open('results.html','w')
print('<html>',file=output)
print('<head><script src=\'https://unpkg.com/vexflow/releases/vexflow-debug.js\'></script></head>',file=output)
print('<body>',file=output)

query = ''
k=1

while True:
	
	chord_i = []
	chords = []
	chord_progressions = []
	
	print('<h4>',file=output)
	print('<pre>',file=output)
	
	print('entrez un accord:')
	
	query = input()
	query = re.sub('#','_',query)
	query = re.findall(r'(C|F|Bb|Eb|Ab|Db|Gb|Cb|G|D|A|E|B|F_|C_)(6|7|M7|dim7|m6|m7\b|m7b5|mM7)',query)
	
	print('nb d\'accords ('+str(len(query))+'):')
	print('nb d\'accords ('+str(len(query))+'):',file=output)

	for i in range(len(query)):
		chords.append(eval(query[i][0]+'[\''+query[i][1]+'\']'))

	if len(query) <= 4:
		chord_progressions = list(itertools.product(*chords))
		print('nb de progressions ('+str(len(chord_progressions))+')')
		print('nb de progressions ('+str(len(chord_progressions))+')',file=output)
		print('\n', file=output)
		for j in chord_progressions:
			for i in range(len(query)):
				print(query[i][0]+'[\''+query[i][1]+'\'] ', end='', file=output)
			print('\n',file=output)
			print(j, file=output)
			k = str(j)
			k = k.replace(' ','')
			k = k.replace('(','')
			k = k.replace(')','')
			k = k.replace('[','')
			k = k.replace(']','')
			k = k.replace(',','')
			k = k.replace('\'','')
			k = k.replace('#','_')
			print('<div id=\"'+k+'\"></div>',file=output)
			print('<script>',file=output)
			print("""const VF_"""+k+""" = Vex.Flow;
					var vf = new VF_"""+k+""".Factory({renderer: {elementId: '"""+k+"""', height: 300}});
					var score = vf.EasyScore();
					score.set({ time: '5/4' });
					var system = vf.System();
					system.addStave({
					voices: [score.voice(score.notes('""", end='', file=output)
			for z in range(len(j)):
				print('('+str(j[z][2])+' '+str(j[z][3])+')/q ,', end='', file=output)
			print("""')).setStrict(false)]
					}).addClef('treble').addTimeSignature('4/4');
					system.addStave({
					voices: [score.voice(score.notes('""", end='', file=output)
			for z in range(len(j)):
				print('('+str(j[z][0])+' '+str(j[z][1])+')/q ,', end='', file=output)
			print("""',{clef: 'bass'})).setStrict(false)]
					}).addClef('bass').addTimeSignature('4/4');
				system.addConnector()
				vf.draw();""",file=output)
			print('</script>',file=output)
	else:
		print('nombre de possibilités de progressions trop élevé')
		print('maximum = 4 accords')
		print('nombre de possibilités de progressions trop élevé',file=output)
		print('maximum = 4 accords',file=output)
		pass
	print('</pre></h4>',file=output)

#For i range (len(chord)):
	#For x in chord.index(i):
	   #X_midi = note_to_midi(x)
	   #If x_midi < 43 or > 79:
		   #Print('out of range')
		   #Chord.pop(i)
		   #Print('suppress:'+chord.index(i))
	  # Else:
			#Print('range=OK')
