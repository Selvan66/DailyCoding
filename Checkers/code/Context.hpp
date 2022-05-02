#pragma once

#include <SFML/Graphics.hpp>

#include "Board.hpp"
#include "Player.hpp"

constexpr unsigned int WINDOW_SIZE = 840;

struct Context
{
    Context();

    sf::RenderWindow window;
    Board board;
    Player pOne;
    Player pTwo;
};

Context::Context()
: window(sf::VideoMode(WINDOW_SIZE, WINDOW_SIZE), "Checkers")
, board()
, pOne(Board::White)
, pTwo(Board::Black)
{ 
    window.setFramerateLimit(60);
}


