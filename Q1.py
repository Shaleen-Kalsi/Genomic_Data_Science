"""Find out what species the DNA sequence came from: Answe is the one with the lowest E value"""
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
fasta_string = 'TGGGCCTCATATTTATCCTATATACCATGTTCGTATGGTGGCGCGATGTTCTACGTGAATCCACGTTCGAAGGACATCATACCAAAGTCGTACAATTAGGACCTCGATATGGTTTTATTCTGTTTATCGTATCGGAGGTTATGTTCTTTTTTGCTCTTTTTCGGGCTTCTTCTCATTCTTCTTTGGCACCTACGGTAGAG'
result_handle = NCBIWWW.qblast("blastn","nt",fasta_string)
#nt: non-redundant nucleotide database
#print out significant matches in a decided format
blast_record = NCBIXML.read(result_handle)
len(blast_record.alignments)
E_VALUE_THRESH = 0.01
for alignment in blast_record.alignments :
	for hsp in alignment.hsps :
		if hsp.expect < E_VALUE_THRESH :
			print("alignment")
			print("sequence:", alignment.title)
			print("length:", alignment.length)
			print("E value", hsp.expect)
			print(hsp.query)
			print(hsp.match)
			print(hsp.sbjct)
