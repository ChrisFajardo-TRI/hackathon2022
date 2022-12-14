# Playing with PyScript

## Web Client App
- Serve from this directory with ```python -m http.server```
- Take a webcam image and try some image segmentation
- Supports Progressive Web App (Can install as Desktop App or Save to Home Screen on iOS) and caching.

### Notes
- iOS needs HTTPS to use webcam (I used ngrok to serve)
- JS for webcam because opencv cv2.VideoCapture() doesn't work

## Promising
- Scientific Python in Browser
- Served as static site, runs on client
- Multi OS support

## Flaws
- Slow load
- Packages
  - not all supported or work correctly (requests, pyTorch)
  - separately compiled and maintained
  - no version choices
- Little docs

## References

### PyScript
- https://pyscript.net
- https://pyodide.org
- https://github.com/mikeckennedy/pyscript-pwa-example
- https://realpython.com/pyscript-python-in-browser
- https://www.jhanley.com/pyscript-javascript-callbacks/

### Python
- https://stackoverflow.com/questions/48717794/matplotlib-embed-figures-in-auto-generated-html
- https://docs.opencv.org/4.x/d3/db4/tutorial_py_watershed.html
- https://docs.opencv.org/4.x/d8/d83/tutorial_py_grabcut.html
- https://scikit-image.org/docs/stable/auto_examples/segmentation/plot_rag_mean_color.html#sphx-glr-auto-examples-segmentation-plot-rag-mean-color-py
- https://scikit-image.org/docs/stable/auto_examples/segmentation/plot_chan_vese.html#sphx-glr-auto-examples-segmentation-plot-chan-vese-py
- https://www.tutorialspoint.com/display-text-on-an-opencv-window-by-using-the-function-puttext

### JavaScript
- https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API/Taking_still_photos
- http://simpl.info/getusermedia/sources/
