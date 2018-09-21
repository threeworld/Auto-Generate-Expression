# -*- coding = 'utf-8 -*-

import argparse
from exp_generate import Config,Generator
from answer import expression_result,check_answer

def main():
    """
    主函数
    """
    parser = argparse.ArgumentParser(description="***** this is auto-generate-expression *****")
    parser.add_argument("-n", metavar = "--number", dest = "expnum_arg", help = "Generate a given number of expressions" )
    parser.add_argument("-r", metavar = "--range", dest = "range_arg", help = "Specify the range of operands")
    parser.add_argument("-e", metavar = "--exercise file", dest = "exercise_arg", help = "Given four arithmetic problem files")
    parser.add_argument("-a", metavar = "--answer file", dest = "answer_arg", help = "Given four arithmetic problem answer files")
    args = parser.parse_args()
    
    #判断生成的表达式的数目
    if args.expnum_arg:
        #表达式的范围
        if args.range_arg:
            config = Config(exp_num=int(args.expnum_arg),num_range=int(args.range_arg))
        else:
            config = Config(exp_num=int(args.expnum_arg))
        generator = Generator()
        res_list = generator.generate(config)
        generator.normalize_exp(res_list)
        expression_result(res_list)
    
    #练习题答案的文件判断
    if args.exercise_arg:
        if args.answer_arg:
            check_answer(args.exercise_arg, args.answer_arg)
        else:
            print('please give an answer files')
            exit(0)

if __name__ == '__main__':
    main()