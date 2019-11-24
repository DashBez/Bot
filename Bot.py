def get_summ(one,two,delimiter='&'):
    result=str(one)+delimiter+str(two)
    return(str.upper(result))


print(get_summ('Learn','Python'))
print(get_summ(1,2))

