from func import *

arraySizes = [100, 1000]

print("\nBest case:\n")

print("Bubble sort:")

for size in arraySizes:
    b = bestCase(size)
    t0 = time.time()
    results = bubbleSort(b)
    print("Array size: {0: <5d} Comparisons: {1: <12d} Swaps: {2: <12d} Time taken: {3: <12.6f}".format(size, results['c'], results['s'], time.time() - t0))

print("Comb sort:")

for size in arraySizes:
    b = bestCase(size)
    t0 = time.time()
    results = combSort(b)
    print("Array size: {0: <5d} Comparisons: {1: <12d} Swaps: {2: <12d} Time taken: {3: <12.6f}".format(size, results['c'], results['s'], time.time() - t0))

print("\nWorst case:\n")

print("Bubble sort:")
for size in arraySizes:
    w = worstCase(size)
    t0 = time.time()
    results = bubbleSort(w)
    print("Array size: {0: <5d} Comparisons: {1: <12d} Swaps: {2: <12d} Time taken: {3: <12.6f}".format(size, results['c'], results['s'], time.time() - t0))

print("Comb sort:")

for size in arraySizes:
    w = worstCase(size)
    t0 = time.time()
    results = combSort(w)
    print("Array size: {0: <5d} Comparisons: {1: <12d} Swaps: {2: <12d} Time taken: {3: <12.6f}".format(size, results['c'], results['s'], time.time() - t0))

print("\nRandom case (average results):\n")

print("Bubble sort:")
for size in arraySizes:
    totalComparisons = 0
    totalSwaps = 0
    totalTime = 0
    for i in range(50):
        r = randomCase(size)
        t0 = time.time()
        results = bubbleSort(r)
        totalComparisons += results['c']
        totalSwaps += results['s']
        totalTime += time.time() - t0
    print("Array size: {0: <5d} Comparisons: {1: <12.1f} Swaps: {2: <12.1f} Time taken: {3: <12.6f}".format(size, totalComparisons/50, totalSwaps/50, totalTime/50))
        
print("Comb sort:")

for size in arraySizes:
    totalComparisons = 0
    totalSwaps = 0
    totalTime = 0
    for i in range(50):
        r = randomCase(size)
        t0 = time.time()
        results = combSort(r)
        totalComparisons += results['c']
        totalSwaps += results['s']
        totalTime += time.time() - t0
    print("Array size: {0: <5d} Comparisons: {1: <12.1f} Swaps: {2: <12.1f} Time taken: {3: <12.6f}".format(size, totalComparisons/50, totalSwaps/50, totalTime/50))
