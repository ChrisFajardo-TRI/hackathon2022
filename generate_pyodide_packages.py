# run in REPL
import micropip
import json
d = json.loads(micropip.freeze())
all = [f'    \"/static/pyodide/{x["file_name"]}\",' for x in d['packages'].values()]
print('\n'.join(all))
