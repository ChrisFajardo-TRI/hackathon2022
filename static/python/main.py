import js
import numpy as np
import matplotlib.pyplot as plt
from pyodide import create_proxy

import image_processing


def grab_a_video_frame():
    video = js.document.getElementById("video")
    canvas = js.document.getElementById("canvas")
    context = canvas.getContext("2d")

    context.drawImage(video, 0, 0, canvas.width, canvas.height)
    img_data = context.getImageData(0, 0, canvas.width, canvas.height)
    d = np.reshape([x for x in img_data.data], (canvas.height, canvas.width, 4))
    return d


def show_image(image, div_id):
    fig, ax = plt.subplots()
    ax.axis('off')
    ax.imshow(image)
    fig.tight_layout()
    Element(div_id).write(fig)


def process(div_id):
    d = grab_a_video_frame()
    input_img = d[:, :, :3].astype('uint8')
    out = image_processing.scikit_image_chan_vese(input_img)
    show_image(out, div_id)


def button_click(event):
    process("fig2")


def setup():

    # Create a JsProxy for the callback function
    click_proxy = create_proxy(button_click)

    # Set the listener to the callback
    e = js.document.getElementById("button")
    e.addEventListener("click", click_proxy)


setup()
