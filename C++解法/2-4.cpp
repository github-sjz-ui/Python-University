#include <iostream>
using namespace std;
int search_Even(int arr1[],int size){
    int arr2[size];
    for (int i=0;i<size;i++){
        if (arr1[i]%2==0){
           arr2[i]=arr1[i];
        }
    }
    return arr2[size];
}