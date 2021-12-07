//
// Created by rafal on 23.03.2021.
//


#include "mark.h"
#include "board.h"
#include <string>

#ifndef TICTACTOE_PLAYER_H
#define TICTACTOE_PLAYER_H

class game;

class player
{
private:
    const mark player_mark;
    std::string name;
public:
    player() = delete;
    player(mark _player_mark, std::string  _name);
    virtual ~player() = default;

    virtual bool make_move(game& _game) = 0;
    mark get_mark() const;
    virtual std::string get_name() const;
};


#endif //TICTACTOE_PLAYER_H
