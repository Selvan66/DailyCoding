//
// Created by rafal on 24.03.2021.
//

#include "cell_view.h"

#include "SFML/Graphics.hpp"

#include <vector>


#ifndef TICTACTOE_BOARD_VIEW_H
#define TICTACTOE_BOARD_VIEW_H


class board;

class board_view : public sf::Drawable
{
private:
    const board& game_board;
    std::vector<cell_view>fields;
public:
    board_view() = delete;
    explicit board_view(const board& _game_board);
    void draw(sf::RenderTarget& target, sf::RenderStates states) const override;
};


#endif //TICTACTOE_BOARD_VIEW_H
