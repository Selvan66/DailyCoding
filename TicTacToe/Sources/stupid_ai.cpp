//
// Created by rafal on 24.03.2021.
//

#include "stupid_ai.h"
#include "game.h"

#include <random>
#include <chrono>
#include <utility>

stupid_ai::stupid_ai(mark _player_mark, std::string _name) : player(_player_mark, std::move(_name))
{}

bool stupid_ai::make_move(game& _game)
{
    std::default_random_engine generator(std::chrono::high_resolution_clock::now().time_since_epoch().count());
    std::uniform_int_distribution<int> distribution(0, (int)(_game.get_board().get_size() * _game.get_board().get_size()) - 1);
    int dice_roll = distribution(generator);
    while (!_game.get_board().set_field_in_position((int)(dice_roll/_game.get_board().get_size()), (int)(dice_roll%_game.get_board().get_size()), player::get_mark()))
    {
        if (_game.get_board().is_fill())
            return false;
        dice_roll = distribution(generator);
    }

    return true;
}

std::string stupid_ai::get_name() const
{
    return player::get_name();
}