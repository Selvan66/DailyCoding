#pragma once

template <typename T>
void selectionsort(T* tab, int size)
{
	for (int i = 0; i < size - 1; ++i)
	{
		int min_index = i;
		for (int j = i + 1; j < size; ++j)
			if (tab[j] < tab[min_index])
				min_index = j;
		std::swap(tab[i], tab[min_index]);
	}
}