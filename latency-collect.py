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
    obj_name = "testObj%08d"%(i,)
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
for i in range(2000):
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

# 记录延迟

with open("latency.csv", "w+") as tracefile:
    tracefile.write("latency\n")
    tracefile.writelines([str(l) + '\n' for l in latency])

