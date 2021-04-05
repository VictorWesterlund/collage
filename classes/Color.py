from PIL import Image

# Calculate the average color of a sample
class AverageColor():
    def __init__(self,image):
        self.image = Image.open(image)
        self.image = self.image.resize((50,50)) # Downscale image to improve performance

    def rgb(self):
        width,height = self.image.size
        rgb = [0,0,0]

        def average(value):
            return round(value / lines)

        # Get RGB of each pixel with by raster scanning
        lines = 0
        for x in range(0,width):
            for y in range(0,height):
                r,g,b = self.image.getpixel((x,y))

                rgb[0] += r
                rgb[1] += g
                rgb[2] += b
                lines += 1

        return tuple(map(average,rgb))

    # Format RGB output as HEX (without #)
    def hex(self):
        return "%02x%02x%02x" % self.rgb()