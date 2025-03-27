import mcpath
import pytest


@pytest.mark.xfail(
    raises=NotImplementedError, reason="Feature not supported on this platform"
)
def test_education():
    mcpath.education.get_game_dir()
    mcpath.education.get_executable()
    mcpath.education.get_worlds_dir()
    mcpath.education.get_resource_packs_dir()
    mcpath.education.get_behavior_packs_dir()
    mcpath.education.get_development_resource_packs_dir()
    mcpath.education.get_development_behavior_packs_dir()
    mcpath.education.get_development_skin_packs_dir()
    mcpath.education.get_screenshots_dir()
    mcpath.education.get_logs_dir()


def test_deprecated_education():
    mcpath.education.game
    mcpath.education.launcher
    mcpath.education.executable
    mcpath.education.worlds
    mcpath.education.resource_packs
    mcpath.education.behavior_packs
    mcpath.education.development_resource_packs
    mcpath.education.development_behavior_packs
    mcpath.education.screenshots
