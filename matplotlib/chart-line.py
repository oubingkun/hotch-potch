#codding=utf-8
import pandas as pd
from matplotlib import pyplot as plt


sourcefile = u"C:/Users/Administrator/Desktop/CZURScanner文档/CZCVTestData/data.xlsx"
data = pd.read_excel(sourcefile)


plt.figure(figsize=(10,5))
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

plt.title('迭代版本速度状态',fontsize=16)
plt.xlabel(u'版本',fontsize=10)
plt.ylabel(u'速度',fontsize=10)

#color：颜色，linewidth：线宽，linestyle：线条类型，label：图例，marker：数据点的类型
plt.plot(data['版本'],data['速度'],color="blue",linewidth=2,linestyle=":",label="version",marker='o')
plt.legend(loc=1)
plt.show()

