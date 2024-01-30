"""Role testing files using testinfra."""


def test_config_file(host):
    """Validate etc/lamp.conf file."""
    f = host.file("etc/lamp.conf")
    assert f.exists
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o640


def test_binary_file(host):
    """Validate /usr/local/bin/lamp file."""
    f = host.file("/usr/local/bin/lamp")
    assert f.exists
    assert f.user == "root"
    assert f.group == "root"


def test_monit2lamp_file(host):
    """Validate /usr/local/bin/monit2opsgenie.sh file."""
    f = host.file("/usr/local/bin/monit2opsgenie.sh")
    assert f.exists
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o755
