from bs4 import BeautifulSoup
import requests
from csv import writer
from re import sub
from re import search
from django import template

register = template.Library()

@register.simple_tag
def scrape_now(printer):

    req1 = requests.get(printer)
    courseParsed = BeautifulSoup(req1.text, "html.parser")
    tutorAnchor = courseParsed.select(".mainContentContainer")

    parsed = courseParsed
    anchorPosition = parsed.select(".table-notlateFlag")
    anchorPositionTutors = parsed.select(".courseHeader")
    anchorPositionName = parsed.select(".font-weight\:bold")
    studentName = anchorPositionName[1].get_text()

    with open("spotV2.csv", "w") as database:
        csv_writer = writer(database)
        csv_writer.writerow(["Name"])
        csv_writer.writerow([studentName])
        csv_writer.writerow(["Course", "Assignment", "Marks", "Deadline"])

    with open("tutorsPage.csv", "w") as database:
        csv_writer = writer(database)
        csv_writer.writerow(
            ["Course", "Credits", "Students", "Courseleader", "Assessment Method"])

    courseLinks = []
    courses = []
    for i in anchorPositionTutors:
        url = ((i.find('a'))['href'])
        courseLinks.append(url)

        req = requests.get(url)
        courseParsed = BeautifulSoup(req.text, "html.parser")
        tutorAnchor = courseParsed.select(".mainContentContainer")

        for i in tutorAnchor:
            result = search('(.*) syllabus', (i.get_text()))
            course = result.group(1)

            if course in courses:
                break
            else:
                courses.append(course)

            with open("tutorsPage.csv", "a") as database:
                csv_writer = writer(database)

                result = search('Credits: (.*)Enrolled', (i.get_text()))
                credits = result.group(1)

                result = search('students: (\d*)', (i.get_text()))
                students = result.group(1)

                result = search('leader: (.*)Additional staff', (i.get_text()))
                courseLeader = result.group(1)

                if (course == "COMP11120 Mathematical Techniques for Computer Science") or (course == "COMP11212 Fundamentals of Computation"):
                    result = search(
                        'Assessment methods(.*)Timetable', (i.get_text()))
                else:
                    result = search(
                        'Assessment methods(.*) assessment', (i.get_text()))
                assessmentMethod = result.group(1)

                print(course, credits, students, courseLeader, assessmentMethod)
                csv_writer.writerow(
                    [course, credits, students, courseLeader, assessmentMethod])


    with open("spotV2.csv", "a") as database:
        csv_writer = writer(database)

        for database in anchorPosition:
            name = database.find_previous_sibling().get_text()
            marks = database.get_text()
            marks = sub('[^\w\()\/\%]', '', marks)
            deadline = database.find_next_sibling().get_text()
            if name[0:5] == "11120":
                name = sub('11120-', '', name)
                course = "Mathematical Techniques for Computer Science"
            elif name[0:5] == "10120":
                name = sub('10120-', '', name)
                course = "First Year Team Project"
            elif name[0:5] == "12111":
                name = sub('12111-', '', name)
                course = "Fundamentals of Computer Engineering"
            elif name[0:5] == "15111":
                name = sub('15111-', '', name)
                course = "Fundamentals of Computer Architecture"
            elif name[0:5] == "16321":
                name = sub('16321-', '', name)
                course = "Introduction to Programming 1"
            csv_writer.writerow([course, name, marks, deadline])
    newpr = "Hi, spot url is " + printer + ", the scrapes has finished executing!"
    return newpr

if __name__ == "__main__":
    main(sys.argv[1])
