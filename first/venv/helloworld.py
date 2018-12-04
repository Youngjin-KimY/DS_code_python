#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def precedence(op):
    ret = 0
    if op == '+' or op == '-':
        ret = 1
    if op == '*' or op == '/':
        ret = 2
    return ret

if __name__ == '__main__':
    s_oprator  = []
    s_oprand = []
    cal = 0
    opra = [')','+','-','*','/']
    N = 1
    for _ in range(N):
        split = "100 * 1 + 2 - 2 + 1".split(' ')
        for i in range(len(split)):
            token = split[i]
            if token != ' ':

                if token not in opra:
                    if token != '(':
                        s_oprand.append(token)
                    else:
                        s_oprator.append(token)
                else:
                    if token != ')':

                        while len(s_oprator) != 0 and (precedence(s_oprator[len(s_oprator)-1]) >= precedence(token)):
                            op1 = int(s_oprand.pop())
                            op2 = int(s_oprand.pop())
                            op = s_oprator.pop()
                            if op == '+':
                                cal = op1 + op2
                            elif op =='-':
                                cal = op2 - op1
                            elif op == '*':
                                cal = op1*op2
                            else:
                                cal = op2/op1
                            s_oprand.append(cal)
                        s_oprator.append(token)

                    else:
                        while s_oprator[len(s_oprator)-1] != '(':
                            op1 = int(s_oprand.pop())
                            op2 = int(s_oprand.pop())
                            op = s_oprator.pop()
                            if op == '+':
                                cal = op1 + op2
                            elif op =='-':
                                cal = op2 - op1
                            elif op == '*':
                                cal = op1*op2
                            else:
                                cal = op2/op1
                            s_oprand.append(cal)
                        s_oprator.pop()
        while len(s_oprator) != 0:
            op1 = int(s_oprand.pop())
            op2 = int(s_oprand.pop())
            op = s_oprator.pop()
            if op == '+':
                cal = op1 + op2
            elif op == '-':
                cal = op2 - op1
            elif op == '*':
                cal = op1 * op2
            else:
                cal = op2 / op1
            s_oprand.append(cal)

        print(s_oprand.pop())