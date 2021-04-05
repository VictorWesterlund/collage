from PIL import Image
from bisect import bisect_left

# Create instructions for the Collage constructor
class Schematic():
	def __init__(self,template,samples):
		self.template = template
		self.samples = samples

		self.schematic = {}
		self.create_schematic()

	# Use array bisection to find the closest matching sample by HEX color
	def query_sample(self,value):
		samples = [*self.samples]
		pos = bisect_left(samples,value)

		# Reset on under- and overflows
		if(pos < 1 or pos > len(samples) - 1):
			pos = 0

		return samples[pos]

	def create_schematic(self):
		for x in range(1,self.template.size[0]):
			self.schematic[x] = {}
			for y in range(1,self.template.size[1]):
				r,g,b = self.template.getpixel((x,y))
				eyedropper = "%02x%02x%02x" % (r,g,b)

				self.schematic[x][y] = self.query_sample(eyedropper)
				print(f"Found best match for index [{x},{y}] ",end="\r",flush="True")
		print("")

# Construct collage by loading images defined in schematic
class Collage():
	def __init__(self,input_file,samples):
		self.template = Image.open(input_file)
		self.samples = samples.samples
		self.samples_posix = samples.samples_posix

		self.size = (20,20)

		self.collage = self.create_canvas()
		self.create_collage()

	# Create the upscaled output image
	def create_canvas(self):
		canvas_width = self.size[0] * self.template.size[0]
		canvas_height = self.size[1] * self.template.size[1]

		return Image.new("RGB",(canvas_width,canvas_height))

	# Assemble the collage
	def create_collage(self):
		schematic = Schematic(self.template,self.samples).schematic

		offset_x = 0
		offset_y = 0

		# Apply each sample by raster scanning
		for x in range(1,self.template.size[0]):
			offset_x = 0
			for y in range(1,self.template.size[1]):
				key = schematic[x][y] # Get sample index for current pixel
				resolve_posix = self.samples[key] # Convert sample index to sample set index
				
				# Load and resize the requested sample from disk
				sample = Image.open(self.samples_posix[resolve_posix])
				sample = sample.resize(self.size)

				# Add the loaded sample to the collage
				self.collage = self.collage.copy()
				self.collage.paste(sample,(offset_x,offset_y))

				offset_x += self.size[0]

				print(f"Pasted sample at index [{x},{y}] ",end="\r",flush="True")
			offset_y += self.size[1]
		print("")

	# Save collage to disk
	def put(self,dest):
		self.collage.save(dest,"JPEG")
