from PIL import Image, ImageFilter
from .lib.colorthief import ColorThief

# Image loader
class PrepImage():
    def __init__(self,image):
        self.image = Image.open(image)
        self.image = self.image.resize((50,50)) # Downscale image to improve performance

    # Format RGB output as HEX (without #)
    def hex(self):
        return "%02x%02x%02x" % self.rgb()

# Calculate the average color of a sample
class AverageColor(PrepImage):
    def __init__(self,image):
        super(AverageColor,self).__init__(image)

    # Normalize colors with a blur
    def blur(self):
        blur = ImageFilter.GaussianBlur(10)
        self.image = self.image.filter(blur)

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

class DominantColor(ColorThief,PrepImage):
    def __init__(self,image):
        super(DominantColor,self).__init__(image)

    def rgb(self):
        return self.get_color(quality=1)

# class DominantColor(PrepImage):
#     def __init__(self,image):
#         super(DominantColor,self).__init__(image)
#         self.palette_size = 16

#     def get_palette(self):
#         palettised = self.image.convert("P",palette=Image.ADAPTIVE,colors=self.palette_size)
        
#         palette = palettised.getpalette()
#         colors = sorted(palettised.getcolors(),reverse=True)
#         index = colors[0][1]
#         dominant_color = palette[index * 3:index * + 3]
        
#         return dominant_color

#     def rgb(self):
#         colors = self.get_palette()
#         return tuple(colors)