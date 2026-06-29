from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
dna1= Seq("ATGCGT")
dna2= Seq("TTAAGC")
record1= SeqRecord(
    dna1,
    "Gene1",

)
record2= SeqRecord(
    dna2,
    "GeneB"
)
l=[record1,record2]
for i in l:
    print(i.id)