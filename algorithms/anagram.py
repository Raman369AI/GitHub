#Anagram: Every single character of a word is in another then it is anagram.
#cat and tac are anagrams.
#ram and sat are not anagrams.
s = 'Raman'
t = 'kanar'
def isAnagram( s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        x = list(s)
        y = list(t)
        dict_1 = {}

        if len(s) != len(t):
            return False
        elif x != y:
            return True
print(isAnagram(s,t))