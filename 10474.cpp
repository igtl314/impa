#include <array>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <fstream>

int main(){
    int c = 0;

    while (true){
        int N{};
        int Q{};
        scanf("%d %d", &N, &Q);
        if (N == 0 && Q == 0){
            return 0;
        }
        c++;
        std::vector<int> numbers(N);
        std::vector<int> queries(Q);

        for (int i = 0; i<N; i++){
            scanf("%d", &numbers[i]);
        }
        for (int i = 0; i<Q; i++){
            scanf("%d", &queries[i]);
        }
        std::sort(numbers.begin(), numbers.end());
        std::cout << "CASE# " << c << ":" << std::endl;
        for (int i = 0; i<Q; i++){
            
            if (std::binary_search(numbers.begin(), numbers.end(), queries[i])){
                auto index = std::lower_bound(numbers.begin(), numbers.end(), queries[i]);
                std::cout << queries[i] << " found at " <<(index-numbers.begin()+1) << std::endl;
            }
            else{
                std::cout << queries[i] << " not found" << std::endl;
            }
        }


    
    }

    return 0;
}