"""
Windows Bedrock Edition
"""

from typing import Optional
from os import path
from mcpath.facades import Bedrock
from mcpath.utils import step_back


class WinBedrockEdition(Bedrock):

    def is_old(self, path: str) -> bool:
        return "Microsoft.MinecraftUWP" in path

    def _get_game_gdk(self) -> Optional[str]:
        """
        New path
        """
        p = path.expandvars(
            "%appdata%\\Minecraft Bedrock\\users\\shared\\games\\com.mojang"
        )
        if path.isdir(p):
            return p
        return None

    def _get_game_uwp(self) -> Optional[str]:
        """
        Old path
        """
        p = path.expandvars(
            "%LOCALAPPDATA%\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\games\\com.mojang"
        )
        if path.isdir(p):
            return p
        return None

    def _get_game_dir(self):
        gdk = self._get_game_gdk()
        if gdk:
            return gdk

        # Fallback to old path
        return self._get_game_uwp()

    def _get_logs_dir(self):
        game_dir = self.get_game_dir()

        if not game_dir:
            return None
        # old
        if self.is_old(game_dir):
            return step_back(game_dir, 2, "logs")
        # new
        return step_back(game_dir, 4, "logs")

    def _get_executable(self):
        return "minecraft://"


def instance():
    return WinBedrockEdition()
