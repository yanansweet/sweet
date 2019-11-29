tank = []
def sweet_FUN_SplitIntNumber(a): # 输出整数各个位数值
    while 1:
        tank.extend([a%10])
        a //= 10
        if a<=0:
            break
    return tank

a = int(input())      
sweet_FUN_SplitIntNumber(a)
print(tank[::-1])