"""
用排队论模型分析尾延迟分布的变化
"""

import numpy as np
# from scipy.stats import poisson
from scipy.special import factorial
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

# *泊松分布*

# 参数：平均请求到达率λ
def arrival(x, λ):
    # return poisson.pmf(k=x, mu=λ)
    return np.power(λ, x) / factorial(x) * np.exp(-λ)

# 单位时间事件数量
x1 = np.linspace(0, 99, 100)

# 平均到达率、服务率初始值
init_λ = 10
init_μ = 15

# 绘图
fig1, ax1 = plt.subplots()
line1, = ax1.plot(x1, arrival(x1, init_λ), lw=2)
ax1.set_xlabel('arrival speed')

# 绘图区域留空给滑动条
fig1.subplots_adjust(bottom=0.25)

# λ设置滑动条
ax_λ = fig1.add_axes([0.1, 0.1, 0.5, 0.03])
λ_slider = Slider(
    ax=ax_λ,
    label='λ',
    valmin=0,
    valmax=50,
    valstep=1,
    valinit=init_λ,
)

# 刷新绘图
def update1(val):
    line1.set_ydata(arrival(x1, λ_slider.val))
    fig1.canvas.draw_idle()
    line2.set_ydata(np.exp(-x2))
    fig2.canvas.draw_idle()

# 注册参数刷新函数
λ_slider.on_changed(update1)

# λ重置按钮
resetax1 = fig1.add_axes([0.8, 0.025, 0.1, 0.04])
button1 = Button(resetax1, 'Reset', hovercolor='0.975')

def reset1(event):
    λ_slider.reset()

button1.on_clicked(reset1)

# *排队论预测延迟*

def queueing_model(x):
    return 1 - np.exp(-x)

x2 = np.linspace(0, 10, 100)

fig2, ax2 = plt.subplots()
line2, = ax2.plot(x2, queueing_model(x2), lw=2)
ax2.set_xlabel('latency')

fig2.subplots_adjust(bottom=0.25)

ax_μ = fig2.add_axes([0.6, 0.1, 1.0, 0.03])
μ_slider = Slider(
    ax=ax_μ,
    label='μ',
    valmin=0,
    valmax=50,
    valstep=1,
    valinit=init_μ,
)

def update2(val):
    line2.set_ydata(queueing_model(x2))
    fig2.canvas.draw_idle()

μ_slider.on_changed(update2)

# λ重置按钮
resetax2 = fig2.add_axes([0.8, 0.025, 0.1, 0.04])
button2 = Button(resetax2, 'Reset', hovercolor='0.975')

def reset(event):
    μ_slider.reset()

button2.on_clicked(reset)

plt.show()
