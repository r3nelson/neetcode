class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        # #my solution
        # counter = 0
        # while students:
        #     if counter >= len(students):
        #         return len(students)

        #     if students[0] == sandwiches[0]:
        #         students.pop(0)
        #         sandwiches.pop(0)
        #         counter = 0
        #     else:
        #         students.append(students.pop(0))
        #         counter += 1
        # return 0

        res = len(students)
        count = Counter(students)
        print(count)

        for s in sandwiches:
            if count[s] > 0:
                res -= 1
                count[s] -= 1
            else:
                return res

        return res