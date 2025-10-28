"""
Linux Education Edition
"""

from mcpath.facades import Education


class LinuxEducationEdition(Education):
    pass


def instance():
    return LinuxEducationEdition()
