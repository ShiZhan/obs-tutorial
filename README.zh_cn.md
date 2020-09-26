# 介绍

对象存储入门实践。

## 基本概念

网络存储工业协会 SNIA 对象存储入门:
* [Object Storage 101](http://www.snia.org/sites/default/files/Object_Storage_101.pdf)
* [Object Storage 201](https://www.snia.org/sites/default/files/Object_Storage_201_Final_1.pdf)
* [Object Storage Technology](http://www.snia.org/sites/default/education/tutorials/2013/spring/file/BrentWelch_Object_Storage_Technology.pdf)

**网络存储工业协会 Storage Networking Industry Association** ([SNIA](https://www.snia.org/)) 是由来自于全球存储市场的众多企业组建的全球性非盈利组织。

# 准备工作

## 基础环境

### Git和Github

Git tutorial <https://github.com/cs-course/git-tutorial>

替代方案

- [bitbucket](https://bitbucket.org/)
- [gitlab](https://about.gitlab.com/)
- [码云](https://gitee.com/)

### Python怎么搞定

* 发行版
    * 选项 1: [Anaconda](https://www.anaconda.com/)
    * 选项 2: [WinPython](http://winpython.github.io/)
* 用容器快速部署 (_**可选**_)
    * 选项 3: Python Docker <https://github.com/cs-course/python-lab>
        * dockerhub (docker大本营) `docker pull zhan2016/python-lab:3.6.0`
        * daocloud (国内平台) `docker login daocloud.io && docker pull daocloud.io/zhan2016/python-lab:master-31a932d`

### Java怎么搞定

**同学期课程**: Java语言程序设计, [2019-2020 第2学期](http://jwc.hust.edu.cn/info/1161/7796.htm)

一些安装辅助脚本 <https://github.com/ShiZhan/java-bundle> (_**给喜欢自己琢磨的同学参考**_)

### Go怎么搞定

* 国内资料 <https://studygolang.com/>
* 墙外本体 <https://golang.org/>
* 经典书籍 <https://github.com/Unknwon/the-way-to-go_ZH_CN>
* 学习资料荟萃 <https://github.com/uhub/awesome-go>

### 怎么在Windows或者MacOS里面跑Linux (_**可选**_)

**目的**: 计划无伤尝试 mock-s3 或 s3proxy

**工具**: Virtualbox, VMWare ...

直奔图形界面，或者参考 Vagrant tutorial <https://github.com/cs-course/vagrant-tutorial>

### docker容器怎么搞定 (_**可选**_)

**目的**: 计划尝试 Openstack Swift 或 Ceph

使用容器简化部署，容器使用可参考 Docker tutorial <https://github.com/cs-course/docker-tutorial>

- [Ceph官方容器](https://hub.docker.com/r/ceph/ceph)
- [Swift简易容器](https://hub.docker.com/r/fnndsc/docker-swift-onlyone)

## 对象存储服务端

* 初学者:
    * 选项 1: [Minio](https://minio.io/), 最新版 <https://minio.io/downloads.html>。
* 实验性模拟服务程序:
    * 选项 2: [mock-s3](https://github.com/ShiZhan/mock-s3)，用Python重写fake-s3模仿Amazon S3。
        * 选项 2.1: 原始版**需要Python 2.7** <https://github.com/jserver/mock-s3>。
    * 选项 3: [s3proxy](https://github.com/gaul/s3proxy)，为各类存储提供S3 API。**预编译包[猛击此处](https://github.com/gaul/s3proxy/releases)**
        * 选项 3.1: 自己用Java/Maven从源码构建 `mvn package -Dmaven.test.skip=true`。
    * 选项 4: [fake-s3](https://github.com/jubos/fake-s3)，Amazon S3轻量级模仿。**需要Ruby**，首个S3克隆项目。
    * 选项 5: [s3mock](https://github.com/findify/s3mock)，用Java/Scala实现S3模拟。**需要用Java/SBT构建**。
    * 选项 6: [S3Mock](https://github.com/adobe/S3Mock)，可以放进Docker容器或者JUnit规则的S3模拟。**需要用Java/SBT构建，需要Docker运行**，由Adobe (c)推出。
* 企业级项目:
    * 选项 7: [Openstack Swift](https://wiki.openstack.org/wiki/Swift)，开箱即用容器版: <https://github.com/cs-course/openstack-swift-docker>。
    * 选项 8: [Ceph](https://ceph.com/)，开箱即用容器版: <https://github.com/ceph/ceph-container>。

除初学用 *选项1* 之外，*选项2,3* 也提供免编译执行程序下载。

## 对象存储客户端

* 独立工具集:
    * 选项 1: **Minio Client** <https://docs.minio.io/docs/minio-client-quickstart-guide>
    * 选项 2: **s3cmd** <https://github.com/s3tools/s3cmd>
        * 于Python环境中运行 `pip install s3cmd`
        * 为 Minio 配置 <https://docs.minio.io/docs/s3cmd-with-minio>
    * 选项 3: **aws-shell** <https://github.com/awslabs/aws-shell>
        * 于Python环境中运行 `pip install aws-shell`
        * 为 Minio 配置 <https://docs.minio.io/docs/aws-cli-with-minio>
        * 官方手册 <https://docs.aws.amazon.com/cli/latest/userguide/using-s3-commands.html>
    * 选项 4: **osm** <https://github.com/appscode/osm>
        * `go get -u github.com/appscode/osm`
        * [Windows版执行程序](https://share.weiyun.com/jPYFmvmw)
* 编程 API:
    * 选项 4: **aws-sdk-java** <https://aws.amazon.com/cn/sdk-for-java/>
    * 选项 5: **boto** <https://github.com/boto/boto3>

*选项 1* 提供可执行文件，开箱即用，*选项 2 & 3* 需要 Python 环境，*选项 4* 需要 go 环境。

## 对象存储评测工具

* 选项 1: **COSBench** <https://github.com/intel-cloud/cosbench>
    * 指南 <https://github.com/intel-cloud/cosbench/raw/master/COSBenchUserGuide.pdf>
    * 负载范例 <https://github.com/cs-course/obs-tutorial/raw/master/workload-example.xml>
    * 其余范例 <https://github.com/open-io/dockerfiles/tree/master/cosbench-openio/examples>
    * 文献
      * COSBench: cloud object storage benchmark https://dl.acm.org/citation.cfm?doid=2479871.2479900
      * COSBench: A Benchmark Tool for Cloud Object Storage Services <http://www.cs.cmu.edu/~qingzhen/files/cosbench_cloud12.pdf>
      * COSBench: A benchmark tool for Cloud Storage <https://www.snia.org/sites/default/files/files2/files2/SDC2013/presentations/Cloud/YaguangWang__COSBench_Final.pdf>
* 选项 2: **S3 Bench** <https://github.com/igneous-systems/s3bench>
    * **安装**
        ```bash
        go get -u github.com/igneous-systems/s3bench
        ```
        
        * Linux: 编译文件缺省位置在 `~/go/bin/s3bench`
        * [预编译Windows执行程序](https://share.weiyun.com/BICMfA4G)，需下载放置在本资料库所在目录中。
        
    * 命令行范例
    
        ```bash
        s3bench \
            -accessKey=hust -accessSecret=hust_obs \
            -endpoint=http://127.0.0.1:9000 \
            -bucket=loadgen -objectNamePrefix=loadgen \
            -numClients=10 -numSamples=100 -objectSize=1024
        ```
    
    * [脚本范例](./run-s3bench.sh)
      
        - 实际使用建议通过定制参数，设计循环结构实现批量测试，将结果重定向进文件用于后期分析。
        - [Windows版](./run-s3bench.cmd)
* 选项 3: **s3-benchmark** <https://github.com/wasabi-tech/s3-benchmark>
    * **安装** 原始版本未更新依赖，且兼容性不足，可以用这个修补版本
        ```bash
        go get -u github.com/chinglinwen/s3-benchmark
        ```
    * 命令行范例
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

## 各类已知问题

* 安装使用过程中的各种["坑"](known-issues.md)
* 经验分享<https://github.com/cs-course/obs-tutorial/wiki>
* 问题报告<https://github.com/cs-course/obs-tutorial/issues>

# 基本功能

在计算机领域中，[create, read, update, and delete (缩写为 CRUD)](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) 是访问持久存储的4项基本操作。

| Operation        | SQL    | HTTP               |
| :---:            | :---:  | :---:              |
| Create           | INSERT | PUT / POST         |
| Read (Retrieve)  | SELECT | GET                |
| Update (Modify)  | UPDATE | PUT / POST / PATCH |
| Delete (Destroy) | DELETE | DELETE             |

在实际应用里面试一试：[zfile](https://github.com/zhaojun1998/zfile)。

# 评测

指标：*吞吐率Throughput*、*延迟Latency*，以及环境参数：*对象尺寸object size*、*并发性*、*服务器数量*。

建议思考:

* 对象尺寸如何影响性能?
    * 对于熟悉的某类应用，根据其数据访问特性，怎样适配对象存储最合适?
* I/O 延迟背后的关键影响要素?
    * 首先要采集全面的 I/O 延迟观测数据。
    * 百分位延迟观测需使用s3bench，然后即可分析尾延迟影响因素。
* 如果客户端爆满将怎样?
* 测试项为何出现 '**fail**'? (不是 terminate)
* 横向扩展系统 (Scaling Out) 效果如何 (向系统中追加更多存储服务器)?

不限于上述内容，鼓励更丰富思考。

## 更进一步

* 前述实验如何自己编程实现 (不借助于 COSBench、s3bench)?
* 把 Python 当作自己的实验台
    * Jupyter Notebook Tutorial <https://github.com/cs-course/jupyter-tutorial>

# 扩展资料

* 对象存储方面 SNIA 最新博文 <http://sniablog.org/category/object-storage/>
* 企业级 [对象存储比较](http://gaul.org/object-store-comparison/)
* [用Go语言自制对象存储系统](https://github.com/stuarthu/go-implement-your-object-storage)

Zhan.Shi @ 2017, 2018, 2019, 2020
