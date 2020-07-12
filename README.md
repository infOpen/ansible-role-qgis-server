# qgis-server

[![CI](https://github.com/infOpen/ansible-role-qgis-server/workflows/CI/badge.svg)](https://github.com/infOpen/ansible-role-qgis-server/actions)
[![Mergify Status][mergify-status]][mergify]
[![Updates](https://pyup.io/repos/github/infOpen/ansible-role-qgis-server/shield.svg)](https://pyup.io/repos/github/infOpen/ansible-role-qgis-server/)
[![Python 3](https://pyup.io/repos/github/infOpen/ansible-role-qgis-server/python-3-shield.svg)](https://pyup.io/repos/github/infOpen/ansible-role-qgis-server/)
[![Ansible Role](https://img.shields.io/ansible/role/24685.svg)](https://galaxy.ansible.com/infOpen/qgis-server/)

Install qgis-server package.

This role not manage webserver, use another role for this job.

## Requirements

This role requires Ansible 2.8 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/ansible-community/molecule) to run tests.

Local and Github Actions tests run tests on Docker by default.
See molecule documentation to use other backend.

Currently, tests are done on:
- Debian Buster
- Debian Stretch
- Ubuntu Bionic
- Ubuntu Focal

and use:
- Ansible 2.8.x
- Ansible 2.9.x

### Running tests

#### Using Docker driver

```
$ tox
```

You can also configure molecule options and molecule command using environment variables:
* `MOLECULE_OPTIONS` Default: "--debug"
* `MOLECULE_COMMAND` Default: "test"

```
$ MOLECULE_OPTIONS='' MOLECULE_COMMAND=converge tox
```

## Role Variables

### Default role variables

``` yaml
# Installation
qgis_server_repository_cache_valid_time: 3600
qgis_server_system_prerequisites: "{{ _qgis_server_system_prerequisites | default([]) }}"
qgis_server_repositories_keys: "{{ _qgis_server_repositories_keys | default([]) }}"
qgis_server_repositories: "{{ _qgis_server_repositories | default([]) }}"
qgis_server_system_packages: "{{ _qgis_server_system_packages | default([]) }}"
qgis_server_use_ltr: False

# Specific Debian installation
qgis_server_use_ubuntugis: False

# Service
qgis_server_service_name: "{{ _qgis_server_service_name | default('qgis-server') }}"
```

## Dependencies

None

## Example Playbook

``` yaml
- hosts: servers
  roles:
    - { role: infOpen.qgis-server }
```

## License

MIT

## Author Information

Alexandre Chaussier (for Infopen company)
- https://www.infopen.pro
- a.chaussier [at] infopen.pro

[mergify]: https://mergify.io
[mergify-status]: https://img.shields.io/endpoint.svg?url=https://gh.mergify.io/badges/infOpen/ansible-role-qgis-server&style=flat
