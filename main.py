import random

NUM_OF_FAILS_POSSIBLE = 13
wrong_guesses = 0
puzzles = ["foo bar blah", "hardcoded puzzle", "tesztelés", "árvíztűrő tükörfúrógép"]
puzzle = random.choice(puzzles).upper()
guesses = []
riddle = ""

def get_riddle(puzzle, tippek):
    riddle = ""
    for c in puzzle:
        if c in tippek or c in " -":
            riddle += c
        else:
            riddle += "_"
    return riddle

def is_valid(guess):
    if len(guess) > 1 or not guess.isalpha() or guess == "" or guess in guesses:
        return False
    else: return True

print("AKASZTÓFA JÁTÉK")
print("---------------")
print("A megfejtendő rejtvény:", get_riddle(puzzle, guesses))

while wrong_guesses < NUM_OF_FAILS_POSSIBLE and puzzle != riddle.upper():
    guess = input("Tipped: ").upper()
    if is_valid(guess):
        guesses.append(guess)
        if guess in puzzle:
            riddle = get_riddle(puzzle, guesses)
        else: wrong_guesses += 1
        print("--------------------")
        print("Hibapontok száma:", wrong_guesses)
        print(riddle)
    else: continue

if wrong_guesses < NUM_OF_FAILS_POSSIBLE:
    print("Gratulálok nyertél!")
else:
    print("Ez most nem sikerült!")


class Employee():
    def __init__(self, row):
        data = row.split(";")
        self.name = data[0]
        self.gender = data[1]
        self.department = data[2]
        self.year_of_join = int(data[3])
        self.wage = int(data[4])

employees = []

with open("berek2020mod.txt", encoding="utf-8") as file:
    for row in file:
        employees.append(Employee(row))

print("Dolgozók száma:", len(employees))

max_wage_index = 0
for i in range(1, len(employees)):
    if employees[i].wage > employees[max_wage_index].wage:
        max_wage_index = i
print("Legnagyobb fizetés:")
print(employees[max_wage_index].name)
print(employees[max_wage_index].department)
print(employees[max_wage_index].wage)

ertekesitok = []

for employee in employees:
    if employee.department == "értékesítés":
        ertekesitok.append(employee)
print("Értékesítők: ")
for e in ertekesitok:
    print(f"\t{e.name}")

print("Értékesítők száma:", len(ertekesitok))
szumma = 0
for e in ertekesitok:
    szumma += e.wage

print(f"Átlagbérük: {(szumma/len(ertekesitok)):.2f}")

departments = []
for e in employees:
    if e.department not in departments:
        departments.append(e.department)
print("Részlegek:", departments)