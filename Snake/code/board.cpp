#include "board.h"

bool board::isCell(const sf::Vector2f pos)
{
    return ((static_cast<int>(pos.x) % cell == 0) && (static_cast<int>(pos.y) % cell == 0));
}