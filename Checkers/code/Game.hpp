#pragma once

#include "Context.hpp"

class Game
{
    public:
        Game();
        void run();
        void processInput();
        void render();
    private:
        Context mContext;
};

Game::Game()
: mContext() 
{ }

void Game::run()
{
    while (mContext.window.isOpen())
    {
        processInput();
        render();
    }
}

void Game::processInput()
{
    sf::Event event;
	while (mContext.window.pollEvent(event)) 
	{
		if (event.type == sf::Event::Closed)
			mContext.window.close();
	}
}

void Game::render()
{
    mContext.window.clear();
    mContext.window.setView(mContext.window.getDefaultView());
    mContext.window.draw(mContext.board);
    mContext.window.display();
}
