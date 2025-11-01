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
    mcpath.java.get_versions()
    mcpath.java.get_saves()
    mcpath.java.get_resource_packs()
    mcpath.java.get_screenshots()
    mcpath.java.get_logs()


def test_deprecated_java():
    attrs = [
        "game",
        "launcher",
        "executable",
        "worlds",
        "resource_packs",
        "behavior_packs",
        "development_resource_packs",
        "development_behavior_packs",
        "screenshots",
    ]

    for attr in attrs:
        with pytest.warns(DeprecationWarning):
            getattr(mcpath.java, attr)
