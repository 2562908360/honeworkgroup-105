import SM3
import random
import time

def rho(exm):
    num = int(exm/4)                # 16进制位数
    x = hex(random.randint(0, 2**(exm+1)-1))[2:]
    x_1 = SM3.SM3(x)               
    x_2 = SM3.SM3(x_1)
    i =1
    while x_1[:num] != x_2[:num]:
        i += 1
        x_1 = SM3.SM3(x_1)              
        x_2 = SM3.SM3(SM3.SM3(x_2))     
    x_2 = x_1           
    x_1 = x         
    for j in range(i):
        if SM3.SM3(x_1)[:num] == SM3.SM3(x_2)[:num]:
            return SM3.SM3(x_1)[:num], x_1, x_2
        else:
            x_1 = SM3.SM3(x_1)
            x_2 = SM3.SM3(x_2)


if __name__ == '__main__':
    example = 16    # 此处进行前8bit的碰撞以作演示
    start_time = time.perf_counter()
    col, m1, m2 = rho(example)
    end_time = time.perf_counter()
    execution_time = (end_time - start_time) * 1000
    print("找到碰撞！")
    print("消息1:", m1)
    print("消息2:", m2)
    print("两者哈希值的前{}bit相同，16进制表示为:{}".format(example, col))
    print("执行时间为：", execution_time, "毫秒")
