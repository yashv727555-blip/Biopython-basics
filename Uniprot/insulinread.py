from Bio import SeqIO
record=SeqIO.read("insulinprotein.fasta", "fasta")
print(record.id)
print(record.description)
print(len(record.seq))
print(record.seq)