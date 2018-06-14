import random

player_card = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
computer_card = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
in_bag = [i for i in range(91)]
in_bag.remove(0)
out_bag = []


def filling(a):
    counter = [0]
    cnt = 0

    for args in (a):
        for i in args:
            num = random.choice(range(90))
            while num in counter:
                num = random.choice(range(90))

            args[cnt] = num
            counter.append(num)
            cnt += 1
        cnt = 0
        args.sort()

    for i in (a):
        cr = []
        for _ in range(4):
            somint = random.choice(range(9))
            while somint in cr:
                somint = random.choice(range(9))
            i[somint] = 0
            cr.append(somint)
        cr = []

    for args in (a):
        for value in args:
            if value == 0:
                args[cnt] = '  '
            cnt += 1
        cnt = 0


def bochonok():
    outbag = random.choice(range(91))
    while outbag not in in_bag:
        outbag = random.choice(range(91))
    in_bag.remove(outbag)
    out_bag.clear()
    out_bag.insert(0, outbag)
    return 'Новый бочёнок: {} (осталось {})'.format(outbag, len(in_bag))


pc = filling(player_card)
cc = filling(computer_card)


class Game():

    def __init__(self, player_card, computer_card, out_bag):
        self.pc = player_card
        self.cc = computer_card
        self.ob = out_bag

    player_points = 0
    computer_points = 0

    def answer_chek(answer):
        x = False
        if answer == 'y':
            if player_card[0].count(*out_bag) == 1 or player_card[1].count(*out_bag) == 1 or player_card[2].count(
                    *out_bag) == 1:
                x = True
                return x
            elif player_card[0].count(*out_bag) == 0 or player_card[1].count(*out_bag) == 0 or player_card[2].count(
                    *out_bag) == 0:
                return x

        elif answer == 'n':
            if player_card[0].count(*out_bag) == 1 or player_card[1].count(*out_bag) == 1 or player_card[2].count(
                    *out_bag) == 1:
                x = True
                return x
            elif player_card[0].count(*out_bag) == 0 or player_card[1].count(*out_bag) == 0 or player_card[2].count(
                    *out_bag) == 0:
                return x

    def cor_answ():
        for args in player_card:
            for values in args:
                if values == out_bag[0]:
                    args[args.index(out_bag[0])] = '-'

    def ii():
        for args in computer_card:
            for values in args:
                if values == out_bag[0]:
                    args[args.index(out_bag[0])] = '-'
                    return True

    def wrong_answ():
        print('Сегодня отличный день, но не для игры в лото. Очень жаль, но вы проиграли.')


    # while player_points or computer_points <= 15:
    print(
        bochonok(), '\n',
        '------ Ваша карточка -----')
    count = 0
    for line in player_card:
        for args in line:
            if count == 9:
                print('\n')
                count = 0

            if args == 1 or args == 2 or args == 3 or args == 4 or args == 5 or args == 6 or args == 7 or args == 8 or args == 9:
                print(' '+str(args),end =' ')
                count += 1
            else:
                print(args, end=' ')
                count += 1

    print('\n','--------------------------')
    print('-- Карточка компьютера ---')

    print('--------------------------', '\n',
            'Зачеркнуть цифру? (y/n)')
        # answer = input()
        # if ii() is True:
        #     computer_points += 1
        #
        # if answer == 'y' and answer_chek(answer) is True:
        #     cor_answ()
        #     player_points += 1
        # elif answer == 'y' and answer_chek(answer) is False: \
        #     wrong_answ()
        #     break
        # elif answer == 'n' and answer_chek(answer) is True:
        #     wrong_answ()
        #     break
        # elif answer == 'n' and answer_chek(answer) is False:
        #     continue


        # if computer_points == 15:
        #     print('Очень жаль, но вы проиграли. Но вы держались молодцом!')
        #     break
        # elif player_points == 15:
        #     print('Поздравляем с заслуженной победой. Вы лучше всех!')
        #     break

Game(pc, cc, out_bag)
