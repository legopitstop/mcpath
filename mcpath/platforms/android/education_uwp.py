"""
Android Education Edition
"""

from mcpath.facades import EducationUWP


# https://play.google.com/store/apps/details?id=com.mojang.minecraftedu
class AndroidEducationEdition(EducationUWP):
    pass


def instance():
    return AndroidEducationEdition()
