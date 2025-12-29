//确实还没想过cpp中集合的交集和并集该如何实现？不懂是否有类似封装的函数
//问了下下copilot确实存在，但是在算法库中
//下面是ai实例
#include <iostream>
#include <vector>
#include <algorithm> // 必须包含这个头文件
#include <iterator>  // 用于 std::back_inserter

int main() {
    // 两个已排序的集合（如果是 vector，必须先 sort）
    std::vector<int> v1 = {1, 2, 3, 4, 5};
    std::vector<int> v2 = {3, 4, 5, 6, 7};

    // 存放结果的容器
    std::vector<int> v_intersection;
    std::vector<int> v_union;

    // 1. 求交集
    std::set_intersection(v1.begin(), v1.end(),
                          v2.begin(), v2.end(),
                          std::back_inserter(v_intersection));

    // 2. 求并集
    std::set_union(v1.begin(), v1.end(),
                   v2.begin(), v2.end(),
                   std::back_inserter(v_union));

    // 输出结果
    std::cout << "交集: ";
    for(int n : v_intersection) std::cout << n << " "; // 输出: 3 4 5
    std::cout << "\n";

    std::cout << "并集: ";
    for(int n : v_union) std::cout << n << " "; // 输出: 1 2 3 4 5 6 7
    std::cout << "\n";

    return 0;
}
//不得不感叹数据处理这一块还得是python