import mcpath
import pytest


@pytest.mark.xfail(
    raises=NotImplementedError, reason="Feature not supported on this platform"
)
def test_bedrock():
    mcpath.bedrock.get_game_dir()
    mcpath.bedrock.get_executable()
    mcpath.bedrock.get_worlds_dir()
    mcpath.bedrock.get_resource_packs_dir()
    mcpath.bedrock.get_behavior_packs_dir()
    mcpath.bedrock.get_development_resource_packs_dir()
    mcpath.bedrock.get_development_behavior_packs_dir()
    mcpath.bedrock.get_development_skin_packs_dir()
    mcpath.bedrock.get_screenshots_dir()
    mcpath.bedrock.get_logs_dir()
