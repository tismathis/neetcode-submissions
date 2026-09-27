class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_final = ""
        t_Map = {}
        s_Map = {}
        have_counter = 0 
        need_counter = len(t)
        max_Size = 0 
        for char in t : 
            t_Map[char] = 1 + t_Map.get(char,0) #initialize the t MAP
        
        l = 0 
        for j,r in enumerate(len(s)) :
            s_Map[r] = 1 + t_Map.get(r,0) #initialize the s_Map 
            
            if s_Map[r] == t_Map[r] :
                have_counter +=1
                if have_counter == need_counter and j-l+1 < min_Size :
                    min_Size = j-l+1
                    s_final = s.substring[l,j+1] 
            elif r not in t_Map : 
                continue
            while have_counter == need_counter :
                if s[l] in s_Map :
                    s_Map[s[l]] -=1
                    if s_Map[s[l]] < t_Map[s[l]] :
                        have_counter -=1
                    else : 
                        break
                else : 
                    continue
        return s_final
            
            
            





