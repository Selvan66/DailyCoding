#include "snake.h"

#include <exception>

snake::snake(sf::Vector2f position) : head(position, snakeCell::direction::none, sf::Color::Red)
{}

void snake::addBody()
{
    sf::Vector2f nextPos;
    snakeCell::direction lastDir;
    if (body.empty())
    {
        nextPos = getPosNextBody(head);
        lastDir = head.dir;
    }
    else
    {
        nextPos = getPosNextBody(body.back());
        lastDir = body.back().dir;
    }

    snakeCell nextBody(nextPos, lastDir);
    body.push_back(std::move(nextBody));
}

sf::Vector2f snake::getPosNextBody(const snakeCell& snake_cell)
{
    sf::Vector2f pos = snake_cell.get_pos();
    sf::Vector2f nextPos;

    switch (snake_cell.dir)
    {
        case snakeCell::direction::right:
            nextPos.x = pos.x - snakeCell::size;
            nextPos.y = pos.y;
            break;
        case snakeCell::direction::left:
            nextPos.x = pos.x + snakeCell::size;
            nextPos.y = pos.y;
            break;
        case snakeCell::direction::up:
            nextPos.x = pos.x;
            nextPos.y = pos.y + snakeCell::size;
            break;
        case snakeCell::direction::down:
            nextPos.x = pos.x;
            nextPos.y = pos.y - snakeCell::size;
            break;
        case snakeCell::direction::none:
            throw std::runtime_error("addBody : none option");
    }
    return nextPos;
}

void snake::draw(sf::RenderTarget& target, sf::RenderStates states) const
{
    target.draw(head.rec);
    for (auto& i : body)
        target.draw(i.rec);
}

void snake::moveUp()
{
    if (head.dir != snakeCell::direction::down)
        head.next_dir = snakeCell::direction::up;
}

void snake::moveDown()
{
    if (head.dir != snakeCell::direction::up)
        head.next_dir = snakeCell::direction::down;
}

void snake::moveRight()
{
    if (head.dir != snakeCell::direction::left)
        head.next_dir = snakeCell::direction::right;
}

void snake::moveLeft()
{
    if (head.dir != snakeCell::direction::right)
        head.next_dir = snakeCell::direction::left;
}

void snake::moving()
{
    movingDirection(head);
    for (auto& i : body)
        movingDirection(i);
}

void snake::movingDirection(snakeCell& snake_cell)
{
    sf::Vector2f newPos = snake_cell.get_pos();
    switch (snake_cell.dir)
    {
        case snakeCell::direction::right:
            newPos.x++;
            break;
        case snakeCell::direction::left:
            newPos.x--;
            break;
        case snakeCell::direction::up:
            newPos.y--;
            break;
        case snakeCell::direction::down:
            newPos.y++;
            break;
        case snakeCell::direction::none:
            break;
    }
    snake_cell.set_pos(newPos);
}

void snake::changeDirection()
{
    head.dir = head.next_dir;
    snakeCell::direction tempDir = head.dir;

    for (auto& i : body)
    {
        i.dir = i.next_dir;
        i.next_dir = tempDir;
        snakeCell::direction tempDir2 = i.dir;

        tempDir = tempDir2;
    }
}

sf::Vector2f snake::get_pos() const
{
    return head.get_pos();
}

const std::list<snake::snakeCell>& snake::get_snake_body() const
{
    return body;
}

bool snake::snake_eat_body() const
{
    if(std::any_of(body.begin(), body.end(), [&](auto& i){return i.get_pos() == head.get_pos();}))
        return true;
    return false;
}