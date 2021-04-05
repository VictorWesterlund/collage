# Collage
**Create a collage of an image using smaller images**

This script attempts to find images of similar color to each pixel of an input image.

![demo](https://storage.googleapis.com/public.victorwesterlund.com/github/VictorWesterlund/collage/demo.png)

[Full resolution output](https://storage.googleapis.com/public.victorwesterlund.com/github/VictorWesterlund/collage/demo_full.jpg) (4000x4000px)

## Create your own collage

### Prerequisites

1. Install the `pip` package manager for Python 3.

```
sudo apt-get install python3-pip
```
2. Install dependencies from `requirements.txt`.
```
python3 -m pip install -r requirements.txt
```

### Using collage

1. Add JPG images to use as samples to the `samples/` folder. [9999 free sample images](#download-sample-images).

Sample sets containing images with a mix of different colors and light intensity will in general produce better results.

2. Run `create.py` from `~/collage` with Python 3.
```
python3 create.py
```
3. Provide an input and output file path when prompted.

You can also pass the input and output file paths as arguments when running `create.py`.
```
python3 create.py [path_to_input] [path_to_output]
```

## Download sample images

9999 free 612x612px sample images (~1GB when inflated).

*Note that 9999 images are probably overkill if the samples are random enough (which these are). 2000-4000 samples should be enough for most use cases.*

Set|Size|Download|
--|--|--
1-2000|193.5 MB|[Download](https://storage.googleapis.com/public.victorwesterlund.com/github/VictorWesterlund/collage/samples/1-2000.zip)
2001-4000|192.2 MB|[Download](https://storage.googleapis.com/public.victorwesterlund.com/github/VictorWesterlund/collage/samples/2001-4000.zip)
4001-6000|191.2 MB|[Download](https://storage.googleapis.com/public.victorwesterlund.com/github/VictorWesterlund/collage/samples/4001-6000.zip)
6001-8000|380.5 MB|[Download](https://storage.googleapis.com/public.victorwesterlund.com/github/VictorWesterlund/collage/samples/6001-8000.zip)
8001-10000|191.4 MB|[Download](https://storage.googleapis.com/public.victorwesterlund.com/github/VictorWesterlund/collage/samples/8001-10000.zip)

## Increase / Decrease the output resolution

Resizing the output doesn't require any modification to the underlying code. It does however require that you instance each class manually.

1. Import the required modules.
```python
from classes.Samples import Samples
from classes.Collage import Collage
```

2. Loading the samples with `Sample`. Nothing exciting here.
```python
samples = Samples("samples",False)
```

3. Initialize `Collage` and define your own `self.size` tuple.
```python
collage = Collage("path/to/input.jpg",samples)
collage.size = (100,50) # (width,height) of each sample in the collage.

collage.put("path/to/write/output.jpg")
```

# License

[This repo is licensed under the MIT License](https://github.com/VictorWesterlund/collage/blob/master/LICENSE)

# Issues & Contribute

Report bugs and suggest features by creating an [Issue](https://github.com/VictorWesterlund/collage/issues).

Pull Requests to this repo are very appreciated.
