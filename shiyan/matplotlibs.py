# import numpy as np
# import matplotlib as mpl
# import matplotlib.pyplot as plt
#
# # 通过rcParams设置全局横纵轴字体大小
# mpl.rcParams['xtick.labelsize'] = 24
# mpl.rcParams['ytick.labelsize'] = 24
#
# np.random.seed(42)
#
# # x轴的采样点
# x = np.linspace(0, 5, 100)
#
# # 通过下面曲线加上噪声生成数据，所以拟合模型就用y了……
# y = 2*np.sin(x) + 0.3*x**2
# y_data = y + np.random.normal(scale=0.3, size=100)
#
# # figure()指定图表名称
# plt.figure('data')
#
# # '.'标明画散点图，每个散点的形状是个圆
# plt.plot(x, y_data, '.')
# plt.show()
a=[[1,2,3],
   [3,4,5],
   [4,5,6]]
print(a)
print(type(a))