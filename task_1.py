from helper.funcs import ( 
    
    get_locations,
    get_moves,
    move_player

)

CELLS = [
        (0, 0), (1, 0), (2, 0), (3, 0),
        (0, 1), (1, 1), (2, 1), (3, 1),
        (0, 2), (1, 2), (2, 2), (3, 2),
        (0, 3), (1, 3), (2, 3), (3, 3)
]

player, dragon, door = get_locations(CELLS)


while True:
    print(f"your are in room {player}")
    valid_move = get_moves(player)
    print(f'Valid moves are {valid_move}')
    move = input('write something: ').casefold()
    if move in valid_move:
        player = move_player(player, move)
    else:
        print('please enter a valid move')
    if player == dragon:
        print("you loos")
    else:
        print("you can continue")

