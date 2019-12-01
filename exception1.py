"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user():
    """
    Замените pass на ваш код
    """
    chat = [{'Вопрос': 'как дела?', 'Ответ': 'хорошо!'},{'Вопрос': 'что делаешь?', 'Ответ': 'программирую'}]
    print('Задай мне вопрос:') 
    question = input()
    for talk in chat:
        while question in talk['Вопрос']:
            try:
                print(talk['Ответ'])    
            except KeyboardInterrupt:
                question = input()
                print('Пока')  
                break
            
        
    
if __name__ == "__main__":
    ask_user()
