#!/bin/sh
PYTHON_VER=`python --version 2>&1`
case "$PYTHON_VER" in
    "Python 2.7."*)
        python mock-s3/mock_s3/main.py --port 9000 --root .root
        ;;
    *)
        echo "Python 2.7 required"
        ;;
esac
