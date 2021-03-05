import text_stats as ts
import sys
import random

def gen_text(text,word,max_length):
    print("Welcome to the Markovian Random World\n")
    print("In this world, all you need is one word \n")
    print("From the first word, the second word is generated and so on till we reach max_length\n")
    word=word.upper()
    
    counter=0
    db=ts.text_database(text)
    
    if word not in db["word"].keys():
        print("Sorry kind Madam/Sir, This word does not appear to be present in the text document you entered")
        print("Exiting")
        return 
    word_list=[]
    word_list.append(word)
    while True:
        next_word=random.choices(list(db["successors"][word].keys()),weights=db["successors"][word].values())[0]
        word_list.append(next_word)
        word=next_word
        counter=counter+1
        if counter>=max_length:
            print("\n \n Quitting because we have reached our limit \n")
            break
        elif len(db["successors"][word])==0:
            print("\n \n Quitting because the word we reached ends the markovian circuit, as there are no successors \n")
            break
            
    a=' '.join(word_list)
    print(a)
    print("Writing all this random text into a Text file\n")
    with open("generate.txt","w") as f:
        f.write(a)
    
    print("\n Exiting Markovian World")
    
    
    

if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv)>=4:
        try:
            with open(sys.argv[1], "r", encoding='utf-8') as file:
                text=file.read()
                word=sys.argv[2]
                max_length=int(sys.argv[3])
                gen_text(text,word=word,max_length=max_length)
                
        except FileNotFoundError:
             print("The file was not found and hence this program will end now. Please check again")
    else:
        print("Not enough arguments provided! Please check and input three arguments: text file, the starting word and then how many random words to be generated")
