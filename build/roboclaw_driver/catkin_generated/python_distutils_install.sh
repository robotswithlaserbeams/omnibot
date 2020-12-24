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

echo_and_run cd "/home/lyle/catkin_ws/src/roboclaw_driver"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/lyle/catkin_ws/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/lyle/catkin_ws/install/lib/python2.7/dist-packages:/home/lyle/catkin_ws/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/lyle/catkin_ws/build" \
    "/usr/bin/python2" \
    "/home/lyle/catkin_ws/src/roboclaw_driver/setup.py" \
    build --build-base "/home/lyle/catkin_ws/build/roboclaw_driver" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/lyle/catkin_ws/install" --install-scripts="/home/lyle/catkin_ws/install/bin"
