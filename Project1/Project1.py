from gmssl import sm3,func
import time
import secrets
import random
import string
#随机生成一段长度为N的字符串
def getrandom(N):
    choice_str = string.ascii_letters + string.digits + string.punctuation
    random_str = ''.join(secrets.choice(choice_str) for _ in range(N))
    return random_str
#生日攻击
def bt_atk(n):
    hash_prefixes = set()  # 存储哈希前缀的集合
    
    while True:
        random_str = getrandom(n)  # 生成随机字符串
        hash_prefix = sm3.sm3_hash(func.bytes_to_list(random_str.encode()))[:n//4]  # 计算哈希前缀
        
        if hash_prefix in hash_prefixes:  # 检查哈希前缀是否存在于集合中
            str0 = next(item for item in hash_prefixes if item == hash_prefix)   # 获取之前存储的字符串
            str1 = random_str  # 当前的字符串
            print(str0, sm3.sm3_hash(func.bytes_to_list(str0.encode())))  # 打印之前字符串的哈希值
            print(str1, sm3.sm3_hash(func.bytes_to_list(str1.encode())))  # 打印当前字符串的哈希值
            return 1  # 发现碰撞，返回1
        
        hash_prefixes.add(hash_prefix)  # 将哈希前缀添加到集合中

    return 0  # 未发现碰撞
n=16
start_time = time.perf_counter()
bt_atk(n)
end_time = time.perf_counter()
execution_time = (end_time - start_time) * 1000
print("执行时间为：", execution_time, "毫秒")


    
    
