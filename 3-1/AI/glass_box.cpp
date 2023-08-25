#include <bits/stdc++.h>
using namespace std;

class GlassBoxesProblem {
private:
    int start_state = 1;
    int goal_state = 6;
    vector<int> box_keys;
    map<int, int> box_to_key; // Maps box number to the key it contains

    void shuffleKeys() {
        srand(time(0)); // Seed for randomness
        random_shuffle(box_keys.begin(), box_keys.end());
        for (int i = 0; i < 6; i++) {
            box_to_key[i + 1] = box_keys[i];
        }
    }

public:
    GlassBoxesProblem() {
        for (int i = 1; i <= 6; i++) {
            box_keys.push_back(i);
        }
        shuffleKeys();
    }

    string bfs() {
        set<int> visited_boxes;
        set<int> keys_possessed;
        queue<int> queue;
        queue.push(start_state);
        keys_possessed.insert(start_state); // You start with the key to the first box

        while (!queue.empty()) {
            int current_box = queue.front();
            queue.pop();

            cout << "Agent is at box " << current_box << endl;

            if (current_box == goal_state) {
                cout << "Agent found the banana in box " << current_box << "!" << endl;
                return "Banana found in box " + to_string(current_box) + "!";
            }

            if (visited_boxes.find(current_box) == visited_boxes.end()) {
                visited_boxes.insert(current_box);
                int key_found = box_to_key[current_box];
                keys_possessed.insert(key_found);

                cout << "Agent unlocked box " << current_box << " and found the key for box " << key_found << endl;

                for (int i = 1; i <= 6; i++) {
                    if (keys_possessed.find(i) != keys_possessed.end() && visited_boxes.find(i) == visited_boxes.end()) {
                        queue.push(i);
                    }
                }
            }
        }

        cout << "Agent couldn't find the banana." << endl;
        return "Banana not found";
    }

    void printBoxKeys() {
        for (int i = 1; i <= 6; i++) {
            cout << "Box " << i << " contains key to box " << box_to_key[i] << endl;
        }
    }
};

int main() {
    GlassBoxesProblem problem;
    problem.printBoxKeys();
    problem.bfs();
    return 0;
}
