# Solution for: https://community.topcoder.com/stat?c=problem_statement&pm=2829&rd=5072

def minSums(numbers, sum, i, j):
    print('Args: ', numbers, sum, i, j)
    if sum <= 0:
        return 0

    if int(numbers[i:j]) == sum:
        return 0
    elif len(numbers) == 1:
        return -1
    elif len(numbers) == 2 and (int(numbers[0]) + int(numbers[1])) == 1:
        return 1
    else:
        totAdds = float('inf')
        for m in range(i+1, j):
            leftSum = int(numbers[i:m])
            rightSum = int(numbers[m:j])
            if leftSum + rightSum == sum:
                totAdds = min(minSums(numbers, leftSum , i, m) + minSums(numbers, rightSum, m, j), totAdds) + 1
        return totAdds


def solution(numbers, sum):
    return minSums(numbers, sum, 0, len(numbers))

print(solution("99999", 45))