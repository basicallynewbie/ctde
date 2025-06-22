# if running X11 and require xauthority
if [ -z "$DISPLAY" ] ; then
    export DISPLAY=:0
    export XAUTHORITY=/path/to/xauthority
fi

# example for running xfce4 in container
cmd="pidof Thunar"
$cmd
status=$?

if ! [ $status -eq 0 ]; then
    nohup startxfce4 > /dev/null 2>&1 &
fi

# example for running labwc in container, remember wayland also depend on XDG_RUNTIME_DIR
if [ -z "$WAYLAND_DISPLAY" ] ; then
    export WAYLAND_DISPLAY=wayland-1
fi

if ! [ -S "$XDG_RUNTIME_DIR/wayland-0" ] ; then
    nohup labwc > /dev/null 2>&1 &
fi
