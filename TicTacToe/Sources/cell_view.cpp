//
// Created by rafal on 24.03.2021.
//

#include "cell_view.h"
#include "cell.h"

cell_view::cell_view(const cell& _single_cell, size_t _cell_size, sf::Vector2i _pos) : single_cell(_single_cell), cell_size(_cell_size), pos(_pos)
{ }

void cell_view::draw(sf::RenderTarget &target, sf::RenderStates states) const
{
   if (single_cell.cell_state == mark::CIRCLE)
       target.draw(get_circle(), states);
   else if (single_cell.cell_state == mark::CROSS)
   {
       sf::Vertex line1[] =
       {
           sf::Vertex(sf::Vector2f((float)pos.x, (float)pos.y)),
           sf::Vertex(sf::Vector2f((float)(cell_size + pos.x), (float)(cell_size + pos.y)))
       };

       sf::Vertex line2[] =
       {
           sf::Vertex(sf::Vector2f((float)pos.x, (float)(cell_size + pos.y))),
           sf::Vertex(sf::Vector2f((float)(cell_size + pos.x), (float)pos.y))
       };

       target.draw(line1, 2, sf::Lines, states);
       target.draw(line2, 2, sf::Lines, states);
   }
}

sf::CircleShape cell_view::get_circle() const
{
    sf::CircleShape circle((float)(cell_size - 10)/2.0f);
    circle.setPosition((float)pos.x, (float)pos.y);
    circle.setFillColor(sf::Color::Transparent);
    circle.setOutlineThickness(2.0);
    circle.setOutlineColor(sf::Color::White);

    return circle;
}