#include "Game.hpp"

#include <iostream>
#include <stdexcept>

int main()
{
    try {
        Game game;
        game.run();
    } catch (std::exception e) {
        std::cout << e.what() << std::endl;
        return -1;
    }
    return 0;
}