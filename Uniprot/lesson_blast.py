
from Bio.Blast import NCBIWWW

result_handle= NCBIWWW.qblast( #sending the query sequence to ncbi
    program="blastp",
    database="nr",
    sequence= "MALWMRLLPLLALLALWGPDPAAAFVNQHLCGSHLVEALYLVCGERGFFYTPKTRREAEDLQVGQVELGGGPGAGSLQPLALEGSLQKRGIVEQCCTSICSLYQLENYCN"
)

with open ("blast_result.xml", "w") as b: ## name is given to a new file with file type xml
    b.write(result_handle.read()) #result will be stored in this

print("Blast performed successfuly")


