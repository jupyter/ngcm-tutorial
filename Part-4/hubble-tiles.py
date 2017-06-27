"""Construct tiles of a high-res hubble image
for sample data
"""

import os, sys

import requests
import skimage.io

from ipywidgets import IntProgress
from IPython.display import display

url = 'http://imgsrc.hubblesite.org/hvi/uploads/image_file/image_attachment/9077/full_jpg.jpg'
here = os.path.dirname(__file__)
full_size_file = os.path.join(here, 'hubble.jpg')

def download_original():
    p = IntProgress(max=1, description="Downloading")
    display(p)
    if os.path.exists(full_size_file):
        print("Already have %s" % full_size_file)
        p.value = p.max
    else:
        r = requests.get(url, stream=True)
        content_length = r.headers.get('content-length', int(1e8))
        print("Downloading %s" % url)
        p.max = content_length
        r.raise_for_status()

        with open(full_size_file, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8096):
                p.value += len(chunk)
                f.write(chunk)
    p.value = p.max

def tile_image(full_size_path, tile_size=400):
    p = IntProgress(description='Tiling', max=1)
    display(p)
    root_dir = os.path.dirname(full_size_path)
    name, ext = os.path.splitext(os.path.basename(full_size_path))
    tile_dir = os.path.join(root_dir, '{0}-{1}x{1}'.format(name, tile_size))
    if not os.path.exists(tile_dir):
        os.mkdir(tile_dir)
    tpl = os.path.join(tile_dir, '{name}-{i:02}-{j:02}{ext}')
    full_size = skimage.io.imread(full_size_path)
    X, Y = full_size.shape[:2]
    total_tiles = (X // tile_size) * (Y // tile_size)
    p.max = total_tiles
    print("Creating %i tiles in %s" % (total_tiles, tile_dir))

    for i in range(X // tile_size):
        for j in range(Y // tile_size):
            tile = full_size[
                i * tile_size: (i+1) * tile_size,
                j * tile_size: (j+1) * tile_size,
                :
            ]
            fname = tpl.format(**locals())
            p.value += 1
            skimage.io.imsave(fname, tile)
    p.value = p.max

if __name__ == '__main__':
    download_original()
    tile_image(full_size_file)
