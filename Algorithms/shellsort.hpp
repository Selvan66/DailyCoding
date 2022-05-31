#pragma once

template <typename T>
void shellsort(T* tab, int size)
{
    for (int gap = size / 2; gap > 0; gap /= 2)
    {
        for (int i = gap; i < size; ++i)
        {
            T temp = tab[i];
            int j;
            for (j = i; j >= gap && tab[j - gap] > temp; j -= gap)
                tab[j] = tab[j - gap];
            tab[j] = temp;
        }
    }
}