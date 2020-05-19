# 读文本文件

# def main():
#     f = open('致橡树.txt', 'r', encoding='utf-8')
#     print(f.read())
#     f.close()
#
#
# if __name__ == '__main__':
#     main()


# 增加一定的健壮性和容错性。
# def main():
#     f = None
#     try:
#         f = open('致橡树.txt', 'r', encoding='utf-8')
#         print(f.read())
#     except FileNotFoundError:
#         print('无法打开指定的文件')
#     except LookupError:
#         print('指定了未知的编码')
#     except UnicodeDecodeError:
#         print('读取文件时解码错误')
#     # finally块的代码总是会执行，关闭打开的文件，释放程序中获取的外部资源。
#     finally:
#         if f:
#             f.close()
#
#
# if __name__ == '__main__':
#     main()





# 还可以用for循环逐行读取或者用readlines方法将文件按行读取到一个列表容器中。
# import time
#
#
# def main():
#     with open('致橡树.txt', 'r', encoding='utf-8') as f:
#         # 打印整个文本内容
#         print(f.read())
#
#     with open('致橡树.txt', mode='r', encoding='utf-8') as f:
#         # 打印每行
#         for line in f:
#             print(line)
#             time.sleep(1)
#     print()
#
#     with open('致橡树.txt', 'r',encoding='utf-8') as f:
#         lines = f.readlines()
#     print(lines)
#
# if __name__ == '__main__':
#     main()

'''
写文本文件
在使用open函数时指定好文件名并将文件模式设置为'w'即可。注意如果需要对文件内容进行追加式写入，应该将模式设置为'a'。如果要写入的文件不存在会自动创建文件而不是引发异常。下面的例子演示了如何将1-9999之间的素数分别写入三个文件中（1-99之间的素数保存在a.txt中，100-999之间的素数保存在b.txt中，1000-9999之间的素数保存在c.txt中）
1、必须是素数
2、1-10000之间不同区间写入不同文件
'''

from math import sqrt

def is_prime(n):
    # 判断素数的函数
    assert n > 0
    for factor in range(2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True if n != 1 else False


def main():
    filenames = ('a.txt', 'b.txt', 'c.txt')
    fs_list = []
    try:
        for filename in filenames:
            fs_list.append(open(filename, 'w', encoding='utf-8'))
        for number in (1, 10000):
            if is_prime(number):
                if number < 100:
                    fs_list[0].write(str(number) + '\n')
                elif number < 1000:
                    fs_list[1].write(str(number) + '\n')
                else:
                    fs_list[2].write(str(number) + '\n')
    except IOError as ex:
        print(ex)
        print('写文件时发生错误')
    finally:
        for fs in fs_list:
            fs.close()
    print('操作完成')
#
#
# # 读取二进制文件
#
# def main():
#     try:
#         with open('guido.jpg', 'rb') as fs1:
#             data = fs1.read()
#             print(type(data))
#         with open('基多.jpg', 'wb') as fs2:
#             fs2.write(data)
#
#     except FileNotFoundError as e:
#         print('指定的文件无法打开')
#     except IOError as e:
#         print('读取文件时出现错误')
#     print('程序已执行结束')
#
#
if __name__ == '__main__':
    main()
#
# # 读取json文件
#
# import json
#
#
# def main():
#     mydict = {
#         'name': '舒景平',
#         'age': 24,
#         'qq': 1048707084,
#         'friends': ['刘昊文', '刘尚美']
#         'cars': [
#             {'brand': 'BYD', 'max_speed': 180},
#             {'brand': 'Audi', 'max_speed': 280},
#             {'brand': 'Benz', 'max_speed': 320}
#         ]
#     }
#     try:
#         with open('data.json', 'w', encoding='utf-8') as fs:
#             # 将python对象按照JSON格式序列化到文件中
#             json.dump(mydict, fs)
#     except IOError as e:
#         print(e)
#     print('数据保存完成')