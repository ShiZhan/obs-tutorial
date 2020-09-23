#!/bin/bash

# Use environment variables MINIO_ACCESS_KEY & MINIO_SECRET_KEY to set keys, for later use in clients.
export MINIO_ACCESS_KEY=hust
export MINIO_SECRET_KEY=hust_obs

# Export metrics
export MINIO_PROMETHEUS_AUTH_TYPE="public"

# Use "-C" flag to store configuration file in local directory "./".
# Use server command to start object storage server with "./root" as root directory, in which holds all buckets and objects.
./minio -C ./ server ./root

# Run above task in one command line.
# export MINIO_ACCESS_KEY=hust && export MINIO_SECRET_KEY=hust_obs && ./minio -C ./ server ./root
