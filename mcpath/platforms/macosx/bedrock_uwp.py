"""
MacOS X Bedrock Edition
"""

from mcpath.facades import BedrockUWP


class OSXBedrockEdition(BedrockUWP):
    pass


def instance():
    return OSXBedrockEdition()
