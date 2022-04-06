'''
This small development program can be run to parse the sentences for Homework 3.
You may either run this as a stand-alone python program or copy it to jupyter notebook.
In either case, it must be in the same directory as the sentences and the grammar.
'''

import nltk

# read the sentences from the file sentences.txt
sentfile = open('sentences.txt', 'r')
# make a list of sentences, separating the tokens by white space.
sentence_list = []
for line in sentfile:
    sentence_list.append(line.split())

# read the grammar file - the nltk data function load will not reload
#    the file unless you set the cache to be False
camg = nltk.data.load('file:camelot_grammar.cfg', cache=False)

# create a recursive descent parser
cam_parser = nltk.RecursiveDescentParser(camg)
count = 1 
# for each sentence print it and its parse trees
# if the grammar cannot parse a sentence, sometimes it gives an error and
#    sometimes it just goes on to the next sentence with no parse tree
for sent in sentence_list:
    print('\n')
    print(count , '): ',sent)
    for tree in cam_parser.parse(sent):
        print (tree)
    count+=1

print('\n')
print("2 Challenge sentences: ")
csent = open('challenge.sentences.txt', 'r')
c_list = []
for line in csent:
    c_list.append(line.split())
    
c_list_2 = []
c_list_2.append(c_list[5])
c_list_2.append(c_list[10])

for sent2 in c_list_2:
    print('\n')
    print(sent2)
    for tree2 in cam_parser.parse(sent2):
        print (tree2)
 
    
p1 = 'the Britons were riding to the castle .'
p2 = '5,000 and unable castle to coconuts are !' 
print("\n Part B : no parsing")
l1 = p1.split()
print(l1,"\n TREE :")
for t1 in cam_parser.parse(l1):
    print (t1)

print("\n Part B : random parsing")
l2 = p2.split()
print(l2,"\n TREE :")
for t2 in cam_parser.parse(l2):
    print (t2)
    