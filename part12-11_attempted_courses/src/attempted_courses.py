class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"

# Write your solution here
def names_of_students(attempts: list):
    return map(lambda student : student.student_name, attempts)

def course_names(attempts: list):
    courses = map(lambda course : course.course_name, attempts)
    unique_courses = []
    for course in courses:
        if course not in unique_courses:
            unique_courses.append(course)
    unique_courses.sort()
    return unique_courses

if __name__ == '__main__':
    attempt = CourseAttempt("Peter Python", "Introduction to Programming", 5)
    print(attempt.student_name)
    print(attempt.course_name)
    print(attempt.grade)
    print(attempt)

    print('--- Part 1 ---')
    s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
    s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
    s3 = CourseAttempt("Peter Python", "Advanced Course in Programming", 2)
    for name in names_of_students([s1, s2, s3]):
        print(name)

    print('--- Part 2 ---')
    s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
    s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
    s3 = CourseAttempt("Peter Python", "Advanced Course in Programming", 2)
    for name in course_names([s1, s2, s3]):
        print(name)