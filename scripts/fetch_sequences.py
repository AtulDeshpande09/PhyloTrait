from Bio import SeqIO
from pathlib import Path


input_file = "../data/SILVA_138.2_SSURef_NR99_tax_silva.fasta"
species_file = "../data/species.txt"
output_file = "../data/selected_bacteria.fasta"

with open(species_file , 'r' ) as file:
    species_list = file.read()
    file.close()

species_list = eval(species_list)

records = []

for record in SeqIO.parse(input_file, "fasta"):
    for species in species_list:
        if species.lower() in record.description.lower():
            
            records.append(record)

SeqIO.write(records[:200], output_file , "fasta")
print("FASTA file written Successfully!!!")

