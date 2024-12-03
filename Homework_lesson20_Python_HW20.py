def hello():                # Тело программы. Каждая цикл это решение одного из заданий.

    border = input('Выберите номер задания на которые ты хочешь увидеть решение(напоминаю в домашнем задании доступно 7 задач): \n',)

    if border == '1':
        print('Задание 1. Написать скрипт, который принимает на вход массив чисел и сортирует его в порядке убывания.')
        numbers = input('Введите числа через пробел: \n').split()
        result = [int(item) for item in numbers]
        result.sort()
        result.reverse()
        print(result)

    elif border == '2':
        print('Задание 2. Написать скрипт, который принимает на вход список чисел и находит медиану этого списка.')
        numbers = input('Введите числа через пробел: \n').split()
        result = [int(item) for item in numbers]
        result.sort()
        if len(result) % 2 == 0:
            med_len = len(result) // 2
            medium = (result[med_len] + result[med_len - 1]) / 2
            print(medium)
        else:
            from math import floor
            medium = len(result) / 2
            print(result[floor(medium)])

    elif border == '3':
        print('Задание 3. Написать скрипт, который принимает на вход строку и заменяет в ней все гласные буквы на символ "-".')
        str_1 = str(input('Введите строку на английском языке:\n'))
        letters = 'aAeEyYuUiIoO'
        str_final = ''
        for i in str_1:
            if i in letters:
                str_final += '-'
            else:
                str_final += i
        print(str_final)
        
    elif border == '4':
        print('Задание 4. Написать скрипт, который принимает на вход строку и выводит на экран \n количество букв  в верхнем регистре, количество букв в нижнем регистре,\nколичество цифр и количество символов пунктуации."')
        str_1 = str(input('Введите строку на английском языке с цифрами, буквами и знаками препинания:\n'))
        numbers = '0123456789'
        letters_big = 'QWERTYUIOPLKJHGFDSAZXCVBNM'
        letters_little = 'qwertyuiopasdfghjklzxcvbnm'
        signs = '!?. ,:;'
        s_1, s_2, s_3, s_4 = 0, 0, 0, 0             # Счетчик для каждого поиска
        for i in str_1:
            if i in numbers:
                s_1 += 1
            elif i in letters_big:
                s_2 += 1
            elif i in letters_little:
                s_3 += 1
            else:
                s_4 += 1
        print(f'В строке введенной Вами: цифр - {s_1}, букв в верхнем регистре - {s_2},\nбукв в нижнем регистре - {s_3}, знаков препинания - {s_4}.')

    elif border == '5':
        print('Задание 5. Написать скрипт, который принимает на вход два списка и находит общие элементы,\nа затем создает новый список, содержащий только уникальные элементы.')
        str_1 = input('Введите первую строку с символами:\n')
        str_2 = input('Введите вторую строку с символами:\n')
        str_3 = ''
        for i in str_1:
            for j in str_2:
                if i == j:
                    str_3 += i
        for k in str_3:             # Проверка на уникальность
            while str_3.count(k) > 1:
                str_3 = str_3.replace(k,'', 1) 
        print(f'Уникальные символы которые встречаются в списках: {str_3}.')

    elif border == '6':
        print('Задание 6. Написать скрипт, который принимает на вход список IP-адресов и\nпроверяет их оступность с помощью ping-запросов. Результаты проверки сохраняются в отдельный файл.')
        import os
        import platform

        def ping_ip(ip_address):
            param = "-n" if platform.system().lower() == "windows" else "-c"
            command = f"ping {param} 1 {ip_address}"
            return os.system(command) == 0

        def check_ips(ip_list, output_file="ping_results.txt"):
            results = []
            for ip in ip_list:
                status = "Доступен" if ping_ip(ip) else "Недоступен"
                results.append(f"{ip}: {status}")
                print(f"{ip}: {status}")

        # Сохраняем результаты в файл
            with open(output_file, "w") as file:
                file.write("\n".join(results))
            print(f"Результаты сохранены в файл {output_file}")

        if __name__ == "__main__":
            ip_addresses = input("Введите IP-адреса через пробел: ").split()
            check_ips(ip_addresses)

    elif border == '7':
        print('Задание 7. Написать скрипт, который принимает на вход список файлов и находит файлы, имена которых содержат определенную подстроку')
        def find_files(files, substring):
            return [file for file in files if substring in file]

        file_list = input("Введите список файлов через запятую: ").split(",")
        file_list = [file.strip() for file in file_list]            # Удаляем лишние пробелы
        sub_string = input("Введите подстроку для поиска: ")
        matched_files = find_files(file_list, sub_string)

        if matched_files:
            print("Найдены файлы:")
            for file in matched_files:
                print(file)
        else:
            print("Файлы с указанной подстрокой не найдены.")

    else:
        print('БАМ! БАМ! Такого задания не существует! Выберите другое или покиньте здание!')
    return()


def main():                                                     # Функция запуска кода и повтора
   again = 'да'
   while again.lower() == 'да':
      hello()
      again = input('Вы еще хотите проверить домашнее задание ? (Да = запустить еще раз, Любая клавиша = выйти из программы) \n' )


print('Добро пожаловать в домашнее задание!')                   # Вход в программу


if __name__ == "__main__":
    main()

print('Всегда рады Вам помочь! Досвидания.')