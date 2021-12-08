#pragma once

#include "Universe.hpp"

class Game{
    public:
        Game();
        void run();
    private:
        void processInput();
        void draw();
    private:
        sf::RenderWindow mWindow;
        Universe mUniverse;
        bool mStart;
        static const int mSize = 200;
};

Game::Game() : mWindow(sf::VideoMode({mSize, mSize}), "Game of life"), 
mUniverse(), mStart(false) {
}

void Game::run() {
    mWindow.setFramerateLimit(11);
    while (mWindow.isOpen())
    {
        processInput();
        draw();
        if (mStart)
            mUniverse.next_generation();
    }
}

void Game::processInput() {
    sf::Event event;
    while (mWindow.pollEvent(event))
    {
        if (event.type == sf::Event::Closed)
            mWindow.close();
        if (event.type == sf::Event::KeyPressed)
            if (event.key.code == sf::Keyboard::P)
                mStart = !mStart;
    }
}

void Game::draw() {
    mWindow.clear();
    mWindow.draw(mUniverse);
    mWindow.display();
}
