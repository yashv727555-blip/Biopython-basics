from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
dna= Seq("ATCGCAT")
record=SeqRecord(
    dna,
    "Gene1",
    " ",
    "Sample gene sequence"
)
print(record.name)
print(record.description)