"""
Supported Platforms
-------------------
iOS, Windows
"""

__all__ = ["Education"]

from .bedrock import Bedrock


class Education(Bedrock):
    """
    Education Edition facade.
    """

    # private

    def _get_executable(self):
        return "minecraftEdu://"
