"""
Get paths to Minecraft Java, Bedrock, Preview, and Education Edition folders.
"""

__all__ = [
    "java",
    "bedrock",
    "preview",
    "education",
    "platform",
    "get_edition",
    "has_edition",
]
__version__ = "2.0.3"

from typing import Any, Optional, cast
from mcpath import facades
from mcpath.utils import platform, Proxy

java: facades.JavaProtocol = cast(facades.JavaProtocol, Proxy("java", facades.Java))
bedrock: facades.BedrockProtocol = cast(
    facades.BedrockProtocol, Proxy("bedrock", facades.Bedrock)
)
preview: facades.PreviewProtocol = cast(
    facades.PreviewProtocol, Proxy("preview", facades.Preview)
)
education: facades.EducationProtocol = cast(
    facades.EducationProtocol, Proxy("education", facades.Education)
)


def get_edition(
    name: str,
) -> Optional[Any]:
    name = name.lower()
    match name:
        case "java":
            return java
        case "bedrock":
            return bedrock
        case "preview":
            return preview
        case "education":
            return education
    return None


def has_edition(name: str) -> bool:
    return get_edition(name) is not None
