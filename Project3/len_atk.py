import SM3
import time
def len_ext_atk(msg, ext, n):
    h_m = SM3.SM3(msg)  # H(m)
    #print('h_m='+h_m)
    Hm = [int(h_m[i * 8:i * 8 + 8], 16) for i in range(8)]
    #print('Hm=',Hm)
    len_e = hex((n + len(ext) ) * 4)[2:]  # 总消息位长
    #print('len_e='+len_e)
    len_e = (16-len(len_e))*'0'+len_e
    #print('len_e='+len_e)
    ext = ext + '8'
    tmp = len(ext)%128
    if tmp > 112:
        ext = ext + '0' * (128 - tmp + 112) + len_e
    else:
        ext = ext + '0' * (112 - tmp) + len_e
    ext_g = SM3.Group(ext) #数组分组
    #print('ext_g = ',ext_g)
    len_ext_g = len(ext_g) #分组个数
    #print('len_ext_g = ',len_ext_g)
    V = [Hm]
    #print('V=',V)
    for i in range(len_ext_g):
        V.append(SM3.CF(V,ext_g,i))
        #print('V=',V)
    res = ''
    for x in V[len_ext_g]:
        res += hex(x)[2:]
        #print('res = ',res)
    return res

if __name__ == '__main__':
    message = '11111111'     # 原始消息
    extend = '222'         # 扩展部分
    if len(message) % 128 < 112:
        
        n = (int(len(message) / 128) + 1) * 128  # 16进制数个数
    else:
        n = (int(len(message) / 128) + 2) * 128  # 16进制数个数
    len_m = hex(len(message)*4)[2:]
    len_m = (16 - len(len_m)) * '0' + len_m  # 消息长度
    pad = n - len(message) - 16 - 1                # 补0个数=总长-消息-消息长度-1
    new_m = message + '8' + pad*'0' + len_m + extend    # new_m = message||1000...|| |message| ||extend
    res_new = SM3.SM3(new_m)
    start_time = time.perf_counter()
    res = len_ext_atk(message, extend, n)
    print("新消息的哈希值为:", res_new)
    print("长度扩展攻击结果:", res)
    if res_new == res:
        print("长度扩展攻击成功!")
    else:
        print("长度扩展攻击失败!")
    end_time = time.perf_counter()
    execution_time = (end_time - start_time) * 1000
    print("执行时间为：", execution_time, "毫秒")
