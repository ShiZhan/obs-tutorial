#!/bin/sh

S3PROXY_ENDPOINT=http://0.0.0.0:9000
S3PROXY_AUTHORIZATION=none
#S3PROXY_IDENTITY=hust
#S3PROXY_CREDENTIAL=hust_obs
JCLOUDS_PROVIDER=filesystem
JCLOUDS_FS_BASEDIR=.s3proxy-data
#JCLOUDS_FS_BASEDIR=/tmp

exec java \
    -DLOG_LEVEL=${LOG_LEVEL} \
    -Ds3proxy.endpoint=${S3PROXY_ENDPOINT} \
    -Ds3proxy.virtual-host=${S3PROXY_VIRTUALHOST} \
    -Ds3proxy.authorization=${S3PROXY_AUTHORIZATION} \
    -Ds3proxy.identity=${S3PROXY_IDENTITY} \
    -Ds3proxy.credential=${S3PROXY_CREDENTIAL} \
    -Ds3proxy.cors-allow-all=${S3PROXY_CORS_ALLOW_ALL} \
    -Ds3proxy.cors-allow-origins="${S3PROXY_CORS_ALLOW_ORIGINS}" \
    -Ds3proxy.cors-allow-methods="${S3PROXY_CORS_ALLOW_METHODS}" \
    -Ds3proxy.cors-allow-headers="${S3PROXY_CORS_ALLOW_HEADERS}" \
    -Ds3proxy.ignore-unknown-headers=${S3PROXY_IGNORE_UNKNOWN_HEADERS} \
    -Djclouds.provider=${JCLOUDS_PROVIDER} \
    -Djclouds.identity=${JCLOUDS_IDENTITY} \
    -Djclouds.credential=${JCLOUDS_CREDENTIAL} \
    -Djclouds.endpoint=${JCLOUDS_ENDPOINT} \
    -Djclouds.region=${JCLOUDS_REGION} \
    -Djclouds.regions=${JCLOUDS_REGIONS} \
    -Djclouds.keystone.version=${JCLOUDS_KEYSTONE_VERSION} \
    -Djclouds.keystone.scope=${JCLOUDS_KEYSTONE_SCOPE} \
    -Djclouds.keystone.project-domain-name=${JCLOUDS_KEYSTONE_PROJECT_DOMAIN_NAME} \
    -Djclouds.filesystem.basedir=${JCLOUDS_FS_BASEDIR}\
    -jar s3proxy_1.6.1.jar \
    --properties /dev/null
