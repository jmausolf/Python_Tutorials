def words(text, k=10, r=0, sw=0):
    """This functions returns all alphabetic words of
        a specified length for a given text.
        
    Defaults, k=10 and r=0, sw=0.
    -------------------------------------------------    
    - k = the length of the word. 
    -------------------------------------------------
    - r = the evaluation option. 
        It takes values 0 (the default), 1, or 2.
        0. "equals" | len(word) == k
        1. "less than" | len(word) < k.
        2. "greater than" | len(word) > k.
    -------------------------------------------------
    - sw = stop words (English)
        Stop words are high-frequency words like 
        (the, to and also, is), among others.
        
        In this function, sw takes values
        0 (the default) or 1. 

        The function prints an exception 
        statement if other values are entered.
        
    -------------------------------------------------
    """  

    #Not Accounting for Stopwords
    if sw == 0:
        #Option to Return Words == K
        if r == 0:
            ucw = [w.lower() for w in text if w.isalpha() and len(w) == k ]
            return ucw

        #Option to Return Words < K
        elif r == 1:
            ucw = [w.lower() for w in text if w.isalpha() and len(w) < k ]
            return ucw

        #Option to Return Words > K
        elif r == 2:
            ucw = [w.lower() for w in text if w.isalpha() and len(w) > k ]
            return ucw
        else:
            pass
    
    elif sw == 1:
        #Option to Return Words == K
        if r == 0:
            ucw = [w.lower() for w in text if w.lower() not in stopwords.words('english') \
                   and w.isalpha() and len(w) == k]
            return ucw

        #Option to Return Words < K
        elif r == 1:
            ucw = [w.lower() for w in text if w.lower() not in stopwords.words('english') \
                   and w.isalpha() and len(w) < k]
            return ucw

        #Option to Return Words > K
        elif r == 2:
            ucw = [w.lower() for w in text if w.lower() not in stopwords.words('english') \
                   and w.isalpha() and len(w) > k]
            return ucw
        else:
            pass
    
    else:
        print ("Please input a valid stopwords option: 0 = no, 1 = yes")

def freq_words(text, k=10, r=0, n=20, sw=0):
    """This function uses the words function to 
        generate a specified frequency distribtion,
        of the most frequent words and related graph.
        
        You can specify word length, an equality option
        (to look for words =, >, or <) a given length.
        
        You can specify how many words to return and
        if you want to exclude stopwords.
        
    Defaults, k=10 and r=0, n=20, sw.
    -------------------------------------------------    
    - k = the length of the word. 
    -------------------------------------------------
    - r = the evaluation option. 
        It takes values 0 (the default), 1, or 2.
        0. "equals" | len(word) == k
        1. "less than" | len(word) < k.
        2. "greater than" | len(word) > k.
    -------------------------------------------------
    - n = the number of most common results. 
        The default value is 20. For example, if you
        want to see the top 100 results, input 100.
    -------------------------------------------------
    - sw = stop words (English)
        Stop words are high-frequency words like 
        (the, to and also, is), among others.
        
        In this function, sw takes values
        0 (the default) or 1. 

        The function prints an exception 
        statement if other values are entered.
        
    -------------------------------------------------
    """        
    
    #Generate the Frequency Distribution for specified text, k, and r. 
    fdist = FreqDist(words(text, k, r, sw))
    
    #Clean up the Title of the Text
    clean_title0 = str(text).replace("<Text: ", "").replace(">", "").replace('[', '').replace(']', '')
    clean_title1 = clean_title0.replace("'", '').replace('"', '').replace(',', '')[0:10]+"..."
    try:
        c2 = clean_title1.split(" by ")[0].title()
    except:
        c2 = clean_title0.title()
    
    #Creating Possible Titles
    figtitle1 = "Most Frequent "+str(k)+"-Letter Words in "+c2
    figtitle2 = "Most Frequent Words Less Than "+str(k)+"-Letters in "+c2
    figtitle3 = "Most Frequent Words Greater Than "+str(k)+"-Letters in "+c2
    figtitle4 = "Most Frequent Words of Any Length "+c2
    figelse = "Most Frequent Words in "+c2
    
    #Setting the Title Based on Inputs

    if r == 0:
        figtitle = figtitle1
    elif r == 1:
        figtitle = figtitle2
    elif r == 2 and k != 0:
        figtitle = figtitle3
    elif r == 2 and k == 0:
        figtitle = figtitle4
    else:
        print ("else")
        figtitle = figelse

    #Print Plot and Most Common Words
    fdist.plot(n, title=figtitle, cumulative=True)
    print (figtitle+":", '\n', fdist.most_common(n))
    if sw == 1:
        print ("*NOTE: Excluding English Stopwords")
    else:
        pass



