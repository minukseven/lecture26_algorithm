import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    words = []
    for _ in range(n):
        words.append(input().strip())
    
    words = sorted(set(words), key=lambda x: (len(x), x))
    
    for word in words:
        print(word)

solve()