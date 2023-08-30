#include <iostream>
#include <unordered_map>
# include <bits/stdc++.h>
using namespace std;

struct Node {
    int key;
    Node* left;
    Node* right;
    Node* parent;
};

class SplayTree {
public:
    Node* root;
    unordered_map<string, int> rotation_count;

    SplayTree() : root(nullptr) {
        rotation_count["Zig"] = 0;
        rotation_count["Zag"] = 0;
        rotation_count["Zig-Zig"] = 0;
        rotation_count["Zag-Zag"] = 0;
        rotation_count["Zig-Zag"] = 0;
        rotation_count["Zag-Zig"] = 0;
    }

    void right_rotate(Node* x) {
        Node* y = x->left;
        x->left = y->right;
        if (y->right) y->right->parent = x;
        y->parent = x->parent;
        if (!x->parent) root = y;
        else if (x == x->parent->right) x->parent->right = y;
        else x->parent->left = y;
        y->right = x;
        x->parent = y;
    }

    void left_rotate(Node* x) {
        Node* y = x->right;
        x->right = y->left;
        if (y->left) y->left->parent = x;
        y->parent = x->parent;
        if (!x->parent) root = y;
        else if (x == x->parent->left) x->parent->left = y;
        else x->parent->right = y;
        y->left = x;
        x->parent = y;
    }

    void splay(Node* x) {
        while (x->parent) {
            if (!x->parent->parent) {
                if (x == x->parent->left) {
                    // print which nodes are rotating
                    cout<<"Zig"<< ":"<<x->key<<endl;
                    right_rotate(x->parent);
                    rotation_count["Zig"]++;
                    
                } else {
                    // print which nodes are rotating
                    cout<<"Zag"<< ":"<<x->key<<endl;
                    left_rotate(x->parent);
                    rotation_count["Zag"]++;
                }
            } else if (x == x->parent->left && x->parent == x->parent->parent->left) {

                cout<<"Zig-Zig"<< ":"<<x->key<<endl;
                right_rotate(x->parent->parent);

                right_rotate(x->parent);
                rotation_count["Zig-Zig"]++;
            } else if (x == x->parent->right && x->parent == x->parent->parent->right) {

                cout<<"Zag-Zag"<< ":"<<x->key<<endl;
                left_rotate(x->parent->parent);
                left_rotate(x->parent);
                rotation_count["Zag-Zag"]++;
            } else if (x == x->parent->right && x->parent == x->parent->parent->left) {

                cout<<"Zig-Zag"<< ":"<<x->key<<endl;
                left_rotate(x->parent);
                right_rotate(x->parent);
                rotation_count["Zig-Zag"]++;
            } else {

                cout<<"Zag-Zig"<< ":"<<x->key<<endl;
                right_rotate(x->parent);
                left_rotate(x->parent);
                rotation_count["Zag-Zig"]++;
            }
        }
    }

    void insert(int key) {
        Node* node = new Node{key, nullptr, nullptr, nullptr};
        if (!root) {
            root = node;
        } else {
            Node* x = root;
            Node* y = nullptr;
            while (x) {
                y = x;
                if (node->key < x->key) x = x->left;
                else x = x->right;
            }
            node->parent = y;
            if (node->key < y->key) y->left = node;
            else y->right = node;
            splay(node);
        }
    }

    void print_rotation_count() {
        for (const auto& pair : rotation_count) {
            cout << pair.first << " rotations: " << pair.second << endl;
        }
    }

    void print_inorder(Node* node) {
        if (!node) return;
        print_inorder(node->left);
        cout << node->key << " ";
        print_inorder(node->right);
    }
};

int main() {
    SplayTree tree;
    // tree.insert(5);
    // tree.insert(9);
    // tree.insert(13);
    // tree.insert(2);
    // tree.insert(7);

    vector<int> v = {10,9,2,90,53,4,64,95,59,85,90};

    for (int i : v) {
        cout << "Inserting " << i << endl;
        tree.insert(i);
    }

    tree.print_rotation_count();
    cout << endl;

    tree.print_inorder(tree.root);
    return 0;
}
