#ifndef SNAKE_BOARD_H
#define SNAKE_BOARD_H

#include "SFML/Graphics.hpp"

struct board
{
    static const size_t cell = 32;

    board() = delete;

    static bool isCell(sf::Vector2f pos);
};


#endif //SNAKE_BOARD_H
