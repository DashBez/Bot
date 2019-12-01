"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
import random


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    pass
    
if __name__ == "__main__":
    main()

SUM_I = 0
SUM_I_2 = 0
SUM_I_3 = 0
COUNT_I = 0

# заполняем словарь рандомными значениями 
tmp = {'school_class':'' ,'scores': '','sum_scores':''}
clas = ['a','б','в']
school_score = []
for i in range (5):
    tmp['school_class'] = str(random.randint(1,5))+random.choice(clas)
    tmp['scores'] = [random.randint(1,5),random.randint(1,5),random.randint(1,5)]
    tmp['sum_scores'] = 0 
    
    school_score.append(tmp)
    tmp={}

name_class = set()

for chel in school_score:
    name_class.add(chel['school_class'])

#рассчитываем среднее ар балл
for chel in school_score:
    for i in chel['scores']:
        SUM_I += i
        SUM_I_2 += i
        SUM_I_3 += i
        COUNT_I += 1 
        chel['sum_scores'] = SUM_I_2          
        
    SUM_I_2 = 0    

print(school_score)


print('Средний балл по всей школе: ',round(SUM_I/COUNT_I,1))
SUM_I = 0
COUNT_I = 0

print(name_class)

name_class = list(name_class)
count_name = 0
name_avg_score = {'name class':'','avg_score': 0, 'count_name':0}  
school = []
sum_1 =0
for chel in school_score:
    for i in range(0,4):
        if chel['school_class'] == name_class[i]:
            name_avg_score['count_name'] = sum_1+1
            if name_avg_score['count_name'] == 1:
                name_avg_score['name class'] = name_class[i]
                name_avg_score['avg_score'] = chel['sum_scores']
                school.append(name_avg_score)
            else:
                name_avg_score['name class'] = name_class[i]
                name_avg_score['avg_score'] = chel['sum_scores'] +1
                school.append(name_avg_score)
        name_avg_score = {}    

    i = 0
print(school)

"""

name_class = set()
name_avg_score = {'name class':'','avg_score': 0}  
school = []


for chel in scool_score:

        name_avg_score['avg_score'] = chel['sum_scores']

        school.append(name_avg_score)
        name_avg_score = {}

        

print(school)



name_avg_score['name class'] = name_class
name_avg_score['avg_score'] = {}

for chel in scool_score:
    if chel['school_class'] in name_class:
        name_avg_score['avg_score'] += chel['avg_score']
    else:
        name_avg_score['avg_score'] = chel['avg_score']


print(name_avg_score)

for chel in scool_score:
    if chel['school_class'] in name_class:
        score.add (chel['avg_score'])
    else:
        name_class.add(chel['school_class'])
        score.add(chel['avg_score'])




print(score)





#среднее ар в разрезе каждого класса
#tmp_CLAS_I = {'name_clas': '','avg_ar': ''}
tmp_CLAS_I = {}
CLAS_I = []

for chel in scool_score:
    tmp_CLAS_I['name_clas']=chel['school_class']
    for i in chel['scores']:
        SUM_I += i
        COUNT_I += 1 

    tmp_CLAS_I['avg_ar']=SUM_I
    CLAS_I.append(tmp_CLAS_I)

    SUM_I = 0
    COUNT_I = 0
    tmp_CLAS_I = {}

print(CLAS_I)

tmp_set=set ()

for i in CLAS_I:
    tmp_set.add(i['name_clas'])

sum_clas=0
clas_1 = {}
for i in CLAS_I:
    for tmp_set_obj in tmp_set:
        clas_1['name_clas_1']=tmp_set_obj
        if i['name_clas'] == tmp_set_obj:
            sum_clas+=i['avg_ar']
            clas_1['avg_ar_1']=sum_clas
            
print(clas_1)

"""




