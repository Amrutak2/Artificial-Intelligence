def Boardprint():
    print("EMPTY(0,0)   BREEZE(0,1)   PIT(0,2)        BREEZE(0,3)")
    print("STENCH(1,0)  EMPTY(1,1)    GLITTER(1,2)    EMPTY(1,3)")
    print("WUMPUS(2,0)  GOLD(2,1)     PIT(2,2)        GLITTER(2,3)")
    print("STENCH(3,0)  EMPTY(3,1)    GLITTER(3,2)    PIT(3,3)")


def knowledge_agent(env, i, j):

    if env[i][j] == 9:
        pos_row, pos_col = i, j
        print("\nNow the agent is at the position: " + str(pos_row) + "," + str(pos_col))
        print(" You have come across a stench!")
        Boardprint()
        return pos_row, pos_col
    elif env[i][j] == 8:
        pos_row, pos_col = i, j
        print("\nNow the agent is at the position:  " + str(pos_row) + "," + str(pos_col))
        print(" You have come across a glitter!")
        Boardprint()
        return pos_row, pos_col

    elif env[i][j] == 7:
        pos_row, pos_col = i, j
        print("\nNow the agent is at the position: " + str(pos_row) + "," + str(pos_col))
        print(" You have come across a pit!")
        Boardprint()
        return -5, -5
    elif env[i][j] == 6:
        pos_row, pos_col = i, j
        print("\nNow the agent is at the position: " + str(pos_row) + "," + str(pos_col))
        print(" Hurray!!!!! You found gold!")
        return -4, -4
    elif env[i][j] == 5:
        pos_row, pos_col = i, j
        print("\nNow the agent is at the position: " + str(pos_row) + "," + str(pos_col))
        print(" You will feel breeze!")
        Boardprint()
        return pos_row, pos_col
    elif env[i][j] == -1:
        pos_row, pos_col = i, j
        print("\nNow the agent is at the position:  " + str(pos_row) + "," + str(pos_col))
        print(" Alas!!!Wumpus is there!")
        Boardprint()
        return -5, -5
    else:
        pos_row, pos_col = i, j
        print("\nNow the agent is at the position: " + str(pos_row) + "," + str(pos_col))
        Boardprint()
        return pos_row, pos_col


def inpcheck(pos_row, pos_col):
    if pos_row == 0 and pos_col == 0:
        print("\n Now you can go at: 	" + str(pos_row + 1) + "	" + str(pos_col))
        print("You can go at: 	" + str(pos_row) + "	" + str(pos_col + 1))
        row_val = int(input("\nEnter the input for the row => "))
        col_val = int(input("nter the input for the column => "))
        if row_val == pos_row + 1 and col_val == pos_col or row_val == pos_row and col_val == pos_col + 1:
            return row_val, col_val
        else:
            return -5
    elif pos_row == 3 and pos_col == 0:
        print("\nNow you can go at: " + str(pos_row - 1) + "	" + str(pos_col))
        print("You can go at:	" + str(pos_row) + "	" + str(pos_col + 1))
        row_val = int(input("\nEnter the input for the row => "))
        col_val = int(input("Enter the input for the column => "))
        if row_val == pos_row - 1 and col_val == pos_col or row_val == pos_row and col_val == pos_col + 1:
            return row_val, col_val
        else:
            return -5
    elif pos_row == 3 and pos_col == 3:
        print("\n Now you can go at:	" + str(pos_row - 1) + "	" + str(pos_col))
        print(" You can go at:  " + str(pos_row) + "	" + str(pos_col - 1))
        row_val = int(input("\nEnter the input for the row => "))
        col_val = int(input("Enter the input for the column => "))
        if row_val == pos_row - 1 and col_val == pos_col or row_val == pos_row and col_val == pos_col - 1:
            return row_val, col_val
        else:
            return -5
    elif pos_row == 0 and pos_col == 3:
        print("\nNow you can go at 	" + str(pos_row + 1) + "	" + str(pos_col))
        print("you can go at 	" + str(pos_row) + "	" + str(pos_col - 1))
        row_val = int(input("\nEnter the input for the row => "))
        col_val = int(input("Enter the input for the column => "))
        if row_val == pos_row + 1 and col_val == pos_col or row_val == pos_row and col_val == pos_col - 1:
            return row_val, col_val
        else:
            return -5, -5
    elif pos_row == 1 and pos_col == 0 or pos_row == 2 and pos_col == 0 or pos_row == 3 and pos_col == 0:
        print("\nNow you can go at 	" + str(pos_row + 1) + "	" + str(pos_col))
        print("you can go at 	" + str(pos_row) + "	" + str(pos_col + 1))
        row_val = int(input("\nEnter the input for the row => "))
        col_val = int(input("Enter the input for the column => "))
        if row_val == pos_row + 1 and col_val == pos_col or row_val == pos_row and col_val == pos_col + 1:
            return row_val, col_val
        else:
            return -5, -5
    elif pos_row == 0 and pos_col == 3 or pos_row == 1 and pos_col == 3 or pos_row == 2 and pos_col == 3 or pos_row == 3 and pos_col == 3:
        print("Now you can go at: 	" + str(pos_row + 1) + "	" + str(pos_col))
        print("And you can go at:	" + str(pos_row) + "	" + str(pos_col - 1))
        row_val = int(input("\nEnter the input for the row => "))
        col_val = int(input("Enter the input for the column => "))
        if row_val == pos_row + 1 and col_val == pos_col or row_val == pos_row and col_val == pos_col - 1:
            return row_val, col_val
        else:
            return -5, -5
    elif pos_row == 3 and pos_col == 1 or pos_row == 3 and pos_col == 2 or pos_row == 3 and pos_col == 3:
        print("\nNow you can go at :  " + str(pos_row) + "	" + str(pos_col + 1))
        print("you can go at :	" + str(pos_row) + "	" + str(pos_col - 1))
        print("you can go at :	" + str(pos_row - 1) + "	" + str(pos_col))
        row_val = int(input("\nEnter the input for the row => "))
        col_val = int(input("Enter the input for the column => "))
        if row_val == pos_row and col_val == pos_col + 1 or row_val == pos_row and col_val == pos_col - 1 or row_val == pos_row - 1 and col_val == pos_col:
            return row_val, col_val
        else:
            return -5, -5
    else:
        print("\nNow you can go at: 	" + str(pos_row) + "	" + str(pos_col + 1))
        print("You can go at: 	" + str(pos_row) + "	" + str(pos_col - 1))
        print("You can go at: 	" + str(pos_row + 1) + "	" + str(pos_col))
        row_val = int(input("\nEnter the input for the row => "))
        col_val = int(input("Enter the input for the column => "))
        if row_val == pos_row and col_val == pos_col + 1 or row_val == pos_row and col_val == pos_col - 1 or row_val == pos_row + 1 and col_val == pos_col:
            return row_val, col_val
        else:
            return -5, -5


def inpreversecheck(pos_row, pos_col):
    if pos_row == 0 and pos_col == 3:
        print("So, you can go at: 	" + str(pos_row) + "	" + str(pos_col - 1))
        row_val = int(input("\nEnter the input for the row => "))
        col_val = int(input("Enter the input for the column => "))
        if row_val == pos_row and col_val == pos_col - 1:
            return row_val, col_val
        else:
            return -5, -5
    elif pos_row == 0 and pos_col == 2 or pos_row == 0 and pos_col == 1:
        print("Now, you can go at " + str(pos_row) + "	" + str(pos_col + 1))
        print("You can go at " + str(pos_row) + "	" + str(pos_col - 1))
        row_val = int(input("\nEnter the input for the row => "))
        col_val = int(input("Enter the input for the column => "))
        if row_val == pos_row and col_val == pos_col - 1 or row_val == pos_row and col_val == pos_col + 1:
            return row_val, col_val
        else:
            return -5, -5
    elif pos_row == 1 and pos_col == 0 or pos_row == 2 and pos_col == 0:
        print("\nNow, you can go at: " + str(pos_row - 1) + "	" + str(pos_col))
        print("\nYou can go at: " + str(pos_row) + "	" + str(pos_col + 1))
        row_val = int(input("\nEnter the input for the row => "))
        col_val = int(input("Enter the input for the column => "))
        if row_val == pos_row - 1 and col_val == pos_col or row_val == pos_row and col_val == pos_col + 1:
            return row_val, col_val
        else:
            return -5, -5
    elif pos_row == 1 and pos_col == 3 or pos_row == 2 and pos_col == 3:
        print("Now, you can go at: " + str(pos_row - 1) + "	" + str(pos_col))
        print("You can go at: " + str(pos_row) + "	" + str(pos_col - 1))
        row_val = int(input("\nEnter the input for the row => "))
        col_val = int(input("Enter the input for the column => "))
        if row_val == pos_row - 1 and col_val == pos_col or row_val == pos_row and col_val == pos_col - 1:
            return row_val, col_val
        else:
            return -5, -5
    else:
        print("\nYou can go at " + str(pos_row - 1) + "	" + str(pos_col))
        print("You can go at " + str(pos_row) + "	" + str(pos_col - 1))
        print("You can go at " + str(pos_row) + "	" + str(pos_col + 1))
        row_val = int(input("\nThe row position is: "))
        col_val = int(input("The column position is: "))
        if row_val == pos_row - 1 and col_val == pos_col or row_val == pos_row and \
        col_val == pos_col - 1 or row_val == pos_row and col_val == pos_col + 1:
            return row_val, col_val
        else:
            return -5, -5


env = [[0, 5, 7, 5],
             [9, 0, 8, 0],
             [-1, 6, 7, 8],
             [9, 0, 8, 7]]

pos_row, pos_col = 0, 0
Boardprint()
print("\nAt the Initial position, the agent is at: " + str(pos_row) + "," + str(pos_col))
print("\nNow, you can go at: " + str(pos_row + 1) + "	" + str(pos_col))
print("You can go at " + str(pos_row) + "	" + str(pos_col + 1))

row_val = int(input("\nThe row position is: "))
col_val = int(input("\nThe column position is:  "))
if row_val == 1 and col_val == 0 or row_val == 0 and col_val == 1:
    pos_row, pos_col = knowledge_agent(env, row_val, col_val)
else:
    print("Oops! Not valid")

while pos_row >= 0:
    row_val, col_val = inpcheck(pos_row, pos_col)
    if row_val != -5 and col_val != -5:
        pos_row, pos_col = knowledge_agent(env, row_val, col_val)
    else:
        print("\nOh ho! Not valid")

if pos_row == -5:
    print("\nOops!!! Game over!!! Better luck next time!!!")
else:
    print("\nYipee!! You have unlocked the next level. So, go back to your initial position")

    pos_row, pos_col = 2, 1

    while pos_row >= 0:
        row_val, col_val = inpreversecheck(pos_row, pos_col)
        if row_val == 0 and col_val == 0:
            pos_row, pos_col = -4, -4
        elif row_val != -5 and col_val != -5:
            pos_row, pos_col = knowledge_agent(env, row_val, col_val)
        else:
            print("\nOops! Not valid")

    if pos_row == -5:
        print("\nAlas!! You were very very close to the game but unfortunately you have failed!!! Better luck next time")
    else:
        print("\nHurray!!! You won the game!!!!! Congratulations.")



def print_hi(name):

    print(f'Hi, {name}')



if __name__ == '__main__':
    print_hi('Pycharm')