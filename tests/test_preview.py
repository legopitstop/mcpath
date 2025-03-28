import mcpath
import pytest


@pytest.mark.xfail(
    raises=NotImplementedError, reason="Feature not supported on this platform"
)
def test_preview():
    mcpath.preview.get_game_dir()
    mcpath.preview.get_executable()
    mcpath.preview.get_worlds_dir()
    mcpath.preview.get_resource_packs_dir()
    mcpath.preview.get_behavior_packs_dir()
    mcpath.preview.get_development_resource_packs_dir()
    mcpath.preview.get_development_behavior_packs_dir()
    mcpath.preview.get_development_skin_packs_dir()
    mcpath.preview.get_screenshots_dir()
    mcpath.preview.get_logs_dir()


def test_deprecated_preview():
    mcpath.preview.game
    mcpath.preview.launcher
    mcpath.preview.executable
    mcpath.preview.worlds
    mcpath.preview.resource_packs
    mcpath.preview.behavior_packs
    mcpath.preview.development_resource_packs
    mcpath.preview.development_behavior_packs
    mcpath.preview.screenshots
