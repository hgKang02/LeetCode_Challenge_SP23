class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        result = 0
        for i in range(1, len(salary) - 1, 1):
            result += salary[i]
        print(salary)
        print(result)
        return result / (len(salary) - 2)