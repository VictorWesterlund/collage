import sys
from classes.Samples import Samples
from classes.Collage import Collage

# sys.argv[1] = Input image
# sys.argv[2] = Output image

sample_scale = (20,20)
force = False # Will generate a new sample set every time when true

# Prompt IO declaration if no CLI arguments provided
if(len(sys.argv) < 2):
	sys.argv.insert(1,input("Input image (.jpg):\n"))
	sys.argv.insert(1,input("Output image (.jpg):\n"))

# Load all images from the "samples/" folder
samples = Samples("samples",force)

# Create a collage from the loaded samples
collage = Collage(sys.argv[1],samples)
collage.size = sample_scale
collage.put(sys.argv[2])