with open('referat.txt','r',encoding='utf-8') as f:
    content = f.read()
    #print(content)
    #print(len(content))
    count_words = 0
    for letter in content:
        if letter == ' ' or letter == '\n':
            count_words += 1 
        
        if letter == '.':
            content = content.replace('.','!')
    print(count_words-1)
    #print(content)
    file_for_write = open('referat2.txt','w')
    file_for_write.write(content)
    file_for_write.close()