#include <iostream>
#include <vector>

#define LOG( A ) std::cout << A << std::endl;

struct Hase {
    std::vector<int> numbers = { 1, 2, 3 };

    __attribute__( ( used ) )
    int& operator[]( const int pos ) { return numbers[pos]; }

    __attribute__( ( used ) )
    int size() const { return  numbers.size(); }
};

int main( int argc, char* argv[] ) {

    Hase hase;

    return 0;
}
