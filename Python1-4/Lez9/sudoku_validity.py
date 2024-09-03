def valid_sudoku(board: list[list[str]]) -> bool:
    lines={0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}
    columns={0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}
    squares={0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}
    for i in range(len(board)):
        for j in range(len(board[i])):
           lines[i].append(board[i][j])
           columns[j].append(board[i][j])
           squares[3*(3//i)+(3//j)].append(board[i][j])
    
    for i in range(9):
        if len(set(lines[i]))<9:
           return False
        if len(set(columns[i]))<9:
           return False
        if len(set(squares[i]))<9:
           return False
    return True