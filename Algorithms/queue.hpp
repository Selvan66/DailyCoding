#pragma once

#include <stdexcept>

template <typename T, size_t size>
class Queue
{
    public:
        Queue();
        bool empty() const;
        void enqueue(T value);
        T dequeue();
    private:
        T tab[size];
        size_t head;
        size_t tail;
};

template<typename T, size_t size>
Queue<T, size>::Queue()
: tab{T()}
, head(0)
, tail(0)
{ }

template<typename T, size_t size>
bool Queue<T, size>::empty() const
{
    if (head == tail)
        return true;
    return false;
}

template<typename T, size_t size>
void Queue<T, size>::enqueue(T value)
{
    tab[tail] = value;
    ++tail;
    if (tail == size)
        tail = 0;
}

template<typename T, size_t size>
T Queue<T, size>::dequeue()
{
    if (empty())
        throw std::range_error("Queue is empty");
    T ret = tab[head];
    ++head;
    if (head == size)
        head = 0;
    return ret;
}
