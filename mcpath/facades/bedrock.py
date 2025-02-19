"""
Supported Platforms
-------------------
Android, iOS, Linux, MacOS, Windows
"""

__all__ = ["Bedrock"]

from os import path
import os


class Bedrock:
    """
    Bedrock Edition facade.
    """

    def get_game_dir(self):
        """
        Get the path to the main Minecraft folder.
        """
        return self._get_game_dir()

    def get_executable(self):
        """
        Get the path of the executable file.
        """
        return self._get_executable()

    def get_worlds_dir(self):
        """
        Get the path of the directory holding world files.
        """
        return self._get_worlds_dir()

    def get_world_templates_dir(self):
        """
        Get the path of the directory holding world template files.
        """
        return self._get_world_templates_dir()

    def get_resource_packs_dir(self):
        """
        Get the path of the directory holding resource pack files.
        """
        return self._get_resource_packs_dir()

    def get_behavior_packs_dir(self):
        """
        Get the path of the directory holding behavior pack files.
        """
        return self._get_behavior_packs_dir()

    def get_skin_packs_dir(self):
        """
        Get the path of the directory holding skin pack files.
        """
        return self._get_skin_packs_dir()

    def get_development_resource_packs_dir(self):
        """
        Get the path of the directory holding development resource pack files.
        """
        return self._get_development_resource_packs_dir()

    def get_development_behavior_packs_dir(self):
        """
        Get the path of the directory holding development behavior pack files.
        """
        return self._get_development_behavior_packs_dir()

    def get_development_skin_packs_dir(self):
        """
        Get the path of the directory holding development skin pack files.
        """
        return self._get_development_skin_packs_dir()

    def get_custom_skins_dir(self):
        """
        Get the path of the directory holding custom skin files.
        """
        return self._get_custom_skins_dir()

    def get_screenshots_dir(self):
        """
        Get the path of the directory holding screenshot files.
        """
        return self._get_screenshots_dir()

    def get_logs_dir(self):
        """
        Get the path of the directory holding game log files.
        """
        return self._get_logs_dir()

    # private

    def _get_game_dir(self):
        raise NotImplementedError()

    def _get_executable(self):
        return "minecraft://"

    def _get_worlds_dir(self):
        return path.join(self.get_game_dir(), "minecraftWorlds")

    def _get_world_templates_dir(self):
        return path.join(self.get_game_dir(), "world_templates")

    def _get_resource_packs_dir(self):
        return path.join(self.get_game_dir(), "resource_packs")

    def _get_behavior_packs_dir(self):
        return path.join(self.get_game_dir(), "behavior_packs")

    def _get_skin_packs_dir(self):
        return path.join(self.get_game_dir(), "skin_packs")

    def _get_development_resource_packs_dir(self):
        return path.join(self.get_game_dir(), "development_resource_packs")

    def _get_development_behavior_packs_dir(self):
        return path.join(self.get_game_dir(), "development_behavior_packs")

    def _get_development_skin_packs_dir(self):
        return path.join(self.get_game_dir(), "development_skin_packs")

    def _get_custom_skins_dir(self):
        return path.join(self.get_game_dir(), "custom_skins")

    def _get_screenshots_dir(self):
        return path.join(self.get_game_dir(), "Screenshots")

    def _get_logs_dir(self):
        return os.path.join(self.get_game_dir(), "logs")
