import zlib
import json
from collections import OrderedDict
from .Color import AverageColor
from pathlib import Path

# Generate a unique identifier for the current sample set
class SamplesFingerprint():
	def __init__(self):
		self.hash = self.create_hash()
		self.memory = f"memory/{self.hash}.json"
		self.created = False

		if(not self.hash_exists()):
			self.save_hash()

	# Checksum by hashing next sample with sum of previous samples
	def create_hash(self):
		samples_hash = "I like coffee" # Initialize with padding
		for i in self.samples_posix:
			seed = str(samples_hash) + str(i)
			samples_hash = zlib.crc32(bytes(seed,encoding="utf8"))
		return samples_hash

	# Test if sample set has been saved
	def hash_exists(self):
		if(self.created or not Path(self.memory).is_file()):
			return False
		
		self.created = True
		return self.created

	# Save identifier of sample set to disk
	def save_hash(self):
		Path(self.memory).touch()

# Load samples from sample set memory file or from samples/ 
class Samples(SamplesFingerprint):
	def __init__(self,samples_path,force = False):
		samples_files = Path(samples_path).glob("*.jpg")
		self.samples_posix = [x for x in samples_files if x.is_file()] # List of PosixPaths
		self.samples = {} # HEX from color calc algorithm

		super(Samples,self).__init__()

		try:
			self.load_sample_set()
		except:
			self.map_color()
			self.save_sample_set()

	# Get the pixel value for each sample using a desired algorithm
	def map_color(self):
		for i,sample in enumerate(self.samples_posix):
			color = AverageColor(sample).hex() # Get the average color of a sample as HEX

			self.samples[color] = i
			print(f"Loaded {i + 1}/{len(self.samples_posix)} samples",end="\r",flush="True")
		print("")

	# Save calculated sample set data
	def save_sample_set(self):
		self.samples = dict(sorted(self.samples.items())) # Sort the dict by chrominance

		with open(self.memory,"w") as f:
			json.dump(self.samples,f)
		print(f"Saved sample set with fingerprint: {self.hash}")

	# Load pre-calulated sample set data
	def load_sample_set(self):
		with open(self.memory) as f:
			self.samples = json.load(f)
		print(f"Loaded {len(self.samples)} samples from set {self.hash}")