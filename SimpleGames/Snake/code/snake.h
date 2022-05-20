#ifndef SNAKE_SNAKE_H
#define SNAKE_SNAKE_H

#include "SFML/Graphics.hpp"
#include <list>

class snake : public sf::Drawable
{
    struct snakeCell
    {
        enum class direction {left, up, down, right, none};
        direction dir;
        direction next_dir;
        sf::RectangleShape rec;
        static const size_t size = 32;
        snakeCell() : dir(direction::none), next_dir(direction::none)
        {}
        explicit snakeCell(sf::Vector2f pos, direction dir_, sf::Color c = sf::Color::Green) : dir(dir_), next_dir(dir_)
        {
            rec.setPosition(pos);
            rec.setFillColor(c);
            rec.setSize(sf::Vector2f(size, size));
        }

        sf::Vector2f get_pos() const
        {
            return rec.getPosition();
        }

        void set_pos(const sf::Vector2f& pos)
        {
            rec.setPosition(pos);
        }
    };
private:
    std::list<snakeCell> body;
    snakeCell head;
private:
    static sf::Vector2f getPosNextBody(const snakeCell&);
    static void movingDirection(snakeCell&);
public:
    snake() = delete;
    snake(const snake& other) = delete;
    snake& operator=(const snake& other) = delete;

    explicit snake(sf::Vector2f position);

    void addBody();
    void draw(sf::RenderTarget& target, sf::RenderStates states) const override;

    void moveUp();
    void moveDown();
    void moveRight();
    void moveLeft();
    void moving();
    void changeDirection();

    sf::Vector2f get_pos() const;
    bool snake_eat_body() const;
    const std::list<snakeCell>& get_snake_body() const;

};


#endif //SNAKE_SNAKE_H
