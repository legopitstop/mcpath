import mcpath

print("Root Folder", mcpath.java.get_root_dir())
print("Game Folder", mcpath.java.get_game_dir())
print("Runtime Folder", mcpath.java.get_runtime("1.16.5"))
print("Launcher Folder", mcpath.java.get_launcher())
print("Launcher Logs", mcpath.java.get_launcher_logs())
print("Versions Folder", mcpath.java.get_versions_dir())
