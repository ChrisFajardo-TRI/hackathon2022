import time

import js
import numpy as np
import matplotlib.pyplot as plt
from pyodide.ffi import create_proxy

import image_processing

video = js.document.getElementById("video")
canvas = js.document.getElementById("canvas")
context = canvas.getContext("2d")


def update_video_frame():
    context.drawImage(video, 0, 0, canvas.width, canvas.height)


def get_video_frame_data():
    img_data = context.getImageData(0, 0, canvas.width, canvas.height)
    d = np.reshape([x for x in img_data.data], (canvas.height, canvas.width, 4))
    return d


def show_image(image, div_id):
    fig, ax = plt.subplots()
    ax.axis('off')
    ax.imshow(image)
    fig.tight_layout()
    Element(div_id).write(fig)


def process(func, div_id):
    d = get_video_frame_data()
    input_img = d[:, :, :3].astype('uint8')
    start = time.time()
    out = func(input_img)
    print(f"{func.__name__} took {time.time() - start} seconds")
    show_image(out, div_id)


def button_click(event):
    update_video_frame()
    process(image_processing.scikit_image_rag, "fig1")
    process(image_processing.scikit_image_chan_vese, "fig2")
    process(image_processing.opencv_grabcut, "fig3")
    process(image_processing.opencv_watershed, "fig4")
    process(image_processing.meme, "fig5")


def setup():

    # Create a JsProxy for the callback function
    click_proxy = create_proxy(button_click)

    # Set the listener to the callback
    e = js.document.getElementById("button")
    e.addEventListener("click", click_proxy)


setup()
