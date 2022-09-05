#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <cctype>
#include <cmath>

struct Node {
    Node() : parent(nullptr), left(nullptr), right(nullptr), lvalue(-1), rvalue(-1) {}
    Node* parent;
    Node* left;
    Node* right;
    int lvalue;
    int rvalue;
};

Node* parse(std::string line) {
    Node* result = new Node;
    Node* current = result;
    for (int i = 0; i < line.size(); ++i)
    {
        if (line[i] == '[')
        {
            Node* node = new Node;
            node->parent = current;
            if (current->left == nullptr && current->lvalue == -1)
                current->left = node;
            else if (current->right == nullptr && current->rvalue == -1)
                current->right = node;
            else
                std::cerr << "CHECK A";

            current = node;
        }
        else if (line[i] == ']')
        {
            current = current->parent;
        }
        else if (isdigit(line[i]))
        {
            if (current->left == nullptr && current->lvalue == -1)
                current->lvalue = line[i] - '0';
            else if (current->right == nullptr && current->rvalue == -1)
                current->rvalue = line[i] - '0';
            else
                std::cerr << "CHECK B";
        }
    }
    return result;
}

void print(Node* node) 
{
    std::cout << "[";
    if (node->left != nullptr)
        print(node->left);
    else 
        std::cout << node->lvalue;
    std::cout << ",";
    if (node->right != nullptr)
        print(node->right);
    else
        std::cout << node->rvalue;
    std::cout << "]";
}

void add_to_left(Node* node, int value)
{
    Node* current = node;
    if (current->parent == nullptr)
        return;
    else if (current->parent->left == nullptr)
    {
        current->parent->lvalue += value;
        return;
    }
    while (current->parent->left == current)
    {    
        current = current->parent;
        if (current->parent == nullptr)
            return;
        else if (current->parent->left == nullptr)
        {
            current->parent->lvalue += value;
            return;
        } 
    }
    current = current->parent->left;
    while (current->right != nullptr)
        current = current->right;
    current->rvalue += value;
}

void add_to_right(Node* node, int value)
{
    Node* current = node;
    if (current->parent == nullptr)
        return;
    else if (current->parent->right == nullptr)
    {
        current->parent->rvalue += value;
        return;
    }
    while (current->parent->right == current)
    {    
        current = current->parent;
        if (current->parent == nullptr)
            return;
        else if (current->parent->right == nullptr)
        {
            current->parent->rvalue += value;
            return;
        } 
    }
    current = current->parent->right;
    while (current->left != nullptr)
        current = current->left;
    current->lvalue += value;
}

bool explode(Node* node, int depth = 0)
{
    if (node->left != nullptr)
        if (explode(node->left, depth + 1))
            return true;
    if (node->right != nullptr)
        if (explode(node->right, depth + 1))
            return true;
    if (depth >= 4 && node->left == nullptr && node->right == nullptr)
    {
        add_to_left(node, node->lvalue);
        add_to_right(node, node->rvalue);
        if (node->parent->left == node)
        {
            node->parent->left = nullptr;
            node->parent->lvalue = 0;
        }
        else if (node->parent->right == node)
        {
            node->parent->right = nullptr;
            node->parent->rvalue = 0;
        }
        return true;
    }
    return false;
}

bool split(Node* node)
{
    if (node->left != nullptr)
        if (split(node->left))
            return true;
    if (node->lvalue > 9)
    {
        Node* n = new Node;
        n->lvalue = node->lvalue / 2;
        n->rvalue = std::ceil(node->lvalue / 2.f);
        node->lvalue = -1;
        node->left = n;
        n->parent = node;
        return true;
    }
    if (node->rvalue > 9)
    {
        Node* n = new Node;
        n->lvalue = node->rvalue / 2;
        n->rvalue = std::ceil(node->rvalue / 2.f);
        node->rvalue = -1;
        node->right = n;
        n->parent = node;
        return true;
    }
    if (node->right != nullptr)
        if (split(node->right))
            return true;
    return false;
}

Node* reduce(Node* lhs, Node* rhs)
{
    Node* sum = new Node;
    sum->left = lhs;
    lhs->parent = sum;
    sum->right = rhs;
    rhs->parent = sum;
    while (explode(sum))
        ;

    while (split(sum))
        while (explode(sum))
            ;
    return sum;
}

int magnitude(Node* node)
{
    if (node->left == nullptr && node->right == nullptr)
        return 3 * node->lvalue + 2 * node->rvalue;
    else if (node->left != nullptr && node->right != nullptr)
        return 3 * magnitude(node->left) + 2 * magnitude(node->right);
    else if (node->left != nullptr)
        return 3 * magnitude(node->left) + 2 * node->rvalue;
    else
        return 3 * node->lvalue + 2 * magnitude(node->right);
}

int main()
{
    std::fstream file;
    file.open("data.txt", std::ios::in);
    std::string line;
    file >> line;
    Node* first = parse(line)->left;
    while (!file.eof())
    {
        file >> line;
        Node* second = parse(line)->left;
        first = reduce(first, second);
    }
    
    std::cout << magnitude(first);
    return 0;
}