"""
На прошлой неделе мы сжимали строки, используя кодирование повторов.
Теперь нашей задачей будет восстановление исходной строки обратно.

Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования повторов,
и производит обратную операцию, получая исходный текст.

Запишите полученный текст в файл и прикрепите его, как ответ на это задание.

В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.

Примечание. Это первое задание типа Dataset Quiz. В таких заданиях после нажатия "Start Quiz" у вас появляется ссылка
"download your dataset". Используйте эту ссылку для того, чтобы загрузить файл со входными данными к себе на компьютер.
Запустите вашу программу, используя этот файл в качестве входных данных.
Выходной файл, который при этом у вас получится, надо отправить в качестве ответа на эту задачу.

Sample Input:

a3b4c2e10b1

Sample Output:

aaabbbbcceeeeeeeeeeb
"""

with open('dataset_3363_2(1).txt', 'r') as my_f:
    s1 = my_f.readline().strip()
print(s1)
for el, sym in enumerate(s1):
    if 'a' <= sym <= 'z' or 'A' <= sym <= 'Z':
        sym_own = sym
        sym_num = ''
    if '0' <= sym <= '9':
        sym_num += sym
    if el+1 > len(s1)-1 or 'a' <= s1[el+1] <= 'z' or 'A' <= s1[el+1] <= 'Z':
        for i in range(int(sym_num)):
            with open('out_1.txt', 'a') as my_of:
                my_of.write(sym_own)
