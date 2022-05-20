//
// Created by rafal on 23.03.2021.
//

#include "cell.h"
#include "board_view.h"

#include <vector>

#ifndef TICTACTOE_BOARD_H
#define TICTACTOE_BOARD_H

class board
{
private:
    size_t size;

    std::vector<std::vector<cell> > fields;

    friend board_view;
public:
    board();
    explicit board(size_t _size);

    bool set_field_in_position(int x, int y, mark state);
    size_t get_size() const;
    bool is_fill() const;
    bool is_win(mark player) const;
};


#endif //TICTACTOE_BOARD_H
