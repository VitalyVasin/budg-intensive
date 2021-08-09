"""
Что будет выведено после выполнения кода? Почему?
"""


def transmit_to_space(message):
   
    def data_transmitter():        
        print(message)

    data_transmitter()


print(transmit_to_space("Test message"))

"""
После выполнения кода будет выведено "Test message", и на следующей строке "None".
"Test message" выводится ввиду того, что в ходе выполнения функции transmit_to_space начинает выполняться функция 
data_transmitter, а далее функция print (строка 9) не обнаружив переменной message внутри себя, интерпретатор выполняет 
поиск переменной на один шаг выше, то есть в функции transmit_to_space, там интерпретатор находит message и выводится 
функцией print (9 строка).
Так как функция transmit_to_space не возвращает никакого значения, то функция print (14 строка) выводит None
"""