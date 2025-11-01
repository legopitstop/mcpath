__all__ = ["BedrockProtocol", "PreviewProtocol", "JavaProtocol", "EducationProtocol"]

from typing import List, Protocol, Optional


class JavaProtocol(Protocol):
    def launch(self) -> Optional[str]:
        """
        Launches Minecraft.
        """
        ...

    def get_runtime(self, version: str) -> Optional[str]:
        """
        Get the path to the java runtime executable.
        """
        ...

    def get_root_dir(self) -> Optional[str]:
        """
        Get the path to the `.minecraft` folder.
        """
        ...

    def get_game_dir(self) -> Optional[str]:
        """
        Get the path to the game directory.

        NOTE: If you want the `.minecraft` folder use get_root_dir instead.
        """
        ...

    def get_launcher(self) -> Optional[str]:
        """
        Get the path to the Minecraft launcher.
        """
        ...

    def get_versions_dir(self) -> Optional[str]:
        """
        Get the path of the directory holding version jar files.
        """
        ...

    def get_saves_dir(self) -> Optional[str]:
        """
        Get the path of the directory holding world files.
        """
        ...

    def get_resource_packs_dir(self) -> Optional[str]:
        """
        Get the path of the directory holding resource pack files.
        """
        ...

    def get_screenshots_dir(self) -> Optional[str]:
        """
        Get the path of the directory holding screenshot files.
        """
        ...

    def get_backups_dir(self) -> Optional[str]:
        """
        Get the path of the directory holding world backups.
        """
        ...

    def get_logs_dir(self) -> Optional[str]:
        """
        Get the path of the directory holding game log files.
        """
        ...

    def get_versions(self) -> List[str]:
        """
        Get a list of game versions.
        """
        ...

    def get_saves(self) -> List[str]:
        """
        Get a list of world saves.
        """
        ...

    def get_resource_packs(self) -> List[str]:
        """
        Get a list of resource packs.
        """
        ...

    def get_screenshots(self) -> List[str]:
        """
        Get a list of screenshots.
        """
        ...

    def get_backups(self) -> List[str]:
        """
        Get a list of world backups.
        """
        ...

    def get_logs(self) -> List[str]:
        """
        Get a list of game logs.
        """
        ...


class BedrockProtocol(Protocol):
    def launch(self) -> Optional[str]:
        """
        Launches Minecraft.
        """
        ...

    def get_game_dir(self, *paths: str) -> Optional[str]:
        """
        Get the path to the main Minecraft folder.
        """
        ...

    def get_executable(self) -> Optional[str]:
        """
        Get the path of the executable file.
        """
        ...

    def get_worlds_dir(self) -> Optional[str]:
        """
        Get the path of the directory holding world files.
        """
        ...

    def get_world_templates_dir(self) -> Optional[str]:
        """
        Get the path of the directory holding world template files.
        """
        ...

    def get_resource_packs_dir(self) -> Optional[str]:
        """
        Get the path of the directory holding resource pack files.
        """
        ...

    def get_behavior_packs_dir(self) -> Optional[str]:
        """
        Get the path of the directory holding behavior pack files.
        """
        ...

    def get_skin_packs_dir(self) -> Optional[str]:
        """
        Get the path of the directory holding skin pack files.
        """
        ...

    def get_development_resource_packs_dir(self) -> Optional[str]:
        """
        Get the path of the directory holding development resource pack files.
        """
        ...

    def get_development_behavior_packs_dir(self) -> Optional[str]:
        """
        Get the path of the directory holding development behavior pack files.
        """
        ...

    def get_development_skin_packs_dir(self) -> Optional[str]:
        """
        Get the path of the directory holding development skin pack files.
        """
        ...

    def get_custom_skins_dir(self) -> Optional[str]:
        """
        Get the path of the directory holding custom skin files.
        """
        ...

    def get_screenshots_dir(self) -> Optional[str]:
        """
        Get the path of the directory holding screenshot files.
        """
        ...

    def get_logs_dir(self) -> Optional[str]:
        """
        Get the path of the directory holding game log files.
        """
        ...

    def get_worlds(self) -> List[str]:
        """
        Get a list of world paths.
        """
        ...

    def get_behavior_packs(self) -> List[str]:
        """
        Get a list of behavior packs.
        """
        ...

    def get_resource_packs(self) -> List[str]:
        """
        Get a list of resource packs.
        """
        ...

    def get_development_behavior_packs(self) -> List[str]:
        """
        Get a list of development behavior packs.
        """
        ...

    def get_development_resource_packs(self) -> List[str]:
        """
        Get a list of development resource packs.
        """
        ...

    def get_development_skin_packs(self) -> List[str]:
        """
        Get a list of development skin packs.
        """
        ...

    def get_logs(self) -> List[str]:
        """
        Get a list of game logs.
        """
        ...

    def get_screenshots(self) -> List[str]:
        """
        Get a list of screenshots.
        """
        ...


class PreviewProtocol(BedrockProtocol):
    pass


class EducationProtocol(BedrockProtocol):
    pass
