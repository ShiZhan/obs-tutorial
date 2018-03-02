# Introduction

Object Storage Tutorial, use [Minio](https://minio.io/) as Guide for Newbies.

# Preparation

## Object Storage Server

* Minio: download latest version from <https://minio.io/downloads.html>.
* Experimental Mock Servers:
    * Option 1: A Python clone of fake-s3, A lightweight server clone of Amazon S3 <https://github.com/jserver/mock-s3>.
    * Option 2: S3 mock library for Java/Scala <https://github.com/findify/s3mock>.
* Industry Level Projects:
    * Option 1: [Openstack Swift](https://wiki.openstack.org/wiki/Swift)
        * All-in-one container: <https://github.com/cs-course/openstack-swift-docker>
    * Option 2: [Ceph](https://ceph.com/)
        * Docker files and images to run Ceph in containers: <https://github.com/ceph/ceph-container>

### A brief tutorial on container

* Docker tutorial <https://github.com/cs-course/docker-tutorial>

## Object Storage Client

* Option 1: Minio Client <https://docs.minio.io/docs/minio-client-quickstart-guide>
* Option 2: s3cmd <https://github.com/s3tools/s3cmd>
    * run `pip install s3cmd` in python environment
* Option 3: aws-shell <https://github.com/awslabs/aws-shell>
    * run `pip install aws-shell` in python environment

Option 2 & 3 are more general and versatile, both are widely used for various object storage services.

### How to establish Python Environment

* Option 1: [Anaconda](https://www.anaconda.com/)
    * Download from <https://repo.continuum.io/archive/Anaconda3-5.1.0-Windows-x86_64.exe> & install
* Option 2: [WinPython](http://winpython.github.io/)
    * Download from <https://sourceforge.net/projects/winpython/files/WinPython_3.6/3.6.3.0/> & install
* Option 3: Python Docker <https://github.com/Zhan2012/python-lab>
    * `docker login daocloud.io && docker pull daocloud.io/zhan2016/python-lab:master-31a932d`

### Using Python as Lab Platform

* Jupyter Notebook Tutorial <https://github.com/cs-course/jupyter-tutorial>

## Object Storage Benchmark

* COSBench <https://github.com/intel-cloud/cosbench>

### References

* COSBench: cloud object storage benchmark https://dl.acm.org/citation.cfm?doid=2479871.2479900
* COSBench: A Benchmark Tool for Cloud Object Storage Services <http://www.cs.cmu.edu/~qingzhen/files/cosbench_cloud12.pdf>
* COSBench: A benchmark tool for Cloud Storage <https://www.snia.org/sites/default/files/files2/files2/SDC2013/presentations/Cloud/YaguangWang__COSBench_Final.pdf>

# Basic Functionality

In computer programming, [create, read, update, and delete (as an acronym CRUD)](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) are the four basic functions of persistent storage.

| Operation        | SQL    | HTTP               |
| :---:            | :---:  | :---:              |
| Create           | INSERT | PUT / POST         |
| Read (Retrieve)  | SELECT | GET                |
| Update (Modify)  | UPDATE | PUT / POST / PATCH |
| Delete (Destroy) | DELETE | DELETE             |

# Evaluation

Throughput, Latency under different object size, server total.

Zhan.Shi @ 2018
