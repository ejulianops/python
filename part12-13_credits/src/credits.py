from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution

# part 1

def credits_sum_helper(balance_sum, attempt):
    return balance_sum + attempt.credits

def sum_of_all_credits(course_attempts):
    return reduce(credits_sum_helper, course_attempts, 0)

# part 2

def sum_passed_credits(balance_sum, attempt):
    if attempt.grade > 0:
        return balance_sum + attempt.credits
    else:
        return balance_sum

def sum_of_passed_credits(course_attempts):
    return reduce(sum_passed_credits, course_attempts, 0)

if __name__ == "__main__":

    print('\n--- Part 1 ---\n')
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 4, 5)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    credit_sum = sum_of_all_credits([s1, s2, s3])
    print(credit_sum)

    print('\n--- Part 2 ---\n')
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    credit_sum = sum_of_passed_credits([s1, s2, s3])
    print(credit_sum)