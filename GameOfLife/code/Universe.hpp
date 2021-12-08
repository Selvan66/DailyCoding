#pragma once

#include "SFML/Graphics.hpp"

#include <random>

class Universe : public sf::Drawable {
    public:
        Universe();
        virtual void draw(sf::RenderTarget &target, sf::RenderStates states) const;
        void next_generation();
    private:
        int count_neighbors(int x, int y);
    private:
        static const int mSize = 200;
        bool mCells[mSize][mSize] = {false};
};

Universe::Universe() {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> distr(0, mSize - 1);
    for (int i = 0; i < mSize; ++i) {
        int j = 0;
        while (j < (mSize / 3)) {
            int rnum = distr(gen);
            if (!mCells[i][rnum]) {
                mCells[i][rnum] = true;
                ++j;
            }
        }
    }
}

void Universe::draw(sf::RenderTarget &target, sf::RenderStates states) const {
    for (int i = 0; i < mSize; ++i)
        for (int j = 0; j < mSize; ++j)
            if (mCells[i][j]) {
                sf::Vertex pixel(sf::Vector2f((float)i, (float)j));
                target.draw(&pixel, 1, sf::Points);
            }
}

void Universe::next_generation() {
    bool newGrid[mSize][mSize];
    for (int i = 0; i < mSize; ++i)
        for (int j = 0; j < mSize; ++j) {
            int num_neig = count_neighbors(i, j);
            if (mCells[i][j])
                newGrid[i][j] = (num_neig == 2 || num_neig == 3) ? true : false;
            else
                newGrid[i][j] =  (num_neig == 3) ? true : false;
        }
    std::swap(mCells, newGrid);
}

int Universe::count_neighbors(int x, int y) {
    int counter = 0;
    try {
        if (mCells[x - 1][y - 1])
            counter++;
    } catch (std::out_of_range) {}
    try {
        if (mCells[x][y - 1])
            counter++;
    } catch (std::out_of_range) {}
    try {
        if (mCells[x + 1][y - 1])
            counter++;
    } catch (std::out_of_range) {}
    try {
        if (mCells[x - 1][y])
            counter++;
    } catch (std::out_of_range) {}
    try {
        if (mCells[x + 1][y])
            counter++;
    } catch (std::out_of_range) {}
    try {
        if (mCells[x - 1][y + 1])
            counter++;
    } catch (std::out_of_range) {}
    try {
        if (mCells[x][y + 1])
            counter++;
    } catch (std::out_of_range) {}
    try {
        if (mCells[x + 1][y + 1])
            counter++;
    } catch (std::out_of_range) {}

    return counter;
}