#include <stdio.h>
#include <map>
#include <utility>

#define ui unsigned int

long  int solution(long* arr, ui n) {
    long long sum = 0;
    ui j = 0;

    std::map<std::pair<ui,ui>, long> memo;

    for(ui i=0; i<n; i++) {
        std::pair<ui, ui> curr;
        curr.first = i;
        curr.second = i;
        memo[curr] = arr[i];
        sum += arr[i];
    }

    for(ui i=0; i<n-2+1; i++) {
        j = i + 2 - 1;
        std::pair<ui, ui> curr;
        curr.first = i;
        curr.second = j;

        //dp[i][j] = arr[i] & arr[j];

        memo[curr] = arr[i] & arr[j];
        sum += memo[curr];
    }
    
    for(ui l=3; l<=n; l++) {
        
        for(ui i=0; i<n-l+1; i++) {
            j = i + l - 1;

            std::pair<ui, ui> curr;
            curr.first = i;
            curr.second = j;

            std::pair<ui, ui> prev;
            prev.first = i+1;
            prev.second = j-1;

            //dp[i][j] = dp[i][i] & dp[i+1][j-1] & dp[j][j];

            memo[curr] = arr[i] & memo[prev] & arr[j];
            sum += memo[curr];
        }
    }

    // for(ui i=0; i<n; i++)
    //     delete dp[i];
    // delete dp;
    return sum;
}  

int main() {
    int t;
    ui n;
    scanf("%d", &t);
    while(t--) {
        scanf("%ud", &n);
        long arr[n];
        // printf("enter");
        for(ui i=0; i<n; i++) {
            // printf("next\n");
            scanf("%ld", &arr[i]);
        }
        // printf("after enter");
        printf("%ld\n", solution(arr, n));
    }
    
}