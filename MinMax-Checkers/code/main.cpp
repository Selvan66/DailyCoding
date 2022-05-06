#include "Checkers.h"

int main()
{
    try
    {   
        Checkers c;
        c.run();
    }
    catch (...)
    {
        std::cerr << "Something worng" << std::endl;
        return -1;
    }
    
    return 0;
}