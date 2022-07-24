import _io
import re
       
def is_it_sentence(string):
    #Every sentence must begin with a capital letter.
    #At the end of the sentence, exclamation point, ellipsis, question mark and dot can be used.
    if(re.search('[A-Z|İ|Ü|Ğ|Ç|Ö|Ş]', string[0]) and re.fullmatch('.*[.|?|!|"|"|”|…|’]', string)):
        return True
    else:
        return False
def is_it_word(string):
    #A word should not consist of both numbers and letters, they can be found separately.
    #Words can start with capital letters or words can be uppercase, but no middle or trailing capital letters.
    for val in string.split(" "):
        if(re.search('[A-Z|İ|Ü|Ğ|Ç|Ö|Ş]+[a-z|i|ş|â|ç|ö|ğ|ü|ı]+[A-Z|İ|Ü|Ğ|Ç|Ö|Ş]+', val) or re.search('[a-z|i|ş|ç|ö|â|ğ|ü|ı]+[A-Z|İ|Ü|Ğ|Ç|Ö|Ş]+', val)):
            return False
        if(re.search('[A-Z|İ|Ü|Ğ|Ç|Ö|Ş] [A-Z|İ|Ü|Ğ|Ç|Ö|Ş]+[a-z|i|ş|ç|â|ö|ğ|ü|ı]+', val)):
            return False
        if(re.search('[a-zA-Z|i|ş|ç|ö|ğ|ü|ı|â|x|İ|Ü|Ğ|Ç|Ö|X|Ş]+[1-9]+', val) or re.search('[1-9]+[a-zA-Z|i|ş|ö|ğ|â|ü|ç|ı|x|İ|Ü|Ğ|Ç|Ö|X|Ş]+', val) ):
            return False
    return True
def numOfSentence(string):
    #In each line, there must be only one sentence. Multiple sentences should not be accepted.
    #the quotation marks and quotes must match.
    #This function returns the number of sentence
    line = string
    ctr = 0
    if(line[line.__len__()-1] == '"' or line[line.__len__()-1] == '’' ):
        ctr = ctr + 1
    line = re.sub('["].*["]', '', line)
    line = re.sub('[‘].*[’]', '', line)
    if(re.search('.*["|‘|’].*', line)):
        return False
    for val in line.split(" "):
        if(re.search('[.|?|!|…]', val)  ):
            ctr = ctr + 1
    return ctr
    
        
def do_punctiation_marks(line):
    #Sentences can contain punctuation marks such as quotes, quotation marks, colons;
    #There may be sentences between quotation marks and quotes.
    if(re.search('.*["].*["]', line)):
        list = line.split('"')[1]
        if(numOfSentence == False or numOfSentence(list) == 0 ):
            return False
        if ( is_it_sentence(list) == False ):
            return False
        if ( is_it_word(list) == False):
            return False
        if (do_punctiation_marks(list) == False):
            return False        
    if(re.search('.*[‘].*[’]', line)):
        list = line.split('‘')[1]
        list = list.split('’')[0]
        if(numOfSentence == False or numOfSentence(list) == 0  ):
            return False
        if ( is_it_sentence(list) == False ):
            return False
        if ( is_it_word(list) == False):
            return False
        if (do_punctiation_marks(list) == False):
            return False
    return True

        
        
        

outputStream = open("sentences_output.txt",'w',encoding='UTF-8')
with open("sentences.txt", 'r', encoding='UTF-8') as file:
    while (line := file.readline().rstrip()):
        if(numOfSentence == False or numOfSentence(line) != 1 ):
            outputStream.write("not valid\n")
            continue
        if ( is_it_sentence(line) == False ):
            outputStream.write("not valid\n")
            continue
        if ( is_it_word(line) == False):
            outputStream.write("not valid\n")
            continue
        if (do_punctiation_marks(line) == False):
            outputStream.write("not valid\n")
            continue
        outputStream.write("valid\n")
outputStream.close()
file.close()

        
        
        


        