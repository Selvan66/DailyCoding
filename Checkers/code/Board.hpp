#pragma once
#include <array>
#include <cassert>

#include <SFML/Graphics.hpp>


class Board : public sf::Drawable
{
    public:
        enum States
        {
            None,
            White,
            Black,
            WhiteKing,
            BlackKing,
            Move
        };
    public:
        Board();
        void set(sf::Vector2u pos, States state);
        States get(sf::Vector2u pos);
    private:
        void draw(sf::RenderTarget& target, sf::RenderStates states) const;
    private:
        constexpr static size_t mSize = 8;
        std::array<std::array<States, mSize>, mSize> mBoard;
};

Board::Board()
{
    for (int i = 0; i < mSize; ++i)
        for (int j = 0; j < mSize; ++j)
            mBoard[i][j] = None;
    
    for (int i = 0; i < 3; ++i)
        for (int j = ((i + 1) % 2); j < mSize; j += 2)
            mBoard[i][j] = White;

    for (int i = 5; i < mSize; ++i)
        for (int j = ((i + 1) % 2); j < mSize; j += 2)
            mBoard[i][j] = Black;
}

void Board::set(sf::Vector2u pos, States state)
{
    assert(pos.x < mSize || pos.y < mSize);
    mBoard[pos.x][pos.y] = state;
}

Board::States Board::get(sf::Vector2u pos)
{
    assert(pos.x < mSize || pos.y < mSize);
    return mBoard[pos.x][pos.y];
}

void Board::draw(sf::RenderTarget& target, sf::RenderStates states) const
{
    auto windowSize = target.getDefaultView().getSize();

    bool isWhite = true;
    int istep = (int)(windowSize.x / mSize);
    float fstep = (float)istep;
    sf::RectangleShape board;
    board.setSize(sf::Vector2f(fstep, fstep));

    sf::CircleShape pawn;
    pawn.setOutlineThickness(3.f);
    pawn.setRadius(fstep / 2.5f);
    pawn.setOrigin(sf::Vector2f((fstep / 2.5f) - (fstep / 2.f), (fstep / 2.5f) - (fstep / 2.f)));

    sf::CircleShape move;
    move.setRadius(fstep / 8.f);
    move.setFillColor(sf::Color::Blue);
    move.setOrigin(sf::Vector2f((fstep / 8.f) - (fstep / 2.f), (fstep / 8.f) - (fstep / 2.f)));


    int x = 0;
    int y = 0;

    for (float i = 0; i < windowSize.x; i += fstep)
    {
        x = 0;
        for (float j = 0; j < windowSize.y; j += fstep)
        {
            if (isWhite)
            {
                board.setFillColor(sf::Color(227, 170, 19));
                board.setPosition(i, j);
                target.draw(board);
            }
            else
            {
                board.setFillColor(sf::Color(87, 55, 3));
                board.setPosition(i, j);
                target.draw(board);
            }
            if(j + fstep < windowSize.y)
                isWhite = !isWhite;

            switch(mBoard[x][y])
            {
                case White:
                    pawn.setFillColor(sf::Color::White);
                    pawn.setOutlineColor(sf::Color::Black);
                    pawn.setPosition(i, j);
                    target.draw(pawn);
                    break;
                case Black:
                    pawn.setFillColor(sf::Color::Black);
                    pawn.setOutlineColor(sf::Color::Black);
                    pawn.setPosition(i, j);
                    target.draw(pawn);
                    break;
                case BlackKing:
                    pawn.setFillColor(sf::Color::Black);
                    pawn.setOutlineColor(sf::Color::Yellow);
                    pawn.setPosition(i, j);
                    target.draw(pawn);
                    break;
                case WhiteKing:
                    pawn.setFillColor(sf::Color::White);
                    pawn.setOutlineColor(sf::Color::Yellow);
                    pawn.setPosition(i, j);
                    target.draw(pawn);
                    break;
                case Move:
                    move.setPosition(i, j);
                    target.draw(move);
                    break;
            }
            x++;
        }
        y++;
    }      
}
