#include <iostream>
#include <vector>
#include <climits>

using namespace std;

int findMinCost(vector<int>& biscuits, int startIndex, int accumulatedCost) {
    int n = biscuits.size();
    
    // Base case: If only one biscuit is left, return the accumulated cost
    if (n == 1) {
        return accumulatedCost;
    }

    int minCost = INT_MAX;

    // Try combining each pair of biscuits
    for (int i = startIndex; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            // New weight after combining two biscuits
            int newWeight = biscuits[i] + biscuits[j];

            // Create a new vector without the two combined biscuits
            vector<int> newBiscuits;
            for (int k = 0; k < n; ++k) {
                if (k != i && k != j) {
                    newBiscuits.push_back(biscuits[k]);
                }
            }
            newBiscuits.push_back(newWeight);

            // Recursive call
            int cost = findMinCost(newBiscuits, 0, accumulatedCost + newWeight);
            minCost = min(minCost, cost);
        }
    }

    return minCost;
}

int main() {
    vector<int> goldWeights = {2, 7, 9, 15, 23, 1, 3, 5};
    int minCost = findMinCost(goldWeights, 0, 0);
    cout << "Minimum number of dirhams spent: " << minCost << endl;
    return 0;
}
