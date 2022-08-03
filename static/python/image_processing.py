import cv2
import numpy as np
from skimage import segmentation, color
from skimage.future import graph


def opencv_grabcut(input_img):
    img = np.copy(input_img)
    mask = np.zeros(img.shape[:2], np.uint8)
    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)
    rect = (50, 50, 450, 290)
    cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    img = img * mask2[:, :, np.newaxis]
    return img


def opencv_watershed(input_img):
    img = np.copy(input_img)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # noise removal
    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
    # sure background area
    sure_bg = cv2.dilate(opening, kernel, iterations=3)
    # Finding sure foreground area
    dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    ret, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
    # Finding unknown region
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg, sure_fg)

    # Marker labelling
    ret, markers = cv2.connectedComponents(sure_fg)
    # Add one to all labels so that sure background is not 0, but 1
    markers = markers + 1
    # Now, mark the region of unknown with zero
    markers[unknown == 255] = 0

    markers = cv2.watershed(img, markers)
    img[markers == -1] = [255, 0, 0]
    return img


def scikit_image_chan_vese(input_img):
    img = np.copy(input_img)
    image = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # Feel free to play around with the parameters to see how they impact the result
    cv = segmentation.chan_vese(image, mu=0.25, lambda1=1, lambda2=1, tol=1e-3,
                                max_num_iter=200, dt=0.5, init_level_set="checkerboard",
                                extended_output=True)

    # ax[1].imshow(cv[0], cmap="gray")
    # title = f'Chan-Vese segmentation - {len(cv[2])} iterations'
    #
    # ax[2].imshow(cv[1], cmap="gray")
    # ax[2].set_title("Final Level Set", fontsize=12)
    #
    # ax[3].plot(cv[2])
    # ax[3].set_title("Evolution of energy over iterations", fontsize=12)

    return cv[1]


def scikit_image_rag(input_img):
    img = np.copy(input_img)

    labels1 = segmentation.slic(img, compactness=30, n_segments=400, start_label=1)
    # out1 = color.label2rgb(labels1, img, kind='avg', bg_label=0)

    g = graph.rag_mean_color(img, labels1)
    labels2 = graph.cut_threshold(labels1, g, 29)
    out2 = color.label2rgb(labels2, img, kind='avg', bg_label=0)

    return out2


def meme(input_img):
    import pyodide
    import textwrap

    img = np.copy(input_img)
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 0.4
    color = (255, 255, 255)
    thickness = 1
    try:
        text = pyodide.http.open_url("https://techy-api.vercel.app/api/text").getvalue()
    except:
        text = "Fetch didn't work, so some dummy text here."
    for i, line in enumerate(textwrap.wrap(text, width=30)):
        coordinates = (0, 20 + 10 * i)
        img = cv2.putText(img, line, coordinates, font, fontScale, color, thickness, cv2.LINE_AA)

    return img


if __name__ == "__main__":
    from time import sleep
    import time
    import matplotlib.pyplot as plt

    cap = cv2.VideoCapture(1)
    sleep(0.2)
    _, frame = cap.read()
    cap.release()

    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (320, 240))

    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB )

    fig, ((ax0, ax1), (ax2, ax3)) = plt.subplots(2, 2)

    start = time.time()
    out = scikit_image_rag(img)
    print(f"{scikit_image_rag.__name__} took {time.time() - start} seconds")
    ax0.imshow(out)

    start = time.time()
    out1 = scikit_image_chan_vese(img)
    print(f"{scikit_image_chan_vese.__name__} took {time.time() - start} seconds")
    ax1.imshow(out1)

    start = time.time()
    out2 = opencv_grabcut(img)
    print(f"{opencv_grabcut.__name__} took {time.time() - start} seconds")
    ax2.imshow(out2)

    start = time.time()
    out3 = opencv_watershed(img)
    print(f"{opencv_watershed.__name__} took {time.time() - start} seconds")
    ax3.imshow(out3)

    plt.show()
