def hello():                # Тело программы. Каждая цикл это решение одного из заданий.

    border = input('Выберите номер задания на которые ты хочешь увидеть решение(напоминаю в домашнем задании доступно 5 задач): \n',)

    if border == '1':
        def task_1():
            class circle:
                def __init__(circle, circle_color = 'неизвестный цвет', radius = None):
                    circle.circle_color = circle_color
                    circle.radius = radius
                def square(circle):
                    square = 2 * circle.radius * circle.radius * 3.14
                    return square
                def circumference(circle):
                    circumference = 2 * 3.14 * circle.radius
                    return circumference
            data = circle(input('Введите цвет круга:\n'), int(input('Введите радиус круга:\n')))
            print(f'Радиус круга равен - {data.radius}. Цвет круга - {data.circle_color}. Площадь круга равна - {data.square()}. Длина круга равна - {data.circumference()}.')
        def main_1():                                                     # Функция запуска кода и повтора
            again = 'да'
            while again.lower() == 'да':
                task_1()
                again = input('Хотите посчитать параметры для другого круга? (Да = запустить еще раз, Любая клавиша = выйти из подпрограммы) \n' )
        main_1()


    if border == '2':
        def task_2():
            class bank_account:
                def __init__(self, check="Номер счета", name='Неизвестное ФИО', operation='Операция', sum=0):
                    self.check = check
                    self.name = name
                    self.operation = operation
                    self.sum = sum
                    self.balance = 10000

                def final_sum(self):
                    if self.operation == '+':
                        final_balance = self.balance + self.sum  
                    else:
                        final_balance = self.balance - self.sum  
                    return final_balance

            data = bank_account(
            int(input("Введите номер счета:\n")),
            input('Введите свое ФИО:\n'),
            input("Введите операцию + - пополнение счета, - - снятие со счета:\n"),
            int(input('Введите сумму операции:\n'))
            )
            
            print(f'Номер счета: {data.check}, ФИО владельца: {data.name}, Ваш баланс после выполненных операций: {data.final_sum()}')

        def main_2():                                                     # Функция запуска кода и повтора
            again = 'да'
            while again.lower() == 'да':
                task_2()
                again = input('Хотите еще произвести операции? (Да = запустить еще раз, Любая клавиша = выйти из подпрограммы) \n' )
        main_2()


    if border == '3':
        def task_3():
            class student:
                def __init__(std, name='ФИО студента', old = 'Возраст студента', gpa = 'Средний бал'):
                    std.name = name
                    std.old = old
                    std.gpa = gpa
                    std.status = None

                def determine_status(std):  # Добавлен метод для определения статуса
                    if std.gpa >= 4.5:
                        std.status = 'Отличник'
                    elif std.gpa <= 3.4:
                        std.status = 'Троечник'
                    else:
                        std.status = 'Хорошист'

            grade = student(
            input('Введите ФИО студента:\n'),
            int(input('Введите возраст студента:\n')),
            float(input('Введите cредний бал:\n'))  
            )

            grade.determine_status()

            print(f'ФИО студента {grade.name}, возраст студента {grade.old} лет. Cредний бал: {grade.gpa}. Статус студента: {grade.status}')
        
        def main_3():                                                     # Функция запуска кода и повтора
            again = 'да'
            while again.lower() == 'да':
                task_3()
                again = input('Хотите оценить еще одного студента? (Да = запустить еще раз, Любая клавиша = выйти из подпрограммы) \n' )
        main_3()

    if border == '4':
        class Book:
            def __init__(self, title, author, year):
                self.title = title
                self.author = author
                self.year = year

            def get_title(self):
                return self.title

            def set_title(self, title):
                self.title = title

            def get_author(self):
                return self.author

            def set_author(self, author):
                self.author = author

            def get_year(self):
                return self.year

            def set_year(self, year):
                self.year = year


        book1 = Book("1984", "Джордж Оруэлл", 1949)                 # Создание объектов класса Book
        book2 = Book("Война и мир", "Лев Толстой", 1869)

        print(f"Название: {book1.get_title()}, Автор: {book1.get_author()}, Год издания: {book1.get_year()}")
        book1.set_year(1950)  # Изменение года издания
        print(f"Обновленный год издания: {book1.get_year()}")


        print(f"Название: {book2.get_title()}, Автор: {book2.get_author()}, Год издания: {book2.get_year()}")
        book2.set_author("Лев Николаевич Толстой")  # Изменение автора
        print(f"Обновленный автор: {book2.get_author()}")

    if border == '5':
        class Car:
            def __init__(self, brand, model, color, year):
                self.brand = brand
                self.model = model
                self.color = color
                self.year = year

            def get_brand(self):
                return self.brand

            def set_brand(self, brand):
                self.brand = brand
            
            def get_model(self):
                return self.model

            def set_model(self, model):
                self.model = model
            
            def get_color(self):
                return self.color

            def set_color(self, color):
                self.color = color
            
            def get_year(self):
                return self.year

            def set_year(self, year):
                self.year = year

        car_1 = Car('Mersedes', 'AMG GT', 'Black', 2025)
        car_2 = Car('BMW', 'M5', 'Blue', 2024)
        car_3 = Car('Ferrari', 'F50', 'Yelloy', 1997)
        print(f'Марка: {car_1.get_brand()}, Модель: {car_1.get_model()}, Цвет: {car_1.get_color()}, Год выпуска: {car_1.get_year()}')
        car_1.set_model('AMG GT 63')
        print(f'Обновленная марка: {car_1.get_model()}')
        print(f'Марка: {car_2.get_brand()}, Модель: {car_2.get_model()}, Цвет: {car_2.get_color()}, Год выпуска: {car_2.get_year()}')
        car_2.set_color('Metalic blue')
        print(f'Обновленный цвет: {car_2.get_color()}')
        print(f'Марка: {car_3.get_brand()}, Модель: {car_3.get_model()}, Цвет: {car_3.get_color()}, Год выпуска: {car_3.get_year()}')
        car_3.set_color('Red')
        car_3.set_year(1996)
        print(f'Обновленный цвет: {car_3.get_color()}, обновленный год: {car_3.get_year()}')


def main():                                                     # Функция запуска кода и повтора
   again = 'да'
   while again.lower() == 'да':
      hello()
      again = input('Вы еще хотите проверить домашнее задание ? (Да = запустить еще раз, Любая клавиша = выйти из программы) \n' )


print('Добро пожаловать в домашнее задание!\n Тема: Цель: Практически применить изученные темы:\n ООП, классы и ООП в Python.')                   # Вход в программу


if __name__ == "__main__":
    main()


print('Всегда рады Вам помочь! Досвидания.')