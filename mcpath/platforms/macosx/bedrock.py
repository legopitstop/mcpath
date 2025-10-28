"""
MacOS X Bedrock Edition
"""

from mcpath.facades import Bedrock


class OSXBedrockEdition(Bedrock):
    pass


def instance():
    return OSXBedrockEdition()
