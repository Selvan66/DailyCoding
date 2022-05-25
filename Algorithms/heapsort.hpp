#pragma once
#include <cmath>

inline int parent(int i)
{
    return std::ceil(i / 2.f) - 1;
}

inline int left(int i)
{
    return (i * 2) + 1;
}

inline int right(int i)
{
    return (i * 2) + 2;
}

template <typename T>
void max_heapify(T* tab, int size, int i)
{
    int l = left(i);
    int r = right(i);
    int largest = i;
    if (l < size && tab[l] > tab[i])
    {
        largest = l;
    }
    if (r < size && tab[r] > tab[largest])
    {
        largest = r;
    }
    if (largest != i)
    {
        std::swap(tab[i], tab[largest]);
        max_heapify(tab, size, largest);
    }
}

template <typename T>
void build_max_heap(T* tab, int size)
{
    for (int i = (size / 2) + 1; i >= 0; --i)
    {
        max_heapify(tab, size, i);
    }
}

template <typename T>
void heapsort(T* tab, int size)
{
    build_max_heap(tab, size);
    for (int i = (size - 1); i >= 1; --i)
    {
        std::swap(tab[0], tab[i]);
        max_heapify(tab, i, 0);
    }
}