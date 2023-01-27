from random import randint as ri
total_candy = 150
take_candy = 0

def Lottery():
    _ = ri(0,1)
    if _ == 0:
        player_turn()
    else: 
        print('Ход компьютера')
        bot_turn()

def player_turn():
    global total_candy
    global take_candy
    take_candy = int(input(f'Ход игрока, осталось {total_candy} конфет: ')) 
    while take_candy > 28 or take_candy < 1 or take_candy > total_candy:
        try: 
            take_candy = int(input('Нельзя не брать конфет, брать больше 28 и больше, чем осталось: ' ))
        except ValueError:
            take_candy = int(input('Нужно ввести ЦЕЛОЕ ЧИСЛО, попробуйте снова: ' ))
    total_candy -= take_candy
    if total_candy > 0:
        bot_turn()
    else: print('Вы победили')


def bot_turn():
    global total_candy
    global take_candy
    if total_candy % 29 != 0:
        take_candy = total_candy % 29
    else: take_candy = ri(1,28)
    total_candy -= take_candy
    print(f'Бот взял {take_candy} конфет')
    if total_candy > 0:
        player_turn()
    else: print('Победил компьютер')

Lottery()


