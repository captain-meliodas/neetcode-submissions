class Solution:
    def longestPalindrome(self, s: str) -> str:
        """Manacher Algorithm's"""
        T = "@#"+"#".join(s)+"#$"
        n = len(T)
        C = 0
        R = 0
        max_radius = 0
        center_idx = 0
        P = [0]*n

        for i in range(1,n-1):
            mirror = 2*C-i

            if i<R:
                P[i] = min(R-i, P[mirror])
            
            while T[i+1+P[i]] == T[i-1-P[i]]:
                P[i]+=1
            
            if i+P[i]>R:
                C = i
                R = i+P[i]
            
            #calculation to get indexes for substring
            if P[i] > max_radius:
                max_radius = P[i]
                center_idx = i
            
        start = (center_idx-max_radius)//2
        return s[start: start+max_radius]

        