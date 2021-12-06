#include <iostream>

#include "SFML/Graphics.hpp"
#include "Boids.h"

int main()
{
    sf::RenderWindow render_window(sf::VideoMode(WINDOW_SIZE, WINDOW_SIZE), "Boids");
    sf::Event event{};

    Boids boids(AMOUNT);

    render_window.setFramerateLimit(33);
    while(render_window.isOpen())
    {
        render_window.pollEvent(event);
        if (event.type == sf::Event::EventType::Closed)
            render_window.close();

        render_window.clear();
        render_window.draw(boids);
        render_window.display();

        boids.move_all_boids_to_new_positions();
    }
    return 0;
}
