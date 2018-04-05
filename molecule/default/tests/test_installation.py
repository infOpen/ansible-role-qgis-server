"""
Role tests
"""

import os
import pytest
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('distribution,repository_file_path', [
    ('debian', '/etc/apt/sources.list.d/qgis_org_debian.list'),
    ('ubuntu', '/etc/apt/sources.list.d/qgis_org_debian.list'),
])
def test_repository_files(host, distribution, repository_file_path):
    """
    Ensure QGIS Server repositories configuration files exists
    """

    if host.system_info.distribution != distribution:
        pytest.skip('Distribution not managed for this file')

    repository_file = host.file(repository_file_path)

    assert repository_file.exists
    assert repository_file.user == 'root'
    assert repository_file.group == 'root'


@pytest.mark.parametrize('distribution,name', [
    ('debian', 'qgis-server'),
    ('debian', 'python-qgis'),
    ('ubuntu', 'qgis-server'),
    ('ubuntu', 'python-qgis'),
])
def test_packages(host, distribution, name):
    """
    Ensure QGIS Server packages installed
    """

    if host.system_info.distribution != distribution:
        pytest.skip('Distribution not managed for this package')

    assert host.package(name).is_installed


@pytest.mark.parametrize('distribution, fcgi_file_path', [
    ('debian', '/usr/lib/cgi-bin/qgis_mapserv.fcgi'),
    ('ubuntu', '/usr/lib/cgi-bin/qgis_mapserv.fcgi'),
])
def test_fcgi_file(host, distribution, fcgi_file_path):
    """
    Ensure QGIS Server packages installed
    """

    if host.system_info.distribution != distribution:
        pytest.skip('Distribution not managed for this file')

    fcgi_file = host.file(fcgi_file_path)

    assert fcgi_file.exists
    assert fcgi_file.user == 'root'
    assert fcgi_file.group == 'root'


@pytest.mark.parametrize('path', [
    ('/opt/qgis-server/'),
    ('/opt/qgis-server/data'),
    ('/opt/qgis-server/data/qgis-server-db'),
    ('/opt/qgis-server/log'),
    ('/opt/qgis-server/www'),
])
def test_additional_folders(host, path):
    """
    Ensure QGIS Server additional folders exists
    """

    current_dir = host.file(path)

    assert current_dir.exists
    assert current_dir.is_directory
    assert current_dir.user == 'www-data'
    assert current_dir.group == 'www-data'
    assert current_dir.mode == 0o700
