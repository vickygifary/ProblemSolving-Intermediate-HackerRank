def renameFile(newName: str, oldName: str) -> int:
    MOD = 10**9 + 7
    m, n = len(newName), len(oldName)
    
    # dp[i][j] represents the number of ways to form newName[0:i] from oldName[0:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # An empty newName can always be formed in one way
    for j in range(n + 1):
        dp[0][j] = 1
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # If characters match, we can either include or exclude the character
            if newName[i - 1] == oldName[j - 1]:
                dp[i][j] = (dp[i][j - 1] + dp[i - 1][j - 1]) % MOD
            else:
                dp[i][j] = dp[i][j - 1]  # Exclude the character in oldName
    
    return dp[m][n]

# Ensure we read input correctly
if __name__ == "__main__":
    newName = input().strip()
    oldName = input().strip()
    print(renameFile(newName, oldName))
