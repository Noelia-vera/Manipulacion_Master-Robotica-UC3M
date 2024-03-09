#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/noelia/manipulacion_ws/src/graspit_commander"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/noelia/manipulacion_ws/install/lib/python3/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/noelia/manipulacion_ws/install/lib/python3/dist-packages:/home/noelia/manipulacion_ws/build/graspit_commander/lib/python3/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/noelia/manipulacion_ws/build/graspit_commander" \
    "/usr/bin/python3" \
    "/home/noelia/manipulacion_ws/src/graspit_commander/setup.py" \
    egg_info --egg-base /home/noelia/manipulacion_ws/build/graspit_commander \
    build --build-base "/home/noelia/manipulacion_ws/build/graspit_commander" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/noelia/manipulacion_ws/install" --install-scripts="/home/noelia/manipulacion_ws/install/bin"
