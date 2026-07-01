from Bio import SeqIO # parse is used to read multiple sequences 
for record in SeqIO.parse("AZVI.fasta","fasta"):
    print(record.id)
    print(record.description)
    print(len(record))
    print("_"*30)