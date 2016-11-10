# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%
#testing
# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text
print("START*******")
# code developed by Jackie Cohen; revised by Paul Resnick
# further revised by Colleen van Lent for Python3
import nltk # requires some downloading/installing dependencies to use all its features; numpy is especially tricky to install
import random
from nltk.book import text2
from nltk import word_tokenize,sent_tokenize


params =  text2[:151]

debug = False #True
if debug:
  print ("Getting information from file madlib_test.txt...\n")

tagged_tokens = nltk.pos_tag(params)

tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective", "VBD":"a past tense verb"} #added past tense verbs
substitution_probabilities = {"NN":.15,"NNS":.1,"VB":.1,"JJ":.1, "VBD":.1} #assign new percentages

def spaced(word):
  if word in [",", ".", "?", "!", ":"]:
    return word
  else:
    return " " + word

print("".join([spaced(word) for word in params])) #1 printing out 150 tokens of the original text 

final_words = []

for (word, tag) in tagged_tokens:
  if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
    final_words.append(spaced(word))
  else:
    new_word = input("Please enter %s:\n" % (tagmap[tag]))
    final_words.append(spaced(new_word))


print (''.join(final_words))
print("\n\nEND*******")

