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

### Git and Github

Git tutorial <https://github.com/cs-course/git-tutorial>.

Alternatives: [bitbucket](https://bitbucket.org/), [gitlab](https://about.gitlab.com/), [gitee](https://gitee.com/).

### How to establish Python Environment

* Python Distributions:
    * Option 1: [Anaconda](https://www.anaconda.com/)
    * Option 2: [WinPython](http://winpython.github.io/)
* Fast deployment by docker:
    * Option 3: Python Docker <https://github.com/cs-course/python-lab>, E.g.:
        * `docker pull zhan2016/python-lab:3.6.0`
        * `docker login daocloud.io && docker pull daocloud.io/zhan2016/python-lab:master-31a932d`

### How to establish Java Environment

**Ongoing course**: Java Programming, [2019-2020 2nd semester](http://jwc.hust.edu.cn/info/1161/7796.htm), just follow your teacher's guide.

Installation helper scripts <https://github.com/ShiZhan/java-bundle> (_**For adventurers**_).

### How to use Linux in Windows or MacOS (_**Optional**_)

**Goal**: try mock-s3 and s3proxy with less trouble

**Method**: Virtual Machine: Virtualbox, VMWare ...

Go directly to GUI, or using vagrant,refer to <https://github.com/cs-course/vagrant-tutorial>.

### How to run servers within docker container (_**Optional**_)

**Goal**: try Openstack Swift or Ceph with less trouble

Better run within docker, refer to Docker tutorial <https://github.com/cs-course/docker-tutorial>.

- [Ceph docker images](https://hub.docker.com/r/ceph/ceph)
- [Openstack Swift all-in-one docker image](https://hub.docker.com/r/fnndsc/docker-swift-onlyone)

## Object Storage Server

* Object Storage for Beginners:
    * Option 1: [Minio](https://minio.io/), latest version <https://minio.io/downloads.html>.
* Experimental Mock Servers:
    * Option 2: [mock-s3](https://github.com/ShiZhan/mock-s3), a Python clone of fake-s3, Amazon S3 mimic.
        * Option 2.1: Original version **Requires Python 2.7** <https://github.com/jserver/mock-s3>.
    * Option 3: [s3proxy](https://github.com/gaul/s3proxy), access other storage via the S3 API. **Binary bundles [here](https://github.com/gaul/s3proxy/releases)**
        * Option 3.1: Use Java/Maven to build `mvn package -Dmaven.test.skip=true`.
    * Option 4: [fake-s3](https://github.com/jubos/fake-s3), a lightweight server clone of Amazon S3. **Depends on Ruby**, the Origin project.
    * Option 5: [s3mock](https://github.com/findify/s3mock), S3 mock library for Java/Scala. **Java/SBT Building is required**.
    * Option 6: [S3Mock](https://github.com/adobe/S3Mock), S3 mock as Docker image or JUnit rule. **Use Java/Maven to build, use docker to run**, contributed by Adobe (c).
* Industry Level Projects:
    * Option 7: [Openstack Swift](https://wiki.openstack.org/wiki/Swift), fast deployment by All-in-one container: <https://github.com/cs-course/openstack-swift-docker>.
    * Option 8: [Ceph](https://ceph.com/), docker files and images to run Ceph in containers: <https://github.com/ceph/ceph-container>.

Besides _Option 1_, _Option 2, 3_ offer compile-free executable.

## Object Storage Client

* Standalone Utilities:
    * Option 1: **Minio Client** <https://docs.minio.io/docs/minio-client-quickstart-guide>
        * **Installation**: download and run
    * Option 2: **s3cmd** <https://github.com/s3tools/s3cmd>
        * **Installation**: run `pip install s3cmd` in python environment
        * Configure for Minio <https://docs.minio.io/docs/s3cmd-with-minio>
    * Option 3: **aws-shell** <https://github.com/awslabs/aws-shell>
        * **Installation**: run `pip install aws-shell` in python environment
        * Configure for Minio <https://docs.minio.io/docs/aws-cli-with-minio>
        * Official Manual <https://docs.aws.amazon.com/cli/latest/userguide/using-s3-commands.html>
    * Option 4: **osm** <https://github.com/appscode/osm>
        * **Installation**: `go get -u github.com/appscode/osm`
        * [Windows binary](https://share.weiyun.com/jPYFmvmw)
* APIs:
    * Option 4: **aws-sdk-java** <https://aws.amazon.com/cn/sdk-for-java/>
    * Option 5: **boto** <https://github.com/boto/boto3>

Binary available for *Option 1*, *Option 2 & 3* require Python, *Option 4* require Go.

## Object Storage Benchmark

* Option 1: **COSBench** <https://github.com/intel-cloud/cosbench>
    * User Guide <https://github.com/intel-cloud/cosbench/raw/master/COSBenchUserGuide.pdf>.
    * Example workload <https://github.com/ShiZhan/obs-tutorial/raw/master/workload-example.xml>.
    * Other examples <https://github.com/open-io/dockerfiles/tree/master/cosbench-openio/examples>.
    * Literatures
      * COSBench: cloud object storage benchmark https://dl.acm.org/citation.cfm?doid=2479871.2479900
      * COSBench: A Benchmark Tool for Cloud Object Storage Services <http://www.cs.cmu.edu/~qingzhen/files/cosbench_cloud12.pdf>
      * COSBench: A benchmark tool for Cloud Storage <https://www.snia.org/sites/default/files/files2/files2/SDC2013/presentations/Cloud/YaguangWang__COSBench_Final.pdf>
    
* Option 2: **S3 Bench** <https://github.com/igneous-systems/s3bench>
    * **Installation**
        ```bash
        go get -u github.com/igneous-systems/s3bench
        ```
        
        * Linux: default location for built binary is `~/go/bin/s3bench`
        * [Prebuilt Windows binary](https://share.weiyun.com/BICMfA4G), download and put into this directory.
        
    * Command line example
      
        ```bash
        s3bench \
            -accessKey=hust -accessSecret=hust_obs \
            -endpoint=http://127.0.0.1:9000 \
            -bucket=loadgen -objectNamePrefix=loadgen \
            -numClients=10 -numSamples=100 -objectSize=1024
        ```
        
    * [Script example](./run-s3bench.sh)
      
      * Customize before using this script, for a broader coverage.
      * [Windows version](./run-s3bench.cmd)
    
* Option 3: **s3-benchmark** <https://github.com/wasabi-tech/s3-benchmark>
    * **Installation** The original version contains broken dependency, lacks minio support, use one of its fixed fork instead
        ```bash
        go get -u github.com/chinglinwen/s3-benchmark
        ```
    * Command line example
        ```bash
        s3-benchmark \
            -a hust -s hust_obs -u http://127.0.0.1:9000 -b wasabi-benchmark \
            -d 3 -t 1 -z 1K
        Wasabi benchmark program v2.0
        Parameters: url=http://127.0.0.1:9000, bucket=wasabi-benchmark, region=us-east-1, duration=3, threads=1, loops=1, size=1K
        Loop 1: PUT time 3.0 secs, objects = 191, speed = 63.5KB/sec, 63.5 operations/sec. Slowdowns = 0
        Loop 1: GET time 0.4 secs, objects = 191, speed = 449.9KB/sec, 449.9 operations/sec. Slowdowns = 0
        Loop 1: DELETE time 0.5 secs, 367.2 deletes/sec. Slowdowns = 0
        result title: name-concurrency-size, uloadspeed, downloadspeed
        result csv: 127-1-1K,0.06,0.44
        ```

## Experiences and Problems

- [Known issues](known-issues.md).
- Contribute your experiences in <https://github.com/ShiZhan/obs-tutorial/wiki>.
- Report more problems in <https://github.com/ShiZhan/obs-tutorial/issues>.

# Basic Functionality

In computer programming, [create, read, update, and delete (as an acronym CRUD)](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) are the four basic functions of persistent storage.

| Operation        | SQL    | HTTP               |
| :---:            | :---:  | :---:              |
| Create           | INSERT | PUT / POST         |
| Read (Retrieve)  | SELECT | GET                |
| Update (Modify)  | UPDATE | PUT / POST / PATCH |
| Delete (Destroy) | DELETE | DELETE             |

Try object storage in some applciations: [zfile](https://github.com/zhaojun1998/zfile).

# Evaluation

**Metrics**: *Throughput*, *Latency* under different *object size*, *concurrency*, *server total*.

**Suggested topics**:

* How object size affects performance?
    * for a particular application, is there a best way to fit into OBS?
* The main factors behind I/O latency?
    * Get latency distribution first.
    * For evaluating percentile latency, s3bench is recommended.
* What will happen when clients are crowded?
* Why tests '**fail**'? (not terminate)
* The outcome of scaling out (putting more servers into system)?

More insights are encouraged.

## Further thoughts

* How to do these experiments on your own codes (besides COSBench)?
* Using Python as Lab Platform
    * Jupyter Notebook Tutorial <https://github.com/cs-course/jupyter-tutorial>

# Future Readings

- Recent SNIA blog posts on Object Storage <http://sniablog.org/category/object-storage/>.

- Enterprise level [Object Store comparison](http://gaul.org/object-store-comparison/).
- Build your own object storage system with Golang <https://github.com/stuarthu/go-implement-your-object-storage>.

Zhan.Shi @ 2017, 2018, 2019, 2020
