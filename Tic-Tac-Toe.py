# coding: UTF-8
"""
Script: AprendiendoPython/12
Creación: sanch, 05/02/2022
"""


# Classes

# Imports

# Functions

# Main program
def main():
    turnos = 0
    xwon = ["X", "X", "X"]
    owon = ["O", "O", "O"]
    charplayer = "X"
    inp = ["_" for x in range(9)]
    lstin = [inp[0:3], inp[3:6], inp[6:]]
    print("---------")
    print("|", lstin[0][0], lstin[0][1], lstin[0][2], "|")
    print("|", lstin[1][0], lstin[1][1], lstin[1][2], "|")
    print("|", lstin[2][0], lstin[2][1], lstin[2][2], "|")
    print("---------")
    while True:
        if turnos == 9:
            print("Draw")
            break
        # inl = 0
        while True:
            try:
                # inl += 1
                # if inl > 10:
                #     exit()
                coord = input("Enter the coordinates: ").split()
                x, y = coord[0], coord[1]
                if not 1 <= int(x) <= 3 or not 1 <= int(y) <= 3:
                    print("Coordinates should be from 1 to 3!")
                elif lstin[int(x)-1][int(y)-1] == "_":
                    lstin[int(x) - 1][int(y) - 1] = charplayer
                    turnos += 1
                    if charplayer == "X":
                        charplayer = "O"
                    else:
                        charplayer = "X"
                    break
                else:
                    print("This cell is occupied! Choose another one!")
            except:
                print("You should enter numbers!")
        print("---------")
        print("|", lstin[0][0], lstin[0][1], lstin[0][2], "|")
        print("|", lstin[1][0], lstin[1][1], lstin[1][2], "|")
        print("|", lstin[2][0], lstin[2][1], lstin[2][2], "|")
        print("---------")
        for i in range(3):
            if lstin[i] == xwon:
                print("X wins")
                exit()
            elif lstin[i] == owon:
                print("O wins")
                exit()
        countx = 0
        counto = 0
        for j in range(3):
            for k in range(3):
                if lstin[k][j] == "X":
                    countx += 1
                    if countx == 3:
                        print("X wins")
                        exit()
                elif lstin[k][j] == "O":
                    counto += 1
                    if counto == 3:
                        print("O wins")
                        exit()
            countx = 0
            counto = 0
        if lstin[0][0] == "X" and lstin[1][1] == "X" and lstin[2][2] == "X":
            print("X wins")
            break
        elif lstin[0][2] == "X" and lstin[1][1] == "X" and lstin[2][0] == "X":
            print("X wins")
            break
        elif lstin[0][0] == "O" and lstin[1][1] == "O" and lstin[2][2] == "O":
            print("O wins")
            break
        elif lstin[0][2] == "O" and lstin[1][1] == "O" and lstin[2][0] == "O":
            print("O wins")
            break

if __name__ == '__main__':
    main()
# End
