#include <iostream>

using namespace std;
int main(){
    int i = 0;
    char c = 'C';
    bool b = true;
    short s = 34;
    long li = 12L;
    long long lli = 10000LL;
    float f = 0.53f;
    double d = 2.03;
    long double ld = 2.569L;

    cout << "int " << sizeof(i) << endl;
    cout << "char " << sizeof(c) << endl;
    cout << "bool " << sizeof(b) << endl;
    cout << "short " << sizeof(s) << endl;
    cout << "long " << sizeof(li) << endl;
    cout << "long long " << sizeof(lli) << endl;
    cout << "float " << sizeof(f) << endl;
    cout << "double " << sizeof(d) << endl;
    cout << "long double " << sizeof(ld) << endl;
    return 0;
}
