import mcpath


def test_java():
    mcpath.java.get_runtime("1.21.3")
    mcpath.java.get_game_dir()
    mcpath.java.get_launcher()
    mcpath.java.get_versions_dir()
    mcpath.java.get_saves_dir()
    mcpath.java.get_resource_packs_dir()
    mcpath.java.get_screenshots_dir()
    mcpath.java.get_logs_dir()
