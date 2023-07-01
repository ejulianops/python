import urllib.request
import json
import math

def retrieve_all():

    active_courses = []

    url = "https://studies.cs.helsinki.fi/stats-mock/api/courses"
    response = urllib.request.urlopen(url)    
    stringfy_response = response.read() 
    json_response = json.loads(stringfy_response)

    for i in json_response:
        if i['enabled'] == True:
            course = []
            course.append(i['fullName'])
            course.append(i['name'])
            course.append(i['year'])
            course.append(sum(i['exercises']))
            active_courses.append(tuple(course))            

    return active_courses

def retrieve_course(course_name: str):
    
    statistics = {}

    url = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"

    response = urllib.request.urlopen(url)
    response = response.read()
    response = json.loads(response)

    weeks = 0
    students = 0
    hours = 0
    exercises = 0
    
    for week in response:
        if response[week]["students"] > students:
            students = response[week]["students"]
        hours += response[week]['hour_total']
        exercises += response[week]['exercise_total']
        weeks += 1  

    statistics['weeks'] = weeks
    statistics['students'] = students
    statistics['hours'] = hours
    hours_average = math.floor(hours / students)
    statistics['hours_average'] = hours_average
    statistics['exercises'] = exercises
    exercises_average = math.floor(exercises / students)
    statistics['exercises_average'] = exercises_average

    return statistics
    
if __name__ == "__main__":
    retrieve_all()
    retrieve_course("docker2019")
