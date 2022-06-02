#pragma once

#include <stdexcept>

template <typename T, size_t size>
class Stack
{
    public:
        Stack();
        bool empty() const;
        void push(T value);
        T pop();
    private:
        T tab[size];
        size_t top;
};

template<typename T, size_t size>
Stack<T, size>::Stack()
: tab{T()} 
, top(0)
{ }

template<typename T, size_t size>
bool Stack<T, size>::empty() const
{
    if (top == 0)
        return true;
    return false;
}

template<typename T, size_t size>
void Stack<T, size>::push(T value)
{
    if (top == size)
        throw std::range_error("stack is overflow");
    tab[top] = value;
    ++top;
}

template<typename T, size_t size>
T Stack<T, size>::pop()
{
    if (empty())
        throw std::range_error("stack is empty");
    --top;
    return tab[top];
}
