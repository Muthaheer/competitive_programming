# https://www.codechef.com/problems/DOWNLOAD

def solution():
    n = int(input())

    recipes = []
    for i in range(n):
        inp = list(map(int, input().split(' ')))
        recipes.append(inp)
    recipes.sort()
    # print(recipes)
    q = int(input())
    for _ in range(q):
        aln = list(map(int, input().split(' ')))
        k = aln[0]
        learnt = [0]*n
        
        for i in range(1, k+1):
            for j, r in enumerate(recipes):
                if r[0] > aln[i]:
                    break
                elif r[1] >= aln[i]:
                    learnt[j] = 1
        

        print(learnt.count(1))



    

solution()