# screenctl
A tool for batch management of Linux Screen.

## Introduction
**screenctl** is a tool that can create, delete, stat screens in batch through a specified json configuration. A web-based admin page is in planning.

## Installation

```bash
# BE SURE YOU HAVE INSTALLED 'SCREEN'

# plan to release on pypi thus you can install it via pip
pip install screenctl
# to be done
```

## Usage

```bash
$ python screenctl.py -h
usage: screenctl.py [-h] [-c CONF] [-v] action

Controller for screen

positional arguments:
  action                create, delete, stat, server

optional arguments:
  -h, --help            show this help message and exit
  -c CONF, --conf CONF  path to configuration
  -v, --verbose         show verbose output
```

## Changelog & Todo

- v0.0.1: 2022-11-28 01:50
    - support basic `create`, `delete` and `stat`.
- v0.0.2: 2023-01-26 21:20
    - update README and release on [pypi](https://pypi.org/project/screenctl/).
- v0.0.3: 2023-01-26 21:55
    - fix a tiny bug and release.  
- v0.0.4: 2023-01-26 22:05
    - update README page. (it requires anothor version even for such a readme-update ...)
- v0.0.5: 2023-02-21 20:25
    - fix issue [#1](https://github.com/QGrain/screenctl/issues/1) and try to fix [#2](https://github.com/QGrain/screenctl/issues/2) (not verified)
- v0.0.6: 2023-02-21 21:15
    - fix a typo bug in line 68 in screenctl.py

## Open-Source

Welcome stars and contributions!