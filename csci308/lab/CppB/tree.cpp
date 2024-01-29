#include"tree.h"
#include<iostream>
#include<string>
using namespace std;
/* If nullptr is causing an error then you are not correctly using C++11 */

BST::BST(){
  this->key = -1; // placeholder till you get a real value
  this->left = nullptr; // nullptr is the null pointer.
  this->right = nullptr;
  this->value = "";
}

bool BST::isleaf(){
  return (this->left == nullptr) && (this->right == nullptr);
}

/* Define the functions insert() and search() here according to their declaration in
the tree.h header file. */
void BST::insert(int key, string value) {
  //cout << key << value << endl;
  if (this->key == -1) {
    this->key = key;
    this->value = value;
  } else if (key < this->key) {
    if (this->left == nullptr) {
      this->left = new BST();
    } 
    this->left->insert(key, value);
  } else {
    if (this->right == nullptr) {
      this->right = new BST();
    }
    this->right->insert(key, value);
  }
}

string BST::search(int key) {
  //cout << key << endl;
  if (key == this->key) {
    return this->value;
  } else if (key < this->key) {
    if (this->left == nullptr) {
      return "Not Found!";
    } 
    return this->left->search(key);
  } else if (key > this->key) {
    if (this->right == nullptr) {
      return "Not Found!";
    } 
    return this->right->search(key);
  }
}


int main(){
  BST * t = new BST();

  t->insert(10,"Ten");
  t->insert(5,"Five");
  t->insert(12, "Twelve");
  t->insert(7, "Seven");
  t->insert(4, "Four");
  t->insert(11, "Eleven");
  
  cout << t->search(5) << endl;
  cout << t->search(10) << endl;
  cout << t->search(6) << endl;
  cout << t->search(7) << endl;
  cout << t->search(11) << endl;
  
  return 0;
}
