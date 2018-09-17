# -*- coding = utf-8 -*-

def to_suffix(exp):
    """
    中缀表达式转为后缀表达式
    :param: exp: 表达式字符串
    :return: result列表
    """
    if not exp:
        return []
    ops_rule = {
            '+' : 1,
            '-' : 1,
            'x' : 2,
            '÷' : 2,
        }
    suffix_stack = []  #后缀表达式结果
    ops_stack = []  #操作符栈
    infix = exp.split(' ')
    #print(infix)
    for item in infix:
        if item in ['+', '-', 'x', '÷']: #遇到运算符
            while len(ops_stack) >= 0:
                if len(ops_stack) == 0:
                    ops_stack.append(item)
                    break
                op = ops_stack.pop()
                if op == '(' or ops_rule[item] > ops_rule[op]:
                    ops_stack.append(op)
                    ops_stack.append(item)
                    break
                else:
                    suffix_stack.append(op)
        elif item == '(': # 左括号直接入栈
            ops_stack.append(item)
        elif item == ')': #右括号
            while len(ops_stack) > 0:
                op = ops_stack.pop()
                if op == "(":
                    break
                else:
                    suffix_stack.append(op)
        else:
            suffix_stack.append(item) # 数值直接入栈
    
    while len(ops_stack) > 0:
        suffix_stack.append(ops_stack.pop())

    return suffix_stack

def suffix_to_value(exp):
    """
    后缀表达式求值
    :param exp: 后缀表达式的后缀字符串
    :return 运算结果
    """
    stack_value = []
    for item in exp:
        #print(item)
        if item in ['+', '-', 'x', '÷']:
            n2 = stack_value.pop()
            n1 = stack_value.pop()
            result = cal(n1, n2, item)
            stack_value.append(result)
        else:
            stack_value.append(int(item))

    return stack_value[0]

def cal(n1, n2, op):
    if op == '+':
        return n1 + n2 
    if op == '-':
        return n1 - n2
    if op == 'x':
        return n1 * n2
    if op == '÷':
        return n1 / n2


if __name__ == '__main__':
    exp = '9 + ( 3 - 1 ) x 3 + 10 ÷ 2'
    re = to_suffix(exp)
    print(re)
    print(suffix_to_value(re))


