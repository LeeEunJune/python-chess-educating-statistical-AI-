from operator import eq
from colorama import Fore, Back, Style
import pandas as pd

counting = 1
move = 0
x1 = 0
y1 = 0
AI_count = 1
turn = 0
ck = 0
aimove = 0

#board Setting
board = [["NON" for j in range(8)] for i in range(8)]

#black
board[0][0] = "BR1"
board[0][1] = "BN1"
board[0][2] = "BB1"
board[0][3] = "BK1"
board[0][4] = "BQ1"
board[0][5] = "BB2"
board[0][6] = "BN2"
board[0][7] = "BR2"
for i in range(8):
    board[1][i] = "BP" + str(i+1)

#white
board[7][0] = "WR1"
board[7][1] = "WN1"
board[7][2] = "WB1"
board[7][3] = "WQ1"
board[7][4] = "WK1"
board[7][5] = "WB2"
board[7][6] = "WN2"
board[7][7] = "WR2"
for i in range(8):
    board[6][i] = "WP" + str(i+1)

#AI
class educating1:
    def setdata(self, object, place):
        self.object = object
        self.place = place

openning1 = educating1()
openning2 = educating1()
openning3 = educating1()
openning4 = educating1()
openning5 = educating1()
openning6 = educating1()
openning7 = educating1()
openning8 = educating1()
openning9 = educating1()
openning10 = educating1()

def AI_educating():
    global counting
    global turn
    if counting == 1:
        openning1.object = move
        openning1.place = [xp, yp]
    elif counting == 2:
        openning2.object = move
        openning2.place = [xp, yp]
    elif counting == 3:
        openning3.object = move
        openning3.place = [xp, yp]
    elif counting == 4:
        openning4.object = move
        openning4.place = [xp, yp]
    elif counting == 5:
        openning5.object = move
        openning5.place = [xp, yp]
    elif counting == 6:
        openning6.object = move
        openning6.place = [xp, yp]
    elif counting == 7:
        openning7.object = move
        openning7.place = [xp, yp]
    elif counting == 8:
        openning8.object = move
        openning8.place = [xp, yp]
    elif counting == 9:
        openning9.object = move
        openning9.place = [xp, yp]
    elif counting == 10:
        openning10.object = move
        openning10.place = [xp, yp]

    turn += 1

movement = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
setplace = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
place1 = []
type1 = []
place2 = []
type2 = []
place3 = []
type3 = []
place4 = []
type4 = []
place5 = []
type5 = []
place6 = []
type6 = []
place7 = []
type7 = []
place8 = []
type8 = []
place9 = []
type9 = []
place10 = []
type10 = []

df1 = pd.read_csv("C:/Users/dataframe/df1.csv")
for i in range(10):
    place1.append(df1.iat[1, i+1])
    type1.append(df1.iat[0, i+1])

df2 = pd.read_csv("C:/Users/dataframe/df2.csv")
for i in range(10):
    place2.append(df2.iat[1, i+1])
    type2.append(df2.iat[0, i+1])

df3 = pd.read_csv("C:/Users/dataframe/df3.csv")
for i in range(10):
    place3.append(df3.iat[1, i+1])
    type3.append(df3.iat[0, i+1])

df4 = pd.read_csv("C:/Users/dataframe/df4.csv")
for i in range(10):
    place4.append(df4.iat[1, i+1])
    type4.append(df4.iat[0, i+1])

df5 = pd.read_csv("C:/Users/dataframe/df5.csv")
for i in range(10):
    place5.append(df5.iat[1, i+1])
    type5.append(df5.iat[0, i+1])

df6 = pd.read_csv("C:/Users/dataframe/df6.csv")
for i in range(10):
    place6.append(df6.iat[1, i+1])
    type6.append(df6.iat[0, i+1])

df7 = pd.read_csv("C:/Users/dataframe/df7.csv")
for i in range(10):
    place7.append(df7.iat[1, i+1])
    type7.append(df7.iat[0, i+1])

df8 = pd.read_csv("C:/Users/dataframe/df8.csv")
for i in range(10):
    place8.append(df8.iat[1, i+1])
    type8.append(df8.iat[0, i+1])

df9 = pd.read_csv("C:/Users/dataframe/df9.csv")
for i in range(10):
    place9.append(df9.iat[1, i+1])
    type9.append(df9.iat[0, i+1])

df10 = pd.read_csv("C:/Users/dataframe/df10.csv")
for i in range(10):
    place10.append(df10.iat[1, i+1])
    type10.append(df10.iat[0, i+1])

class play:
    def setdata(self, move, place):
        self.move = move
        self.place = place

User1 = play()
User2 = play()
User3 = play()
User4 = play()
User5 = play()
Userm = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Userp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
User = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

AI = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#Searching function
def searching(b):
    tester = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == b:
                x = int(i)
                y = int(j)
                tester = 1
            else:
                tester = tester

    if tester == 1:
        print(b + " is at (" + str(x + 1) + ", " + str(y + 1) + ")")
        return x, y
    else:
        print(str(b) + " is not in defined")
        return 100, 100

def searching_end(b):
    tester = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == b:
                tester = 1
            else:
                tester = tester

    if tester == 0:
        return 0
    else:
        return 1

#WP
#forward
def wp_forward(a, b, c):
    if eq(board[b - 1][c],'NON'):
        board[b][c] = "NON"
        board[b - 1][c] = a
        AI_educating()
    else:
        print("can't move")

#p_forward
def wp_p_forward(a, b, c):
    if b == 6:
        if eq(board[b - 2][c], 'NON'):
            board[b][c] = "NON"
            board[b - 2][c] = a
            AI_educating()
        else:
            print("can't move")
    else:
        print("can't move")

#eat_left
def wp_eat_left(a, b, c):
    if eq(board[b - 1][c - 1],'NON'):
        print("can't move")
    else:
        board[b][c] = "NON"
        board[b - 1][c-1] = a
        AI_educating()

#eat_right
def wp_eat_right(a, b, c):
    if eq(board[b - 1][c + 1],'NON'):
        print("can't move")
    else:
        board[b][c] = "NON"
        board[b - 1][c + 1] = a
        AI_educating()

#BP
#forward
def bp_forward(a, b, c):
    if eq(board[b + 1][c],'NON'):
        board[b][c] = "NON"
        board[b + 1][c] = a
        AI_educating()
    else:
        print("can't move")
        return 1

#p_forward
def bp_p_forward(a, b, c):
    if b == 1:
        if eq(board[b + 2][c], 'NON'):
            board[b][c] = "NON"
            board[b + 2][c] = a
            AI_educating()
        else:
            print("can't move")
            return 1
    else:
        print("can't move")
        return 1

#eat_left
def bp_eat_left(a, b, c):
    if eq(board[b + 1][c - 1],'NON'):
        print("can't move")
        return 1
    else:
        board[b][c] = "NON"
        board[b + 1][c-1] = a
        AI_educating()

#eat_right
def bp_eat_right(a, b, c):
    if eq(board[b + 1][c + 1],'NON'):
        print("can't move")
        return 1
    else:
        board[b][c] = "NON"
        board[b + 1][c + 1] = a
        AI_educating()

#WR
#forward
def wr_h(a, b, c, d):
    tester = 0
    if b-d > 1:
        for i in range(d+1, b-1):
            if board[i][c] == 'NON':
                tester = tester
            else:
                tester = 1
    elif b-d < -1:
        for i in range(b+1, d-1):
            if board[i][c] == 'NON':
                tester = tester
            else:
                tester = 1

    if "W" in board[d][c]:
        tester = 1
    else:
        tester = tester

    if tester == 1:
        print("can't move")
    else:
        board[d][c] = a
        board[b][c] = "NON"
        AI_educating()


#side
def wr_v(a, b, c, d): #move, x, y, yp
    tester = 0
    if d-c > 1:
        for i in range(c+1,d-1):
            if board[b][i] == 'NON':
                tester = tester
            else:
                tester = 1
    elif d-c < -1:
        for i in range(d+1,c-1):
            if board[b][i] == 'NON':
                tester = tester
            else:tester = 1

    if "W" in board[b][d]:
        tester = 1
    else:
        tester = tester

    if tester == 1:
        print("can't move")
    else:
        board[b][d] = a
        board[b][c] = "NON"
        AI_educating()

#BR
#forward
def br_h(a, b, c, d):
    tester = 0
    if b-d > 1:
        for i in range(d+1, b-1):
            if board[i][c] == 'NON':
                tester = tester
            else:
                tester = 1
    elif b-d < -1:
        for i in range(b+1, d-1):
            if board[i][c] == 'NON':
                tester = tester
            else:
                tester = 1

    if "B" in board[d][c]:
        tester = 1
    else:
        tester = tester

    if tester == 1:
        print("can't move")
        return tester
    else:
        board[d][c] = a
        board[b][c] = "NON"
        AI_educating()

#side
def br_v(a, b, c, d): #move, x, y, yp
    tester = 0
    if d-c > 1:
        for i in range(c+1,d-1):
            if board[b][i] == 'NON':
                tester = tester
            else:
                tester = 1
    elif d-c < -1:
        for i in range(d+1,c-1):
            if board[b][i] == 'NON':
                tester = tester
            else:
                tester = 1

    if "B" in board[b][d]:
        tester = 1
    else:
        tester = tester

    if tester == 1:
        print("can't move")
        return tester
    else:
        board[b][d] = a
        board[b][c] = "NON"
        AI_educating()

#WB
def wb(a, b, c, d, e): #(move, x1, y1, xp, yp)
    tester = 0
    if abs(b-d) == abs(c-e):
        if b-d > 1:
            if c-e > 1:
                for i in range(abs(b-d)-1):
                    if board[b-i-1][c-i-1] == 'NON':
                        tester = tester
                    else:
                        tester = 1
            elif c-e < -1:
                for i in range(abs(b-d)-1):
                    if board[b-i-1][c+i+1] == 'NON':
                        tester = tester
                    else:
                        tester = 1
        elif b-d < -1:
            if c-e > 1:
                for i in range(abs(b-d)-1):
                    if board[b+i+1][c-i-1] == 'NON':
                        tester = tester
                    else:
                        tester = 1
            elif c-e < -1:
                for i in range(abs(b-d)-1):
                    if board[b+i+1][c+i+1] == 'NON':
                        tester = tester
                    else:
                        tester = 1

        if "W" in board[d][e]:
            tester = 1
        else:
            tester = tester

        if tester == 1:
            print("can't move")
        else:
            board[d][e] = a
            board[b][c] = "NON"
            AI_educating()
    else:
        print("can't move")

#BB
def bb(a, b, c, d, e): #(move, x1, y1, xp, yp)
    tester = 0
    if abs(b-d) == abs(c-e):
        if b-d > 1:
            if c-e > 1:
                for i in range(abs(b-d)-1):
                    if board[b-i-1][c-i-1] == 'NON':
                        tester = tester
                    else:
                        tester = 1
            elif c-e < -1:
                for i in range(abs(b-d)-1):
                    if board[b-i-1][c+i+1] == 'NON':
                        tester = tester
                    else:tester = 1
        elif b-d < -1:
            if c-e > 1:
                for i in range(abs(b-d)-1):
                    if board[b+i+1][c-i-1] == 'NON':
                        tester = tester
                    else:
                        tester = 1
            elif c-e < -1:
                for i in range(abs(b-d)-1):
                    if board[b+i+1][c+i+1] == 'NON':
                        tester = tester
                    else:
                        tester = 1

        if "B" in board[d][e]:
            tester = 1
        else:
            tester = tester

        if tester == 1:
            print("can't move")
            return tester
        else:
            board[d][e] = a
            board[b][c] = "NON"
            AI_educating()

    else:
        print("can't move")
        return tester

#WN
def wn(a, b, c, d, e): #(move, x1, y1, xp, yp)
    tester = 0
    if "W" in board[d][e]:
        tester = 1

    if b-d == 2:
        if c-e == 1 or e-c == 1:
            for i in range(2):
                if board[b-i-1][c] == 'NON' or "W" in board[b-i-1][c]:
                    tester = tester
                else:
                    tester = 1
        else:
            tester = 1
    elif b-d == -2:
        if c-e == 1 or e-c == 1:
            for i in range(2):
                if board[b+i+1][c] == 'NON' or "W" in board[b+i+1][c]:
                    tester = tester
                else:
                    tester = 1
        else:
            tester = 1
    elif c-e == 2:
        if b-d == 1 or d-b == 1:
            for i in range(2):
                if board[b][c-i-1] == 'NON' or "W" in board[b][c-i-1]:
                    tester = tester
                else:
                    tester = 1
        else:
            tester = 1
    elif c-e == -2:
        if b-d == 1 or d-b == 1:
            for i in range(2):
                if board[b][c+i+1] == 'NON' or "W" in board[b][c+i+1]:
                    tester = tester
                else:
                    tester = 1
        else:
            tester = 1
    else:
        tester = 1

    if tester == 1:
        print("can't move")
    else:
        board[d][e] = a
        board[b][c] = "NON"
        AI_educating()

#BN
def bn(a, b, c, d, e): #(move, x1, y1, xp, yp)
    tester = 0
    if "B" in board[d][e]:
        tester = 1
    if b-d == 2:
        if c-e == 1 or e-c == 1:
            for i in range(2):
                if board[b-i-1][c] == 'NON' or "B" in board[b-i-1][c]:
                    tester = tester
                else:
                    tester = 1
        else:
            tester = 1
    elif b-d == -2:
        if c-e == 1 or e-c == 1:
            for i in range(2):
                if board[b+i+1][c] == 'NON' or "B" in board[b+i+1][c]:
                    tester = tester
                else:
                    tester = 1
        else:
            tester = 1
    elif c-e == 2:
        if b-d == 1 or d-b == 1:
            for i in range(2):
                if board[b][c-i-1] == 'NON' or "B" in board[b][c-i-1]:
                    tester = tester
                else:
                    tester = 1
        else:
            tester = 1
    elif c-e == -2:
        if b-d == 1 or d-b == 1:
            for i in range(2):
                if board[b][c+i+1] == 'NON' or "B" in board[b][c+i+1]:
                    tester = tester
                else:
                    tester = 1
        else:
            tester = 1
    else:tester = 1

    if tester == 1:
        print("can't move")
        return tester
    else:
        board[d][e] = a
        board[b][c] = "NON"
        AI_educating()

#WK
def wk(a, b, c, d, e): #(move, x1, y1, xp, yp)
    tester = 0
    if b == d:
        if abs(e-c) == 1:
            if "W" in board[d][e]:
                tester = 1
            else:
                tester = tester
    elif c == e:
        if abs(d-b) == 1:
            if "W" in board[d][e]:
                tester = 1
            else:
                tester = tester
    else:
        if abs(e-c) == 1 and abs(d-b) == 1:
            if "W" in board[d][e]:
                tester = 1
            else:
                tester = tester

    if tester == 1:
        print("can't move")
    else:
        board[d][e] = a
        board[b][c] = "NON"
        AI_educating()

#BK
def bk(a, b, c, d, e): #(move, x1, y1, xp, yp)
    tester = 0
    if b == d:
        if abs(e-c) == 1:
            if "B" in board[d][e]:
                tester = 1
            else:
                tester = tester
    elif c == e:
        if abs(d-b) == 1:
            if "B" in board[d][e]:
                tester = 1
            else:
                tester = tester
    else:
        if abs(e-c) == 1 and abs(d-b) == 1:
            if "B" in board[d][e]:
                tester = 1
            else:
                tester = tester

    if tester == 1:
        print("can't move")
        return tester
    else:
        board[d][e] = a
        board[b][c] = "NON"
        AI_educating()

#WQ
def wq(a, b, c, d, e):
    tester = 0
    if b == d or c == e:
        if b == d:
            if c < e:
                for i in range(c+1, e):
                    if board[b][i] != 'NON':
                        tester = 1
            else:
                for i in range(e+1, c):
                    if board[b][i] != 'NON':
                        tester = 1
        else:
            if b < d:
                for i in range(b+1, d):
                    if board[i][c] != 'NON':
                        tester = 1
            else:
                for i in range(d+1, b):
                    if board[i][c] != 'NON':
                        tester = 1

    elif abs(b-d) == abs(c-e):
        if b < d and c < e:
            for i in range(1, abs(b-d)):
                if board[b+i][c+i] != 'NON':
                    tester = 1
        elif b < d and c > e:
            for i in range(1, abs(b-d)):
                if board[b+i][c-i] != 'NON':
                    tester = 1
        elif b > d and c < e:
            for i in range(1, abs(b-d)):
                if board[b-i][c+i] != 'NON':
                    tester = 1
        elif b > d and c > e:
            for i in range(1, abs(b-d)):
                if board[b-i][c-i] != 'NON':
                    tester = 1
    else:
        tester = 1

    if "W" in board[d][e]:
        tester = 1

    if tester == 1:
        print("can't move")
    else:
        board[d][e] = a
        board[b][c] = "NON"
        AI_educating()

#BQ
def bq(a, b, c, d, e):
    tester = 0
    if b == d or c == e:
        if b == d:
            if c < e:
                for i in range(c+1, e):
                    if board[b][i] != 'NON':
                        tester = 1
            else:
                for i in range(e+1, c):
                    if board[b][i] != 'NON':
                        tester = 1
        else:
            if b < d:
                for i in range(b+1, d):
                    if board[i][c] != 'NON':
                        tester = 1
            else:
                for i in range(d+1, b):
                    if board[i][c] != 'NON':
                        tester = 1

    elif abs(b-d) == abs(c-e):
        if b < d and c < e:
            for i in range(1, abs(b-d)):
                if board[b+i][c+i] != 'NON':
                    tester = 1
        elif b < d and c > e:
            for i in range(1, abs(b-d)):
                if board[b+i][c-i] != 'NON':
                    tester = 1
        elif b > d and c < e:
            for i in range(1, abs(b-d)):
                if board[b-i][c+i] != 'NON':
                    tester = 1
        elif b > d and c > e:
            for i in range(1, abs(b-d)):
                if board[b-i][c-i] != 'NON':
                    tester = 1
    else:
        tester = 1

    if "B" in board[d][e]:
        tester = 1

    if tester == 1:
        print("can't move")
        return tester
    else:
        board[d][e] = a
        board[b][c] = "NON"
        AI_educating()

#main loop
print("규칙 및 약속")
print("board : 열(세로) - 1~8, 행(가로) - 1~8")
print("Choice : 움질일 말 입력")
print("board : '열,행' 으로 입력(','로 구분)")

#Play With Human
while True:
    check = searching_end("WK1")
    if check == 0:
        print("black win")

        # board Setting
        board = [["NON" for j in range(8)] for i in range(8)]
        # black
        board[0][0] = "BR1"
        board[0][1] = "BN1"
        board[0][2] = "BB1"
        board[0][3] = "BK1"
        board[0][4] = "BQ1"
        board[0][5] = "BB2"
        board[0][6] = "BN2"
        board[0][7] = "BR2"
        for i in range(8):
            board[1][i] = "BP" + str(i + 1)

        # white
        board[7][0] = "WR1"
        board[7][1] = "WN1"
        board[7][2] = "WB1"
        board[7][3] = "WQ1"
        board[7][4] = "WK1"
        board[7][5] = "WB2"
        board[7][6] = "WN2"
        board[7][7] = "WR2"
        for i in range(8):
            board[6][i] = "WP" + str(i + 1)

        continue
    else:
        pass

    check = searching_end("BK1")
    if check == 0:
        print("white win")

        # board Setting
        board = [["NON" for j in range(8)] for i in range(8)]

        # black
        board[0][0] = "BR1"
        board[0][1] = "BN1"
        board[0][2] = "BB1"
        board[0][3] = "BK1"
        board[0][4] = "BQ1"
        board[0][5] = "BB2"
        board[0][6] = "BN2"
        board[0][7] = "BR2"
        for i in range(8):
            board[1][i] = "BP" + str(i + 1)

        # white
        board[7][0] = "WR1"
        board[7][1] = "WN1"
        board[7][2] = "WB1"
        board[7][3] = "WQ1"
        board[7][4] = "WK1"
        board[7][5] = "WB2"
        board[7][6] = "WN2"
        board[7][7] = "WR2"
        for i in range(8):
            board[6][i] = "WP" + str(i + 1)

        continue
    else:
        pass

    # printing boar
    df = 0
    for i in range(8):
        for j in range(8):
            if i % 2 == 0:
                if j == 7:
                    print(Back.WHITE + Style.BRIGHT + Fore.BLACK + " " + str(board[i][j]) + " " + Style.RESET_ALL)
                elif j % 2 == 0:
                    print(Back.BLACK + Style.BRIGHT + Fore.WHITE + " " + str(board[i][j]), end=" " + Style.RESET_ALL)
                else:
                    print(Back.WHITE + Style.BRIGHT + Fore.BLACK + " " + str(board[i][j]), end=" " + Style.RESET_ALL)
            elif i % 2 != 0:
                if j == 7:
                    print(Back.BLACK + Style.BRIGHT + Fore.WHITE + " " + str(board[i][j]) + " " + Style.RESET_ALL)
                elif j % 2 != 0:
                    print(Back.BLACK + Style.BRIGHT + Fore.WHITE + " " + str(board[i][j]), end=" " + Style.RESET_ALL)
                else:
                    print(Back.WHITE + Style.BRIGHT + Fore.BLACK + " " + str(board[i][j]), end=" " + Style.RESET_ALL)

    #searching
    while True:
        move = input("Choice : ")
        x1, y1 = searching(move)
        if x1 != 100:
            break
        else:
            print("Try again")

    xp, yp = map(int, input("board : ").split(','))

    #p
    for i in range(8):
        # wp
        if move == "WP" + str((i+1)):
            xp -= 1
            yp -= 1
            if x1 - 1 == xp and y1 == yp:
                wp_forward(move, x1, y1)
            elif x1 - 2 == xp and y1 == yp:
                wp_p_forward(move, x1, y1)
            elif x1 - 1 == xp and y1 - 1 == yp:
                wp_eat_left(move, x1, y1)
            elif x1 - 1 == xp and y1 + 1 == yp:
                wp_eat_right(move, x1, y1)

    #r
    for i in range(2):
        #wr
        if move == "WR" + str((i+1)):
            xp = xp-1
            yp = yp-1
            if yp == y1:
                wr_h(move, x1, y1, xp)
            elif xp == x1:
                wr_v(move, x1, y1, yp)

    #b
    for i in range(2):
        #wb
        if move == "WB" + str((i+1)):
            xp = xp-1
            yp = yp-1
            wb(move, x1, y1, xp, yp)

    #n
    for i in range(2):
        #wn
        if move == "WN" + str((i+1)):
            xp = xp-1
            yp = yp-1
            wn(move, x1, y1, xp, yp)

    #k
    if move == "WK1":
        xp = xp - 1
        yp = yp - 1
        wk(move, x1, y1, xp, yp)

    #Q
    if move == "WQ1":
        xp = xp - 1
        yp = yp - 1
        wq(move, x1, y1, xp, yp)

    if turn == 1:
        User1.move = move
        User1.place = [xp, yp]
        Userm[0] = User1.move
        Userp[0] = User1.place
    elif turn == 3:
        User2.move = move
        User2.place = [xp, yp]
        Userm[2] = User2.move
        Userp[2] = User2.place
    elif turn == 5:
        User3.move = move
        User3.place = [xp, yp]
        Userm[4] = User3.move
        Userp[4] = User3.place
    elif turn == 7:
        User4.move = move
        User4.place = [xp, yp]
        Userm[6] = User4.move
        Userp[6] = User4.place
    elif turn == 9:
        User5.move = move
        User5.place = [xp, yp]
        Userm[8] = User5.move
        Userp[8] = User5.place

    if Userm[turn-1] == type1[turn-1] and str(Userp[turn-1]) == str(place1[turn-1]):
        movement[turn-1] = type1[turn-1]
        setplace[turn-1] = place1[turn-1]
        User[turn-1] = 1
    elif Userm[turn-1] == type2[turn-1] and str(Userp[turn-1]) == str(place2[turn-1]):
        movement[turn-1] = type2[turn-1]
        setplace[turn-1] = place1[turn-1]
        User[turn-1] = 2
    elif Userm[turn-1] == type3[turn-1] and str(Userp[turn-1]) == str(place3[turn-1]):
        movement[turn-1] = type3[turn-1]
        setplace[turn-1] = place1[turn-1]
        User[turn-1] = 3
    elif Userm[turn - 1] == type4[turn - 1] and str(Userp[turn - 1]) == str(place4[turn - 1]):
        movement[turn - 1] = type4[turn - 1]
        setplace[turn - 1] = place1[turn - 1]
        User[turn - 1] = 4
    elif Userm[turn - 1] == type5[turn - 1] and str(Userp[turn - 1]) == str(place5[turn - 1]):
        movement[turn - 1] = type5[turn - 1]
        setplace[turn - 1] = place1[turn - 1]
        User[turn - 1] = 5
    elif Userm[turn - 1] == type6[turn - 1] and str(Userp[turn - 1]) == str(place6[turn - 1]):
        movement[turn - 1] = type6[turn - 1]
        setplace[turn - 1] = place1[turn - 1]
        User[turn - 1] = 6
    elif Userm[turn - 1] == type7[turn - 1] and str(Userp[turn - 1]) == str(place7[turn - 1]):
        movement[turn - 1] = type7[turn - 1]
        setplace[turn - 1] = place1[turn - 1]
        User[turn - 1] = 7
    elif Userm[turn - 1] == type8[turn - 1] and str(Userp[turn - 1]) == str(place8[turn - 1]):
        movement[turn - 1] = type8[turn - 1]
        setplace[turn - 1] = place1[turn - 1]
        User[turn - 1] = 8
    elif Userm[turn - 1] == type9[turn - 1] and str(Userp[turn - 1]) == str(place9[turn - 1]):
        movement[turn - 1] = type9[turn - 1]
        setplace[turn - 1] = place1[turn - 1]
        User[turn - 1] = 9
    elif Userm[turn - 1] == type10[turn - 1] and str(Userp[turn - 1]) == str(place10[turn - 1]):
        movement[turn - 1] = type10[turn - 1]
        setplace[turn - 1] = place1[turn - 1]
        User[turn - 1] = 10
    else:
        pass

    # AI searching
    while True:
        if User[turn-1] == 1:
            aimove = type1[turn]
            xp = int(place1[turn][1])+1
            yp = int(place1[turn][4])+1
        elif User[turn - 1] == 2:
            aimove = type2[turn]
            xp = int(place2[turn][1])+1
            yp = int(place2[turn][4])+1
        elif User[turn - 1] == 3:
            aimove = type3[turn]
            xp = int(place3[turn][1])+1
            yp = int(place3[turn][4])+1
        elif User[turn - 1] == 4:
            aimove = type4[turn]
            xp = int(place4[turn][1])+1
            yp = int(place4[turn][4])+1
        elif User[turn - 1] == 5:
            aimove = type5[turn]
            xp = int(place5[turn][1])+1
            yp = int(place5[turn][4])+1
        elif User[turn - 1] == 6:
            aimove = type6[turn]
            xp = int(place6[turn][1])+1
            yp = int(place6[turn][4])+1
        elif User[turn - 1] == 7:
            aimove = type7[turn]
            xp = int(place7[turn][1])+1
            yp = int(place7[turn][4])+1
        elif User[turn - 1] == 8:
            aimove = type8[turn]
            xp = int(place8[turn][1])+1
            yp = int(place8[turn][4])+1
        elif User[turn - 1] == 9:
            aimove = type9[turn]
            xp = int(place9[turn][1])+1
            yp = int(place9[turn][4])+1
        elif User[turn - 1] == 10:
            aimove = type10[turn]
            xp = int(place10[turn][1])+1
            yp = int(place10[turn][4])+1

        if x1 != 100:
            break
        else:
            print("Try again")

    x1, y1 = searching(aimove)

    #BP
    for i in range(8):
        if aimove == "BP" + str((i + 1)):
            xp -= 1
            yp -= 1
            print(x1)
            print(y1)
            print(xp)
            print(yp)
            if x1 + 1 == xp and y1  == yp:
                ck = bp_forward(aimove, x1, y1)
            elif x1 + 2 == xp and y1  == yp:
                ck = bp_p_forward(aimove, x1, y1)
            elif x1 + 1 == xp and y1 -1 == yp:
                ck = bp_eat_left(aimove, x1, y1)
            elif x1 + 1 == xp and y1 + 1 == yp:
                ck = bp_eat_right(aimove, x1, y1)

    #BR
    for i in range(2):
        if aimove == "BR" + str((i + 1)):
            xp = xp - 1
            yp = yp - 1
            if yp == y1:
                ck = br_h(aimove, x1, y1, xp)
            elif xp == x1:
                ck = br_v(aimove, x1, y1, yp)

    #BB
    for i in range(2):
        if aimove == "BB" + str((i + 1)):
            xp = xp - 1
            yp = yp - 1
            ck = bb(move, x1, y1, xp, yp)

    #BN
    for i in range(2):
        if move == "BN" + str((i + 1)):
            xp = xp - 1
            yp = yp - 1
            ck = bn(move, x1, y1, xp, yp)

    #BK
    if move == "BK1":
        xp = xp - 1
        yp = yp - 1
        ck = bk(move, x1, y1, xp, yp)

    #BQ
    if move == "BQ1":
        xp = xp - 1
        yp = yp - 1
        ck = bq(move, x1, y1, xp, yp)
