from Bio.Blast import NCBIXML
with open("blast_result.xml") as b:
    blast_record=NCBIXML.read(b)

print(len(blast_record.alignments)) #alignment compares query sequence with blast file and gives similarity

first_alignment=blast_record.alignments[0]
print(first_alignment.title)
print(first_alignment.length)
for i in blast_record.alignments:
    print(i.title)