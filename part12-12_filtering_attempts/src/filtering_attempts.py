class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"

# part 1
def accepted(attempts: list):
    grades_1_min = filter(lambda attempt : attempt.grade >= 1, attempts)
    return grades_1_min

# part 2
def attempts_with_grade(attempts: list, grade: int):
    matching_grade_attempts = filter(lambda attempt : attempt.grade == grade, attempts)
    return matching_grade_attempts

#  part 3
def passed_students(attempts: list, course: str):
    filtered_passed = filter(lambda attempt : attempt.grade > 0 and attempt.course_name == course, attempts)
    passed_names_map = map(lambda student : student.student_name, filtered_passed)
    passed_names_list = []
    for i in passed_names_map:
        passed_names_list.append(i)
    passed_names_list.sort()
    return passed_names_list    

if __name__ == '__main__':

    print('\n--- Part 1 ---\n')
    s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
    s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
    s3 = CourseAttempt("Peter Python", "Advanced Course in Programming", 0)
    for attempt in accepted([s1, s2, s3]):
        print(attempt)

    print('\n--- Part 2 ---\n')
    s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
    s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
    s3 = CourseAttempt("Peter Python", "Introduction to AI", 3)
    s4 = CourseAttempt("Olivia C. Objective", "Data Structures and Algorithms", 3)
    for attempt in attempts_with_grade([s1, s2, s3, s4], 3):
        print(attempt)

    print('\n--- Part 3 ---\n')
    s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
    s2 = CourseAttempt("Olivia C. Objective", "Introduction to AI", 5)
    s3 = CourseAttempt("Peter Python", "Introduction to AI", 0)
    s4 = CourseAttempt("Jack Java", "Introduction to AI", 3)
    for attempt in passed_students([s1, s2, s3, s4], "Introduction to AI"):
        print(attempt)
