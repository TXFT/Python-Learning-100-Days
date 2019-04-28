"""
列表生成式、生成器生成式
"""

# import sys

# def main():
#     f = [x for x in range(1, 10)]
#     print(sys.getsizeof(f))
#     print(f)
#     f = (x for x in range(1, 10))
#     print(sys.getsizeof(f))
#     print(f)
#     for var in f:
#         print(var)
# if __name__ == "__main__":
#     main()

"""
yield 生成器函数
"""

# def fib(n):
#         a, b = 0, 1
#         for _ in range(n):
#                 a, b = b, a+b
#                 yield a

# def main():
#         for val in fib(20):
#                 print(val)

# if __name__ == '__main__':
#         main()

"""
使用集合
跟数学上的集合是一致的，不允许有重复元素，而且可以进行交集、并集、差集。
"""

