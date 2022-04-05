# Author : MacVinay

'''
T => Number of test cases
N => Total number of questions
X => Correct responses
P => Passing marks
'''

T = int(input())

for i in range(T):
    
    N, X, P = map(int, input().split())
    
    if (X * 3 + (X - N )) >= P:
        print("PASS")
    else:
        print("FAIL")
