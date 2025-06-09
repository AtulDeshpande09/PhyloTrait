from Bio import AlignIO
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
from Bio import Phylo

aligned_path = "../data/aligned/aligned.fasta"

# Read the aligned FASTA file
alignment = AlignIO.read(aligned_path, "fasta")

# Use identity to compute distances
calculator = DistanceCalculator('identity')
dm = calculator.get_distance(alignment)

# Build tree using NJ 
constructor = DistanceTreeConstructor()
tree = constructor.nj(dm)

tree_path = "../trees/tree.nwk"

# Save tree in Newick format
Phylo.write(tree, tree_path, "newick")

print(f"Tree Generated at path : {tree_path}")

