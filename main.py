from classes.Samples import Samples
from classes.Collage import Collage
from pathlib import Path

force = False
input_path = "input/"

# Load all JPGs from the "samples/" folder
samples = Samples("samples",force)

input_file = str("input/coffee-resized.jpg")

collage = Collage(input_file,samples)
collage.put(input_file + "_collage.jpg")

# input_files = Path(input_path).glob("*.jpg")
# input_files_posix = [x for x in input_files if x.is_file()] # List of PosixPaths

# for input_file in input_files_posix:
# 	input_file = str(input_file)
# 	collage = Collage(input_file,samples)
# 	collage.put(input_file + "_collage.jpg")