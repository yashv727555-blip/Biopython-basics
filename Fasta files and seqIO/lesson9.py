from Bio import SeqIO
record = SeqIO.read("COX1.fasta", "fasta")
print(record.id)
print(record.description)
print(len(record))
print(record.seq)