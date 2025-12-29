#include <iostream>
using namespace std;
void Sort(int arr[],int n){
    int temp;
    for (int i=0;i<n;i++){
        for (int j=0;j<n-i-1;j++){
            if (arr[j+1]>arr[j]){
                temp=arr[j+1];
                arr[j+1]=arr[j];
                arr[j]=temp;
            }
        }
    }

    
}
int main(){
    int arr[]={3,5,1,4,2};
    int n=sizeof(arr)/sizeof(arr[0]);
    Sort(arr,n);
    for (int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
}