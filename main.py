from datetime import date

from art import tprint

from application.db.people import get_employees
from application.salary import calculate_salary


if __name__ == '__main__':
    tprint("Import Module Package")
    print(f'Сurrent date: {date.today()}')
    get_employees()
    calculate_salary()