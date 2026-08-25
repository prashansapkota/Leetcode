class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        start from s[0] and t[0]

        move index at t[0] till we find a match
        if found, we move index for s

        """
        s_i = 0

        for t_i in range(len(t)):
            if s_i >= len(s):
                return True
            if s[s_i] == t[t_i]:
                s_i+=1  

        return s_i >= len(s)
        
            

                    

            
        