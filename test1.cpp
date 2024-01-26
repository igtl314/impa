#include <iostream>
#include <bitset>

int main()
{
    std::string binary = std::bitset<32>(0.984375).to_string(); //to binary
    std::cout<<binary<<"\n";

    unsigned long decimal = std::bitset<32>(binary).to_ulong();
    std::cout<<decimal<<"\n";
    return 0;
}