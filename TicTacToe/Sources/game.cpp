//
// Created by rafal on 24.03.2021.
//

#include "game.h"
#include "mark.h"
#include "person_player.h"
#include "stupid_ai.h"


game::game() : title("TicTacToe"), render_window(sf::VideoMode(size, size), title), game_board()
{

}

sf::Vector2u game::get_mouse_on_board_position()
{
    const sf::Vector2i pos = sf::Mouse::getPosition(render_window);

    sf::Vector2u ret;

    if (pos.x < 0)
        ret.x = 0;
    else if (pos.x > size)
        ret.x = game_board.get_size() - 1;
    else
        ret.x = pos.x / (size / game_board.get_size());

    if (pos.y < 0)
        ret.y = 0;
    else if (pos.y > size)
        ret.y = game_board.get_size() - 1;
    else
        ret.y = pos.y / (size / game_board.get_size());

    return ret;
}

size_t game::get_window_size()
{
    return size;
}

#include <iostream>

void game::run(mode _player_mode)
{
    render_window.setFramerateLimit(60);

    player* one;
    player* two;

    switch(_player_mode)
    {
        case mode::ONE_PLAYER:
            one = new person_player(mark::CIRCLE, "Player One");
            two = new stupid_ai(mark::CROSS, "Stupid AI");
            break;
        case mode::TWO_PLAYERS:
            one = new person_player(mark::CIRCLE, "Player One");
            two = new person_player(mark::CROSS, "Player Two");
            break;
    }

    bool one_player_turn = true;
    player* player_turn;
    while(render_window.isOpen())
    {
        if (one_player_turn)
            player_turn = one;
        else
            player_turn = two;
        events();
        if (player_turn->make_move(*this))
            one_player_turn = !one_player_turn;

        draw();

        if (game_board.is_win(one->get_mark()))
        {
            draw_winner(one->get_name());
            break;
        }
        else if (game_board.is_win(two->get_mark()))
        {
            draw_winner(two->get_name());
            break;
        }
        else if (game_board.is_fill())
        {
            draw_winner(" No one");
            break;
        }
    }

    delete one;
    delete two;

    while(!sf::Keyboard::isKeyPressed(sf::Keyboard::Escape) && render_window.isOpen())
        events();
}

void game::draw()
{
    render_window.clear();

    board_view bv(game_board);

    render_window.draw(bv);
    render_window.display();
}

void game::events()
{
    sf::Event event{};
    while(render_window.pollEvent(event))
    {
        if (event.type == sf::Event::EventType::Closed)
            render_window.close();
    }
}

void game::draw_winner(const std::string& name)
{
    sf::Text text;
    sf::Font f;
    if(!f.loadFromFile("../fonts/SPEEC.ttf"))
        throw std::runtime_error("Cannot open font file");

    text.setFont(f);

    text.setString(name + std::string(" Win"));
    text.setFillColor(sf::Color::Cyan);
    text.setCharacterSize(size / 10);
    text.setPosition(sf::Vector2f(size/5.0, size/2.5));

    render_window.draw(text);
    render_window.display();
}

board& game::get_board()
{
    return game_board;
}