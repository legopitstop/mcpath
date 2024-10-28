import mcpath
import os

path = mcpath.java.launcher
if os.name == "nt":  # Windows
    os.system(f'"{path}"')  # os.startfile makes the launcher crash.
else:  # other
    os.system(f'open "{path}"')
