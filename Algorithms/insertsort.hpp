#pragma once

// Insert sort
template <typename T>
void insertsort(T* tab, int size)
{
    int i;
    T key;
    for(int j = 1; j < size; ++j)
    {
        key = tab[j];
        i = j - 1;
        while(i >= 0 && tab[i] > key)
        {
            tab[i+1] = tab[i];
            i--;
        }
        tab[i+1] = key;
    }
} 