word_list = ["aardvark","baboon","camel"]
lives = 4
import random
ans = random.choice(word_list)
#print(ans,word_list)
ans1 = []
for i in ans:
    ans1.append('_')
print(ans1)
while lives>0 and '_' in ans1:
    #print(lives,ans1)
    char = input("enter a letter")
    if char in ans:
        for i in range(len(ans)):

            if char == ans[i]:
                #print('h')
                ans1[i]=char
        j=''
        for i in ans1:
            j+=i
        print(j)

        
    else:
        lives = lives-1
if '_'in ans1:
    print('game over you lost')
else:
    print('you guessed the word correctly you won')