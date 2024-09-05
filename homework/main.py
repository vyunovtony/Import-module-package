from datetime import datetime
from application.db.people import get_employees
from application.salary import calculate_salary


def get_current_time() -> None:
    current_time = datetime.now().strftime("%d/%m/%Y")
    print(f"Текущая дата: {current_time}")


if __name__ == '__main__':
    get_current_time()
    calculate_salary()
    get_employees()