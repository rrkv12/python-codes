from __future__ import print_function, division
import time

def word_list1():

    t= []
    fin=open('word.txt')
    for line in fin:
        word = line.strip()
        t.append(word)
    return t
def word_list2():

    t=[]
    fin = open('word.txt')
    for line in fin:
        word = line.strip()
        t=t+[word]
    return t

start_time = time.time()
t = word_list1()
elapsed_time = time.time() - start_time
print(len(t))
print(t[:10])
print(elapsed_time, 'seconds')

start_time = time.time()
t=word_list2()
elapsed_time = time.time() - start_time

print(len(t))
print(t[:10])
print(elapsed_time, 'seconds')
