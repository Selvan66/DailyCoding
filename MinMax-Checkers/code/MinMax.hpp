#pragma once
#include <limits>

#include "Checkers.h"

struct Node
{
    Checkers checkers;
    Checkers::Move move;
    int value;
    Node* parent;
};

std::vector<Node> makeNodes(Checkers checkers, bool player)
{
    std::vector<Checkers::Move> moves;
    std::vector<Node> nodes;
    if (player)
        moves = checkers.findPlayerMoves();
    else
        moves = checkers.findComputerMoves();
    
    for (auto& move : moves)
    {
        Checkers copy = checkers;
        copy.makeMove(move, player);
        nodes.push_back({copy, move, 0, nullptr});
    }
    return nodes;
}


int calculateHeuristics(const Checkers::Board& board)
{
    int result = 0;
    int computer = 0;
    int player = 0;


    for (int i = 0; i < Checkers::size; ++i)
        for (int j = 0; j < Checkers::size; ++j)
            if (board[i][j][0] == 'c' || board[i][j][0] == 'C')
            {
                computer++;

                if (board[i][j][0] == 'c')
                    result += 5;
                if (board[i][j][0] == 'C')
                    result += 10;
                if (i == 0 || j == 0 || i == (Checkers::size - 1) || j == (Checkers::size - 1))
                    result += 7;

                if (i + 1 > (Checkers::size - 1) || j + 1 > (Checkers::size - 1) || i - 1 < 0 || j - 1 < 0)
                    continue;

                if ((board[i + 1][j - 1][0] == 'b' || board[i + 1][j - 1][0] == 'B') && board[i - 1][j + 1] == "---")
                    result -= 3;
                if ((board[i + 1][j + 1][0] == 'b' || board[i + 1][j + 1][0] == 'B') && board[i - 1][j - 1] == "---")
                    result -= 3;
                if (board[i - 1][j - 1][0] == 'B' && board[i + 1][j + 1] == "---")
                    result -= 3;
                if (board[i - 1][j + 1][0] == 'B' && board[i + 1][j - 1] == "---")
                    result -= 3;

                if (i + 2 > (Checkers::size - 1) || (j - 2) < 0)
                    continue;
                
                if ((board[i + 1][j - 1][0] == 'b' || board[i + 1][j - 1][0] == 'B') && board[i + 2][j - 2] == "---")
                    result += 6;
                
                if (j + 2 > (Checkers::size - 1))
                    continue;
                
                if ((board[i + 1][j + 1][0] == 'b' || board[i + 1][j + 1][0] == 'B') && board[i + 2][j + 2] == "---")
                    result += 6;
            }
            else if (board[i][j][0] == 'b' || board[i][j][0] == 'B')
            {
                player++;
            }
    
    return result + (computer - player) * 1000;
}

int minMax(Checkers checkers, int depth, int alpha, int beta, bool player)
{
    if (depth == 0)
        return calculateHeuristics(checkers.getBoard());

    if (!player)
    {
        int max = -std::numeric_limits<int>::max();
        auto nodes = makeNodes(checkers, player);
        for (auto& node : nodes)
        {
            int val = minMax(node.checkers, depth - 1, alpha, beta, true);
            max = std::max(max, val);
            alpha = std::max(alpha, val);
            if (beta <= alpha)
                break;
        }
        return max;
    }
    else
    {
        int min = std::numeric_limits<int>::max();
        auto nodes = makeNodes(checkers, player);
        for (auto& node : nodes)
        {
            int val = minMax(node.checkers, depth - 1, alpha, beta, false);
            min = std::min(min, val);
            beta = std::min(beta, val);
            if (beta <= alpha)
                break;
        }
        return min;
    }
}