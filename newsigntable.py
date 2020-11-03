"""This program is a complex program allowing to create sign tables
you enter a function in its factorized form, such as "(2x+4)(x+1)", and this program returns you the sign table corresponding"""

import sys
from eqsolve import *

#(7x+2)(-x+5)(2x+7)
def sign_table(equation):

    #the arguments are the differents parts of the equation that needs to be treated independantly
    arguments = '%'.join(equation.split(")(")).replace('(', '').replace(')', '').split('%')

    #Finds the solutions of arguments=0
    solutions = []
    for each in arguments:
        solutions.append(str(esolve(each)[0]))
    soldiv = []
    for each in solutions:
        if each.count("/") != 0:
            num,denom = map(int, each.split("/"))
            soldiv.append(num/denom)
        else:
            soldiv.append(float(each))
    #Finds the direction of each straight line, according to their directing coefficient
    direction = []
    for each in arguments:
        if str(esolve(each)[1])[0] != '-':
            direction.append("+")
        else:
            direction.append("-")

    #sorting everything in a big table
    soldiv, solutions, arguments, direction = zip(*sorted(zip(soldiv, solutions, arguments, direction)))


    #this parts finds all the signs that are needed in the table for every argument
    signs = []
    for each in arguments:
        for i in range(len(arguments) + 1):
            if direction[arguments.index(each)] == "+":
                if i < (arguments.index(each) + 1):
                    signs.append("-")
                else:
                    signs.append("+")
            if direction[arguments.index(each)] == "-":
                if i < (arguments.index(each) + 1):
                    signs.append("+")
                else:
                    signs.append("-")

    signCalcul = []
    for i in range(len(arguments) + 1):
        signCalcul.append(signs[i::(len(arguments) + 1)])

    #adds the last lign, where is the product of the signs
    for items in signCalcul:
        if items.count("-") % 2 == 0 or items.count("-") == 0:
            signs.append("+")
        else:
            signs.append("-")


    #part that puts all the 0s and | in the table
    arguments = list(arguments)
    arguments.append(equation)
    signs2 = []
    k = 0
    for i in range(len(arguments)):
        if i == len(arguments) - 1:
            for j in range(len(arguments)):
                signs2.append(signs[k])
                if j != len(arguments) - 1:
                    signs2.append("0")
                k = k + 1
        else:
            for j in range(len(arguments)):
                signs2.append(signs[k])
                if j == i and j != len(arguments) - 1:
                    signs2.append("0")
                elif j != len(arguments) - 1:
                    signs2.append("|")
                k = k + 1
    data = []
    tempList = []
    for each in arguments:
        tempList.append(each)
        for i in range(len(arguments) + len(arguments) - 1):
            tempList.append(signs2[i])
        for i in range(len(arguments) + len(arguments) - 1):
            signs2.pop(0)
        data.append(tempList)
        tempList = []


    #highly complex and ununderstanable part, where the table is created from the data, simply
    columnSize = 7 * (len(arguments))
    header = ["-∞", "+∞"]
    for i in solutions:
        header.insert((1 + solutions.index(i)), str(i).replace("[", "").replace("]", ""))
    print("\n{:<2s}".format("x"), end=' ')
    if len(data) == 2:
        data.pop(0)
    for each in header:
        if header.index(each) == 0:
            print(("{:^" + str(columnSize) + "s}").format(each), end=' ')
        elif header.index(each) == len(header) - 1:
            print(("{:^" + str(columnSize) + "s}").format(each), end=' ')
        else:
            print("{:^11s}".format(each), end=' ')
    for parts in data:
        for each in parts:
            if parts.index(each) == 0:
                print(("\n{:<" + str(columnSize) + "s}").format(each), end=' ')
            else:
                print("{:^5s}".format(each), end=' ')
    print('\n')
    input()

if __name__ == "__main__":
	sign_table(input("Put here sign table > "))
