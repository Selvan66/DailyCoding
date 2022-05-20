#include "game.h"
#include "board.h"

#include <random>
#include <string>

game::game(sf::Vector2u size_, std::string title_)  : size(size_), title(std::move(title_)), player_snake(sf::Vector2f(float(size.x) / 2.f, float(size.y) / 2.f)),
                                                      render_window(sf::VideoMode(size.x, size.y), title), event(), game_speed(60), points(0)
{
    game_apple.apple_shape.setFillColor(sf::Color::Yellow);
    game_apple.apple_shape.setSize(sf::Vector2f(board::cell, board::cell));
    game_apple.isEat = true;
    spawn_apple();
}

void game::run()
{
    while(render_window.isOpen())
    {
        render_window.setFramerateLimit(game_speed + points);

        events();

        snake_moving();

        if (game_apple.apple_shape.getPosition() == player_snake.get_pos())
            eat_apple();

        drawing();

        if (snake_collision())
            break;
    }

}

void game::drawing()
{
    render_window.clear();

    render_window.draw(player_snake);
    render_window.draw(game_apple.apple_shape);

    sf::Text text = get_point_text();
    render_window.draw(text);

    render_window.display();
}

void game::moving_key()
{
    if (sf::Keyboard::isKeyPressed(sf::Keyboard::S))
        player_snake.moveDown();
    else if (sf::Keyboard::isKeyPressed(sf::Keyboard::A))
        player_snake.moveLeft();
    else if (sf::Keyboard::isKeyPressed(sf::Keyboard::D))
        player_snake.moveRight();
    else if (sf::Keyboard::isKeyPressed(sf::Keyboard::W))
        player_snake.moveUp();
}

void game::events()
{
    while (render_window.pollEvent(event))
    {
        if (event.type == sf::Event::EventType::Closed)
            render_window.close();
    }
}

void game::snake_moving()
{
    moving_key();
    if(board::isCell(player_snake.get_pos()))
    {
        player_snake.changeDirection();
    }
    player_snake.moving();
}

bool game::snake_collision()
{
    if ((player_snake.get_pos().x >= float(size.x)) || (player_snake.get_pos().y >= float(size.y)))
        return true;
    if ((player_snake.get_pos().x < 0) || (player_snake.get_pos().y < 0))
        return true;

    if (player_snake.snake_eat_body())
        return true;

    return false;
}

void game::spawn_apple()
{

    game_apple.isEat = false;
    auto body = player_snake.get_snake_body();
    std::random_device rd;
    bool isSnake;
    float roll_x;
    float roll_y;
    do
    {
        isSnake = false;
        roll_x = float(unsigned int(rd()) % 19) * board::cell;
        roll_y = float(unsigned int(rd()) % 19) * board::cell;

        if (player_snake.get_pos().x == roll_x && player_snake.get_pos().y == roll_y)
            isSnake = true;

        for (auto& i : body)
            if (i.get_pos().x == roll_x && i.get_pos().y == roll_y)
                isSnake = true;

    }while(isSnake);

    game_apple.apple_shape.setPosition(roll_x, roll_y);
}

void game::eat_apple()
{
    game_apple.isEat = true;
    spawn_apple();
    player_snake.addBody();
    points += 5;
}

sf::Text game::get_point_text() const
{
    sf::Text text;
    static sf::Font f;
    f.loadFromFile("../fonts/SPEEC.ttf");
    text.setFont(f);

    text.setString((std::string("Points: ") + std::to_string(points)));
    text.setFillColor(sf::Color::White);
    text.setCharacterSize(24);
    text.setPosition(sf::Vector2f(0, float(size.y - 40.)));

    return text;
}