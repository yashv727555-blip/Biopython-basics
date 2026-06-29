from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
protein_seq=Seq("MLKTV")
protein_record= SeqRecord(
    protein_seq,
     "prot01", #id
    "test Protein", #name
    "Sample Protein seq example" #description

)
print(protein_record.name)
print(protein_record.description)
print(protein_record.id)