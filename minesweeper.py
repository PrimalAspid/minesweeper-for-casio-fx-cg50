import random

def get_random():

    return random.randint(0,10)
     

def check_number_mines(x, y): #checks how many mines there are neer it
    count = 0
    for i in range(3):
        for j in range(3):
            if not (x + i - 1 < 0 or x + i - 1 > size - 1 or y + j - 1 > size - 1 or y + j - 1 < 0):
                if mine_grid[x+i-1][y+j-1] == True:
                    count += 1
    return count

grid = []
mine_grid = []
mine_number = []
running = True
alphabet = ["A", "B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
move_x = 0
move_y = 0
number_free = 0

size = int(input("size of grid: "))
odds = int(input("bombs% (0->10): "))
if size > 26:
    size = 26
    print("max size is 26")

# makes the grid
for i in range(size):
    grid_line = []
    mine_grid_line = []
    for j in range(size):
        grid_line.append("-")
        if get_random() >= odds:
            mine_grid_line.append(False)
            number_free += 1
        else:
            mine_grid_line.append(True)
    grid.append(grid_line)
    mine_grid.append(mine_grid_line)

while running:
    # prints the grid
    line = "   "
    for i in range(size):
        line += alphabet[i] + " "
    print(line)
    for i in range(size):
        line = ""
        line += str(i) + "  "
        for j in range(size):
            line += grid[i][j] + " "
        print(line)

    #gets the movea
    accept = False
    while accept == False:
        accept = True
        move = input("move: ")
        try:
            move_x = int(move[1])
        except:
            accept = False
        
        if move_x > size - 1:
            accept = False
        
        move_index = -1
        for i in range(26):
            if alphabet[i] == move[0].upper():
                move_y = i
        if move_y == -1:
            accept = False

    #test if lose
    
    if mine_grid[move_x][move_y] == True:
        print("you lose")
        running = False
    else:
        #shows how many mines neerby
        grid[move_x][move_y] = str(check_number_mines(move_x, move_y))
        #exposes any free spaces neerby
        tiles_to_check = [[move_x, move_y]]
        checked_tiles = []
        while len(tiles_to_check) > 0:
            current_tile = tiles_to_check[len(tiles_to_check) - 1]
            checked = False
            for a in range(len(checked_tiles)):
                if checked_tiles[a] == [current_tile[0], current_tile[1]]:
                    checked = True
            if checked == False:
                if current_tile[0] > size - 1 or current_tile[0] < 0 or current_tile[1] > size - 1 or current_tile[1] < 0: #if out of bounds
                    checked_tiles.append(current_tile)
                    tiles_to_check.pop()
                else:
                    for i in range(-1, 2, 1):
                        for j in range(-1, 2, 1):
                            if not ((i == 0 and j == 0) or current_tile[0] + i < 0 or current_tile[0] + i > size-1 or current_tile[1] + j < 0 or current_tile[1] + j > size-1):
                                if check_number_mines(current_tile[0]+i, current_tile[1]+j) == 0:
                                    tiles_to_check.append([current_tile[0] + i, current_tile[1] + j])
                                    grid[current_tile[0]+i][current_tile[1]+j] = str(0)
                                else:
                                    if check_number_mines(current_tile[0], current_tile[1]) == 0:
                                        grid[current_tile[0]+i][current_tile[1]+j] = str(check_number_mines(current_tile[0]+i, current_tile[1]+j))
                checked_tiles.append(current_tile)
            else:
                tiles_to_check.pop()

    #checked if win
    number_checked = 0
    for i in range(size):
        for j in range(size):
            if grid[i][j] != "-":
                number_checked += 1
    if number_checked >= number_free:
        print("you win!")
        running = False