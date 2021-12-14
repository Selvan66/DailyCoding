
size = 5

def read_board(file):
    output = []
    for i in range(size):
       output.extend([int(x) for x in file.readline().split(' ') if x != ''])
    return output

def all_true(tab):
    for a in tab:
        if not a:
            return False
    return True

def check_false_borad(false_board):
    for i in range(5):
        if all_true(false_board[size * i : size * i + (size)]):
            return True
        if all_true(false_board[i:(size*size):size]):
            return True
    return False

def find_bingo(board, numbers):
    false_board = [False for _ in range(size * size)]
    index = 0
    for num in numbers:
        i = 0
        for val in board:
            if val == num:
                false_board[i] = True
                if check_false_borad(false_board):
                    sum = 0
                    j = 0
                    for state in false_board:
                        if not state:
                            sum += board[j]
                        j += 1
                    return num * sum, index 
            i += 1   
        index += 1
        
if __name__ == '__main__':
    f = open('file.txt')
    bingo = [int(x) for x in f.readline().split(',')]
    _ = f.readline()
    
    val, m = 0, 0
    while True:
        board = read_board(f)
        newline = f.readline()
        if not board:
            break
        
        a, b = find_bingo(board, bingo)
        if b > m:
            val, m = a, b
    
    print(val, m)        
        
        