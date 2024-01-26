#include <iostream>

#include <array>

#include <sstream>


int main(){
    int testCase{};
    while (true){
        testCase++;
        int problemsAtStart;
        scanf("%d", &problemsAtStart);
        std::array<int,13> producedProblems{problemsAtStart};
        std::array<int,12> requiredProblems{};
        if (problemsAtStart == -1){
            break;
        }
        for (int i = 0; i < 12; ++i){
            int producded{};
            scanf("%d", &producded);
            producedProblems[i+1] = producded;
        }
        printf("Case %d:\n", testCase);
        for (int i = 0; i < 12; ++i){
            int required{};
            scanf("%d", &required);
             if (producedProblems[i]>= required){
                printf("No problem! :D\n");
                producedProblems[i+1] += (producedProblems[i] - required);
            }
            else{
                printf("No problem. :(\n");
                producedProblems[i+1] += producedProblems[i];
            }
        }

    }
    return 0;
}