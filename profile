# if running X11 and require xauthority
if [ -z "$DISPLAY" ] ; then
    export DISPLAY=:0
    export XAUTHORITY=/path/to/xauthority
fi

# if running wayland, WAYLAND_DISPLAY need to be pointed to host wayland socket first, remember wayland also depend on XDG_RUNTIME_DIR
if [ -z "$WAYLAND_DISPLAY" ] ; then
    export WAYLAND_DISPLAY=wayland-1
fi
