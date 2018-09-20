
import random
import sys


#SETUP

ballsleft = 90
p1 = 15
p2 = 15
balls = random.sample(range(90), 90)
game_set = random.sample(range(90), 30)
p1_set = random.sample(game_set, 15)
p2_set = [e for e in game_set if not e in p1_set]
p1_field = [p1_set[:5], p1_set[5:10], p1_set[10:]]
p2_field = [p2_set[:5], p2_set[5:10], p2_set[10:]]
for p1line in p1_field:
    p1line.sort()
    p1line.insert(random.randint(0, 4), ' ')
    p1line.insert(random.randint(0, 5), ' ')
    p1line.insert(random.randint(0, 6), ' ')
    p1line.insert(random.randint(0, 7), ' ')
for p2line in p2_field:
    p2line.sort()
    p2line.insert(random.randint(0, 4), ' ')
    p2line.insert(random.randint(0, 5), ' ')
    p2line.insert(random.randint(0, 6), ' ')
    p2line.insert(random.randint(0, 7), ' ')


#FUNCTIONS

def field(p):

    if p == 0:
        print('{:-^26}'.format(' Ваша карточка '))
        for line1 in p1_field:
            for n1 in line1:
                print('{0:>2}'.format(n1), end=' ')
            print()
        print('{:-^26}\n'.format('-'))
    if p == 1:
        print('{:-^26}'.format(' Карточка компьютера '))
        for line2 in p2_field:
            for n2 in line2:
                print('{0:>2}'.format(n2), end=' ')
            print()
        print('{:-^26}\n'.format('-'))


def you_move():

    a = input('Зачеркнуть цифру? (y/n): ')
    if a == 'y':
        if ball in p1_set:
            for l in p1_field:
                try:
                    l.insert(l.index(ball), '><')
                    l.pop(l.index(ball))
                except ValueError:
                    continue
            print('\nOK')
            return 1
        else:
            print('\nGAME OVER')
            sys.exit()
    if a == 'n':
        if ball in p1_set:
            print('\nGAME OVER')
            sys.exit()
        else:
            print('\nOK')


def com_move():

    if ball in p2_set:
        for i in p2_field:
            try:
                i.insert(i.index(ball), '><')
                i.pop(i.index(ball))
            except ValueError:
                continue
        return 1


#GAME

for ball in balls:
    ballsleft -= 1
    print('\nНовый бочонок: {} (осталось: {})\n'.format(ball, ballsleft))
    field(0)
    field(1)
    if you_move() == 1:
        p1 -= 1
    if com_move() == 1:
        p2 -= 1
    if p1 == 0:
        print('\nYOU WON')
        sys.exit()
    if p2 == 0:
        print('\nYOU LOST')
        sys.exit()
    if ballsleft == 0:
        print('\nGAME OVER')
        sys.exit()