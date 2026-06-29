#seq record is an object that stores a biological sequence along its details like id,name,description
#  in sequencial order
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
dna=Seq("ATGCGT")
record= SeqRecord(
    dna,
    id="Gene1",
    name="Example Gene",
    description="Sample Dna seq for practice"
)
print(record.id)
print(record.name)
print(record.description)
print(dna)
print(record.seq)