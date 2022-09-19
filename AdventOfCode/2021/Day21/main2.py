# https://www.youtube.com/watch?v=YDoohWx8204


rolls = [[3, 1], [4, 3], [5, 6], [6, 7], [7, 6], [8, 3], [9, 1]]

def game(turn, p1_pos, p1_score, p2_pos, p2_score):
    player = [p1_pos, p2_pos]
    scores = [p1_score, p2_score]
    
    if p1_score >= 21:
        return [1, 0]
    elif p2_score >= 21:
        return [0, 1]
    
    ans = [0, 0]
    who = turn % 2
    
    for roll in rolls:
        player[who] = (player[who] + roll[0] - 1) % 10 + 1
        scores[who] += player[who]
        now = game(turn + 1, player[0], scores[0], player[1], scores[1])
        ans[0] += roll[1] * now[0]
        ans[1] += roll[1] * now[1]
        scores[who] -= player[who]
        player[who] = (player[who] - roll[0] - 1) % 10 + 1
        
    return ans   


def main():
    print(game(0, 6, 0, 7, 0))

if __name__ == '__main__':
    main()