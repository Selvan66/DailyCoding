dice = 0
times_dice = 0

def get_next_roll(): 
    global dice, times_dice
    dice = (dice % 100) + 1
    times_dice += 1
    return dice

def get_pos_after_roll(player_pos):
    return ((player_pos - 1) % 10) + 1

def main():
    p1_start = 6
    p2_start = 7
    p1_score = 0
    p2_score = 0
    player_turn = True
    while p1_score < 1000 and p2_score < 1000:
        if player_turn:
            p1_start += get_next_roll() + get_next_roll() + get_next_roll()
            p1_start = get_pos_after_roll(p1_start)
            p1_score += p1_start
        else:
            p2_start += get_next_roll() + get_next_roll() + get_next_roll()
            p2_start = get_pos_after_roll(p2_start)
            p2_score += p2_start
        player_turn = not player_turn
                
    print(p1_score, p2_score, times_dice,  min(p1_score, p2_score) * times_dice)

if __name__ == '__main__':
    main()