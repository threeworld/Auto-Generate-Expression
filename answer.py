# -*- coding = 'uft-8' -*-

from suffix_expression import suffix_to_value,to_suffix

def expression_result(exp_list):
    """
    求表达式的结果
    :param exp_list: 表达式列表
    :return 
    """
    for i, exp in enumerate(exp_list):
        order_str = str(i+1)
        exp_value = str(suffix_to_value(to_suffix(exp))) + '\n'
        result = order_str + ': '+ exp_value
        with open('Answer.txt','a+', encoding='utf-8') as f:
            f.write(result)

def check_answer(exercisefile, answerfile):
    """
    校对答案
    :param 
        exercisefile: 练习题
        answerfile: 答案
    :return
    """
    wrong = 0
    correct = 0
    with open(exercisefile, 'r', encoding = 'utf-8') as f:
        exp = f.readlines()
        pass
    
if __name__ == '__main__':
    str_ = r'Exercises.txt'
    check_answer(str, 's')