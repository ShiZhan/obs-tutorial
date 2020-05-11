#!/bin/bash
# Get script location
called=$_
if [[ $called == $0 ]]; then
    SCRIPT_PATH="$0"
else
    SCRIPT_PATH="${BASH_SOURCE[0]}"
fi
SCRIPT_DIR=$( cd "$(dirname $SCRIPT_PATH )" && pwd )

# Get OSM location (GOPATH default to ~/go)
osm=~/go/bin/osm
if [ -n "$GOPATH" ]; then
    osm=$GOPATH/bin/osm
fi

# Setting up OSM with local configuration file "osm.conf"
$osm --osmconfig $SCRIPT_DIR/osm.conf \
    config set-context osm-minio \
        --provider=s3 \
        --s3.access_key_id=hust \
        --s3.secret_key=hust_obs \
        --s3.endpoint=http://127.0.0.1:9000

# Check this configuration
$osm --osmconfig $SCRIPT_DIR/osm.conf \
    config view

# Prepare alias for simplified command line
alias osm="osm --osmconfig $SCRIPT_DIR/osm.conf"
