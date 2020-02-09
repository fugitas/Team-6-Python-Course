print('Hi, lets play TIC TAC TOE!')
print('\n1 | 2 | 3\n---------- \n4 | 5 | 6 \n----------\n7 | 8 | 9 \n')
malha = '  var1 |   |  \n ----------- \n    |   |   \n ----------- \n    |   |   '

var1 = ' '
var2 = ' '
var3 = ' '
var4 = ' '
var5 = ' '
var6 = ' '
var7 = ' '
var8 = ' '
var9 = ' '



i = 0
while (i == 0):
    print ('Player 1 what is your move? Choose a position from 1 - 9.')
    int = input('Your answer')
    if int == '1':
        if var1 != ' ':
            print('Place already taken, please choose again')
            int = input('Your answer')
        else:
            var1 = 'X'
    if int == '2':
        if var2 != ' ':
            print('Place already taken, please choose again')
            int = input('Your answer')
            if int == '1':
                var1 = 'X'
        else:
            var2 = 'X'
    if int == '3':
        if var3 != ' ':
            print('Place already taken, please choose again')
            int = input('Your answer')
            if int == '1':
                var1 = 'X'
            if int == '2':
                var2 = 'X'
        else:
            var3 = 'X'
    if int == '4':
        if var4 != ' ':
            print('Place already taken, please choose again')
            int = input('Your answer')
            if int == '1':
                var1 = 'X'
            if int == '2':
                var2 = 'X'
            if int == '3':
                var3 = 'X'
        else:
            var4 = 'X'
    if int == '5':
        if var5 != ' ':
            print('Place already taken, please choose again')
            int = input('Your answer')
            if int == '1':
                var1 = 'X'
            if int == '2':
                var2 = 'X'
            if int == '3':
                var3 = 'X'
            if int == '4':
                var4 = 'X'
        else:
            var5 = 'X'
    if int == '6':
        if var6 != ' ':
            print('Place already taken, please choose again')
            int = input('Your answer')
            if int == '1':
                var1 = 'X'
            if int == '2':
                var2 = 'X'
            if int == '3':
                var3 = 'X'
            if int == '4':
                var4 = 'X'
            if int == '5':
                var5 = 'X'
        else:
            var6 = 'X'
    if int == '7':
        if var7 != ' ':
            print('Place already taken, please choose again')
            int = input('Your answer')
            if int == '1':
                var1 = 'X'
            if int == '2':
                var2 = 'X'
            if int == '3':
                var3 = 'X'
            if int == '4':
                var4 = 'X'
            if int == '5':
                var5 = 'X'
            if int == '6':
                var6 = 'X'
        else:
            var7 = 'X'
    if int == '8':
        if var8 != ' ':
            print('Place already taken, please choose again')
            int = input('Your answer')
            if int == '1':
                var1 = 'X'
            if int == '2':
                var2 = 'X'
            if int == '3':
                var3 = 'X'
            if int == '4':
                var4 = 'X'
            if int == '5':
                var5 = 'X'
            if int == '6':
                var6 = 'X'
            if int == '7':
                var7 = 'X'
        else:
            var8 = 'X'
    if int == '9':
        if var9 != ' ':
            print('Place already taken, please choose again')
            int = input('Your answer')
            if int == '1':
                var1 = 'X'
            if int == '2':
                var2 = 'X'
            if int == '3':
                var3 = 'X'
            if int == '4':
                var4 = 'X'
            if int == '5':
                var5 = 'X'
            if int == '6':
                var6 = 'X'
            if int == '7':
                var7 = 'X'
            if int == '8':
                var8 = 'X'
        else:
            var9 = 'X'

    print(var1, end=' ')
    print('|', end=' ')
    print(var2, end=' ')
    print('|', end=' ')
    print(var3)
    print('----------')
    print(var4, end=' ')
    print('|', end=' ')
    print(var5, end=' ')
    print('|', end=' ')
    print(var6)
    print('----------')
    print(var7, end=' ')
    print('|', end=' ')
    print(var8, end=' ')
    print('|', end=' ')
    print(var9)

    if var1 == var2 == var3 == 'X' or var4 == var5 == var6 == 'X' or var7 == var8 == var9 == 'X' or var1 == var4 == var7 == 'X'or var2 == var5 == var8 == 'X'or var3 == var6 == var9 == 'X' or var1 == var5 == var9 == 'X' or var3 == var5 == var7 == 'X':
        print('End of the game, player 1 won!')
        i = 1
        break
    if var1 != ' ' and var2 != ' ' and var3 != ' ' and var4 != ' ' and var5 != ' ' and var6 !=' ' and var7 != ' ' and var8 !=' ' and var9 != ' ':
        print ('It is a draw! No winners this time!')
        break

    print('Player 2 what is your move? Choose a position from 1 - 9.')
    int = input('Your answer')
    if int == '1':
        if var1 != ' ':
            print('Place already taken, please choose again')
            int = input('Your answer')
        else:
            var1 = 'O'
    if int == '2':
        if var2 != ' ':
            print('Place already taken, please choose again')
            int = input('Your answer')
            if int == '1':
                var1 = 'O'
        else:
            var2 = 'O'
    if int == '3':
        if var3 != ' ':
            print('Place already taken, please choose again')
            int = input('Your answer')
            if int == '1':
                var1 = 'O'
            if int == '2':
                var2 = 'O'
        else:
            var3 = 'O'
    if int == '4':
        if var4 != ' ':
            print('Place already taken, please choose again')
            int = input('Your answer')
            if int == '1':
                var1 = 'O'
            if int == '2':
                var2 = 'O'
            if int == '3':
                var3 = 'O'
        else:
            var4 = 'O'
    if int == '5':
        if var5 != ' ':
            print('Place already taken, please choose again')
            int = input('Your answer')
            if int == '1':
                var1 = 'O'
            if int == '2':
                var2 = 'O'
            if int == '3':
                var3 = 'O'
            if int == '4':
                var4 = 'O'
        else:
            var5 = 'O'
    if int == '6':
        if var6 != ' ':
            print('Place already taken, please choose again')
            int = input('Your answer')
            if int == '1':
                var1 = 'O'
            if int == '2':
                var2 = 'O'
            if int == '3':
                var3 = 'O'
            if int == '4':
                var4 = 'O'
            if int == '5':
                var5 = 'O'
        else:
            var6 = 'O'
    if int == '7':
        if var7 != ' ':
            print('Place already taken, please choose again')
            int = input('Your answer')
            if int == '1':
                var1 = 'O'
            if int == '2':
                var2 = 'O'
            if int == '3':
                var3 = 'O'
            if int == '4':
                var4 = 'O'
            if int == '5':
                var5 = 'O'
            if int == '6':
                var6 = 'O'
        else:
            var7 = 'O'
    if int == '8':
        if var8 != ' ':
            print('Place already taken, please choose again')
            int = input('Your answer')
            if int == '1':
                var1 = 'O'
            if int == '2':
                var2 = 'O'
            if int == '3':
                var3 = 'O'
            if int == '4':
                var4 = 'O'
            if int == '5':
                var5 = 'O'
            if int == '6':
                var6 = 'O'
            if int == '7':
                var7 = 'O'
        else:
            var8 = 'O'
    if int == '9':
        if var9 != ' ':
            print('Place already taken, please choose again')
            int = input('Your answer')
            if int == '1':
                var1 = 'O'
            if int == '2':
                var2 = 'O'
            if int == '3':
                var3 = 'O'
            if int == '4':
                var4 = 'O'
            if int == '5':
                var5 = 'O'
            if int == '6':
                var6 = 'O'
            if int == '7':
                var7 = 'O'
            if int == '8':
                var8 = 'O'
        else:
            var9 = 'O'


    print(var1, end=' ')
    print('|', end=' ')
    print(var2, end=' ')
    print('|', end=' ')
    print(var3)
    print('----------')
    print(var4, end=' ')
    print('|', end=' ')
    print(var5, end=' ')
    print('|', end=' ')
    print(var6)
    print('----------')
    print(var7, end=' ')
    print('|', end=' ')
    print(var8, end=' ')
    print('|', end=' ')
    print(var9)

    if var1 == var2 == var3 == 'O' or var4 == var5 == var6 == 'O' or var7 == var8 == var9 == 'O' or var1 == var4 == var7 == 'O' or var2 == var5 == var8 == 'O' or var3 == var6 == var9 == 'O' or var1 == var5 == var9 == 'O' or var3 == var5 == var7 == 'O':
        print('End of the game, player 2 won!')
        i = 1
        break
