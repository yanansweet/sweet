# 打印水仙花数
tank = []
def sweet_FUN_SplitIntNumber(a): # 输出整数a，输出a各个位数值到tank
    while 1:
        tank.extend([a%10])
        a //= 10
        if a<=0:
            break
    return tank

def sweet_FUN_Narcissus():
    
    sweet_FUN_SplitIntNumber(a) # 调用函数，输入整数，得到整数各数位值
    
    for i in range(len(tank)):
        
        Narcissues = 1
        
        Narcissues = 0
        
    return Narcissues
    
# Input = int(input())
a = 153
sweet_FUN_Narcissus(a)