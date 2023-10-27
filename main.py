RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
END = '\u001b[0m'


def draw_flag():
    for i in range(7):
        if i % 6 == 0:
            print(f'{RED}{" " * 21}{END}')
        elif i == 3:
            print(f'{RED}{" " * 3}{WHITE}{" " * 15}{RED}{" " * 3}{END}')
        else:
            print(f'{RED}{" " * 9}{WHITE}{" " * 3}{RED}{" " * 9}{END}')


def draw_uzor():
    for i in range(7):
        if i % 7 in [0, 6]:
            print(f'{" " * 3 * 2}{WHITE}{" " * 3 * 3}{END}{" " * 3 * 2}'*2)
        elif i % 7 in [1, 5]:
            print(f'{" " * 3}{WHITE}{" " * 3}{END}{" " * 3 * 3}{WHITE}{" " * 3}{END}{" " * 3}'*2)
        elif i % 7 in [2, 3, 4]:
            print(f'{WHITE}{" " * 3}{END}{" " * 3 * 5}{WHITE}{" " * 3}{END}'*2)


def draw_graphic():
    plot_list = [[0 for i in range(10)] for i in range(10)]
    result = [0 for i in range(10)]

    for i in range(10):
        result[i] = i / 3

    step = round(abs(result[0] - result[9]) / 9, 2)
    print(step)

    for i in range(10):
        for j in range(10):
            if j == 0:
                plot_list[i][j] = step * (8 - i) + step

    for i in range(9):
        for j in range(10):
            if abs(plot_list[i][0] - result[9 - j]) < step:
                for k in range(9):
                    if 8 - k == j:
                        plot_list[i][k + 1] = 1

    for i in range(9):
        line = ''
        for j in range(10):
            if j == 0:
                line += '\t' + str(int(plot_list[i][j])) + '\t'
            if plot_list[i][j] == 0:
                line += '--'
            if plot_list[i][j] == 1:
                line += '//'
        print(line)
    print('\t0\t1 2 3 4 5 6 7 8 9')


def analiz():
    with open('sequence.txt', 'r') as f:
        data = [float(i) for i in f.readlines()]
        U03 = []
        other = []
        for i in data:
            if abs(i) < 3:
                U03.append(i)
            else:
                other.append(i)
        print('от -3 до 3: ', round(len(U03)/2.5, 2), '%', sep='')
        print('остальные: ', round(len(other)/2.5, 2), '%', sep='')


def dop_task():
    import time
    import sys
    import os

    animation = "|/-\\"
    anicount = 0
    counttime = 0
    i = 0

    while (counttime != 100):
        time.sleep(0.075)

        sys.stdout.write("\r" + animation[anicount])
        sys.stdout.flush()

        anicount = (anicount + 1) % 4
        i = (i + 1) % 4
        counttime = counttime + 1

        os.system("cls")