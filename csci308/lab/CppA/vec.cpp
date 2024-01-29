#include <iostream>
#include <vector>

using namespace std;
int main(){
    vector<double> vec;
    vec.push_back(-1.58);    
    vec.push_back(-0.12);    
    vec.push_back(-0.15);    
    vec.push_back(-1.29);    
    vec.push_back(1.27);    
    
    double sum = 0;
    for (double &d: vec)
        sum += d;
    cout << sum / vec.size() << endl;

    return 0;
}
