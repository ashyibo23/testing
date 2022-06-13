#code forces range of sum query II, dynamic range of sum 

class Solution:
    def querySum(self, n, arr, q, queries):
        s = []
        t = 0
        res = []
        
        for i in arr:
            t += i
            s += [t]
        for j in range(0, 2*q, 2):
            x, y = queries[j]-1, queries[j+1]-1
            res += [s[y] -s[x]+arr[x]]
        return res 



if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = input().split()
        for i in range(n):
            arr[i] = int(arr[i])
        q = int(input())
        queries = input().split()
        for i in range(0,2*q,2):
            queries[i] = int(queries[i])
            queries[i+1] = int(queries[i+1])
        
        ob = Solution()
        ans = ob.querySum(n, arr, q, queries)
        for it in(ans):
            print(it, end=" ")
        print()



# n = 4
# arr = [1, 2, 3, 4]
# q = 2
# queries = [1, 4, 2, 3]
# # Output: 10 5

# sol = Solution()
# print(sol.querySum(n, arr, q, queries))



