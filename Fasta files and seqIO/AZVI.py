from Bio import SeqIO
record=SeqIO.read("AZVI.fasta", "fasta")
print(record.id)
print(len(record))
print(record.seq)
