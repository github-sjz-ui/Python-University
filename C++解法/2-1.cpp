/*
Created on Tue Dec 23 13:55:04 2025

@author: zxl



（1）	编写程序，输入任意大的自然数，输出各位数字之和。
*/
#include <iostream>
using namespace std;   
class Solution {
    public:
        void add(){
            Solution s;
            cout << "请输入一个自然数：";
            cin >> s.a;
            while(s.a > 0){
                s.sum += s.a % 10; 
                s.a /= 10; 
            }
            cout << "各位数字之和为：" << s.sum << endl;
        }
    private:
        int a;
        int sum=0;
};

int main(){
    Solution s;
    s.add();

}