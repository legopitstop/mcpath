"""
Linux Preview Edition
"""

from mcpath.facades import Preview


class LinuxPreviewEdition(Preview):
    pass


def instance():
    return LinuxPreviewEdition()
