import argparse
import math_lib.py as ml

parser = argparse.ArgumentParser(
        description='Calc add and div'
        prog='math_lib')

parser.add_argument('--first_int',
                    type=int,
                    help='first integer'
                    required=True)

parser.add_argument('--sec_int',
                    type=int,
                    help='second integer'
                    required=True)

args = parser.parser_args()

x3 = ml.add(first_int, sec_int)
x4 = ml.div(first_int, sec_int)

if __name__ == '__main__':
    main()
