class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        t_Map = {}
        for c in t:
            t_Map[c] = 1 + t_Map.get(c, 0)

        s_Map = {}
        have, need = 0, len(t_Map)
        min_Size = float('inf')
        res = (-1, -1)
        l = 0

        for r, c in enumerate(s):
            if c in t_Map:
                s_Map[c] = 1 + s_Map.get(c, 0)
                if s_Map[c] == t_Map[c]:
                    have += 1

            while have == need:
                if r - l + 1 < min_Size:
                    min_Size = r - l + 1
                    res = (l, r)
                left = s[l]
                if left in t_Map:
                    s_Map[left] -= 1
                    if s_Map[left] < t_Map[left]:
                        have -= 1
                l += 1

        return s[res[0]:res[1] + 1] if min_Size != float('inf') else ""