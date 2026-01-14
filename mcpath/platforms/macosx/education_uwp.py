"""
MacOS X Education Edition
"""

from mcpath.facades import EducationUWP


class OSXEducationEdition(EducationUWP):
    pass


def instance():
    return OSXEducationEdition()
