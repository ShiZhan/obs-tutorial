import boto3
import time
import random
import matplotlib.pyplot as plt
import numpy as np

# 配置 MinIO 参数
minio_endpoint = 'http://10.12.56.182:9000'
access_key = 'hust'
secret_key = 'hust_obs'
bucket_name = 'delay-experiment-bucket'

# 初始化 S3 客户端
s3_client = boto3.client(
    's3',
    endpoint_url=minio_endpoint,
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    region_name='us-east-1'
)

# 创建存储桶（如果不存在），并清空已有内容
def create_and_empty_bucket(bucket_name):
    try:
        s3_client.create_bucket(Bucket=bucket_name)
        print(f"Bucket {bucket_name} created.")
    except Exception as e:
        print(f"Bucket {bucket_name} already exists or error: {e}")

    # 列出并删除所有对象
    try:
        objects = s3_client.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in objects:
            for obj in objects['Contents']:
                s3_client.delete_object(Bucket=bucket_name, Key=obj['Key'])
            print(f"All objects in {bucket_name} deleted.")
        else:
            print(f"No objects found in bucket {bucket_name}.")
    except Exception as e:
        print(f"Error deleting objects: {e}")


# 生成随机文件内容
def generate_random_data(size=4*1024):  # 4KB
    return b'0' * size

# 记录延迟的函数
def measure_latency(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    return end_time - start_time

# 上传文件并记录延迟（使用顺序编号）
def upload_file(file_size=4*1024, file_index=0):
    file_name = f'test_file_{file_index}.txt'  # 使用顺序编号
    data = generate_random_data(file_size)
    try:
        s3_client.put_object(Bucket=bucket_name, Key=file_name, Body=data)
        return measure_latency(s3_client.put_object, Bucket=bucket_name, Key=file_name, Body=data)
    except Exception as e:
        print(f"Upload failed: {e}")
        return None

# 下载文件并记录延迟
def download_file(file_name):
    try:
        response = s3_client.get_object(Bucket=bucket_name, Key=file_name)
        content = response['Body'].read()
        return measure_latency(s3_client.get_object, Bucket=bucket_name, Key=file_name)
    except Exception as e:
        print(f"Download failed: {e}")
        return None

# 执行实验
def run_experiment(num_operations=1000):
    upload_latencies = []
    download_latencies = []

    # Step 1: Upload 1000 sequentially named files
    for i in range(1, num_operations + 1):
        upload_latency = upload_file(file_index=i)
        if upload_latency is not None:
            upload_latencies.append(upload_latency)

    # Step 2: Randomly download from the 1000 uploaded files
    for _ in range(num_operations):
        file_index = random.randint(1, num_operations)  # 随机选择一个文件编号
        file_name = f'test_file_{file_index}.txt'
        download_latency = download_file(file_name)
        if download_latency is not None:
            download_latencies.append(download_latency)

    return upload_latencies, download_latencies

# 主程序
if __name__ == '__main__':
    create_and_empty_bucket(bucket_name)  # 清空存储桶

    upload_latencies, download_latencies = run_experiment(num_operations=500)

    # 绘制延迟分布直方图
    plt.figure(figsize=(12, 6))
    plt.hist(upload_latencies, bins=20, alpha=0.7, label='Upload Latency')
    plt.hist(download_latencies, bins=20, alpha=0.7, label='Download Latency')
    plt.title('Object Storage Latency Distribution')
    plt.xlabel('Latency (seconds)')
    plt.ylabel('Frequency')
    plt.legend()
    plt.grid(True)
    plt.show()

    # 保存下载延迟到 latency.csv
    import pandas as pd
    pd.DataFrame(download_latencies, columns=["Latency"]).to_csv("latency.csv", index=False)
    print("Download latencies saved to latency.csv")
