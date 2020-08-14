import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_rsyslog_is_installed(host):
    package = host.package('rsyslog')
    assert package.is_installed
    assert package.version.startswith("8.24")


def test_rsyslog_running_and_enabled(host):
    service = host.service('rsyslog')
    assert service.is_running
    assert service.is_enabled


def test_rsyslog_is_listen(host):
    assert host.socket('tcp://0.0.0.0:514').is_listening
