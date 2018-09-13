# -*- coding: utf-8 -*-

import random
from fractions import Fraction

class Config:
    """
    配置参数类
    """
    def __init__(self, exp_num=10, num_range=10, has_fraction=False, has_mul_div= True, max_num_of_oper=3, has_parentheses=False, has_neg=False):
        self.exp_num = exp_num
        self.num_range = num_range
        self.has_fraction = has_fraction
        self.has_mul_div = has_mul_div
        self.max_num_of_oper = max_num_of_oper
        self.has_parentheses = has_parentheses
        self.has_neg = has_neg

class Generator:
    """
    表达式生成类
    """
    def __init__(self):
        pass

    #表达式生成
    def generate(self, config):
        pass

    # 生成操作数
    def generate_Operand(self, is_fraction, num_range):
        if is_fraction:
            return self.generate_fraction(num_range)
        else:
            return str(random.randint(0, num_range))
    
    # 生成真分数
    def generate_fraction(self, num_range):
        denominator = random.randint(2, num_range)
        numerator = random.randint(1, denominator - 1)
        #调用fraction方法生成真分数
        real_fraction = Fraction(numerator, denominator) 
        return real_fraction
            
    # 随机生成`+ - * ÷`操作
    def generate_opertation(self, operators):
        pass

class Constants:
    """
    运算符常量类
    """
    PLUS = '+'
    MINUS = '-'
    MULTIPLY = 'x'
    DIVIDE = '÷'
    ZERO = '0'
    VIRGULE = '/'
    SINGLE_QUOTE = "'"
    LEFT_PARENTHESES = '('
    RIGHT_PARENTHESES = ')'

    def __init__(self):
        pass

def main():
    """
    主函数
    """
    



def generate():
    pass



if __name__ == '__main__':
    main()