from Bio import SeqIO
record=SeqIO.read("keratine.fasta", "fasta")
print(record.id)
print(record.description)
print(record.seq)
print(len(record))