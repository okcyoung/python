def wordcounter(filename,n):
    #this function will read in a filename , and return a dictionary
    #of the word count for each word in the file
    
    with open(filename,'r') as f:
        words=f.read()
        words=words.lower()
        #clean_words="".join(c for c in words if c not in string.punctuation)
        my_punctuation="".join(chr(i) for i in range(33,127) if not chr(i).isalnum())
        table= str.maketrans('','',my_punctuation)
        clean_words=words.translate(table)
        #for c in my_punctuation:
        #   clean_words=words.replace(c," ")
        
        
        clean_words=clean_words.split()
        
        word_counter={}
        for word in clean_words:
            word_counter[word]=word_counter.get(word,0)+1

    #print(word_counter)
        word_counter=list(word_counter.items())
        word_counter.sort()
        word_counter.sort(key = lambda x : x[1], reverse=True)
        #print(word_counter)
        print(f"***Top  {n}  words***")
        for i in range(n):
            word, count=word_counter[i]
            
            print(f"{word} encountered {count} times")