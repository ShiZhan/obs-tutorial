#!/bin/bash

# Use environment variables MINIO_ROOT_USER & MINIO_ROOT_PASSWORD to set keys, for later use in clients.
export MINIO_ROOT_USER=hust
export MINIO_ROOT_PASSWORD=hust_obs

# Export metrics
export MINIO_PROMETHEUS_AUTH_TYPE="public"

# Use "-C" flag to store configuration file in local directory "./".
# Use server command to start object storage server with "./root" as root directory, in which holds all buckets and objects.
./minio -C ./ server ./root --console-address ":9090"

# Run above task in one command line.
# export MINIO_ROOT_USER=hust && export MINIO_ROOT_PASSWORD=hust_obs && ./minio -C ./ server ./root
