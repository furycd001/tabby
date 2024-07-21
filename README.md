# Tabby

![alt text](tabby.png "Tabby")

This is a script for extracting URLs from Firefox sessionstore files.  
It's useful for recovering tabs from session backups, especially when it's not possible to successfully restore a previous session.

## Prerequisites

+   Python 3.x
+   `lz4` library
    +   Install using `pip`: `pip install lz4`
    +   Alternatively, you can install it using your distro's package manager. For me that's pacman on Arch, so `sudo pacman -S python-lz4` does it for me.

## Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/furycd001/tabby.git
cd tabby
```

## Running

```bash
python3 tabby.py /path/to/firefox/sessionstore_dir/
```
