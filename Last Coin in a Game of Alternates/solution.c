#include <stdio.h>
#include <stdlib.h>
#include <time.h>


int coin(int arr[], int n) {
    if (n==1)
        return arr[0];
    int l=0;
    int r=n-1;
    while (l<r){
        if (arr[l]>=arr[r])
            l++;
        else
            r--;
    }
    return arr[l];
}

// second solution

int coin(int arr[], int n) {
    int res = arr[0];
    for (int i=1; i<n; i++){
        if (res> arr[i])
            res = arr[i];
    }
    return res;
}


int main(){
    srand(time(NULL));
    for (int i=0; i<1000; i++){
        int size = (rand() % 100000 ) + 1;
        int arr[size];
        for (int j=0; j<size; j++){
            arr[j] = (rand() %1000000) + 1;
        }
        int a = coin2(arr, size);
        printf("progress %i\r", i);

    }
    printf("\n");
    return 0;
}