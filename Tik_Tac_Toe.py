try:
    Size = int(input("Board Size: Enter a odd number: "))
    boxSize = 0                       # initialize the box size
    if Size > 1 and Size%2 != 0:
        boxSize = Size
    else:
        print("Invalid Number! Please enter Odd Number.")

    CvRange = boxSize * boxSize
    cellval = list(range(1,(CvRange+1)))

    matrix = []
    moves = int((CvRange/2) + 0.5)

    Turn1 = []
    Turn2 = []

    x = 0
    y = 0

    P1 = 0
    P2 = 0

    p1Input= []
    for i in range(boxSize):            # player1 input for comparison
        p1Input.append('X')
    #print(p1Input)

    p2Input = []
    for j in range(boxSize):            # player2 input for comparison
        p2Input.append('o')
    #print(p2Input)
    colMatrix = []
    digMatrix = []
    rdigMatrix = []

    output = 0
    coloutput = 0
    digoutput = 0
    rdigoutput = 0

    class TTCgame:
        def __init__(self, a, b):
            self.a = a
            self.b = b

        def boxSize(self, cV): # Create Matrix Box for Game
            self.cV = cV
            for k in range(boxSize):
                innerCell = []
                for m in range(boxSize):
                    innerCell.append(self.cV[m])
                matrix.append(innerCell)
                self.cV = self.cV[boxSize::]

        def gameRule(self, Xindex, Yindex, op, cop, dop, rop):
            self.Xindex = Xindex
            self.Yindex = Yindex
            self.op = op
            self.cop = cop
            self.dop = dop
            self.rop = rop

            for q in range(boxSize):  # Show Matrix
                print(boxSize * " ---  ")
                for w in range(boxSize):
                    print(f"| {matrix[q][w]} |", end=" ")
                print()
            print(boxSize * " ---  ")

            while True :
                for l in range(len(matrix)):                        # Row wise Input
                    if matrix[l] == p1Input:
                        self.op = matrix[l]
                        print(self.op)
                    elif matrix[l] == p2Input:
                        self.op = matrix[l]
                        print(self.op)

                if self.op == p1Input:
                    print("P1 Is Winner!")
                    break

                if self.op == p2Input:
                    print("P2 Is Winner!")
                    break

                for n in range(len(matrix)):                       # Column wise Input
                    matrixColumn = []
                    for p in range(len(matrix)):
                        matrixColumn.append(matrix[p][n])
                    colMatrix.append(matrixColumn)
                #print(colMatrix)

                for r in range(len(colMatrix)):
                    if colMatrix[r] == p1Input:
                        self.cop = colMatrix[r]
                        print(self.cop)
                    elif colMatrix[r] == p2Input:
                        self.cop = colMatrix[r]
                        print(self.cop)

                if self.cop == p1Input:
                    print("P1 Is Winner!")
                    break

                if self.cop == p2Input:
                    print("P2 Is Winner!")
                    break

                for d1 in range(len(matrix)):                       # Diagonal wise Input
                    dM = []
                    for d2 in range(len(matrix)):
                        dM.append(matrix[d2][d2])
                    digMatrix.append(dM)
                    break
                #print(digMatrix)

                for d3 in range(len(digMatrix)):
                    if digMatrix[d3] == p1Input:
                        self.dop = digMatrix[d3]
                        print(self.dop)
                    elif digMatrix[d3] == p2Input:
                        self.dop = digMatrix[d3]
                        print(self.dop)

                if self.dop == p1Input:
                    print("P1 Is Winner!")
                    break

                if self.dop == p2Input:
                    print("P2 Is Winner!")
                    break

                for rd1 in range(len(matrix)):                       # Reverse Diagonal wise Input
                    rdM = []
                    for rd2 in range(len(matrix)):
                        rdM.append(matrix[rd2][len(matrix)-rd2-1])
                    rdigMatrix.append(rdM)
                    break
                # print(rdigMatrix)

                for rd3 in range(len(rdigMatrix)):
                    if rdigMatrix[rd3] == p1Input:
                        self.rop = rdigMatrix[rd3]
                        print(self.rop)
                    elif rdigMatrix[rd3] == p2Input:
                        self.rop = rdigMatrix[rd3]
                        print(self.rop)

                if self.rop == p1Input:
                    print("P1 Is Winner!")
                    break

                if self.rop == p2Input:
                    print("P2 Is Winner!")
                    break

                Turn1.append(self.a)
                # print(Turn1)
                Turn2.append(self.b)

                if len(Turn1) > moves or len(Turn2) > moves:
                    print("Moves are Over")
                    break

                self.a = int(input("P1: Choose any cell number: "))    # Player 1 Turn

                for item in matrix:                                    # Find the exact location of the given input
                    if self.a in item:
                        self.Xindex = matrix.index(item)
                        self.Yindex = item.index(self.a)
                P1value = matrix[self.Xindex][self.Yindex]
                print(f"Player 1: {P1value} --> X")

                while True:
                    if self.a == P1value and P1value <= CvRange:      # Change the matrix value by P1 input
                        matrix[self.Xindex][self.Yindex] = 'X'
                        break
                    else:
                        print(f"Try Again! Number Should not grater than {CvRange}.")
                    self.a = int(input("P1: Choose any cell number: "))

                    for item in matrix:  # Find the exact location of the given input
                        if self.a in item:
                            self.Xindex = matrix.index(item)
                            self.Yindex = item.index(self.a)
                    P1value = matrix[self.Xindex][self.Yindex]
                    print(f"Player 1: {P1value} --> X")

                for q in range(boxSize):  # Show Matrix
                    print(boxSize * " ---  ")
                    for w in range(boxSize):
                        print(f"| {matrix[q][w]} |", end=" ")
                    print()
                print(boxSize * " ---  ")

                self.b = int(input("P2: Choose any cell number: "))
                for itm in matrix:                                    # Find the exact location of the given input
                    if self.b in itm:
                        self.Xindex= matrix.index(itm)
                        self.Yindex = itm.index(self.b)
                P2value = matrix[self.Xindex][self.Yindex]
                print(f"Player 2: {P2value} --> o")

                while True:
                    if self.b == P2value and P2value <= CvRange:      # Change the matrix value by P2 input
                        matrix[self.Xindex][self.Yindex] = 'o'
                        break
                    else:
                        print(f"Try Again! Number Should not grater than {CvRange}.")
                    self.b = int(input("P2: Choose any cell number: "))
                    for itm in matrix:  # Find the exact location of the given input
                        if self.b in itm:
                            self.Xindex = matrix.index(itm)
                            self.Yindex = itm.index(self.b)
                    P2value = matrix[self.Xindex][self.Yindex]
                    print(f"Player 2: {P2value} --> o")

                for q in range(boxSize):  # Show Matrix
                    print(boxSize * " ---  ")
                    for w in range(boxSize):
                        print(f"| {matrix[q][w]} |", end=" ")
                    print()
                print(boxSize * " ---  ")

    TTC = TTCgame(P1, P2)
    TTC.boxSize(cellval)
    TTC.gameRule(x,y,output,coloutput,digoutput,rdigoutput)
except ValueError:
    print("Try Again! Do not Enter Decimal Number.")
