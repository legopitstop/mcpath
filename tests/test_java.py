import mcpath
import pytest


@pytest.mark.xfail(
    raises=NotImplementedError, reason="Feature not supported on this platform"
)
def test_java():
    mcpath.java.get_runtime("1.21.3")
    mcpath.java.get_game_dir()
    mcpath.java.get_launcher()
    mcpath.java.get_versions_dir()
    mcpath.java.get_saves_dir()
    mcpath.java.get_resource_packs_dir()
    mcpath.java.get_screenshots_dir()
    mcpath.java.get_logs_dir()


def test_deprecated_java():
    mcpath.java.game
    mcpath.java.launcher
    mcpath.java.executable
    mcpath.java.worlds
    mcpath.java.resource_packs
    mcpath.java.behavior_packs
    mcpath.java.development_resource_packs
    mcpath.java.development_behavior_packs
    mcpath.java.screenshots
