#include <iostream>
#include <string>
#include <array>
#include <cmath>

int main(){
    while (true){
    int temp{};
    int count = 0;
    int N{};
    int D{};
    scanf("%d %d", &N, &D);
    if (N == 0 && D == 0){
        return 0;
    }
    for (int i = N; i<=D; i++){
        if (std::floor(std::sqrt(i)) == std::sqrt(i)){
            count++;
        }
    }
    std::cout << count << std::endl;
    
    
    
    }
    return 0;
}