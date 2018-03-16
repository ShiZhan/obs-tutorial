# Introduction

Object Storage Tutorial.

## Basic Concept

SNIA Tutorials on Object Storage:
* [Object Storage 101](http://www.snia.org/sites/default/files/Object_Storage_101.pdf)
* [Object Storage 201](https://www.snia.org/sites/default/files/Object_Storage_201_Final_1.pdf)
* [Object Storage Technology](http://www.snia.org/sites/default/education/tutorials/2013/spring/file/BrentWelch_Object_Storage_Technology.pdf).

The **Storage Networking Industry Association** ([SNIA](https://www.snia.org/)) is a not–for–profit global organization, made up of member companies spanning the global storage market.

# Preparation

## Environment

### How to establish Python Environment

* Python Distributions:
    * Option 1: [Anaconda](https://www.anaconda.com/)
        * Download from <https://repo.continuum.io/archive/Anaconda3-5.1.0-Windows-x86_64.exe> & install
    * Option 2: [WinPython](http://winpython.github.io/)
        * Download from <https://sourceforge.net/projects/winpython/files/WinPython_3.6/3.6.3.0/> & install
* Fast deployment by docker:
    * Option 3: Python Docker <https://github.com/Zhan2012/python-lab>
        * `docker login daocloud.io && docker pull daocloud.io/zhan2016/python-lab:master-31a932d`

### How to establish Java Environment

**Ongoing course**: Java Programming, [2017-2018 2nd semester](http://jwc.hust.edu.cn/info/1161/6122.htm), just follow your teacher's guide.

Installation helper scripts <https://github.com/Zhan2012/java-bundle> (_**For adventurers**_).

### Git and Github (_**Recommended**_)

Git tutorial <https://github.com/cs-course/git-tutorial>.

For those who want unlimited private repositories, try [bitbucket](https://bitbucket.org/).

### How to run servers within docker container (_**Optional**_)

For those who want to run Openstack Swift or Ceph in docker, refer to Docker tutorial <https://github.com/cs-course/docker-tutorial>.

## Object Storage Server

* Object Storage for Beginners:
    * Option 1: [Minio](https://minio.io/), latest version <https://minio.io/downloads.html>.
* Experimental Mock Servers:
    * Option 2: [fake-s3](https://github.com/jubos/fake-s3), a lightweight server clone of Amazon S3. **Depends on Ruby**, the Origin.
    * Option 3: [mock-s3](https://github.com/jserver/mock-s3), a Python clone of fake-s3. **Requires Python 2.7**.
    * Option 4: [s3mock](https://github.com/findify/s3mock), S3 mock library for Java/Scala. **Java/SBT Building is required**.
    * Option 5: [S3Mock](https://github.com/adobe/S3Mock), S3 mock as Docker image or JUnit rule. **Java/Maven Building is required**, contributed by Adobe (c).
    * Option 6: [s3proxy](https://github.com/gaul/s3proxy), access other storage via the S3 API. **Binary bundles [here](https://github.com/gaul/s3proxy/releases)**, use Java/Maven to build.
* Industry Level Projects:
    * Option 7: [Openstack Swift](https://wiki.openstack.org/wiki/Swift), fast deployment by All-in-one container: <https://github.com/cs-course/openstack-swift-docker>.
    * Option 8: [Ceph](https://ceph.com/), docker files and images to run Ceph in containers: <https://github.com/ceph/ceph-container>.

## Object Storage Client

* Standalone Utilities:
    * Option 1: Minio Client <https://docs.minio.io/docs/minio-client-quickstart-guide>
    * Option 2: s3cmd <https://github.com/s3tools/s3cmd>
        * run `pip install s3cmd` in python environment
        * Configure for Minio <https://docs.minio.io/docs/s3cmd-with-minio>
    * Option 3: aws-shell <https://github.com/awslabs/aws-shell>
        * run `pip install aws-shell` in python environment
        * Configure for Minio <https://docs.minio.io/docs/aws-cli-with-minio>
        * Official Manual <https://docs.aws.amazon.com/cli/latest/userguide/using-s3-commands.html>
* APIs:
    * Option 4: [aws-sdk-java](https://aws.amazon.com/cn/sdk-for-java/)
    * Option 5: [boto](https://github.com/boto/boto3)

Option 2 & 3 are more general and versatile, both are widely used for various object storage services.

## Object Storage Benchmark

* COSBench <https://github.com/intel-cloud/cosbench>
    * User Guide <https://github.com/intel-cloud/cosbench/raw/master/COSBenchUserGuide.pdf>.
    * Example workload <https://github.com/Zhan2012/obs-tutorial/raw/master/minio-workload-example.xml>.
    * Other examples <https://github.com/open-io/dockerfiles/tree/master/cosbench-openio/examples>.

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

*Throughput*, *Latency* under different *object size*, *concurrency*, *server total*.

Suggested topics:

* How object size affects performance?
    * for a particular application, is there a best way to fit into OBS?
* The main factors behind I/O latency?
    * Get latency distribution first.
* What will happen when clients are crowded?
* Why tests '**fail**'? (not terminate)
* The outcome of scaling out (putting more servers into system)?

More insights are encouraged.

## Further thoughts

* How to do these experiments on your own codes (besides COSBench)?
* Using Python as Lab Platform
    * Jupyter Notebook Tutorial <https://github.com/cs-course/jupyter-tutorial>

# Future Readings

Recent SNIA blog posts on Object Storage <http://sniablog.org/category/object-storage/>.

Enterprise level [Object Store comparison](http://gaul.org/object-store-comparison/).

Zhan.Shi @ 2018
