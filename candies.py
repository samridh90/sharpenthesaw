"""
Hackerrank problem: https://www.hackerrank.com/challenges/candies
Greedy + DP
"""

def main():
    n = int(raw_input())
    if n <= 1:
        return 1
    ranking = []
    counts = []
    for i in xrange(n):
        ranking.append(int(raw_input()))
        counts.append(1)

    for i in xrange(1, n):
        if ranking[i] > ranking[i - 1]:
            counts[i] = counts[i - 1] + 1
    for i in xrange(n-1, 0, -1):
        if ranking[i-1] > ranking[i]:
            counts[i-1] = max(counts[i] + 1, counts[i-1])
    return sum(counts)

if __name__ == '__main__':
    print main()
