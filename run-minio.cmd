@echo off
@rem set MINIO_ACCESS_KEY=hust& set MINIO_SECRET_KEY=hust2019& minio.exe -C ./ server c:/minio/root
set MINIO_ACCESS_KEY=hust
set MINIO_SECRET_KEY=hust2019
minio.exe -C ./ server ./root
