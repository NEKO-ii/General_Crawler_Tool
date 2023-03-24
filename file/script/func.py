from decimal import Decimal as dec, InvalidOperation


def plus():
    input1 = input()
    input2 = input()
    x1 = dec(input1)
    x2 = dec(input2)
    print(F"{x1+x2}")


def minus():
    input1 = input("输入被减数 > ")
    input2 = input("输入减数 > ")
    x1 = dec(input1)
    x2 = dec(input2)
    print(F"{x1} - {x2} = {x1-x2}")


def multiply():
    input1 = input("输入第一个因数 > ")
    input2 = input("输入第二个因数 > ")
    x1 = dec(input1)
    x2 = dec(input2)
    print(F"{x1} × {x2} = {x1*x2}")


def divide():
    input1 = input("输入被除数 > ")
    input2 = input("输入除数 > ")
    x1 = dec(input1)
    x2 = dec(input2)
    if x2 == 0:
        print("除数不能为0")
    else:
        print(F"{x1} ÷ {x2} = {x1/x2}")


def pow():
    input1 = input("输入底数 > ")
    input2 = input("输入指数 > ")
    x1 = dec(input1)
    x2 = dec(input2)
    print(F"{x1} ^ {x2} = {x1**x2}")


if __name__ == '__main__':
    plus()
    # print(0)
