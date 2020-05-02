#!/bin/bash
# OSM default location
osm=~/go/bin/osm

# Update OSM executable path based on GOPATH
if [ -n "$GOPATH" ]; then
    osm=$GOPATH/bin/osm
fi

# Setting up OSM with local configuration file "osm.conf"
$osm --osmconfig osm.conf config set-context osm-minio --provider=s3 --s3.access_key_id=hust --s3.secret_key=hust_obs --s3.endpoint=http://127.0.0.1:9000
$osm --osmconfig osm.conf config view

# Prepare alias for simplified command line
called=$_
if [[ $called == $0 ]]; then
  SCRIPT_PATH="$0"
else
  SCRIPT_PATH="${BASH_SOURCE[0]}"
fi
SCRIPT_DIR=$( cd "$(dirname $SCRIPT_PATH )" && pwd )
alias osm='osm --osmconfig $SCRIPT_DIR/osm.conf'
