#!/usr/bin/env python
# coding: utf-8

# 1. Write a function that returns True if a given name can generate an array of
# words.
# Examples
# anagram(&quot;Justin Bieber&quot;, [&quot;injures&quot;, &quot;ebb&quot;, &quot;it&quot;]) ➞ True
# anagram(&quot;Natalie Portman&quot;, [&quot;ornamental&quot;, &quot;pita&quot;]) ➞ True
# anagram(&quot;Chris Pratt&quot;, [&quot;chirps&quot;, &quot;rat&quot;]) ➞ False
# # Not all letters are used
# anagram(&quot;Jeff Goldblum&quot;, [&quot;jog&quot;, &quot;meld&quot;, &quot;bluffs&quot;]) ➞ False
# # &quot;s&quot; does not exist in the original name
# 
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[1]:


def anagram(in_string,in_list):
    in_string_list = list(in_string.lower())
    in_string_list.remove(' ')
    not_exist_list = []
    output = False
    for item in in_list:
        for ele in item:
            if ele in in_string_list:
                in_string_list.remove(ele)
            else:
                not_exist_list.append(ele)
    if len(in_string_list) == 0 and len(not_exist_list) == 0:
        output = True
    print(f'anagram{in_string,in_list} ➞ {output}')
            
anagram("Justin Bieber", ["injures", "ebb", "it"])
anagram("Natalie Portman", ["ornamental", "pita"])
anagram("Chris Pratt", ["chirps", "rat"])
anagram("Jeff Goldblum", ["jog", "meld", "bluffs"])


# 2. Given an array of users, each defined by an object with the following
# properties: name, score, reputation create a function that sorts the array to
# form the correct leaderboard.
# The leaderboard takes into consideration the score of each user of course,
# but an emphasis is put on their reputation in the community, so to get the
# trueScore, you should add the reputation multiplied by 2 to the score.
# Once you know the trueScore of each user, sort the array according to it in
# descending order.
# Examples
# leaderboards([
# { &quot;name&quot;: &quot;a&quot;, &quot;score&quot;: 100, &quot;reputation&quot;: 20 },
# { &quot;name&quot;: &quot;b&quot;, &quot;score&quot;: 90, &quot;reputation&quot;: 40 },
# { &quot;name&quot;: &quot;c&quot;, &quot;score&quot;: 115, &quot;reputation&quot;: 30 },
# ]) ➞ [
# { &quot;name&quot;: &quot;c&quot;, &quot;score&quot;: 115, &quot;reputation&quot;: 30 }, # trueScore = 175
# { &quot;name&quot;: &quot;b&quot;, &quot;score&quot;: 90, &quot;reputation&quot;: 40 }, # trueScore = 170
# { &quot;name&quot;: &quot;a&quot;, &quot;score&quot;: 100, &quot;reputation&quot;: 20 } # trueScore = 140
# ]
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[2]:


def leaderboards(in_list):
    temp_dict = {}
    out_list = []
    for ele in in_list:
        temp_dict[(ele['reputation']*2)+ele['score']] = ele
    for ele in sorted(temp_dict.keys(),reverse=True):
        out_list.append(temp_dict[ele])
    print(f'leaderboards({in_list}) ➞ {out_list}')
    
leaderboards([
  { "name": "a", "score": 100, "reputation": 20 },
  { "name": "b", "score": 90, "reputation": 40 },
  { "name": "c", "score": 115, "reputation": 30 },
])


# 3. Create a function that, given a phrase and a number of letters guessed,
# returns a string with hyphens - for every letter of the phrase not guessed, and
# each letter guessed in place.
# Examples
# hangman(&quot;helicopter&quot;, [&quot;o&quot;, &quot;e&quot;, &quot;s&quot;]) ➞ &quot;-e---o--e-&quot;
# 
# hangman(&quot;tree&quot;, [&quot;r&quot;, &quot;t&quot;, &quot;e&quot;]) ➞ &quot;tree&quot;
# hangman(&quot;Python rules&quot;, [&quot;a&quot;, &quot;n&quot;, &quot;p&quot;, &quot;r&quot;, &quot;z&quot;]) ➞ &quot;P----n r----&quot;
# hangman(&quot;He&quot;s a very naughty boy!&quot;, [&quot;e&quot;, &quot;a&quot;, &quot;y&quot;]) ➞ &quot;-e&quot;- a -e-y -a----y –y!&quot;
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[3]:


def hangman(in_string,in_list):
    out_string = ''
    for ele in range(len(in_string)):
        if in_string[ele].lower() in in_list:
            out_string += in_string[ele]
        elif in_string[ele] in '"! ':
            out_string += in_string[ele]
        else:
            out_string += '-'
    print(f'hangman{in_string,in_list} ➞ {out_string}')
        
hangman("helicopter", ["o", "e", "s"])
hangman("tree", ["r", "t", "e"])
hangman("Python rules", ["a", "n", "p", "r", "z"])
hangman("He\"s a very naughty boy!", ["e", "a", "y"])


# 4. The Collatz sequence is as follows:
# - Start with some given integer n.
# - If it is even, the next number will be n divided by 2.
# - If it is odd, multiply it by 3 and add 1 to make the next number.
# - The sequence stops when it reaches 1.
# According to the Collatz conjecture, it will always reach 1. If that&#39;s true, you
# can construct a finite sequence following the aforementioned method for any
# given integer.
# Write a function that takes in an integer n and returns the highest integer in
# the corresponding Collatz sequence.
# Examples
# max_collatz(10) ➞ 16
# # Collatz sequence: 10, 5, 16, 8, 4, 2, 1
# max_collatz(32) ➞ 32
# # Collatz sequence: 32, 16, 8, 4, 2, 1
# max_collatz(85) ➞ 256
# # Collatz sequence: 85, 256, 128, 64, 32, 16, 8, 4, 2, 1
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[4]:


def max_collatz(in_num):
    out_list = []
    out_list.append(in_num)
    temp_in_num = in_num
    while True:
        if temp_in_num%2 == 0:
            temp_in_num /= 2
        else:
            temp_in_num = (temp_in_num*3)+1
        out_list.append(int(temp_in_num))
        if temp_in_num ==1:
            break
            
    x= str(out_list)
    print(f'max_collatz({in_num}) ➞ {max(out_list)}')

max_collatz(10)
max_collatz(32)
max_collatz(85)


# 5. Write a function that sorts a list of integers by their digit length in
# descending order, then settles ties by sorting numbers with the same digit
# length in ascending order.
# Examples
# digit_sort([77, 23, 5, 7, 101])
# ➞ [101, 23, 77, 5, 7]
# digit_sort([1, 5, 9, 2, 789, 563, 444])
# ➞ [444, 563, 789, 1, 2, 5, 9]
# digit_sort([53219, 3772, 564, 32, 1])
# 
# ➞ [53219, 3772, 564, 32, 1]
# 
# 
# 
# 
# 
# 
# Ans:-

# In[5]:


def digit_sort(in_list):
    max_len = len(str(max(in_list)))
    output = []
    for item in range(max_len,0,-1):
        temp = []
        for ele in in_list:
            if len(str(ele)) == item:
                temp.append(ele)
        output.extend(sorted(temp))
    print(f'digit_sort({in_list}) ➞ {output}')
    
digit_sort([77, 23, 5, 7, 101])
digit_sort([1, 5, 9, 2, 789, 563, 444])
digit_sort([53219, 3772, 564, 32, 1])

