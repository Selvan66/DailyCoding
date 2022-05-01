#include <SFML/Graphics.hpp>

#include "Board.hpp"

int main()
{
    sf::RenderWindow window(sf::VideoMode(840, 840), "Checkers");
    window.setFramerateLimit(60);

    Board board;
    while (window.isOpen())
    {
        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                window.close();
        }

        window.clear();
        window.draw(board);
        window.display();
    }

    return 0;
}