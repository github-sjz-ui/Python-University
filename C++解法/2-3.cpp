//对于这种处理数据还是面向过程这种来的快，那我直接用cpp的语法试着写下进制转换
#include <iostream>
#include <cstdlib>
using namespace std;
int transfer(int a,int n){
    cout<<"请输入自然数a和进制数n";
    cin>>a>>n;
    int res=0 ,i=1;
    while (a!=0){
        res+=(a%n)*i;
        a=a/n;
        i*=10;
    }
    return res;
}

int main(){
    system("chcp 65001"); // 解决终端中文乱码问题
    int a,n;
    int result=transfer(a,n);
    cout<<"转换后的结果为："<<result<<endl;
}