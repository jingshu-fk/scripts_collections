import random
import sys

english = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
digital = '0123456789'
wenzi = '今天是个好日子值得庆祝大吃大喝大保健继续加油持续努力用慢变量形成聚成强大的力量'

num = int(sys.argv[1])

str_output = ''

for i in range(num):
	str_temp = random.choice(english + digital)
	str_output += str_temp

print(type(str_output))
print(str_output)




import random


def generate_code(code_len=4):
    """
    生成指定长度的验证码

    :param code_len: 验证码的长度(默认4个字符)

    :return: 由大小写英文字母和数字构成的随机验证码
    """
    code = ' '
    # 取值范围
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyz今天是个好日子值得庆祝大吃大喝大玩'
    # 循环四次，生成指定长度为4的验证码
    for length in range(code_len):
        # 从取值范围随机产生一个
        index = random.randint(0, len(all_chars) - 1)
        # 字符串也是序列，也有下标索引。
        code += all_chars[index]
    print(code)
    return code




