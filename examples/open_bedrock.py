import mcpath
import webbrowser
import os

url = mcpath.bedrock.get_executable()
if url:
    if mcpath.platform == "linux":
        os.system(f'"{ url }"')
    else:
        webbrowser.open(url)
