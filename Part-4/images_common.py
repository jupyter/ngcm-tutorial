import os
import matplotlib.pyplot as plt

from skimage.io import imread

def plot_corners(img, corners, show=True):
    """Display the image and plot all contours found"""
    plt.imshow(img, cmap='gray')
    plt.plot(corners[:,1], corners[:,0], 'r+', markeredgewidth=1.5, markersize=8) # Plot corners
    plt.axis('image')
    plt.xticks([])
    plt.yticks([])
    if show:
        plt.show()

def find_corners(path, min_distance=5):
    """Find corners in an image at path
    
    Returns the image and the corner lists.
    """
    from skimage.feature import corner_harris, corner_peaks
    img = imread(path, flatten=True)
    corners = corner_peaks(corner_harris(img), min_distance=min_distance)
    return img, corners

def get_corners_image(path):
    """Given a path, return a PNG of the image with contour lines
    
    Calls both find_contours and plot_contours
    """
    from IPython.core.pylabtools import print_figure
    
    img, corners = find_corners(path)
    plot_corners(img, corners, show=False)
    fig = plt.gcf()
    pngdata = print_figure(fig)
    plt.close(fig)
    return pngdata

def get_pictures(pictures_dir):
    """Return a list of picture files found in pictures_dir"""

    pictures = []
    for directory, subdirs, files in os.walk(pictures_dir):
        for fname in files:
            if fname.lower().endswith(('.jpg', '.png')):
                pictures.append(os.path.join(directory, fname))
    
    return pictures


def find_blobs(img_path):
    """Find the blobs in an image"""
    from skimage.color import rgb2gray
    from skimage.feature import blob_doh
    from skimage.io import imread

    image = imread(img_path)
    image_gray = rgb2gray(image)
    return image, blob_doh(image_gray, max_sigma=30, threshold=.01)


def plot_blobs(image, blobs):
    """Plot the blobs in an image"""
    fig, ax = plt.subplots()
    ax.grid(False)
    ax.imshow(image, interpolation='nearest')
    ax.set_xticks([])
    ax.set_yticks([])
    for blob in blobs:
        y, x, r = blob
        c = plt.Circle((x, y), r, color='r', linewidth=2, fill=False)
        ax.add_patch(c)

