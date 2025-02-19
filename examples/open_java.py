import mcpath
import os

path = mcpath.java.get_launcher()
if path:
    if mcpath.platform in ["win", "linux"]:
        os.system(f'"{path}"')
    else:  # other
        print(path)
