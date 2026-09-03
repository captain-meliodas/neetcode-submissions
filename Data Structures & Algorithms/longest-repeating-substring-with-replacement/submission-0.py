class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l=0
        maxf=0
        for r in range(len(s)):
            #add new char to window
            count[s[r]] = count.get(s[r],0)+1

            #update the most frequent char count
            maxf = max(maxf, count[s[r]])
            #if replacement exceeds k shrink the window from left
            if r-l+1 - maxf > k:
                count[s[l]] -= 1
                l += 1

            #update the max window size so far
            res = max(res, r-l+1)
        
        return res