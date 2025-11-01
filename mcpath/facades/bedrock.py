"""
Supported Platforms
-------------------
Android, iOS, Linux, MacOS, Windows
"""

__all__ = ["Bedrock"]

from typing import Optional, List
from os import path
import glob
import webbrowser
import os

from ..utils import deprecated


class Bedrock:
    """
    Bedrock Edition facade.
    """

    def launch(self) -> Optional[str]:
        return self._launch()

    def get_game_dir(self, *paths: str) -> Optional[str]:
        return self._get_game_dir(*paths)

    def get_executable(self) -> Optional[str]:
        return self._get_executable()

    def get_worlds_dir(self) -> Optional[str]:
        return self._get_worlds_dir()

    def get_world_templates_dir(self) -> Optional[str]:
        return self._get_world_templates_dir()

    def get_resource_packs_dir(self) -> Optional[str]:
        return self._get_resource_packs_dir()

    def get_behavior_packs_dir(self) -> Optional[str]:
        return self._get_behavior_packs_dir()

    def get_skin_packs_dir(self) -> Optional[str]:
        return self._get_skin_packs_dir()

    def get_development_resource_packs_dir(self) -> Optional[str]:
        return self._get_development_resource_packs_dir()

    def get_development_behavior_packs_dir(self) -> Optional[str]:
        return self._get_development_behavior_packs_dir()

    def get_development_skin_packs_dir(self) -> Optional[str]:
        return self._get_development_skin_packs_dir()

    def get_custom_skins_dir(self) -> Optional[str]:
        return self._get_custom_skins_dir()

    def get_screenshots_dir(self) -> Optional[str]:
        return self._get_screenshots_dir()

    def get_logs_dir(self) -> Optional[str]:
        return self._get_logs_dir()

    def get_worlds(self) -> List[str]:
        root = self.get_worlds_dir()
        if not root:
            return []
        return [
            path.join(root, folder)
            for folder in os.listdir(root)
            if path.isdir(path.join(root, folder))
        ]

    def __get_packs(self, root: str) -> List[str]:
        return [
            path.join(root, folder)
            for folder in os.listdir(root)
            if path.isdir(path.join(root, folder))
            and path.isfile(path.join(root, folder, "manifest.json"))
        ]

    def get_behavior_packs(self) -> List[str]:
        root = self.get_behavior_packs_dir()
        if not root:
            return []
        return self.__get_packs(root)

    def get_resource_packs(self) -> List[str]:
        root = self.get_resource_packs_dir()
        if not root:
            return []
        return self.__get_packs(root)

    def get_development_behavior_packs(self) -> List[str]:
        root = self.get_development_behavior_packs_dir()
        if not root:
            return []
        return self.__get_packs(root)

    def get_development_resource_packs(self) -> List[str]:
        root = self.get_development_resource_packs_dir()
        if not root:
            return []
        return self.__get_packs(root)

    def get_development_skin_packs(self) -> List[str]:
        root = self.get_development_skin_packs_dir()
        if not root:
            return []
        return self.__get_packs(root)

    def get_logs(self) -> List[str]:
        root = self.get_logs_dir()
        if not root:
            return []
        return [
            path.join(root, file)
            for file in os.listdir(root)
            if path.isfile(path.join(root, file)) and file.endswith(".txt")
        ]

    def get_screenshots(self) -> List[str]:
        root = self.get_screenshots_dir()
        if not root:
            return []
        return [file for file in glob.glob(f"{root}/**/*.jpeg")]

    # backwards compatibility

    @property
    @deprecated
    def game(self):
        return self.get_game_dir()

    @property
    @deprecated
    def launcher(self):
        return ""

    @property
    @deprecated
    def executable(self):
        return self.get_executable()

    @property
    @deprecated
    def worlds(self):
        return self.get_worlds_dir()

    @property
    @deprecated
    def resource_packs(self):
        return self.get_resource_packs_dir()

    @property
    @deprecated
    def behavior_packs(self):
        return self.get_behavior_packs_dir()

    @property
    @deprecated
    def development_resource_packs(self):
        return self.get_development_resource_packs_dir()

    @property
    @deprecated
    def development_behavior_packs(self):
        return self.get_development_behavior_packs_dir()

    @property
    @deprecated
    def screenshots(self):
        return self.get_screenshots_dir()

    # private

    def _launch(self) -> Optional[str]:
        url = self.get_executable()
        if url:
            webbrowser.open(url)
        return url

    def _get_game_dir(self, *paths: str) -> Optional[str]:
        return None

    def _get_executable(self) -> Optional[str]:
        return None

    def _get_worlds_dir(self) -> Optional[str]:
        return self.get_game_dir("minecraftWorlds")

    def _get_world_templates_dir(self) -> Optional[str]:
        return self.get_game_dir("world_templates")

    def _get_resource_packs_dir(self) -> Optional[str]:
        return self.get_game_dir("resource_packs")

    def _get_behavior_packs_dir(self) -> Optional[str]:
        return self.get_game_dir("behavior_packs")

    def _get_skin_packs_dir(self) -> Optional[str]:
        return self.get_game_dir("skin_packs")

    def _get_development_resource_packs_dir(self) -> Optional[str]:
        return self.get_game_dir("development_resource_packs")

    def _get_development_behavior_packs_dir(self) -> Optional[str]:
        return self.get_game_dir("development_behavior_packs")

    def _get_development_skin_packs_dir(self) -> Optional[str]:
        return self.get_game_dir("development_skin_packs")

    def _get_custom_skins_dir(self) -> Optional[str]:
        return self.get_game_dir("custom_skins")

    def _get_screenshots_dir(self) -> Optional[str]:
        return self.get_game_dir("screenshots")

    def _get_logs_dir(self) -> Optional[str]:
        return self.get_game_dir("logs")
