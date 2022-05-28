#pragma once
#include <cstdlib>
#include <ctime>

#include "utility.hpp"

template <typename T>
int partition(T* tab, int p, int r)
{
    T x = tab[r];
    int i = p - 1;
    for (int j = p; j < r; ++j)
    {
        if (tab[j] <= x)
        {
            ++i;
            swap(tab[i], tab[j]);
        }
    }
    swap(tab[i + 1], tab[r]);
    return i + 1;
}

template <typename T>
int randomized_partition(T* tab, int p, int r)
{
    std::srand(std::time(0));
    int i = (std::rand() % (r - p)) + p;
    swap(tab[i], tab[r]);
    return partition(tab, p, r);
}

template <typename T>
void quicksort(T* tab, int p, int r)
{
    if (p < r)
    {
        int q = randomized_partition(tab, p, r);
        quicksort(tab, p, q - 1);
        quicksort(tab, q + 1, r);
    }
}