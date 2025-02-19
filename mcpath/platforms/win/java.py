"""
Windows Java Edition
"""

from os import path
from mcpath.facades import Java
from mcpath.utils import _get_latest_profile, _version_to_component


class WinJavaEdition(Java):
    def _get_runtime(self, version):
        component, major_version = _version_to_component(version)
        if component is None:
            return "java"
        p = path.expandvars(
            path.join(
                "%localappdata%",
                "Packages",
                "Microsoft.4297127D64EC6_8wekyb3d8bbwe",
                "LocalCache",
                "Local",
                "runtime",
                component,
                "windows-x64",
                component,
                "bin",
                "java.exe",
            )
        )
        if path.isfile(p):
            return p
        return "java"

    def _get_launcher(self):
        p = path.join(
            "C:\\" + "XboxGames", "Minecraft Launcher", "Content", "Minecraft.exe"
        )
        if path.isfile(p):
            return p
        return None

    def _get_game_dir(self):
        fp = path.expandvars("%APPDATA%\\.minecraft\\launcher_profiles.json")
        p = _get_latest_profile(fp)
        if p and path.isdir(p):
            return p
        # fallback
        p = path.expandvars("%APPDATA%\\.minecraft")
        if path.isdir(p):
            return p
        return None

    def _get_versions_dir(self):
        p = path.expandvars("%APPDATA%\\.minecraft\\versions")
        if path.isdir(p):
            return p
        return None


def instance():
    return WinJavaEdition()
