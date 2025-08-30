#Anagram: Every single character of a word is in another then it is anagram.
#cat and tac are anagrams.
#ram and sat are not anagrams.
#Case-1: If the lengths are not equal then they are not anagrams
#Case-2: If they have different characters then they are not anagrams.
s = 'Raman'
t = 'kanar'
def isAnagram( s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        x = set(s)
        y = set(t)
        dict_1 = {}
        dict_2 = {}
        
             
        #if the lengths are not equal it obsviously is not an anagram.
        if len(s) != len(t):
            return False
        #if the set of characters is itself is not equal then it is not an anagram, equal sets.
        elif x != y:
            return False
        else:
            for i in s:
                dict_1[i] = dict_1.get(i,0)+1
            for i in t:
                dict_2[i] = dict_2.get(i,0)+1
        if dict_1.items() == dict_2.items():
            return True
        else:
            return False
        
        #length is equal and constituents are the same indicating the 
print(isAnagram(s,t))