"""
Get paths to Minecraft Java, Bedrock, Preview, and Education Edition folders.
"""

__all__ = ["java", "bedrock", "preview", "education", "platform", "get_edition"]
__version__ = "2.0.2"

from typing import Optional
from mcpath import facades
from mcpath.utils import platform, Proxy

java = Proxy("java", facades.Java)
bedrock = Proxy("bedrock", facades.Bedrock)
preview = Proxy("preview", facades.Preview)
education = Proxy("education", facades.Education)


def get_edition(name: str) -> Optional[Proxy]:
    match name.lower():
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
