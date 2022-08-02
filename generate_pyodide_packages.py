import subprocess
freeze = subprocess.check_output("pip freeze", shell=True)
desired_packages = [x.partition("==")[0] for x in freeze.decode().splitlines()]
avail = subprocess.check_output("ls static/pyodide/", shell=True)
packages_to_include = [f"/static/pyodide/{x}" for x in avail.decode().splitlines() if any([x.startswith(y) for y in desired_packages])]
print("\n".join([f'    "{x}", ' for x in packages_to_include]))
