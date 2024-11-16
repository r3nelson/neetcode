class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:    

        if not s2:
            return False

        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False

        s1_counts = [0] * 26
        s2_counts = [0] * 26

        for r in range(n1):
            s1_counts[(ord(s1[r]) - ord('a'))] += 1
            s2_counts[(ord(s2[r]) - ord('a'))] += 1

        if s1_counts == s2_counts:
            return True

        for r in range(n1, n2):
            s2_counts[(ord(s2[r]) - ord('a'))] += 1
            s2_counts[(ord(s2[r - n1] ) - ord('a'))] -= 1

            if s1_counts == s2_counts:
                return True
        return False
