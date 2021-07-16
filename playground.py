def adding(i1: int, i2: int) -> int:
    return i1 + i2


game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]


def game_board(player=0, row=0, column=0, just_display=False):
    print('   a  b  c')

    if not just_display:
        game[row][column] = player

    for count, row in enumerate(game):
        print(count, row)


game_board(just_display=True)
game_board(1,2,2)
