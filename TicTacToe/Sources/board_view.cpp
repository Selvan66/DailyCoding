//
// Created by rafal on 24.03.2021.
//

#include "board_view.h"
#include "board.h"
#include "game.h"

board_view::board_view(const board& _game_board) : game_board(_game_board)
{
    size_t size = game_board.get_size();
    size_t cell_size = game::get_window_size() / size;
    for (int i = 0; i < size; ++i)
        for (int j = 0; j < size; ++j)
            fields.emplace_back(game_board.fields[i][j], cell_size, sf::Vector2i((int)(i * cell_size), (int)(j * cell_size)));
}

void board_view::draw(sf::RenderTarget &target, sf::RenderStates states) const
{
    size_t size = game_board.get_size();
    size_t cell_size = game::get_window_size() / size;
    for (int i = 0; i < size; ++i)
    {
        sf::Vertex horizontal_line[] =
                {
                        sf::Vertex(sf::Vector2f(0, (float)(cell_size * i))),
                        sf::Vertex(sf::Vector2f((float)game::get_window_size(), (float)(cell_size * i)))
                };
        target.draw(horizontal_line, 2, sf::Lines, states);
    }

    for (int i = 0; i < size; ++i)
    {
        sf::Vertex vertical_line[] =
                {
                        sf::Vertex(sf::Vector2f((float)(cell_size * i), 0)),
                        sf::Vertex(sf::Vector2f((float)(cell_size* i), (float)game::get_window_size()))
                };
        target.draw(vertical_line, 2, sf::Lines, states);
    }

    for (auto& cell : fields)
        target.draw(cell, states);
}