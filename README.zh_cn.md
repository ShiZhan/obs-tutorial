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

### Python怎么搞定

* 发行版:
    * 选项 1: [Anaconda](https://www.anaconda.com/)
        * 向这里伸手 <https://repo.continuum.io/archive/Anaconda3-5.1.0-Windows-x86_64.exe> 然后安装
    * 选项 2: [WinPython](http://winpython.github.io/)
        * 向这里伸手 <https://sourceforge.net/projects/winpython/files/WinPython_3.6/3.6.3.0/> 然后安装
* 用容器快速部署:
    * 选项 3: Python Docker <https://github.com/Zhan2012/python-lab>
        * `docker login daocloud.io && docker pull daocloud.io/zhan2016/python-lab:master-31a932d`

### Java怎么搞定

**同学期课程**: Java语言程序设计, [2017-2018 第2学期](http://jwc.hust.edu.cn/info/1161/6122.htm)

一些安装辅助脚本 <https://github.com/Zhan2012/java-bundle> (_**给喜欢自己琢磨的同学参考**_)。

### Git和Github (_**建议学习**_)

Git tutorial <https://github.com/cs-course/git-tutorial>。

如果需要不限数量的私密仓库，可以试一试 [bitbucket](https://bitbucket.org/)。

### docker容器怎么搞定 (_**可选**_)

如果计划尝试 Openstack Swift 或 Ceph，容器可以帮助简化部署，可参考 Docker tutorial <https://github.com/cs-course/docker-tutorial>。

## 对象存储服务端

* 初学者:
    * 选项 1: [Minio](https://minio.io/), 最新版 <https://minio.io/downloads.html>。
* 实验性模拟服务程序:
    * 选项 2: [fake-s3](https://github.com/jubos/fake-s3)，Amazon S3轻量级模仿。**需要Ruby**，首个S3克隆项目。
    * 选项 3: [mock-s3](https://github.com/jserver/mock-s3)，用Python重写fake-s3。**需要Python 2.7**。
        * 选项 3.1: **Python 3 移植(测试)版** <https://github.com/Zhan2012/mock-s3>。
    * 选项 4: [s3mock](https://github.com/findify/s3mock)，用Java/Scala实现S3模拟。**需要用Java/SBT构建**。
    * 选项 5: [S3Mock](https://github.com/adobe/S3Mock)，可以放进Docker容器或者JUnit规则的S3模拟。**需要用Java/SBT构建**，由Adobe (c)推出。
    * 选项 6: [s3proxy](https://github.com/gaul/s3proxy)，为各类存储提供S3 API。**预编译包[猛击此处](https://github.com/gaul/s3proxy/releases)**，或者可以自己用Java/Maven构建。
* 企业级项目:
    * 选项 7: [Openstack Swift](https://wiki.openstack.org/wiki/Swift)，开箱即用容器版: <https://github.com/cs-course/openstack-swift-docker>。
    * 选项 8: [Ceph](https://ceph.com/)，开箱即用容器版: <https://github.com/ceph/ceph-container>。

除初学用 _选项1_ 之外，_选项6_ 也提供免编译执行程序下载，仅需要Java虚拟机支持。

## 对象存储客户端

* 独立工具集:
    * 选项 1: Minio Client <https://docs.minio.io/docs/minio-client-quickstart-guide>
    * 选项 2: s3cmd <https://github.com/s3tools/s3cmd>
        * 于Python环境中运行 `pip install s3cmd`
        * 为 Minio 配置 <https://docs.minio.io/docs/s3cmd-with-minio>
    * 选项 3: aws-shell <https://github.com/awslabs/aws-shell>
        * 于Python环境中运行 `pip install aws-shell`
        * 为 Minio 配置 <https://docs.minio.io/docs/aws-cli-with-minio>
        * 官方手册 <https://docs.aws.amazon.com/cli/latest/userguide/using-s3-commands.html>
* APIs:
    * 选项 4: [aws-sdk-java](https://aws.amazon.com/cn/sdk-for-java/)
    * 选项 5: [boto](https://github.com/boto/boto3)

选项 2 & 3 更具通用性，已广泛用于各类云存储服务。

## 对象存储评测工具

* COSBench <https://github.com/intel-cloud/cosbench>
    * 指南 <https://github.com/intel-cloud/cosbench/raw/master/COSBenchUserGuide.pdf>。
    * 负载范例 <https://github.com/Zhan2012/obs-tutorial/raw/master/minio-workload-example.xml>。
    * 其余范例 <https://github.com/open-io/dockerfiles/tree/master/cosbench-openio/examples>。

### 参考文献

* COSBench: cloud object storage benchmark https://dl.acm.org/citation.cfm?doid=2479871.2479900
* COSBench: A Benchmark Tool for Cloud Object Storage Services <http://www.cs.cmu.edu/~qingzhen/files/cosbench_cloud12.pdf>
* COSBench: A benchmark tool for Cloud Storage <https://www.snia.org/sites/default/files/files2/files2/SDC2013/presentations/Cloud/YaguangWang__COSBench_Final.pdf>

# 基本功能

在计算机领域中，[create, read, update, and delete (缩写为 CRUD)](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) 是访问持久存储的4项基本操作。

| Operation        | SQL    | HTTP               |
| :---:            | :---:  | :---:              |
| Create           | INSERT | PUT / POST         |
| Read (Retrieve)  | SELECT | GET                |
| Update (Modify)  | UPDATE | PUT / POST / PATCH |
| Delete (Destroy) | DELETE | DELETE             |

# 评测

指标：*吞吐率Throughput*、*延迟Latency*，以及环境参数：*对象尺寸object size*、*并发性*、*服务器数量*。

建议思考:

* 对象尺寸如何影响性能?
    * 对于熟悉的某类应用，根据其数据访问特性，怎样适配对象存储最合适?
* I/O 延迟背后的关键影响要素?
    * 首先要采集全面的 I/O 延迟观测数据。
* 如果客户端爆满将怎样?
* 测试项为何出现 '**fail**'? (不是 terminate)
* 横向扩展系统 scaling out 效果如何 (向系统中追加更多存储服务器)?

不限于上述内容，鼓励更丰富思考。

## 更进一步

* 前述实验如何自己编程实现 (不借助于 COSBench)?
* 把 Python 当作自己的实验台
    * Jupyter Notebook Tutorial <https://github.com/cs-course/jupyter-tutorial>

# 扩展资料

对象存储方面 SNIA 最新博文 <http://sniablog.org/category/object-storage/>。

企业级 [对象存储比较](http://gaul.org/object-store-comparison/)。

Zhan.Shi @ 2018
