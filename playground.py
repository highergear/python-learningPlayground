def adding(i1: int, i2: int) -> int:
    return i1 + i2


# initiate a game object list of list
game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]


def game_board(game_map=game, player=0, row=0, column=0, just_display=False):
    print('   a  b  c')
    if not just_display:
        # global game_map  # to make the change of the game object applied globally
        game_map[row][column] = player

    for count, row in enumerate(game_map):
        print(count, row)
    return game_map


game_map = game_board(just_display=True)
game_map = game_board(game, 1, 2, 2)
