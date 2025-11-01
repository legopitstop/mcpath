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

    mcpath.preview.get_worlds()
    mcpath.preview.get_resource_packs()
    mcpath.preview.get_behavior_packs()
    mcpath.preview.get_development_resource_packs()
    mcpath.preview.get_development_behavior_packs()
    mcpath.preview.get_development_skin_packs()
    mcpath.preview.get_screenshots()
    mcpath.preview.get_logs()


def test_deprecated_preview():
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
            getattr(mcpath.preview, attr)
