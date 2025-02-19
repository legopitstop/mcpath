import mcpath
import webbrowser

url = mcpath.preview.get_executable()
if url:
    webbrowser.open(url)
