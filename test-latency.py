import botocore
from boto3.session import Session
import time
import throttle

# 准备密钥
aws_access_key_id = 'hust'
aws_secret_access_key = 'hust_obs'

# 建立会话
session = Session(aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# 连接到服务
s3 = session.resource('s3', endpoint_url='http://127.0.0.1:9000')

# 查看所有bucket
for bucket in s3.buckets.all():
    print('bucket name:%s' % bucket.name)

# 新建一个bucket(bucket name 中不能有_下划线)
bucket_name = 'test100objs'
if s3.Bucket(bucket_name) not in s3.buckets.all():
    s3.create_bucket(Bucket=bucket_name)

# 查看一个bucket下的所有object
bucket = s3.Bucket(bucket_name)
for obj in bucket.objects.all():
    print('obj name:%s' % obj.key)

# 发起请求和计算系统停留时间
def request_timing(i):
    # 上传obj
    obj_name = "testObj%03d"%(i,)
    local_file = 'README.md'
    # temp_file = '.tempfile'
    service_time = 0
    start = time.time()
    s3.Object(bucket_name, obj_name).upload_file(local_file)
    # 或
    # bucket.put_object(Key=obj_name, Body=open(local_file, 'rb'))
    # 下载obj
    # s3.Object(bucket_name, obj_name).download_file(temp_file)
    end = time.time()
    system_time = end - start
    return system_time * 1000 # 换算为毫秒

# 按照请求到达率限制来执行和跟踪请求
@throttle.wrap(0.1, 2) # 100ms 2 个
def arrival_rate_2(i):
    return request_timing(i)

@throttle.wrap(0.1, 4)
def arrival_rate_4(i):
    return request_timing(i)

@throttle.wrap(0.1, 8)
def arrival_rate_8(i):
    return request_timing(i)

# 按照前述间隔连续发起请求
latency = []
for i in range(100):
    # 上传obj
    st = arrival_rate_8(i)
    succ = not st is throttle.fail
    print(succ, st)
    if succ:
        latency.append(st)

# 删除bucket(只能删除空的bucket)
try:
    # 删除bucket下所有object
    bucket.objects.filter().delete()

    # 删除bucket下某个object
    # bucket.objects.filter(Prefix=obj_name).delete()

    bucket.delete()
except botocore.exceptions.ClientError as e:
    print('error in bucket removal')

# 绘图
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from matplotlib.pyplot import MultipleLocator, plot

plt.subplot(211)
plt.plot(latency)
plt.subplot(212)
plt.plot(sorted(latency, reverse=True))
plt.show()

# 排队论模型
import numpy as np

# F(t)=1-e^(-1*a*t)
alpha = 0.3
X_qt = np.arange(min(latency), max(latency), 1.)
Y_qt = 1 - np.exp(alpha * (min(latency) - X_qt))
plt.plot(X_qt, Y_qt)

# 百分比换算
def to_percent(y, position):
    return str(100 * round(y, 2)) + "%"

plt.hist(latency, cumulative=True, histtype='step', weights=[1./ len(latency)] * len(latency))
fomatter = FuncFormatter(to_percent)
ax = plt.gca()
# ax.xaxis.set_major_locator(MultipleLocator(5))
ax.yaxis.set_major_formatter(fomatter)
x_min = max(min(latency) * 0.8, min(latency) - 5)
x_max = max(latency)
plt.xlim(x_min, x_max)
plt.grid()
plt.show()