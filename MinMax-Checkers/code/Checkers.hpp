#pragma once

#include <iostream>
#include <array>
#include <vector>
#include <string>

class Checkers
{
    public:
        struct Move
        {
            int oldI, oldJ, newI, newJ;
            bool operator==(const Move& o) 
            { return newI == o.newI && newJ == o.newJ && oldI == o.oldI && oldJ == o.oldJ;}
        };
    public:
        Checkers();
        void run();
    private:
        void printBoard() const;
        bool checkMove(Move move, bool player) const;
        bool checkJumps(Move move, int viaI, int viaJ, bool player) const;
        std::vector<Move> findComputerMoves() const;
        std::vector<Move> findPlayerMoves() const;
        void makeMove(Move move, bool player);
        void countPieces();
    private:
        static constexpr std::size_t mSize = 8;
        std::array<std::array<std::string, mSize>, mSize> mBoard;
        bool mPlayerTurn;
        unsigned int mPlayerPieces;
        unsigned int mComputerPieces;
};

Checkers::Checkers()
: mBoard()
, mPlayerTurn(true)
, mPlayerPieces(12)
, mComputerPieces(12)
{
    // Fill board
    for (int i = 0; i < mSize; ++i)
        for (int j = 0; j < mSize; ++j)
            mBoard[i][j] = "---";

    // Fill computer piecies
    for (int i = 0; i < 3; ++i)
        for (int j = 0; j < mSize; ++j)
            if ((i + j) % 2 == 1)
                mBoard[i][j] = "c" + std::to_string(i) + std::to_string(j);
    
    // Fill player piecies
    for (int i = 5; i < mSize; ++i)
        for (int j = 0; j < mSize; ++j)
            if ((i + j) % 2 == 1)
                mBoard[i][j] = "b" + std::to_string(i) + std::to_string(j);
}

void Checkers::run()
{
    while (true)
    {
        printBoard();
        
        if (mPlayerTurn)
        {
            std::cout << "Player move: " << std::endl;

            auto moves = findPlayerMoves();
            if (moves.size() == 0)
            {
                if (mComputerPieces > mPlayerPieces)
                    std::cout << "No move left, YOU LOSE" << std::endl;
                else
                    std::cout << "No move left, Pass" << std::endl;
                break;
            }
            Move newMove;
            std::cout << "Which piece (i j): " << std::endl;
            if (!(std::cin >> newMove.oldI >> newMove.oldJ))
            {
                std::cout << "Bad input" << std::endl;
                break;
            }
            std::cout << "Where to (i j): " << std::endl;
            if (!(std::cin >> newMove.newI >> newMove.newJ))
            {
                std::cout << "Bad input" << std::endl;
                break;
            }
            if (std::find(moves.begin(), moves.end(), newMove) == moves.end())
            {
                std::cout << "Illegal move" << std::endl;
                continue;
            }

            makeMove(newMove, true);
            countPieces();
        }
        else
        {
            std::cout << "Computer move: " << std::endl;
        }

        if (mPlayerPieces == 0)
        {
            std::cout << "YOU LOSE" << std::endl;
            break;
        }
        else if (mComputerPieces == 0)
        {
            std::cout << "YOU WIN" << std::endl;
            break;
        }

        mPlayerTurn = !mPlayerTurn;
    }
}

void Checkers::printBoard() const
{
    std::cout << std::endl;
    for (int i = 0; i < mSize; ++i)
    {
        std::cout << i << " |";
        for (int j = 0; j < mSize; ++j)
        {
            std::cout << mBoard[i][j] << " ";
        }
        std::cout << std::endl;
    }
    std::cout << "  ________________________________" << std::endl;
    for (int i = 0; i < mSize; ++i)
    {
        if (i == 0)
            std::cout << "    ";
        std::cout << i << "   "; 
    }

    std::cout << std::endl;
}

bool Checkers::checkMove(Checkers::Move move, bool player) const
{
    if (move.newI >= mSize || move.newI < 0)
        return false;
    if (move.newJ >= mSize || move.newJ < 0)
        return false;
    if (mBoard[move.oldI][move.oldJ] == "---")
        return false;
    if (mBoard[move.newI][move.newJ] != "---")
        return false;
    if (player && (mBoard[move.oldI][move.oldJ][0] == 'c' || mBoard[move.oldI][move.oldJ][0] == 'C'))
        return false;
    if (!player && (mBoard[move.oldI][move.oldJ][0] == 'b' || mBoard[move.oldI][move.oldJ][0] == 'B'))
        return false;
    return true;
}

bool Checkers::checkJumps(Checkers::Move move, int viaI, int viaJ, bool player) const
{
    if (!checkMove(move, player))
        return false;
    if (mBoard[viaI][viaJ] == "---")
        return false;
    if (!player && (mBoard[viaI][viaJ][0] == 'c' || mBoard[viaI][viaJ][0] == 'C'))
        return false;
    if (player && (mBoard[viaI][viaJ][0] == 'b' || mBoard[viaI][viaJ][0] == 'B'))
        return false;
    return true;
}

std::vector<Checkers::Move> Checkers::findComputerMoves() const
{
    std::vector<Move> moves;
    std::vector<Move> jumps;

    for (int i = 0; i < mSize; ++i)
        for (int j = 0; j < mSize; ++j)
            if (mBoard[i][j][0] == 'c')
            {
                if (checkMove({i, j, i + 1, j + 1}, false))
                    moves.push_back({i, j, i + 1, j + 1});
                if (checkMove({i, j, i + 1, j - 1}, false))
                    moves.push_back({i, j, i + 1, j - 1});
                if (checkJumps({i, j, i + 2, j + 2}, i + 1, j + 1, false))
                    jumps.push_back({i, j, i + 2, j + 2});
                if (checkJumps({i, j, i + 2, j - 2}, i + 1, j - 1, false))
                    jumps.push_back({i, j, i + 2, j - 2});
            }
            else if (mBoard[i][j][0] == 'C')
            {
                if (checkMove({i, j, i + 1, j + 1}, false))
                    moves.push_back({i, j, i + 1, j + 1});
                if (checkMove({i, j, i + 1, j - 1}, false))
                    moves.push_back({i, j, i + 1, j - 1});
                if (checkMove({i, j, i - 1, j + 1}, false))
                    moves.push_back({i, j, i - 1, j + 1});
                if (checkMove({i, j, i - 1, j - 1}, false))
                    moves.push_back({i, j, i - 1, j - 1});
                if (checkJumps({i, j, i + 2, j + 2}, i + 1, j + 1, false))
                    jumps.push_back({i, j, i + 2, j + 2});
                if (checkJumps({i, j, i + 2, j - 2}, i + 1, j - 1, false))
                    jumps.push_back({i, j, i + 2, j - 2});
                if (checkJumps({i, j, i - 2, j + 2}, i - 1, j + 1, false))
                    jumps.push_back({i, j, i - 2, j + 2});
                if (checkJumps({i, j, i - 2, j - 2}, i - 1, j - 1, false))
                    jumps.push_back({i, j, i - 2, j - 2});
            }
    
    if (jumps.size() == 0)
        return moves;
    return jumps;
}

std::vector<Checkers::Move> Checkers::findPlayerMoves() const
{
    std::vector<Move> moves;
    std::vector<Move> jumps;

    for (int i = 0; i < mSize; ++i)
        for (int j = 0; j < mSize; ++j)
            if (mBoard[i][j][0] == 'b')
            {
                if (checkMove({i, j, i - 1, j - 1}, true))
                    moves.push_back({i, j, i - 1, j - 1});
                if (checkMove({i, j, i - 1, j + 1}, true))
                    moves.push_back({i, j, i - 1, j + 1});
                if (checkJumps({i, j, i - 2, j - 2}, i - 1, j - 1, true))
                    jumps.push_back({i, j, i - 2, j - 2});
                if (checkJumps({i, j, i - 2, j + 2}, i - 1, j + 1, true))
                    jumps.push_back({i, j, i - 2, j + 2});
            }
            else if (mBoard[i][j][0] == 'B')
            {
                if (checkMove({i, j, i + 1, j + 1}, true))
                    moves.push_back({i, j, i + 1, j + 1});
                if (checkMove({i, j, i + 1, j - 1}, true))
                    moves.push_back({i, j, i + 1, j - 1});
                if (checkMove({i, j, i - 1, j + 1}, true))
                    moves.push_back({i, j, i - 1, j + 1});
                if (checkMove({i, j, i - 1, j - 1}, true))
                    moves.push_back({i, j, i - 1, j - 1});
                if (checkJumps({i, j, i + 2, j + 2}, i + 1, j + 1, true))
                    jumps.push_back({i, j, i + 2, j + 2});
                if (checkJumps({i, j, i + 2, j - 2}, i + 1, j - 1, true))
                    jumps.push_back({i, j, i + 2, j - 2});
                if (checkJumps({i, j, i - 2, j + 2}, i - 1, j + 1, true))
                    jumps.push_back({i, j, i - 2, j + 2});
                if (checkJumps({i, j, i - 2, j - 2}, i - 1, j - 1, true))
                    jumps.push_back({i, j, i - 2, j - 2});
            }
    
    if (jumps.size() == 0)
        return moves;
    return jumps;
}

void Checkers::makeMove(Move move, bool player)
{
    char letter;
    if (player)
    {
        if (move.newI == 0)
            letter = 'B';
        else
            letter = 'b';
    }
    else
    {
        if (move.newI == (mSize - 1))
            letter = 'C';
        else
            letter = 'c';
    }
    
    int i_diff = move.oldI - move.newI;
    int j_diff = move.oldJ - move.oldJ;

    if (i_diff == -2 && j_diff == 2)
        mBoard[move.oldI + 1][move.oldJ - 1] = "---";
    else if (i_diff == 2 && j_diff == 2)
        mBoard[move.oldI - 1][move.oldJ - 1] = "---";
    else if (i_diff == 2 && j_diff == -2)
        mBoard[move.oldI - 1][move.oldJ + 1] = "---";
    else if (i_diff == -2 && j_diff == -2)
        mBoard[move.oldI + 1][move.oldJ + 1] = "---";

    mBoard[move.oldI][move.oldJ] = "---";
    mBoard[move.newI][move.newJ] = letter + std::to_string(move.newI) + std::to_string(move.newJ);
}

void Checkers::countPieces()
{
    mComputerPieces = 0;
    mPlayerPieces = 0;

    for (int i = 0; i < mSize; ++i)
        for (int j = 0; j < mSize; ++j)
            if (mBoard[i][j][0] == 'c' || mBoard[i][j][0] == 'C')
                mComputerPieces++;
            else if (mBoard[i][j][0] == 'b' || mBoard[i][j][0] == 'B')
                mPlayerPieces++;
}