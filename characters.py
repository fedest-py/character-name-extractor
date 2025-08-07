#******************************************************************************
# characters.py
#******************************************************************************
#Eduardo E
#


#open story to read
story = open('story.txt', 'r')

read_story = story.read()
#turn it into a list
broken_story = read_story.split()

words_in_story = len(broken_story)

characters = []


for word in range(words_in_story):
    check_word = str(broken_story[word])
    #the first letter has to be uppercase
    condition = check_word[0].isupper()
    if word >= 1:
        word_before = str(broken_story[word -1])
        #The last letter of the word before
        end = word_before[-1]     
        #exclude I's
        not_i = broken_story[word] != 'I'
        #not consecutive to punctuation
        not_end_sentence = end != '.' and end != '!' and end != '?' and end != ',' and end != '"'
        if not_i and not_end_sentence and condition:
            characters.append(broken_story[word])
            
print(characters)

story.close()


        







