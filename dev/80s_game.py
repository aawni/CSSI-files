pos_list=["Name","A Weird Hobby", "Same Name", "Place", "Same Name", "Random Clothing Item", "Crazy Action", "Drink", "Same Name", "Same Place", "Monster", "Super Power", "Same Monster", "Animal", "Same Monster", "Dance Move", "Same Drink"]
counter=0
for pos in pos_list:
    if(counter==0):
        user_input= raw_input("This is a madlibs! Please enter a " + pos + ": ")
    else:
        user_input= raw_input("Please enter a " + pos + ": ")
    pos_list[counter]= user_input
    counter+=1






print "Once upon a time there was a person whose name was %s he/she was a peculiar individual. That liked to do %s in their spare time. In fact %s lived  in a %s where he/she could do it everyday. BUT today was different. %s wanted to get turnt! So he/she took off his/her %s and swung it around while %s needless to say this was not enough to satisfy his/her turnt needs so he/she drank 18 cans of %s. unfortunately %s realized that he/she needed to go to %s and finish Oren's Collatz Conjecture code. In the midst of writing his/her  code he/she  was attacked by the wiggly wild %s and forced to unleash his crazy ninja %s. The %s would not stop attacking him/her! So he started screaming like a %s but the %s still chased him/her! Suddenly, He/She came up with an idea: how about I %s  my way out of this! Right before he/she started dancing, Larry Page ascended from the heavens and saved him/her. He/she woke up at his/her computer in the middle of the street. Moral of story : dont drink %s." %tuple(pos_list)
