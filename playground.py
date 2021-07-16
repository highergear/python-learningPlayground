def adding(i1: int, i2: int) -> int:
    return i1 + i2


def game_board():
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    print('   a  b  c')
    for count, row in enumerate(game):
        print(count, row)


x = game_board()
