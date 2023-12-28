# rangerdc
A workaround for using `ranger` as a filepicker for Discord, and a few other related utilities. Inspired by [claudius](https://github.com/daedreth/claudius).

## Requirements
Python 3.5+, [discord.py-self](https://pypi.org/project/discord.py-self/) (building from source is recommended, as releases are seldom), `ranger`, and optionally `scrot` (for screenshots).

## Installation
Clone this repository, modify the parameters in `config.ini` and run:
```shell
$ make
$ make install
```
You can disable any unneeded commands by replacing them with `""` in the `config.ini`.
