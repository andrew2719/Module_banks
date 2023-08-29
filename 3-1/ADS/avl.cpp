// construst AVL tree from a given array that calculates the total rotations that are happened in the process
// Created by junaid on 05/02/21.
//
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

struct Node {
    int data;
    Node *left;
    Node *right;
    int height;

    Node(int data) {
        this->data = data;
        left = nullptr;
        right = nullptr;
        height = 1;
    }
};

class AVLTree {
    Node *root;
    int totalRotations = 0;

    int height(Node *node) {
        if (node == nullptr) {
            return 0;
        }
        return node->height;
    }

    int getBalanceFactor(Node *node) {
        if (node == nullptr) {
            return 0;
        }
        return height(node->left) - height(node->right);
    }

    Node *leftRotate(Node *node) {
        Node *newRoot = node->right;
        Node *newRight = newRoot->left;

        newRoot->left = node;
        node->right = newRight;

        node->height = max(height(node->left), height(node->right)) + 1;
        newRoot->height = max(height(newRoot->left), height(newRoot->right)) + 1;

        return newRoot;
    }

    Node *rightRotate(Node *node) {
        Node *newRoot = node->left;
        Node *newLeft = newRoot->right;

        newRoot->right = node;
        node->left = newLeft;

        node->height = max(height(node->left), height(node->right)) + 1;
        newRoot->height = max(height(newRoot->left), height(newRoot->right)) + 1;

        return newRoot;
    }

    Node *insert(Node *node, int data) {
        if (node == nullptr) {
            return new Node(data);
        }
        if (data < node->data) {
            node->left = insert(node->left, data);
        } else {
            node->right = insert(node->right, data);
        }

        node->height = max(height(node->left), height(node->right)) + 1;

        int balanceFactor = getBalanceFactor(node);

        // left-left case
        if (balanceFactor > 1 && data < node->left->data) {
            totalRotations += 1;
            return rightRotate(node);
        }

        // right-right case
        if (balanceFactor < -1 && data > node->right->data) {
            totalRotations += 1;
            return leftRotate(node);
        }

        // left-right case

        if (balanceFactor > 1 && data > node->left->data) {
            totalRotations += 2;
            node->left = leftRotate(node->left);
            return rightRotate(node);
        }

        // right-left case
        if (balanceFactor < -1 && data < node->right->data) {
            totalRotations += 2;
            node->right = rightRotate(node->right);
            return leftRotate(node);
        }

        return node;

    }

    void preOrder(Node *node) {
        if (node == nullptr) {
            return;
        }
        cout << node->data << " ";
        preOrder(node->left);
        preOrder(node->right);
    }

public:
    AVLTree() {
        root = nullptr;
    }

    void insert(int data) {
        root = insert(root, data);
    }

    void preOrder() {
        preOrder(root);
    }

    int getTotalRotations() {
        return totalRotations;
    }
};

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    AVLTree tree;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
        tree.insert(arr[i]);
    }
    cout << tree.getTotalRotations() << endl;
    return 0;
}