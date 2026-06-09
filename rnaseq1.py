from Bio.Seq import Seq
m_dna= Seq("ATGCCGTAATGCCATGCATAGTCA")
m_rna=m_dna.transcribe()
print(m_rna)

