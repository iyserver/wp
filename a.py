# 引入numpy模块并创建两个向量x和y
import numpy as np
slark=1
while(slark):
 a1 = float(input("请输入第一个向量x1= "))
 a2 = float(input("请输入第一个向量y1= "))
 a3 = float(input("请输入第一个向量z1= "))
 b1 = float(input("请输入第二个向量x2= "))
 b2 = float(input("请输入第二个向量y2= "))
 b3 = float(input("请输入第二个向量z2= "))
 x=np.array((a1,a2,a3))
 y=np.array([b1,b2,b3])

# 分别计算两个向量的模：
 l_x=np.sqrt(x.dot(x))
 l_y=np.sqrt(y.dot(y))
 print('向量的模=',l_x,l_y)

# 计算两个向量的点积
 dian=x.dot(y)
 print('向量的点积=',dian)

# 计算夹角的cos值：
 cos_=dian/(l_x*l_y)
 print('夹角的cos值=',cos_)

# 求得夹角（弧度制）：
 angle_hu=np.arccos(cos_)
 print('夹角（弧度制）=',angle_hu)

# 转换为角度值：
 angle_d=angle_hu*180/np.pi
 print('夹角=%f°'%angle_d)
