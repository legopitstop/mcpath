import mcpath
import webbrowser

url = mcpath.bedrock.get_executable()
if url:
    webbrowser.open(url)
