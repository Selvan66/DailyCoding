//
// Created by rafal on 24.03.2021.
//

#include "person_player.h"
#include "board.h"

#include <string>

#include "SFML/Graphics.hpp"

#ifndef TICTACTOE_GAME_H
#define TICTACTOE_GAME_H

#define WINDOW_SIZE 600

class game
{
    board game_board;
    static const size_t size = WINDOW_SIZE;
    const std::string title ;
    sf::RenderWindow render_window;

    void events();
    void draw();
    void draw_winner(const std::string& name);
public:
    enum class mode{ONE_PLAYER, TWO_PLAYERS};

    game();

    sf::Vector2u get_mouse_on_board_position();
    void run(mode player_mode);

    static size_t get_window_size();
    board& get_board();
};


#endif //TICTACTOE_GAME_H
