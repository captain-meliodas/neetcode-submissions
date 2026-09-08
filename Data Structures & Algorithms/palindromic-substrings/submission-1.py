class Solution:
    def countSubstrings(self, s: str) -> int:
        """Manacher's algorithm"""
        T = "@#"+"#".join(s)+"#$"
        n = len(T)
        C = R = 0
        P = [0]*n

        for i in range(1,n-1):
            mirror = 2*C-i

            if i<R:
                P[i] = min(R-i, P[mirror])
            
            #Expand around center
            while T[i+1+P[i]] == T[i-1-P[i]]:
                P[i]+=1
            
            if i+P[i] > R:
                R = i+P[i]
                C = i
            
        return sum((radius+1)//2 for radius in P)


        