import base64
import io

import js
import numpy as np
import matplotlib.pyplot as plt
from pyodide import create_proxy

from skimage.segmentation import random_walker
from skimage.data import binary_blobs
from skimage.exposure import rescale_intensity
import skimage


def do_stuff_with_canvas(target_id):
    video = js.document.getElementById("video")
    canvas = js.document.getElementById("canvas")
    context = canvas.getContext("2d")

    context.drawImage(video, 0, 0, canvas.width, canvas.height)
    img_data = context.getImageData(0, 0, canvas.width, canvas.height)
    d = np.reshape([x for x in img_data.data], (canvas.height, canvas.width, 4))

    # img_png = Element("photo").element.src.replace('data:image/png;base64,', '')
    # res = base64.b64decode(img_png.encode('utf-8'))
    # d = plt.imread(io.BytesIO(res))

    fig, ax = plt.subplots()
    ax.axis('off')
    ax.imshow(d)

    Element(target_id).write(fig)


# def main():
#     rng = np.random.default_rng()
#
#     # Generate noisy synthetic data
#     data = skimage.img_as_float(binary_blobs(length=128, seed=1))
#     sigma = 0.35
#     data += rng.normal(loc=0, scale=sigma, size=data.shape)
#     data = rescale_intensity(data, in_range=(-sigma, 1 + sigma),
#                              out_range=(-1, 1))
#
#     # The range of the binary image spans over (-1, 1).
#     # We choose the hottest and the coldest pixels as markers.
#     markers = np.zeros(data.shape, dtype=np.uint)
#     markers[data < -0.95] = 1
#     markers[data > 0.95] = 2
#
#     # Run random walker algorithm
#     labels = random_walker(data, markers, beta=10, mode='bf')
#
#     # Plot results
#     fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(8, 3.2),
#                                         sharex=True, sharey=True)
#     ax1.imshow(data, cmap='gray')
#     ax1.axis('off')
#     ax1.set_title('Noisy data')
#     ax2.imshow(markers, cmap='magma')
#     ax2.axis('off')
#     ax2.set_title('Markers')
#     ax3.imshow(labels, cmap='gray')
#     ax3.axis('off')
#     ax3.set_title('Segmentation')
#
#     fig.tight_layout()
#
#     # plt.show()
#
#     Element("fig").write(fig)


# main()

def button_click(event):
    do_stuff_with_canvas("fig2")


def setup():

    # Create a JsProxy for the callback function
    click_proxy = create_proxy(button_click)

    # Set the listener to the callback
    e = js.document.getElementById("button")
    e.addEventListener("click", click_proxy)


setup()
