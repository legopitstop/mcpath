"""
MacOS X Preview Edition
"""

from mcpath.facades import Preview


class OSXPreviewEdition(Preview):
    pass


def instance():
    return OSXPreviewEdition()
