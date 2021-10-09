import random
word_list = ["funny","young", "acceptable", "proportional", "cultured", "apple",
            "debt", "amount", "head", "pencil", "literature", "title", "example", "tickle"]
word = random.choice(word_list)

lst = []
lives = 10
cnt = 0

while cnt < lives:
    a = ""
    for i in word:
        a+="_"
    print(a)
    ltr = str(input("Enter a letter: "))

    ## direct guess 
    if ltr == word:
        print("congrats u won")
        break

    ## hangman starts
    else:
        if ltr not in word:
            lives-=1
        lst.append(ltr)

        ## constructing word's structure 
        guess = ""
        for i in word:
            if i in lst:
                guess+=i
            else:
                guess+="_"

        ## game interface 
        if guess == word:
            print("\n"+word,"\ncongrats u won")
            break
        elif lives ==0:
            print("u lost, the word was",word)
        else:
            print(guess)
            print("u have",lives,"lives now\n")
                
