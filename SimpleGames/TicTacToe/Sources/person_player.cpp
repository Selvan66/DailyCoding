//
// Created by rafal on 23.03.2021.
//

#include <utility>

#include "board.h"
#include "game.h"
#include "person_player.h"

#include "SFML/Graphics.hpp"


person_player::person_player(mark _player_mark, std::string _name) : player(_player_mark, std::move(_name))
{}


bool person_player::make_move(game& _game)
{

    if (sf::Mouse::isButtonPressed(sf::Mouse::Left))
    {
        sf::Vector2u pos = _game.get_mouse_on_board_position();
        if (_game.get_board().set_field_in_position((int)pos.x, (int)pos.y, player::get_mark()))
            return true;
    }

    return false;
}

std::string person_player::get_name() const
{
    return player::get_name();
}