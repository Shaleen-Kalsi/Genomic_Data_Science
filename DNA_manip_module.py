def gc(dna) :
	n = dna.count('n')+dna.count('N')
	gc_percent = (dna.count('g')+dna.count('c'))/len(dna)
	print(gc_percent)
	return gc_percent
#dna = 'acgtcgatgctcgctagctcgatcgctcgatagcatccgccaacacccaccgaagatatatattatatatat'
#gc(dna)
def has_stop(dna, frame=0) :
	"Checks if given dna sseq has an inframe stop codon"
	stop_found = False
	stop_codons = ['tga', 'tag', 'taa']
	print(int(frame))
	for i in range(int(frame),len(dna),3) :
		codon=dna[i:i+3].lower()
		print(codon)
		if codon in stop_codons :
			stop_found = True
			break
	return stop_found

#dna = input('enter')
#frame = input('enter frame')
#if(has_stop(dna, frame)) :
#	print('Has stop codon')
#else :
#	print('No stop codon')
def rev_str(seq) :
	seq = seq[::-1] #reverses the string. str[start:end+1:step]. if step =-1; reversed.
	return seq

def comp(dna) :
	base_comp = {'a': 't', 'g':'c', 't' : 'a', 'c' : 'g'}
	letters = list(dna)
	letters = [base_comp[base] for base in letters]
	return ''.join(letters) #''is the connector
def revcomp(seq) :
	seq = rev_str(seq)
	seq = comp(seq)
	return seq
