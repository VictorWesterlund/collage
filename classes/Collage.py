from PIL import Image
from bisect import bisect_left

class Schematic():
	def __init__(self,template,samples):
		self.template = template
		self.samples = samples

		self.schematic = {}
		self.create_schematic()

	def query_sample(self,value):
		samples = [*self.samples]
		pos = bisect_left(samples,value)

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
				print(f"Generated schematic for pixel at index [{x},{y}] ",end="\r",flush="True")
		print("")

class Collage():
	def __init__(self,input_file,samples):
		self.template = Image.open(input_file)
		self.samples = samples.samples
		self.samples_posix = samples.samples_posix

		self.size = (20,20)

		self.collage = self.create_canvas()
		self.create_collage()

	def create_canvas(self):
		canvas_width = self.size[0] * self.template.size[0]
		canvas_height = self.size[1] * self.template.size[1]

		return Image.new("RGB",(canvas_width,canvas_height))

	def create_collage(self):
		schematic = Schematic(self.template,self.samples).schematic

		offset_x = 0
		offset_y = 0

		for x in range(1,self.template.size[0]):
			offset_x = 0
			for y in range(1,self.template.size[1]):
				key = schematic[x][y]
				resolve_posix = self.samples[key]
				
				sample = Image.open(self.samples_posix[resolve_posix])
				sample = sample.resize(self.size)

				self.collage = self.collage.copy()
				self.collage.paste(sample,(offset_x,offset_y))

				offset_x += self.size[0]

				print(f"Pasted best matched sample for index [{x},{y}] ",end="\r",flush="True")
			offset_y += self.size[1]
		print("")

	def put(self,dest):
		self.collage.save(dest,"JPEG")
