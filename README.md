# update

  no need ssh now, can start instance with api.

# For ctde.py:

  Change Start('the path to your compositor', 'cmd of your container manager only support "lxc" for LXD and "incus" for Incus', 'name of the container', 'username in container', 'startcmd of desktop like sway|labwc|startx|mate-session...')() in if \__name__ == '\__main__' to fit you.

# For ctde.desktop:

  Change /path/to/ctde.py to the real path of ctde.py.

# detail
https://discuss.linuxcontainers.org/t/autostart-container-desktop-environment/
https://discuss.linuxcontainers.org/t/an-update-about-nest-x11/
https://discuss.linuxcontainers.org/t/its-possible-to-run-containerlized-x11-without-nesting-or-vnc-or-rdp-but-i-need-help-with-input/
