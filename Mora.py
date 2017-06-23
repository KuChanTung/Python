import random
import re
import functools
import itertools

totalElement = list(filter(lambda x: x != "stop" and x != '' ,input("輸入所有元素\n").split(' ') ) )
howManyCase = list( map( lambda x: [ totalElement[x[0]], totalElement[x[1]] ], itertools.product( range(len(totalElement)), range(len(totalElement)) ) ) )
howManyCaseWillWin = []

print("輸入勝利的組合(一次一組)，直到你打stop")
while True:
    winCase = list(filter(lambda x: x != '', input("輸入").split(' ') ))
    print(winCase)
    if  "stop" in  set(winCase):
        break
    elif len(winCase) != 2:
        print("目前只能你和電腦兩人玩")
        continue
    elif set(winCase) >= set(totalElement):
        continue
    howManyCaseWillWin.append(winCase)

robot = []
yourInput = ""

while True :
    robot = random.sample( totalElement, 1 )
    while True :
        tmp = input("你猜:\n")
        if re.search("^({})$".format( "|".join(totalElement) ), tmp):
            yourInput = tmp
            break
        else:
            print("包含前面沒有輸入的元素")
    print("你出 {} 電腦出 {}".format(yourInput, robot))
    if functools.reduce(lambda x, y: x or y , [ [yourInput] + robot  ==  x for  x in howManyCaseWillWin ]):
        print("你贏了")
        break
    else :
        print("繼續加油")



