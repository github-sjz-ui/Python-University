#include <iostream>
using namespace std;
int my_multiply(int arr[],int n)
{
    int res;
    res=arr[0];
    for (int i=1;i<n;i++){
        res=res*arr[i];
    }
    return res;
}
int main(){
    int arr[]={1,2,3,4};
    int n=sizeof(arr)/sizeof(arr[0]);
    int result=my_multiply(arr,n);
    cout<<"数组元素的乘积为："<<result<<endl;
}