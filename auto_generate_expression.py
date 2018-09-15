# -*- coding: utf-8 -*-

import random
from fractions import Fraction

from Constants import Constants

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

    def generate(self, config):
        """
        表达式生成主函数
        :param
            config: config类
        :return: 
        """
        pass

    def generate_parentheses(self, exp, number_of_oprand):
        """
        生成括号表达式
        :param
            exp: 表达式
            number_of_oprand: 操作的数目
        :return: 括号表达式
        """
        expression = []
        num = number_of_oprand
        if exp:
            exp_length = len(exp)
            left_position = random.randint(0,(num/2))
            right_position = random.randint(left_position+1, (num/2)+1)
            mark = -1
            for i in range(exp_length):
                if self.is_operation(exp[i]):
                    expression.append(exp[i])
                else:
                    mark += 1
                    if mark == left_position:
                        expression.append(Constants.LEFT_PARENTHESES)
                        expression.append(exp[i])
                    elif mark == right_position:
                        expression.append(exp[i])
                        expression.append(Constants.RIGHT_PARENTHESES)
                    else:
                        expression.append(exp[i])
        #如果生成的括号表达式形如 (1 + 2/3 + 3) 则重新生成
        if expression[0] == '(' and expression[-1] ==')':
            expression = self.generate_parentheses(exp, number_of_oprand)
            return expression
        return expression


    def generate_Operand(self, is_fraction, num_range):
        """
        生成操作数值，判断是否需要真分数
        :param: 
            is_fra ction: True or False
            num_range: 操作数的范围
        :return: 操作数
        """
        if is_fraction:
            return self.generate_fraction(num_range)
        else:
            return str(random.randint(0, num_range))
    
    
    def generate_fraction(self, num_range):
        """
        生成真分数
        :param: 
            num_range: 操作数的范围
        :return: 真分数，例如1/2        
        """
        denominator = random.randint(2, num_range)
        numerator = random.randint(1, denominator - 1)
        #调用fraction方法生成真分数
        real_fraction = Fraction(numerator, denominator) 
        return real_fraction
            
    def generate_operation(self):
        """
        随机生成`+ - x ÷`运算符
        :param: None
        :return: + - x ÷
        """
        operators = [Constants.PLUS, Constants.MINUS, Constants.MULTIPLY, Constants.DIVIDE]
        return operators[random.randint(0,len(operators) - 1)]
    
    def is_operation(self, item):
        """
        判断是否是运算符
        :param
            item: 需要判断的字符
        :return: True or False
        """
        return {
            '+': True,
            '-': True,
            'x': True,
            '÷': True
        }.get(item, False)


def main():
    """
    主函数
    """

if __name__ == '__main__':
    main()