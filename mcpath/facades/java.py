"""
Supported Platforms
-------------------
Linux, MacOS, Windows
"""

__all__ = ["Java"]

from os import path


class Java:
    """
    Java Edition facade.
    """

    def get_runtime(self, version: str):
        """
        Get the path to the java runtime executable.
        """
        return self._get_runtime(version)

    def get_game_dir(self):
        """
        Get the path to the main Minecraft folder.
        """
        return self._get_game_dir()

    def get_launcher(self):
        """
        Get the path to the Minecraft launcher.
        """
        return self._get_launcher()

    def get_versions_dir(self):
        """
        Get the path of the directory holding version jar files.
        """
        return self._get_versions_dir()

    def get_saves_dir(self):
        """
        Get the path of the directory holding world files.
        """
        return self._get_saves_dir()

    def get_resource_packs_dir(self):
        """
        Get the path of the directory holding resource pack files.
        """
        return self._get_resource_packs_dir()

    def get_screenshots_dir(self):
        """
        Get the path of the directory holding screenshot files.
        """
        return self._get_screenshots_dir()

    def get_backups_dir(self):
        """
        Get the path of the directory holding world backups.
        """
        return self._get_backups_dir()

    def get_logs_dir(self):
        """
        Get the path of the directory holding game log files.
        """
        return self._get_logs_dir()

    # private

    def _get_runtime(self, version):
        raise NotImplementedError()

    def _get_launcher(self):
        raise NotImplementedError()

    def _get_game_dir(self):
        raise NotImplementedError()

    def _get_versions_dir(self):
        raise NotImplementedError()

    def _get_saves_dir(self):
        return path.join(self.get_game_dir(), "saves")

    def _get_resource_packs_dir(self):
        return path.join(self.get_game_dir(), "resourcepacks")

    def _get_screenshots_dir(self):
        return path.join(self.get_game_dir(), "screenshots")

    def _get_backups_dir(self):
        return path.join(self.get_game_dir(), "backups")

    def _get_logs_dir(self):
        return path.join(self.get_game_dir(), "logs")
