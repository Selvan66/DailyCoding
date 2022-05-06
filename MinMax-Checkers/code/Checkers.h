#pragma once

#include <iostream>
#include <array>
#include <vector>
#include <string>

class Checkers
{
    public:
        static constexpr std::size_t size = 8;
        typedef std::array<std::array<std::string, size>, size> Board;

        struct Move
        {
            int oldI, oldJ, newI, newJ;
            bool operator==(const Move& o) 
            { return newI == o.newI && newJ == o.newJ && oldI == o.oldI && oldJ == o.oldJ;}
        };
    public:
        Checkers();
        void run();
        void makeMove(Move move, bool player);
        std::vector<Move> findComputerMoves() const;
        std::vector<Move> findPlayerMoves() const;
        const Board& getBoard() const;
    private:
        void printBoard() const;
        bool checkMove(Move move, bool player) const;
        bool checkJumps(Move move, int viaI, int viaJ, bool player) const;
        void countPieces();
    private:
        Board mBoard;
        bool mPlayerTurn;
        unsigned int mPlayerPieces;
        unsigned int mComputerPieces;
};
