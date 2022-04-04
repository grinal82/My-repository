documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }


def people():
    x = input('Введите номер документа: ')
    for element in documents:
      if element['number'] == x:
        return f'Документ с данным номером принадлежит - {element["name"]}'
    else:
      return 'Документа с данным номером у нас нет'


def shelf():
    y = input('Введите номер документа: ')
    for doc in directories.items():
        if y in doc[1]:
            return f'Документ с данным номером лежит на полке № - {doc[0]}'
    else:
        return 'Данного документа нет у нас на хранении'
           

def my_list():
    for z in documents:
        print(z['type'], z['number'], z['name'])
        

def add_document(documents, directories):
    doc_type = input('Введите тип документа: ')
    doc_number = input('Введите номер документа: ')
    name = input('Введите имя: ')
    extra_document = {}
    extra_document.setdefault('type', doc_type)
    extra_document.setdefault('number', doc_number)
    extra_document.setdefault('name', name)
    documents.append(extra_document)
    shelf_input = input('Введите номер полки: ')
    if shelf_input in list(directories.keys()):
        directories[shelf_input].append(doc_number)
        print('Документ добавлен на полку', shelf_input)
        print(f'Каталог документов: \n {documents}')
        print()
        print(f'Перечень полок: \n {directories}')
            
    else:
        directories.setdefault(shelf_input,[doc_number])
        print(f'Каталог документов: \n {documents}')
        print()
        print(f'Перечень полок: \n {directories}')
        
    
def main():
  while True:
    comand = input('Введите команду: ')
    if comand == 'p':
      print(people())
    elif comand == 's':
      print(shelf())
    elif comand == 'l':
      my_list()
    elif comand == 'a':
      add_document(documents,directories)
    

main()



# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.
# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, 
# имя владельца и номер полки, на котором он будет храниться. Корректно обработайте ситуацию, 
# когда пользователь будет пытаться добавить документ на несуществующую полку.