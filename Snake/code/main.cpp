#include <SFML/Graphics.hpp>

#include "game.h"

int main(int, char**)
{
    game snake_game(sf::Vector2u(640, 640), "Snake");
    snake_game.run();

    return 0;
}