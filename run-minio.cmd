@echo off

@rem Use environment variables MINIO_ACCESS_KEY & MINIO_SECRET_KEY to set keys, for later use in clients.
set MINIO_ACCESS_KEY=hust
set MINIO_SECRET_KEY=hust_obs

@rem Export metrics
set MINIO_PROMETHEUS_AUTH_TYPE=public

@rem Use "-C" flag to store configuration file in local directory "./".
@rem Use server command to start object storage server with "./root" as root directory, in which holds all buckets and objects.
minio.exe -C ./ server ./root

@rem Run above task in one command line.
@rem set MINIO_ACCESS_KEY=hust& set MINIO_SECRET_KEY=hust_obs& minio.exe -C ./ server ./root
