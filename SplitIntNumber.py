# 功能：将整数的各个位数拆分开
# 创建人：常甜甜
# 创建时间：2019-11-29
# 隶属:西安邮电大学理学院
# 联系方式：80078358@qq.com

a = int(input())
tank = [] # 输出整数各个位数值

while 1:
    tank.extend([a%10])
    a //= 10
    if a<=0:
        break

print(tank[::-1])