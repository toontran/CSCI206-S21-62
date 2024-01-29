#ifndef TREE_H
#define TREE_H

#include<string>
using std::string;

//Definition of the Binary Search Tree class.
class BST{
protected:
  int key;
  BST * left;
  BST * right;
  string value;
  bool isleaf();

public:
  BST();

  // the function insert() inserts an element v at the given key k.
  void insert(int k, string v);

  // the function search() returns the value stored at the given key k.
  string search(int k);
};

#endif
