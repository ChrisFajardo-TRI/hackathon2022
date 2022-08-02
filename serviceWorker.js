const staticPyPWA = "dev-pypwa-v4"
const assets = [
    // "",
    // "/",
    "/static/js/pwa-scaffold.js",

    "/static/python/main.py",

    "/static/pyscript/pyscript.css",
    "/static/pyscript/pyscript.js",
    "/static/pyscript/pyscript.py",

    "/static/pyodide/pyodide.js",
    "/static/pyodide/package.json",
    "/static/pyodide/pyodide_py.tar",
    "/static/pyodide/pyodide.asm.js",
    "/static/pyodide/pyodide.asm.data",
    "/static/pyodide/pyodide.asm.wasm",
    "/static/pyodide/micropip-0.1-py3-none-any.whl",
    "/static/pyodide/distutils.tar",

    "/static/pyodide/Jinja2-3.1.2-py3-none-any.whl",
    "/static/pyodide/MarkupSafe-2.1.1-cp310-cp310-emscripten_3_1_14_wasm32.whl",
    "/static/pyodide/PyWavelets-1.3.0-cp310-cp310-emscripten_3_1_14_wasm32.whl",
    "/static/pyodide/Pygments-2.12.0-py3-none-any.whl",
    "/static/pyodide/attrs-21.4.0-py2.py3-none-any.whl",
    "/static/pyodide/beautifulsoup4-4.11.1-py3-none-any.whl",
    "/static/pyodide/beautifulsoup4-tests.tar",
    "/static/pyodide/bleach-5.0.0-py3-none-any.whl",
    "/static/pyodide/cffi-1.15.0-cp310-cp310-emscripten_3_1_14_wasm32.whl",
    "/static/pyodide/cffi_example-0.1-cp310-cp310-emscripten_3_1_14_wasm32.whl",
    "/static/pyodide/cycler-0.11.0-py3-none-any.whl",
    "/static/pyodide/decorator-5.1.1-py3-none-any.whl",
    "/static/pyodide/fonttools-4.33.3-py3-none-any.whl",
    "/static/pyodide/imageio-2.19.3-py3-none-any.whl",
    "/static/pyodide/jedi-0.18.1-py2.py3-none-any.whl",
    "/static/pyodide/jedi-tests.tar",
    "/static/pyodide/jsonschema-4.6.0-py3-none-any.whl",
    "/static/pyodide/jsonschema-tests.tar",
    "/static/pyodide/kiwisolver-1.4.3-cp310-cp310-emscripten_3_1_14_wasm32.whl",
    "/static/pyodide/matplotlib-3.5.2-cp310-cp310-emscripten_3_1_14_wasm32.whl",
    "/static/pyodide/matplotlib-tests.tar",
    "/static/pyodide/networkx-2.8.4-py3-none-any.whl",
    "/static/pyodide/networkx-tests.tar",
    "/static/pyodide/numpy-1.22.4-cp310-cp310-emscripten_3_1_14_wasm32.whl",
    "/static/pyodide/numpy-tests.tar",
    "/static/pyodide/packaging-21.3-py3-none-any.whl",
    "/static/pyodide/parso-0.8.3-py2.py3-none-any.whl",
    "/static/pyodide/pycparser-2.21-py2.py3-none-any.whl",
    "/static/pyodide/pyparsing-3.0.9-py3-none-any.whl",
    "/static/pyodide/pyrsistent-0.18.1-cp310-cp310-emscripten_3_1_14_wasm32.whl",
    "/static/pyodide/scikit-image-tests.tar",
    "/static/pyodide/scipy-1.8.1-cp310-cp310-emscripten_3_1_14_wasm32.whl",
    "/static/pyodide/scipy-tests.tar",
    "/static/pyodide/six-1.16.0-py2.py3-none-any.whl",
    "/static/pyodide/soupsieve-2.3.2.post1-py3-none-any.whl",
    "/static/pyodide/webencodings-0.5.1-py2.py3-none-any.whl"
]

self.addEventListener("install", installEvent => {
    installEvent.waitUntil(
        caches.open(staticPyPWA).then(cache => {
            cache.addAll(assets).then(r => {
                console.log("Cache assets downloaded");
            }).catch(err => console.log("Error caching item", err))
            console.log(`Cache ${staticPyPWA} opened.`);
        }).catch(err => console.log("Error opening cache", err))
    )
})

self.addEventListener("fetch", fetchEvent => {
    fetchEvent.respondWith(
        caches.match(fetchEvent.request).then(res => {
            return res || fetch(fetchEvent.request)
        }).catch(err => console.log("Cache fetch error: ", err))
    )
})
