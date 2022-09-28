class solution():
    def richestCus(accounts:list[list[int]])-> int:
        finalAccounts = []
        for i in accounts:
            sums = sum(i)
            finalAccounts.append(sums)
            biggest= max(finalAccounts)
        return biggest


acco = [[1,2,3],[3,2,1]]
print(solution.richestCus(acco))