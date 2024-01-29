#include<iostream>
using namespace std;

template<typename A, typename B, typename C>
class Triple{
public:
    A first;
    B second;
    C third;

    Triple(A a, B b, C c){ first = a; second = b; third = c;}

    A fst(){return first;}
    B snd(){return second;}
    C thd(){return third;}

    // The function change1(), changes the first component of a triple. 
    void change1(A a){ first = a;}
};

// A linked list of triples where the order of the triple rotates as it goes.
template<typename A, typename B, typename C>
class RotateList{ 
public:
    Triple<A,B,C> *t;
    RotateList<B,C,A> * next; // Notice the order has changed

    RotateList(Triple<A,B,C> *t1, RotateList<B,C,A> * n1){ this->t = t1; this->next = n1;}

    /* THE RECURSIVE FUNCTION
     * create() is a class member function (static), creating a rotating list of length i.
     * Notice that the function is recursive. It creates i triples, each with
     * the order rotated from the previous triple.
     * If nullptr does not compile, then you are not properly compiling as C++11.
     */
    static RotateList<A,B,C> * create(A a, B b, C c, int i){
	if (i <= 0) return nullptr;
	Triple<A,B,C> * t = new Triple<A,B,C>(a,b,c);
	RotateList<B,C,A> * n = RotateList<B,C,A>::create(b,c,a, i-1); 
    
	return new RotateList<A,B,C>(t, n);
    }

    /* THE ITERATIVE FUNCTION
     * Complete the function create2() such that it behaves
     * as specified by the output in the lab. Notice how the changed numbers
     * repeat down the list.
     */
    static RotateList<A,B,C> * create2(A a, B b, C c, int i){
	// Your code goes here

	// Create the three pointers to triples (not i triples) and 
	// call the Triple constructor to instantiate them.
	// Hint: They all have different parameterized types. 
	// What types do the triples created by the iterative create use?
	Triple<A,B,C> *t1 = new Triple<A,B,C>(a,b,c);
	Triple<B,C,A> *t2 = new Triple<B,C,A>(b,c,a);
	Triple<C,A,B> *t3 = new Triple<C,A,B>(c,a,b);
	
	// Create three pointers to RotateLists, each with a different
	// parameterized type. Each can be used to point to a list beggining
	// with that type. Set them all to nullptr for now.
    RotateList<A,B,C> *l1 = nullptr;
    RotateList<B,C,A> *l2 = nullptr;
    RotateList<C,A,B> *l3 = nullptr; 


	// Use a loop to assemble them into a rotating list.
	// Which triple goes first in the list? goes last? 
	// How do you know which triple to add on next?
	// Do you want to build you list from front to back or back to front?
	// Hint: % is the C++ mod operator
	if (i % 3 == 1)
        l1 = new RotateList<A,B,C>(t1, nullptr); 
	else if (i % 3 == 2)
        l2 = new RotateList<B,C,A>(t2, nullptr);
	else 
        l3 = new RotateList<C,A,B>(t3, nullptr);

    for (int j=1; j<i; j++) {
	    if ((i-j) % 3 == 1)
            l1 = new RotateList<A,B,C>(t1, l2); 
	    else if ((i-j) % 3 == 2)
            l2 = new RotateList<B,C,A>(t2, l3);
	    else 
            l3 = new RotateList<C,A,B>(t3, l1);      
    }

	// Remember to return a pointer to your resulting RotateList.
	
	return l1;
    }

    /* Print the whole rotating list. */ 
    void print(){
	cout << "{" << t->fst() << " "<< t->snd() << " "<< t->thd() << "}";
	if (next != nullptr) 
	    next->print();
	else 
	    cout << endl;
    }
};


int main(){
    float f = 3.14;
    int i = 3;
    char c = 'c';

    Triple<float,int,char> t = Triple<float,int,char>(f,i,c);
    Triple<float,int,char> t1 = t;
    cout << "Starting triple: [" << t.fst() << " "<< t.snd() << " "<< t.thd() << "]" << endl;

    cout << endl << "Rotating list created recursively" << endl;
    RotateList<float,int,char> * r= RotateList<float,int,char>::create(f,i,c, 10);
    r->print();

    r->t->change1(42.42);
    r->print();

    cout << endl << "Rotating list created iteratively" << endl;
    RotateList<float,int,char> * s= RotateList<float,int,char>::create2(f,i,c, 10);
    s->print();

    s->t->change1(42.42);
    s->print();
    
    s->next->t->change1(501);
    s->print();
}
