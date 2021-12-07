//
// Created by rafal on 24.03.2021.
//

#include "player.h"
#include "mark.h"


#ifndef TICTACTOE_STUPID_AI_H
#define TICTACTOE_STUPID_AI_H

class stupid_ai : public player
{
public:
    stupid_ai() = delete;
    stupid_ai(mark _player_mark, std::string _name);
    ~stupid_ai() override = default;

    bool make_move(game& _game) override;
    std::string get_name() const override;
};


#endif //TICTACTOE_STUPID_AI_H
