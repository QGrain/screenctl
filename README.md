# screenctl
A tool for batch management of Linux Screen.

## Introduction
**screenctl** is a tool that can create, delete, stat screens in batch through a specified json configuration. A web-based admin page is in planning.

## Installation

```bash
# plan to released on pypi thus you can install it via pip
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

## Opensource

Welcome stars and contributions!