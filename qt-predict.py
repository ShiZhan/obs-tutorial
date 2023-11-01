"""
用排队论模型分析尾延迟分布的变化
"""

import numpy as np
# from scipy.stats import poisson
from scipy.special import factorial
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from matplotlib.ticker import PercentFormatter

# 1. 给出请求到达率λ，绘制泊松分布曲线

# 参数：平均请求到达率λ
def arrival(x, λ):
    # return poisson.pmf(k=x, mu=λ)
    return np.power(λ, x) / factorial(x) * np.exp(-λ)

# 单位时间事件数量
x1 = np.linspace(0, 99, 100)

# 平均到达率、服务率初始值
init_arrival_rate = 10

# 绘图
fig1, ax1 = plt.subplots()
line1, = ax1.plot(x1, arrival(x1, init_arrival_rate), lw=2)
ax1.set_xlabel('arrival speed')

# 绘图区域留空给滑动条
fig1.subplots_adjust(bottom=0.25)

# 设置请求到达率滑动条
ax_arrival_rate = fig1.add_axes([0.2, 0.1, 0.5, 0.03])
slider_arrival_rate = Slider(
    ax=ax_arrival_rate,
    label='arrival rate',
    valmin=0,
    valmax=50,
    valstep=1,
    valinit=init_arrival_rate,
)

# 刷新绘图
def update1(val):
    line1.set_ydata(arrival(x1, slider_arrival_rate.val))
    fig1.canvas.draw_idle()

# 注册参数刷新函数
slider_arrival_rate.on_changed(update1)

# λ重置按钮
resetax1 = fig1.add_axes([0.8, 0.025, 0.1, 0.04])
button1 = Button(resetax1, 'Reset', hovercolor='0.975')

def reset1(event):
    slider_arrival_rate.reset()

button1.on_clicked(reset1)

# 2. 给出请求到达率λ和服务速率μ，使用排队论模型预测延迟分布

def queueing_model(x, λ, μ):
    return 1 - np.exp(-1*(μ-λ)*x)

x2 = np.linspace(0, 10, 100)

init_λ = 10
init_μ = 20

fig2, ax2 = plt.subplots()
line2, = ax2.plot(x2, queueing_model(x2, init_λ, init_μ), lw=2)
ax2.set_xlabel('latency')
ax2.set_xticks(np.linspace(0, 10, 11))
ax2.set_xticks(np.linspace(0, 10, 21), minor=True)
ax2.grid(which='both', alpha=0.3)
ax2.yaxis.set_major_formatter(PercentFormatter(xmax=1, decimals=1)) # 纵轴用百分位指标

fig2.subplots_adjust(bottom=0.25)

# 请求到达率调节条
λ_ax = fig2.add_axes([0.1, 0.1, 0.3, 0.03])
λ_slider = Slider(
    ax=λ_ax,
    label='λ',
    valmin=0,
    valmax=50,
    valstep=1,
    valinit=init_λ,
)

# 服务速率调节条
μ_ax = fig2.add_axes([0.5, 0.1, 0.3, 0.03])
μ_slider = Slider(
    ax=μ_ax,
    label='μ',
    valmin=0,
    valmax=50,
    valstep=1,
    valinit=init_μ,
)

# 绘图更新，基于即时更新的λ和μ
def update_λ_μ(val):
    line2.set_ydata(queueing_model(x2, λ_slider.val, μ_slider.val))
    fig2.canvas.draw_idle()

λ_slider.on_changed(update_λ_μ)
μ_slider.on_changed(update_λ_μ)

# λ、μ重置按钮
resetax2 = fig2.add_axes([0.8, 0.025, 0.1, 0.04])
button2 = Button(resetax2, 'Reset', hovercolor='0.975')

def reset2(event):
    λ_slider.reset()
    μ_slider.reset()

button2.on_clicked(reset2)

plt.show()
