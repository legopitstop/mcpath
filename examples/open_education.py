import mcpath
import webbrowser

url = mcpath.education.get_executable()
if url:
    webbrowser.open(url)
