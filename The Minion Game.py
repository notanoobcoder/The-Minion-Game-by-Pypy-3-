#!/usr/bin/env python
# coding: utf-8

# In[4]:


#A simple two-player game, "The Minion Game", in which the name of the players are Kevin and Stuart
#Game Rules: Both players are given the same string. 
#Both players have to make substrings using the letters of the string. 
#Stuart has to make words starting with consonants. Kevin has to make words starting with vowels. 
#The game ends when both players have made all possible substrings. 
#Scoring A player gets +1 point for each occurrence of the substring in the string.
#Th game could be played 10 times t once.
def minion_game(string):
    vowels = 'AEIOU'

    kevsc = 0
    stusc = 0
    
    for i in range(len(s)):
        if string[i] in vowels:
            kevsc += (len(string)-i)
        else:
            stusc += (len(string)-i)

    if kevsc > stusc:
        print("Kevin", kevsc)
    elif kevsc < stusc:
        print("Stuart", stusc)
    else:
        print("Draw")

if __name__ == '__main__':
    for i in range(0,10):
        s = input()
        minion_game(s)


# In[ ]:





# In[3]:


def minion_game(string):

    vowels = 'AEIOU'

    kevsc = 0
    stusc = 0
    for i in range(len(s)):
        if string[i] in vowels:
            kevsc += (len(string)-i)
        else:
            stusc += (len(string)-i)

    if kevsc > stusc:
        print("Kevin", kevsc)
    elif kevsc < stusc:
        print("Stuart", stusc)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)


# In[ ]:




