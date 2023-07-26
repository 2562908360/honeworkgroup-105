# 使用教程
  - 将两个.py文件放在同一文件目录下，执行就可以。
# 代码说明
  - SM3代码实现参考了网上的资料：https://blog.csdn.net/weixin_45688634/article/details/123292997
  - Pho方法是根据上学期密码学引论作业更改以及参考网上资料：https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm
  ##Pho代码部分介绍
    - `rho(exm)` 函数：这个函数实现了一个简单的碰撞搜索算法，它在输入位数为 `exm` 的情况下找到两个不同的消息（m1 和 m2），它们的前 `exm` 位 SM3 哈希值相同。
    - `example` 变量：这个变量设置了要搜索碰撞的位数。在示例中，设置为 16 表示搜索前 16 位的碰撞。
    - `start_time` 和 `end_time` 变量：用于计算代码执行时间。
    - `col`, `m1`, `m2` = `rho(example)`：通过调用 rho() 函数找到碰撞。`col` 存储两个消息的前 example 位 SM3 哈希值的相同部分，`m1` 和 `m2` 分别是找到的两个碰撞消息。
