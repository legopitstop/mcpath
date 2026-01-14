"""
Linux Education Edition
"""

from mcpath.facades import EducationUWP


class LinuxEducationEdition(EducationUWP):
    pass


def instance():
    return LinuxEducationEdition()
