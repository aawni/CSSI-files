# countries = ["Chad",
# "Cuba",
# "Greenland",
# "Iraq",
# "Mali",
# "Oman",
# "India"]
# countries.append("Fiji")
# countries.insert(4, "Iran")
# del countries[-1]
# countries.reverse()
# countries[2]="Togo"
# countries.append("Laos")
# countries.reverse()
# countries.insert(0,"Peru")
#
#
def find_most_steps():
    current_most_steps=0
    num_with_most_steps=1
    for num in range(1,1000001):
        orig_num=num
        counter=0
        while num!=1:
            if num%2==0:
                num=num/2
            else:
                num=num*3+1
            counter+=1
        if counter>current_most_steps:
            current_most_steps=counter
            num_with_most_steps=orig_num

#    return "Largest amount of steps: %i"%(current_most_steps)
    return "Largest amount of steps: %i Num that took most steps: %i"%(current_most_steps, num_with_most_steps)

print find_most_steps()
#
# words = ["Mary", "had", "a", "little", "lamb"]
# words.reverse()
# i=0
# for word in words:
#     word=word[::-1]
#     words[i]=word
#     i+=1
# print words
#
#
#
# some_numbers =[2, 52, 19, 46, 1000]
# for num in some_numbers:
#     num= (num+10)/20
#     print num

# for i in range(10,0,-1):
#     print str(i)+" bottle of milk on the wall"
