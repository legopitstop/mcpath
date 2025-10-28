"""
Android Preview Edition
"""

from mcpath.facades import Preview


class AndroidPreviewEdition(Preview):
    pass


def instance():
    return AndroidPreviewEdition()
