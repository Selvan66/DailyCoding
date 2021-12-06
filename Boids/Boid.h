//
// Created by rafal on 02.04.2021.
//

#ifndef BOIDS_BOID_H
#define BOIDS_BOID_H

#include "SFML/Graphics.hpp"
#include <cmath>
#include <chrono>
#include <list>


float abs(sf::Vector2f _vec)
{
    return std::sqrt(_vec.x * _vec.x + _vec.y * _vec.y);
}


const double pi = std::acos(-1);

class Boid : public sf::Drawable
{
public:
    sf::Vector2f velocity;
    sf::Vector2f position;

    Boid() = delete;
    Boid(sf::Vector2f _velocity, sf::Vector2f _position) : velocity(_velocity), position(_position)
    {}

    void draw(sf::RenderTarget &target, sf::RenderStates states) const override
    {
        sf::VertexArray triangle(sf::Triangles, 3);

        sf::Transform transform;
        transform.rotate(165);

        sf::Vector2f first_vertex = transform.transformPoint(velocity);

        sf::Transform transform2;
        transform2.rotate(-165);

        sf::Vector2f second_vertex = transform2.transformPoint(velocity);

        first_vertex = (first_vertex / abs(first_vertex)) * 20.f;
        second_vertex = (second_vertex / abs(second_vertex)) * 20.f;


        triangle[0].position = sf::Vector2f(position);
        triangle[1].position = sf::Vector2f(position + first_vertex);
        triangle[2].position = sf::Vector2f(second_vertex + position);

        triangle[0].color = sf::Color::Cyan;
        triangle[1].color = sf::Color::Cyan;
        triangle[2].color = sf::Color::Cyan;

        target.draw(triangle, states);
    }

};


#endif //BOIDS_BOID_H
