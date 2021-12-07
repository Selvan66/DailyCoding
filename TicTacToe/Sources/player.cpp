//
// Created by rafal on 23.03.2021.
//

#include "player.h"

#include <utility>

player::player(const mark _player_mark, std::string  _name) : player_mark(_player_mark), name(std::move(_name))
{}

mark player::get_mark() const
{
    return player_mark;
}

std::string player::get_name() const
{
    return name;
}