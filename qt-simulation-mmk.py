import simpy
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import argparse

def handler(env, name, server, service_time, latencies):
    """顾客进程"""
    arrive_time = env.now
    print(f"{name} arrives at time {arrive_time:.2f}")
    
    with server.request() as req:
        yield req
        
        start_service_time = env.now
        print(f"{name} starts being handled at time {start_service_time:.2f}")
        
        yield env.timeout(service_time)
        
        end_service_time = env.now
        latency = end_service_time - arrive_time
        print(f"{name} finishes at time {end_service_time:.2f}, total service time: {latency:.2f}")
        
        # record request latency in latencies list
        latencies.append(latency)

def simulate(λ, μ, r, latencies, server):
    """模拟函数"""
    for i in range(r):
        service_time = random.expovariate(μ)
        env.process(handler(env, f"REQUEST {i+1}", server, service_time, latencies))
        
        inter_arrival_time = random.expovariate(λ)
        yield env.timeout(inter_arrival_time)
    
    yield env.timeout(0)  # 等待所有请求完成
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--lamda", type=float, default=9, help="Arrival rate (default: 9)")
    parser.add_argument("-m", "--mu", type=float, default=10, help="Service rate (default: 10)")
    parser.add_argument("-k", "--servers", type=int, default=1, help="Number of servers (default: 1)")
    parser.add_argument("-r", "--requests", type=int, default=100, help="Number of requests to simulate (default: 100)")
    args = parser.parse_args()

    latencies = []
    random.seed(42)

    env = simpy.Environment()
    server = simpy.Resource(env, capacity=args.requests)

    env.process(simulate(args.lamda, args.mu, args.requests, latencies, server))
    env.run()

    # Save latencies to a CSV file
    with open('latencies.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Latency'])  # Write header
        writer.writerows([[latency] for latency in latencies])  # Write data

    """绘制累计概率分布图"""
    ax = plt.gca()
    ax.yaxis.set_major_formatter(PercentFormatter(xmax=1, decimals=1))

    plt.xlim(0, max(latencies))
    plt.hist(latencies, cumulative=True, histtype='step', weights=[1./ len(latencies)] * len(latencies))

    # 排队论模型
    # F(t)=1-e^(-1*a*t)
    μ_λ = args.mu - args.lamda
    X_qt = np.arange(0, max(latencies), .01)
    Y_qt = 1 - np.exp(-1 * μ_λ * X_qt)
    # 绘制排队论模型拟合
    plt.plot(X_qt, Y_qt)

    plt.grid()
    plt.show()
