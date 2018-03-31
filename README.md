# qgis-server

[![Build Status](https://travis-ci.org/infOpen/ansible-role-qgis-server.svg?branch=master)](https://travis-ci.org/infOpen/ansible-role-qgis-server)

Install qgis-server package.

This role not manage webserver, use another role for this job.

## Requirements

This role requires Ansible 2.2 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/metacloud/molecule/) to run tests.

Local and Travis tests run tests on Docker by default.
See molecule documentation to use other backend.

Currently, tests are done on:
- Debian Jessie
- Ubuntu Xenial

and use:
- Ansible 2.4.x
- Ansible 2.5.x

### Running tests

#### Using Docker driver

```
$ tox
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
- http://www.infopen.pro
- a.chaussier [at] infopen.pro
