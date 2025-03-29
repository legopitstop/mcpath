# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - unreleased

### General

- If a path doesn't exist, it will return None.
- Rewrote package structure.
- Example using the new structure.

```py
import mcpath

mcpath.bedrock.get_worlds_dir() # ...\\com.mojang\\minecraftWorlds
mcpath.java.get_backups_dir() # ...\\.minecraft\\backups

mcpath.java.get_runtime('1.21.3') # ...\\java-runtime-delta\\bin\\java.exe
```

## [1.1.0] - 10/27/2024

### General

- Added `executable` and `launcher` paths
- Added `get_runtime` function to get the java runtime executable.
- Added support for bedrock on linux and iOS.
- Renamed `root` to `game` which goes to the .minecraft or com.mojang directory.
- Java Edition on Windows, linux, and macOS will now read launcher_profiles.json to get the game directory.
- Bedrock Edition on linux will now check profiles.ini to get the game directory.

## [1.0.0] - 9/11/2024

### General

- Initial commit
