# Introduction

Object Storage Tutorial, use [Minio](https://minio.io/) as Guide for Newbies.

# Preparation

* Object Storage Server
    * Minio: download latest version from <https://minio.io/downloads.html>.
    * Experimental Mock Servers:
        * Option 1: A Python clone of fake-s3, A lightweight server clone of Amazon S3 <https://github.com/jserver/mock-s3>.
        * Option 2: S3 mock library for Java/Scala <https://github.com/findify/s3mock>.
    * Industry Level Projects:
        * Option 1: Openstack Swift
            * All-in-one container: <https://github.com/cs-course/openstack-swift-docker>
            * A brief tutorial on container: <https://github.com/cs-course/docker-tutorial>
        * Option 2: Ceph
* Object Storage Client
    * option 1: Minio Client <https://docs.minio.io/docs/minio-client-quickstart-guide>
    * option 2: s3cmd <https://github.com/s3tools/s3cmd>, run `pip install s3cmd` in python environment
    * option 3: aws-shell <https://github.com/awslabs/aws-shell>, run `pip install aws-shell` in python environment.
* Object Storage Benchmark
    * COSBench <https://github.com/intel-cloud/cosbench>
        * COSBench: cloud object storage benchmark https://dl.acm.org/citation.cfm?doid=2479871.2479900
        * COSBench: A Benchmark Tool for Cloud Object Storage Services <https://www.techrepublic.com/resource-library/whitepapers/cosbench-a-benchmark-tool-for-cloud-object-storage-services/> <http://www.cs.cmu.edu/~qingzhen/files/cosbench_cloud12.pdf>
        * COSBench: A benchmark tool for Cloud Storage <https://www.snia.org/sites/default/files/files2/files2/SDC2013/presentations/Cloud/YaguangWang__COSBench_Final.pdf>

# Basic Functionality

CRUD

...

# Evaluation

Throughput, Latency under different object size, server total.

...

Zhan.Shi @ 2018
