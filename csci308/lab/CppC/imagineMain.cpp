// Don't edit this file
#include "imagine.h" // this is where we define the Imag class
using namespace std;

int main(){
    Imag n1 = Imag(0.3, 0.2);
    Imag n2 = Imag(0.6, 0.75);
    cout << n1 << endl;
    cout << n2 << endl;
    cout << "n1 + n2 = " << (n1+n2) << endl;
    cout << "n1 * n2 = " << (n1*n2) << endl;
    cout << "n1 * n1 * n1 * n1 = " << (n1 * n1 * n1 * n1) << endl;
}
