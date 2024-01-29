#include <iostream>
#include <vector>

using namespace std;


int fib(vector<int> &table, int n) {
    //cout << table[n];
    
    if (table[n] != -1)
        return table[n];
    else if (n <= 0)
        return 0;
    else if (n == 1)
        return 1;
    else if (n >= 47)
        return -1;

    table[n] = fib(table, n-1) + fib(table, n-2);
    return table[n];
}


int main(){
    int i;
    int ret;
    cout << "Enter an integer number: ";
    cin >> i;

    vector<int> memo(i+1, -1);
    //cout << memo[i-1];
    ret = fib(memo, i);
    if (ret == -1) 
        cout << "NOPE" << endl;
    else
        cout << ret << endl;
    return 0;
}
