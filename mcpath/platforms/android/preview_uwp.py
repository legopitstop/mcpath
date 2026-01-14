"""
Android Preview Edition
"""

from mcpath.facades import PreviewUWP


class AndroidPreviewEdition(PreviewUWP):
    pass


def instance():
    return AndroidPreviewEdition()
