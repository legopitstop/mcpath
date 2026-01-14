"""
Linux Preview Edition
"""

from mcpath.facades import PreviewUWP


class LinuxPreviewEdition(PreviewUWP):
    pass


def instance():
    return LinuxPreviewEdition()
