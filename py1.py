import requests

class Fetcher:
    def __init__(self):
        url = "https://cdn.ituring.ir/ex/users.json"
        response = requests.get(url)
        if response.status_code == 200:
            self.students = response.json()
        else:
            self.students = []

    def nerds(self):
        result = set()
        for student in self.students:
            if student["score"] > 18.5:
                name = student["first_name"] + " " + student["last_name"]
                result.add(name)
        return result

    def sultans(self):
        max_score = 0
        names = []
        for student in self.students:
            if student["score"] > max_score:
                max_score = student["score"]
                names = []
                names.append(student["first_name"] + " " + student["last_name"])
            elif student["score"] == max_score:
                names.append(student["first_name"] + " " + student["last_name"])
        return tuple(names)

    def mean(self):
        total = 0
        count = 0
        for student in self.students:
            total += student["score"]
            count += 1
        if count > 0:
            return total / count
        else:
            return 0

    def get_students(self):
        result = []
        for student in self.students:
            new_student = {}
            for key in student:
                if key not in ["city", "province", "location"]:
                    new_student[key] = student[key]
            result.append(new_student)
        return result
