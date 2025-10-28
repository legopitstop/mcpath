"""
MacOS X Education Edition
"""

from mcpath.facades import Education


class OSXEducationEdition(Education):
    pass


def instance():
    return OSXEducationEdition()
