#ifndef SNAKE_GAME_H
#define SNAKE_GAME_H

#include "SFML/Graphics.hpp"

#include <string>

#include "snake.h"

class game
{
private:
    std::string title;
    sf::Vector2u size;
    sf::Event event;
    sf::RenderWindow render_window;

    unsigned int game_speed;
    unsigned int points;

    snake player_snake;
    struct apple
    {
        sf::RectangleShape apple_shape;
        bool isEat;
        explicit apple() : isEat(true)
        {}
    };

    apple game_apple;
public:
    game() = delete;
    game(sf::Vector2u size_, std::string title_);

    void run();
    void drawing();
    void moving_key();
    void events();
    void snake_moving();
    bool snake_collision();

    void spawn_apple();
    void eat_apple();

    sf::Text get_point_text() const;
};


#endif //SNAKE_GAME_H
