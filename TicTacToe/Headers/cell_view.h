//
// Created by rafal on 24.03.2021.
//

#include "SFML/Graphics.hpp"


#ifndef TICTACTOE_CELL_VIEW_H
#define TICTACTOE_CELL_VIEW_H


class cell;

class cell_view : public sf::Drawable
{
private:
    const cell& single_cell;
    size_t cell_size;
    sf::Vector2i pos;

    sf::CircleShape get_circle() const;
public:
    cell_view() = delete;
    cell_view(const cell& _single_cell, size_t _cell_size, sf::Vector2i _pos);

    void draw(sf::RenderTarget& target, sf::RenderStates states) const override;
};


#endif //TICTACTOE_CELL_VIEW_H
