//
// Created by rafal on 23.03.2021.
//

#include "game.h"

int main(int argc, char* argv[])
{
    game _game;
    if (argc == 2)
    {
        if (std::string(argv[1]) == "two")
            _game.run(game::mode::TWO_PLAYERS);
        else
            _game.run(game::mode::ONE_PLAYER);
    }
    else
    {
        _game.run(game::mode::ONE_PLAYER);
    }
    return 0;
}