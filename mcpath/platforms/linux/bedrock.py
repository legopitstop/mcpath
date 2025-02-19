"""
Linux Bedrock Edition
"""

from os import path
from mcpath.facades import Bedrock
import configparser


class LinuxBedrockEdition(Bedrock):
    def _get_game_dir(self):
        fp = path.join(
            path.expanduser("~"),
            ".var",
            "app",
            "io.mrarm.mcpelauncher",
            "data",
            "mcpelauncher",
            "profiles",
            "profiles.ini",
        )
        if path.isfile(fp):
            try:
                config = configparser.ConfigParser()
                config.read(fp)
                if config.has_section("General"):
                    general = config["General"]
                    profile = config[general.get("selected")]
                    p = path.join(profile.get("dataDir"), "games", "com.mojang")
                    if path.isdir(p):
                        return p
                    return None
            except KeyError:
                ...

        # Fallback
        p = path.join(
            path.expanduser("~"),
            ".var",
            "app",
            "io.mrarm.mcpelauncher",
            "data",
            "mcpelauncher",
            "games",
            "com.mojang",
        )
        if path.isdir(p):
            return p
        return None

    def _get_executable(self):
        p = path.join(
            "/var",
            "lib",
            "flatpak",
            "app",
            "io.mrarm.mcpelauncher",
            "current",
            "active",
            "export",
            "bin",
            "io.mrarm.mcpelauncher",
        )
        if path.isfile(p):
            return p
        return None

    def _get_executable(self):
        return "minecraft://"


def instance():
    return LinuxBedrockEdition()
