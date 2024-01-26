#include <iostream>
#include <cmath>
#include <array>
#include <bitset>
#include <sstream>
#include <string>
#include <algorithm>
#include <iomanip>
#include <fstream> 


std::string mantissaToBinary(double mantissa) {
    std::string binary = ".";
    mantissa -= 0.5;
    while (mantissa > 0) {
        mantissa *= 2;
        if (mantissa >= 1) {
            binary += '1';
            mantissa -= 1;
        } else {
            binary += '0';
        }
    }
    return binary;
}

int main(){
    std::ofstream outputFile("output.txt");
    while (true){
        double N{};
        double mantissa;
        int exponent;
        scanf("%lf", &N);
        if (N == 0){
            break;
        }
        mantissa = std::frexp(N, &exponent);
        int exp = std::ceil(std::log2(std::abs(exponent)));
        std::stringstream ss;
        ss << std::setprecision(15) << mantissa;
        std::string mantissaWithPrecision = ss.str();
        int test = mantissaWithPrecision.length()-3;
        
        
       
      
       outputFile << test<< " " << exp << std::endl;


    }
    outputFile.close();

    return 0;
}