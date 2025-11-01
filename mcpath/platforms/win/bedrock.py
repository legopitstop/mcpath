"""
Windows Bedrock Edition
"""

from typing import Optional
from os import path
from mcpath.facades import Bedrock
from mcpath.utils import step_back, get_bedrock_gdk


class WinBedrockEdition(Bedrock):

    def is_old(self, path: str) -> bool:
        return "Microsoft.MinecraftUWP" in path

    def _get_game_uwp(self, *paths: str) -> Optional[str]:
        """
        Old path
        """
        p = path.expandvars(
            "%LOCALAPPDATA%\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\games\\com.mojang"
        )
        p = path.join(p, *paths)
        if path.isdir(p):
            return p
        return None

    def _get_game_dir(self, *paths):
        return get_bedrock_gdk("Minecraft Bedrock", *paths) or self._get_game_uwp(
            *paths
        )

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
