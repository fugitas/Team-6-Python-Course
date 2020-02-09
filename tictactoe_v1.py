#Este programa é uma simulação em python do famoso jogo tic tac toe, também conhecido como jogo da velha.

#Chamada para convidar jogadores e layout da matriz 3x3
print('Hi, lets play TIC TAC TOE!')
print('\n1 | 2 | 3\n---------- \n4 | 5 | 6 \n----------\n7 | 8 | 9 \n')

#Definição das variáveis que estarão em cada célula
var1 = ' '
var2 = ' '
var3 = ' '
var4 = ' '
var5 = ' '
var6 = ' '
var7 = ' '
var8 = ' '
var9 = ' '


#Loop para rodadas. Obs.: a definição do fim do loop i != 0 não está funcionando como eu gostaria. O programa está pausando com a função 'break'.
i = 0
while (i == 0):
    print ('Player 1 what is your move? Choose a position from 1 - 9.')
    int = input('Your answer')
    if int == '1':
        #Caso o jogador escolha uma posição já ocupada, a mensagem abaixo é retornada e ele escolhe outra posição.
        #Após a escolha da célula, a variável correspondente é atualizada.
        # O mesmo ocorre para os demais casos abaixo.
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

#Impressão da matriz do jogo. Observe que as células são impressas por funções prints diferentes.
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

#Condições teste para verificação se o jogador 1 venceu. Caso possa dar empate, o jogador 1 será o último a jogar.
#Portanto, a condição de empate está apenas neste setor.
    if var1 == var2 == var3 == 'X' or var4 == var5 == var6 == 'X' or var7 == var8 == var9 == 'X' or var1 == var4 == var7 == 'X'or var2 == var5 == var8 == 'X'or var3 == var6 == var9 == 'X' or var1 == var5 == var9 == 'X' or var3 == var5 == var7 == 'X':
        print('End of the game, player 1 won!')
        i = 1
        break
    if var1 != ' ' and var2 != ' ' and var3 != ' ' and var4 != ' ' and var5 != ' ' and var6 !=' ' and var7 != ' ' and var8 !=' ' and var9 != ' ':
        print ('It is a draw! No winners this time!')
        break

#Mesmo bloco de comando que o anterior, apenas repetido para o jogador 2.
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

#Impressão da matriz
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

#Teste para verificação se o jogador 2 venceu.
    if var1 == var2 == var3 == 'O' or var4 == var5 == var6 == 'O' or var7 == var8 == var9 == 'O' or var1 == var4 == var7 == 'O' or var2 == var5 == var8 == 'O' or var3 == var6 == var9 == 'O' or var1 == var5 == var9 == 'O' or var3 == var5 == var7 == 'O':
        print('End of the game, player 2 won!')
        i = 1
        break

#O programa ainda contém alguns erros como por exemplo se o jogador selecionar duas vezes uma célula já ocupada, ou seja,
#tentar trapacear, o programa irá sobrescrever o valor pedido sobre o já escrito. Além disso, se o usuário responder um valor
#diferente de 1 a 9 o programa irá continuar como se o jogador tivesse escolhido normalmente.
#O programa ainda não é a prova de trapaaceiros rsrsrs.