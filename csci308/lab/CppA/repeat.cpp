#include <iostream>
using namespace std;

int countWords(string str) {
    int answer = 0;
    bool inword = false;
    for (auto x : str) {
        if (x == ' ' && inword) { // end of word
            inword = false;
        }
        else if (x != ' ' && !inword) { // just found new word
            inword = true;
            answer += 1;
        }
    }
    cout << endl;
    return answer;
}

int main() {
    string s;
    cout << "Enter a sentence of some sort:\n";
    getline(cin, s); // Read in a whole line into a string
    int x = countWords(s);
    
    for (int i=0; i<x; i++) {
        cout << s << endl;
    }
    return 0;
}
