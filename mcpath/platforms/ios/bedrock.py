"""
iOS Bedrock Edition
"""

from os import path
from mcpath.facades import Bedrock
from mcpath.utils import _get_app
import os


class iOSBedrockEdition(Bedrock):
    def _get_game_dir(self):
        id = "EE96DC3D-86D7-4109-9A8D-D33CDDE06D7B"
        p = path.join(
            "/private",
            "var",
            "mobile",
            "Containers",
            "Data",
            "Application",
            id,
            "Documents",
            "games",
            "com.mojang",
        )
        if os.access(p, os.R_OK):
            return p
        app = _get_app()
        match app:
            case "pyto":
                import file_system

                while True:
                    d = file_system.pick_directory()
                    if id in d:
                        return p
                    print("Invalid directory!")
            case "pythonista":
                # 1. Tap the hamburger menu at the top left
                # 2. Under "EXTERNAL FILES" tap "Open..."
                # 3. Then tap "Folder..."
                # 5. Navigate to your Minecraft folder and tap "Open"
                # 6. Finally, run the script again.
                ...
        raise PermissionError()

    def _get_executable(self):
        return "minecraft://"


def instance():
    return iOSBedrockEdition()
