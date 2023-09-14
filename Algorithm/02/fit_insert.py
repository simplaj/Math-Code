import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.optimize import curve_fit

# 数据拟合示例

# 定义待拟合的函数模型
def func(x, a, b, c):
    return a * np.exp(-b * x) + c

# 生成带噪声的数据
x = np.linspace(0, 4, 50)
y = func(x, 2.5, 1.3, 0.5)
y_noise = y + 0.2 * np.random.normal(size=len(x))

# 使用 curve_fit 进行拟合
params, params_covariance = curve_fit(func, x, y_noise)

# 绘制原始数据和拟合曲线
plt.scatter(x, y_noise, label='Data')
plt.plot(x, func(x, *params), color='red', label='Fit')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()


# 参数估计示例

# 生成一组随机样本
data = np.random.normal(loc=0, scale=1, size=100)

# 估计均值和标准差
mean_estimated = np.mean(data)
std_estimated = np.std(data, ddof=1)

# 绘制直方图和核密度估计曲线
sns.histplot(data, kde=True)
plt.axvline(mean_estimated, color='red', linestyle='dashed', label='Mean')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()
plt.show()


# 插值示例

from scipy.interpolate import interp1d

# 原始数据
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 2, 1, 3, 7, 10])

# 创建插值函数
f = interp1d(x, y, kind='linear')

# 在新位置进行插值
x_new = np.linspace(0, 5, num=50)
y_new = f(x_new)

# 绘制原始数据和插值曲线
plt.scatter(x, y, label='Data')
plt.plot(x_new, y_new, color='red', label='Interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
