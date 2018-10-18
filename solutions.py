vowel_list = ["a", "e", "i", "o", "u","A", "E", "I", "O", "U",]

def find_prefix(word):
    """find_prefix is a helper function that takes a word and
    returns a substring containing the first letters of the
    word before it hit a vowel. Will return empty string
    if the word start with a vowel"""
    substring = ""
    for char in word:
        if char in vowel_list:
            return substring
        else:
             substring += char
             return ""

def reverse_stem(word):
     """the helper function 'reverse_stem' take one argument (str) and
     will return the reversed word. The reversed word is the
     initial prefix found with the function 'find_prefix'
     removed frof the word and put at the end"""
     reversed_word = ""

     prefix = find_prefix(word)
     stem = word.replace(prefix,"")#Remove the prefix of the word
     reversed_word = stem + prefix


     return reversed_word

def pig_latin_word(word):

    result = ""
    pyg = 'ay'

  
    PUNCTUATION = ['.',',','!','?']
    end = ""
    if len(word) > 0:

        if word[-1] in PUNCTUATION:
             end += word[-1]
             word = word[:-1]

             first = word [0]
             new_word_vowel = word + 'way'
             new_word_consonant = reverse_stem(word) + pyg
   
                if first in vowel_list :
                     result = new_word_vowel+end
   
                else:
                     result = new_word_consonant+end
   
         else:
             result = word

    return result

def pig_latin_sentence(eng_sentence):
     word_list = eng_sentence.split(" ")

     pigword_list = []

     for word in word_list:
         pigword_list.append(pig_latin_word(word))

         return " ".join(pigword_list)


def pig_latin_translator():
    print "Enter the English sentence:"
    sentence = raw_input("")
    print "In Pig Latin: " + pig_latin_sentence(sentence)
    yes = 'y'
    no = 'n'
    while True:
        print "Do another? [y/n] "   
        inp = raw_input("")
        if inp is yes:
            print "Enter the English sentence:"
            sentence = raw_input("")
            print "In Pig Latin: " + pig_latin_sentence(sentence)
        elif inp is no:
            print "Goodbye!"
            break
        else :
            continue
   
 if __name__ == "__main__":
     pig_latin_translator()
