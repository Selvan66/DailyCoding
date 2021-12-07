//
// Created by rafal on 23.03.2021.
//

#include "board.h"

#define BOARD_SIZE 3

board::board() : size(BOARD_SIZE)
{
    fields.resize(size);
    for (auto& i : fields)
        i = std::vector<cell>(size);
}

board::board(size_t _size) : size(_size)
{
    fields.resize(size);
    for (auto& i : fields)
        i = std::vector<cell>(size);
}

bool board::set_field_in_position(const int x, const int y, mark state)
{
    cell& change_ceil = fields[x][y];
    return change_ceil.set_state(state);
}

size_t board::get_size() const
{
    return size;
}

bool board::is_fill() const
{
    for (auto& i : fields)
        for (auto& j : i)
            if (!j.is_set())
                return false;

    return true;
}

bool board::is_win(mark player) const
{
    for (int i = 0; i < size; ++i)
    {
        bool horizontal = true;
        bool vertical = true;
        bool slash = true;
        bool backslash = true;
        for (int j = 0; j < size; ++j)
        {
            if (fields[i][j].get_cell_state() != player)
                horizontal = false;

            if (fields[j][i].get_cell_state() != player)
                vertical = false;

            if (fields[j][j].get_cell_state() != player)
                slash = false;
            if (fields[j][size - j - 1].get_cell_state() != player)
                backslash = false;
        }

        if (vertical || horizontal || slash || backslash)
            return true;
    }

    return false;
}