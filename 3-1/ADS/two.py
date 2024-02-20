import heapq

def minCost(goldWeights):
    # Create a priority queue
    heapq.heapify(goldWeights)
    totalCost = 0

    while len(goldWeights) > 1:
        # Extract two smallest elements
        smallest = heapq.heappop(goldWeights)
        second_smallest = heapq.heappop(goldWeights)

        # Calculate cost and add combined weight back
        cost = smallest + second_smallest
        print("Cost:", cost, "Smallest:", smallest, "Second Smallest:", second_smallest)
        totalCost += cost
        heapq.heappush(goldWeights, cost)

    return totalCost

# Example
gold_weights = [2, 7, 9, 15, 23, 1, 3, 5]
print("Minimum no of dirhams spent:", minCost(gold_weights))

# def dividing_2(goldweights):
#     cost = 0
#     while len(goldweights) > 1:
#         goldweights = [int(a+b) for a,b in zip(goldweights[::2], goldweights[1::2])]
#         cost+=sum(goldweights)
#         print(goldweights)
#     return cost



# gold_weights = [2, 7, 9, 15, 23, 1, 3, 5]
# gold_weights.sort()
# cost = dividing_2(gold_weights)
# print(cost)