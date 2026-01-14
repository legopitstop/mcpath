"""
MacOS X Preview Edition
"""

from mcpath.facades import PreviewUWP


class OSXPreviewEdition(PreviewUWP):
    pass


def instance():
    return OSXPreviewEdition()
