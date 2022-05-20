//
// Created by rafal on 23.03.2021.
//

#include "player.h"
#include "mark.h"

#ifndef TICTACTOE_PERSON_PLAYER_H
#define TICTACTOE_PERSON_PLAYER_H


class person_player : public player
{
public:
    person_player() = delete;
    person_player(mark _player_mark, std::string _name);
    ~person_player() override = default;


    bool make_move(game& _game) override;
    std::string get_name() const override;
};


#endif //TICTACTOE_PERSON_PLAYER_H
