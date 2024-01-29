#include <iostream>

using namespace std;
int main(){
    char c;
    cout << "Enter a character: ";
    cin >> c;
    if (c == 'a')
        cout << "A is for Ada Lovelace; the world’s first computer programmer." << endl;
    else if (c == 'g')
        cout << "G is for Grace Hopper who invented the compiler." << endl;
    else if (c == 'k')    
        cout << "K is for Katherine Johnson who hand calculated all the equations that ensured safe space travel in the 1950s and 1960. NASA used her work to double check the computer programs they were developing." << endl;
    else if (c == 'm')
        cout << "M is for Margaret Hamilton who coined the term software engineering and whose thorough testing on the Apollo 11 software resulted in the safety of the mission and its astronauts." << endl;
    else
        cout << "Any other letter.. Is there a famous women in CS with that letter? You could look it up." << endl;
        
    return 0;
}
