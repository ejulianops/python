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

def sum_of_passed_credits(course_attempts):
    sum_passed_credits = list(filter(lambda attempt : attempt.grade > 0, course_attempts))

    return reduce(lambda credits, attempt : credits + attempt.credits, sum_passed_credits, 0)

# part 3

def average(course_attempts: list):
    passed_attempts = list(filter(lambda attempt : attempt.grade > 0, course_attempts))

    return reduce(lambda grades, attempt: grades + attempt.grade, passed_attempts, 0) / len(passed_attempts)

if __name__ == "__main__":cd ..

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

    print('\n--- Part 3 ---\n')
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    ag = average([s1, s2, s3])
    print(ag)