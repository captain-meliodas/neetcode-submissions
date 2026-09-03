class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        countT = {}
        window = {}

        #populate the required target count
        for c in t:
            countT[c] = countT.get(c,0)+1
        
        have = 0
        need = len(countT)
        res = [-1,-1]
        resLen = float('infinity')
        l = 0
        
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c,0)+1
            # If the current character is needed and its count matches the requirement
            if c in countT and window[c] == countT[c]:
                have += 1
            # While the window is valid, try to shrink it from the left
            while have == need:
                # Update our result if this window is smaller than previous best
                if r-l+1 < resLen:
                    res = [l,r]
                    resLen = r-l+1

                # Pop the left character from the window
                window[s[l]] -= 1
                # If popping it broke the validity, update 'have'
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                
                l += 1
        l,r = res
        return s[l:r+1] if resLen != float('infinity') else ""
        