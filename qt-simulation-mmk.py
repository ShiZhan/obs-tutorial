import argparse
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import time
import random

def mmk_simulation(lambda_param, mu, R, k):
    # 初始化队列和服务时间列表
    queue = []
    latency = []

    # 开始仿真
    for i in range(R):
        # 根据到达率计算请求到达时间
        arrival_time = np.random.exponential(1/lambda_param)
        time.sleep(arrival_time)

        # 请求到达，加入队列
        queue.append(i)

        # 如果服务台空闲，开始服务
        if len(queue) <= k:
            start_time = time.time()
            service_time = np.random.exponential(1/mu)
            time.sleep(service_time)
            end_time = time.time()
            latency.append(end_time - start_time)
            queue.pop(0)
        else:
            # 如果队列过长，等待服务
            start_time = time.time()
            while len(queue) > k:
                time.sleep(0.01)
            service_time = np.random.exponential(1/mu)
            time.sleep(service_time)
            end_time = time.time()
            latency.append(end_time - start_time)
            queue.pop(0)

    return latency

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--arrival", type=float, default=9, help="请求到达率λ")
    parser.add_argument("-m", "--mu", type=float, default=10, help="服务速率μ")
    parser.add_argument("-r", "--requests", type=int, default=10, help="总请求数R")
    parser.add_argument("-k", "--servers", type=int, default=1, help="服务台数k")
    args = parser.parse_args()

    latency = mmk_simulation(args.arrival, args.mu, args.requests, args.servers)

    ax = plt.gca()
    ax.yaxis.set_major_formatter(PercentFormatter(xmax=1, decimals=1))
    plt.xlim(0, max(latency))
    plt.hist(latency, cumulative=True, histtype='step', weights=[1./ len(latency)] * len(latency))
    plt.grid()
    plt.show()
