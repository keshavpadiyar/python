import sys

#Takes out some unnecessary characters   
def filter_words(text):
    words=[word.upper() for word in text.split()]
    for i in range(len(words)): 
        for ch in words[i]:
            if not(ch.isalpha()) and ch!=".":#Removes non alphabets
                words[i] = words[i].replace(ch,"")
            
    return words

#Increases the counter of a key in a dictionary, or initiates it to 1
def add_value_to_dict(key,dictionary):
    if key in dictionary.keys():
        dictionary[key]+=1
    else:
        dictionary[key]=1
    return dictionary

#Function which returns a dictionary of dictionaries containing information about the text document
def text_database(text):
    words = filter_words(text)
    
    alphabet_dict={}
    words_dict={}
    successor_dict={}
    
    for i in range(len(words)):
        if "." in words[i]:
            ending_word_flag=1
            words[i] = words[i].replace(".","")
         
        word=words[i]
        words_dict=add_value_to_dict(word,words_dict)
        
        for j in word:
            alphabet_dict=add_value_to_dict(j,alphabet_dict)
        
        
        if i != (len(words)-1):
            if word in successor_dict.keys() :
                successor_dict[word]=add_value_to_dict(words[i+1],successor_dict[word])
            else:
                successor_dict[word]={}
                successor_dict[word]=add_value_to_dict(words[i+1],successor_dict[word])
        #This section can be improved by ensuring that if full stop follows a word, there are no successors to that word
    
    
    alphabet_dict=dict(sorted(alphabet_dict.items(),key=lambda item: item[1],reverse=True))
    
    words_dict = dict(sorted(words_dict.items(),key=lambda item: item[1],reverse=True))
    most_common_words=list(words_dict.keys())[0:5]

    successors_five_words_dict={i:dict(sorted(successor_dict[i].items(),key=lambda item:item[1],reverse=True)[0:3]) for i in most_common_words}
    
    database={}

    database={"alphabet":alphabet_dict,"word":words_dict,"successors":successor_dict,"successors_five_words":successors_five_words_dict}
    
    return database
        
    


        
def output_database(text):

    database=text_database(text)
    
    if(len(sys.argv)>2):
        output_file=sys.argv[2]
        type_of_append="a"
        print("Hey! Since you have provided an output file, the information about the text document will be appended to that file \n")
        
    else:
        output_file="output.txt"
        type_of_append="w"
        print("Hey! Since you have not provided an output file, the information about the text document will be written to a new file called output.txt \n")
        
    with open(output_file,type_of_append) as file:
        file.write("Below, we have printed the information about the database \n \n")
        file.write("**********************************************************")
        file.write("\n \n \n")
        file.write("Frequency table of alphabetic letters \n")
        
        for key,value in enumerate(database["alphabet"].items()):
            file.write(str(key)+"\t"+str(value))
            file.write("\n")
        
        file.write("****************\n")
        
        file.write("Total number of words the text contains is "+ str(sum(database["word"].values()))+"\n")
        
        file.write("****************\n")
        
        file.write("We have converted every word to its uppercase and also removed non-alphabetic characters from each word \n")
        
        file.write("Number of Unique words that the text contains is "+str(len(database["word"]))+"\n")
        
        file.write("****************\n")
        
        file.write("The five most frequently occuring words along with the frequency: \n")
        
        for i in list(database["word"].keys())[0:5]:
            file.write(i+" ("+str(database["word"][i])+" occurences )"+"\n")
            for j in list(database["successors_five_words"][i].keys())[0:3]:
                file.write("--"+j+", "+ str(database["successors_five_words"][i][j])+"\n")
            file.write("\n")
                
        file.write("****************\n")
        file.write("Thank you! \n")      
        file.write("End of Document \n")
        
    
    print("Writing to the text document is complete! Now, printing the contents of the text document \n") 
    
    with open(output_file,"r") as file:
        for s in file.readlines():
            print(s)
        
    print("The program is ending now! Thank you!")
        
    


if __name__ == "__main__":
    if len(sys.argv)>1:
        try:
            with open(sys.argv[1], "r", encoding='utf-8') as file:
                text=file.read()
                output_database(text)
                
        except FileNotFoundError:
             print("Hello! The file you input was not found and hence this program will end now. Please check again and run this program")
    else:
        print("Kind madam/sir! No argument provided for the source text file! Please enter the argument as the text file to be summarized")
   