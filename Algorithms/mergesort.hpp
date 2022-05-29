#pragma once

template <typename T>
void merge(T tab[], int p, int q, int r)
{
    int n1 = q - p + 1;
    int n2 = r - q;

    T* L = new T[n1];
    T* R = new T[n2];

    int i = 0;
    int j = 0;
    for (i = 0; i < n1; ++i)
    {
        L[i] = tab[p + i];
    }
    for (i = 0; i < n2; ++i)
    {
        R[i] = tab[i + q + 1];
    }
    i = 0;
    j = 0;
    for (int k = p; k <= r; ++k)
    {
        if ((L[i] <= R[j] || j >= n2) && (i < n1))
        {
            tab[k] = L[i];
            ++i;
        }
        else
        {
            tab[k] = R[j];
            ++j;
        }
    }
    delete[] R;
    delete[] L;
}

template <typename T>
void mergesort(T tab[], int p, int r)
{
    if (p < r)
    {
        int q = (p + r) / 2;
        mergesort(tab, p, q);
        mergesort(tab, q + 1, r);
        merge(tab, p, q, r);
    }
}