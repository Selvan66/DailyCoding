//
// Created by rafal on 24.03.2021.
//


#include "mark.h"
#include "cell_view.h"


#ifndef TICTACTOE_CELL_H
#define TICTACTOE_CELL_H


class cell
{
private:
    mark cell_state;

    friend cell_view;
public:
    cell();
    explicit cell(mark _cell_state);

    bool set_state(mark state);
    bool is_set() const;
    mark get_cell_state() const;
};

#endif //TICTACTOE_CELL_H
