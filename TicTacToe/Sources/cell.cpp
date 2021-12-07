//
// Created by rafal on 24.03.2021.
//

#include "cell.h"


cell::cell() : cell_state(mark::NONE)
{}

cell::cell(mark _cell_state) : cell_state(_cell_state)
{}

bool cell::set_state(mark state)
{
    if (is_set())
        return false;

    cell_state = state;
    return true;
}

bool cell::is_set() const
{
    if (cell_state == mark::NONE)
        return false;
    return true;
}

mark cell::get_cell_state() const
{
    return cell_state;
}