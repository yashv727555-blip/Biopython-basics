from Bio.Blast import NCBIXML

with open("blast_result.xml") as b:
    blast_record=NCBIXML.read(b)
print(len(blast_record.alignments))

first_alignment=blast_record.alignments[0]
print(len(first_alignment.hsps))
first_hsp=first_alignment.hsps[0]
print(first_hsp.score) #score tells that how good the match is i.e alignment strength
print(first_hsp.expect) #expect tells E value

print("Query sequence")
print(first_hsp.query)

print("Matched sequence")
print(first_hsp.sbjct)

print("Alignment sequence")
print(first_hsp.match)