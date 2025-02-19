import mcpath

# Java - windows, linux

print(mcpath.java.get_runtime("1.16.5"))
print(mcpath.java.get_launcher())
print(mcpath.java.get_game_dir())
print(mcpath.java.get_versions_dir())

# Bedrock - windows, linux

print(mcpath.bedrock.get_game_dir())
print(mcpath.bedrock.get_executable())
print(mcpath.bedrock.get_logs_dir())
print(mcpath.bedrock.get_custom_skins_dir())

# Preview - windows

print(mcpath.preview.get_game_dir())
print(mcpath.preview.get_executable())

# Education - Windows

print(mcpath.education.get_game_dir())
print(mcpath.education.get_executable())
