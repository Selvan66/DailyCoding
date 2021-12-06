//
// Created by rafal on 02.04.2021.
//

#ifndef BOIDS_BOIDS_H
#define BOIDS_BOIDS_H

#include <vector>
#include <random>

#include "Boid.h"

#define WINDOW_SIZE 1000
#define SEPARATION 15.f
#define VELOCITY_LIMIT 30.f
#define VISUAL_RANGE 100.f
#define ALIGNMENT 8.f
#define AMOUNT 100


class Boids : public sf::Drawable
{
private:
    std::vector<Boid> boids;
    size_t size;

    sf::Vector2f rule1(Boid& _boid)
    {
        sf::Vector2f center_position(0, 0);

        auto range = visual_range(_boid);
        for (auto& i : range)
            center_position += i.position;

        center_position = center_position / float(range.size() + 1);
        if (center_position == sf::Vector2f(0, 0))
            return {0, 0};
        else
            return (center_position - _boid.position) / float(WINDOW_SIZE);
    }

    sf::Vector2f rule2(Boid& _boid)
    {
        sf::Vector2f distance(0, 0);

        auto range = visual_range(_boid);
        for (auto& i : range)
            if (abs(i.position - _boid.position) < SEPARATION)
                distance = distance - (i.position - _boid.position);

        return distance;
    }

    sf::Vector2f rule3(Boid& _boid)
    {
        sf::Vector2f preceived_velocity(0,0);

        auto range = visual_range(_boid);
        for (auto& i : range)
            preceived_velocity = preceived_velocity + i.velocity;

        preceived_velocity = preceived_velocity / float(range.size() + 1);

        if (preceived_velocity == sf::Vector2f(0, 0))
            return {0, 0};
        else
            return (preceived_velocity - _boid.velocity) / ALIGNMENT;
    }
    sf::Vector2f rule4(Boid& _boid)
    {
        float distance = 50.f;
        size_t window_size = WINDOW_SIZE;
        sf::Vector2f center(window_size/2.f, window_size/2.f);
        sf::Vector2f dir = center - _boid.position;
        dir = dir / abs(dir);

        if ((_boid.position.x > (window_size - distance)) || (_boid.position.x < distance))
            return dir * 1.5f;

        if ((_boid.position.y > (window_size - distance)) || (_boid.position.y < distance))
            return dir * 1.5f;

        return dir/1.5f;
    }
    void limit_velocity(Boid& _boid)
    {
        float vlim = VELOCITY_LIMIT;
        if (abs(_boid.velocity) > vlim)
            _boid.velocity = (_boid.velocity / abs(_boid.velocity)) * vlim;
    }

    std::list<Boid> visual_range(Boid& _boid)
    {
        std::list<Boid> range;

        for (auto& i : boids)
            if (&i != &_boid)
                if (abs( _boid.position - i.position) <= VISUAL_RANGE)
                    range.push_back(i);

        return range;
    }
public:
    Boids() = delete;
    explicit Boids(size_t _size) : size(_size)
    {
        std::mt19937 mt_19937(std::chrono::high_resolution_clock::now().time_since_epoch().count());
        std::uniform_int_distribution<int> uniform(20, WINDOW_SIZE - 20);
        std::uniform_real_distribution<float> float_uniform(0, 5);

        for (int i = 0; i < _size; ++i)
        {
            sf::Vector2f pos(uniform(mt_19937), uniform(mt_19937));
            float roll = float_uniform(mt_19937);
            sf::Vector2f vel(roll, std::sqrt(100 - (roll * roll)));
            boids.emplace_back(vel, pos);
        }
    }

    void move_all_boids_to_new_positions()
    {
        sf::Vector2f v1, v2, v3, v4;

        for (auto& i : boids)
        {
            v1 = rule1(i);
            v2 = rule2(i);
            v3 = rule3(i);
            v4 = rule4(i);


            limit_velocity(i);

            i.velocity = i.velocity + v1 + v2 + v3 + v4;
            i.position = i.position + i.velocity;
        }
    }

    void draw(sf::RenderTarget &target, sf::RenderStates states) const override
    {
        for (auto& i : boids)
            target.draw(i, states);
    }
};


#endif //BOIDS_BOIDS_H
