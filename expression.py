# -*- coding=utf-8 -*-

from fractions import Fraction
class Expression:
    """表达式类"""
    def __init__(self, expression):
        self.expression = expression
        self.value = 0
        self.fraction = Fraction()

    def create(self, expression):
        return self.__init__(expression)

    def get_expression(self):
        return self.expression

    def get_value(self):
        return self.value

    def tostring(self):
        return self.expression + " = " + str(self.value)

    def set_fraction(self,frac):
        self.fraction = frac

    def set_value(self, value):
        self.value = value