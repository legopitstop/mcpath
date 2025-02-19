"""
Supported Platforms
-------------------
iOS, Windows
"""

__all__ = ["Preview"]

from .bedrock import Bedrock


class Preview(Bedrock):
    """
    Preview Edition facade.
    """

    # private

    def _get_executable(self):
        return "minecraft-preview://"
