file = open('./test.txt')
#open our file and store it

word_counts = {}
#creating an empty dictionary

for line in file: #when using a file we iterate by lines

     #removing the white space
    words = line.split() #we are separating each word in line
    
    for word in words: #looping through a dicitonary
        word_counts[word] = word_counts.get(word, 0) + 1 #counting the word
       
print (word_counts)
            
