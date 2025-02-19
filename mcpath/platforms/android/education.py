"""
Android Education Edition
"""

from mcpath.facades import Education


class AndroidEducationEdition(Education): ...


def instance():
    return AndroidEducationEdition()
