import random


def main():
    tmp = {'school_class':'' ,'scores': ''}
    clas = ['a','б','в']
    school_score = []
    for i in range (5):
        tmp['school_class'] = str(random.randint(1,5))+random.choice(clas)
        tmp['scores'] = [random.randint(1,5),random.randint(1,5),random.randint(1,5)]
    
        school_score.append(tmp)
        tmp={}

    SUM_I = 0
    SUM_I_2 = 0
    COUNT_I = 0
    COUNT_I_2 = 0

    for chel in school_score:
        for i in chel['scores']:
            SUM_I += i
            SUM_I_2 += i
            COUNT_I += 1 
            COUNT_I_2 += 1
            chel['Средний балл в классе'] = round(SUM_I_2 /  COUNT_I_2,1)      
        
        SUM_I_2 = 0   
        COUNT_I_2 = 0 

    print(school_score) 
    print('Средний балл по всей школе: ',round(SUM_I/COUNT_I,1))

    
if __name__ == "__main__":
    main()
 