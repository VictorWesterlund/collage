from pathlib import Path

class Samples:
	def __init__(self,samples_path):
		samples_files = Path(samples_path).glob("*.jpg")
		self.samples = [x for x in samples_files if x.is_file()]

		self.hash = self.create_hash()
		self.memory = f"mem/{self.hash}"
	
	# Create hash from sample names and path
	def create_hash(self):
		samples_hash = ""
		for i in self.samples:
			samples_hash = hash(i)
		return samples_hash

	# Test if the current sample set has been saved
	def hash_exists(self):
		if(Path(self.memory).is_file()):
			return True
		return False

	# Save hash to memory location on disk
	def save_hash(self):
		Path(self.memory,"w").touch()