#pragma once

template <typename T>
void bubblesort(T* tab, int size)
{
    for (int i = size; i >= 2; --i)
    {
        for (int j = 0; j < i - 1; ++j)
        {
            if (tab[j] > tab[j + 1])
            {
                std::swap(tab[j], tab[j + 1]);
            }
        }
    }
}