import sys
from classes.Samples import Samples
from classes.Collage import Collage
from pathlib import Path

force = False # Will generate a new sample set every time when true

# Prompt IO declaration if no CLI arguments provided
if(len(sys.argv) < 2):
	input_file = input("Input image (.jpg):\n")
	output_file = input("Output image (.jpg):\n")
else:
	input_file = sys.argv[1]
	output_file = sys.argv[2]

# Load all images from the "samples/" folder
samples = Samples("samples",force)

# Create a collage from the loaded samples
collage = Collage(input_file,samples)
collage.put(output_file)