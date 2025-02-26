"""未使用原始字符串"""
print("D:\three\two\one\now")
"""D:        hree        wo\one
ow"""

"""# 使用原始字符串"""
print(r"D:\three\two\one\now")
"""D:\three\two\one\now"""

"""打印一个九九乘法表"""

for i in range(1, 10):
    for j in range(1, i+1):
        print(i, "x", j, "=", i * j, end=' ')
        print("\n")
