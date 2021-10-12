@echo off

@rem Use environment variables MINIO_ROOT_USER & MINIO_ROOT_PASSWORD to set keys, for later use in clients.
set MINIO_ROOT_USER=hust
set MINIO_ROOT_PASSWORD=hust_obs

@rem Export metrics
set MINIO_PROMETHEUS_AUTH_TYPE=public

@rem Use "-C" flag to store configuration file in local directory "./".
@rem Use server command to start object storage server with "./root" as root directory, in which holds all buckets and objects.
minio.exe -C ./ server ./root --console-address ":9090"

@rem Run above task in one command line.
@rem set MINIO_ROOT_USER=hust& set MINIO_ROOT_PASSWORD=hust_obs& minio.exe -S ./certs server ./root
