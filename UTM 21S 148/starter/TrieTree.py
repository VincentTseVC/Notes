from TrieNodeAbstract import TrieNodeAbstract
from ChildrenDictionary import ChildrenDictionary
import math
from typing import Dict, List, Union
# For help in traversing children
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


class TrieTree(TrieNodeAbstract):
    def __init__(self, char='', value: str = ''):
        '''
        Initializes:
            This node's char, `self._char`, ie. your current character in the key
            This node's set of subtrees, 'children', using a dictionary
            This node's value, `self._value`  only set iff its a valid word in the dictionary
        '''
        self._value = value
        self._children: ChildrenDictionary = ChildrenDictionary()
        self._char = char

    # TASK 1
    def insert(self, word: str) -> None:
        '''
        Insert your new word, keep in mind, you must insert all child nodes
        >>> trie = TrieTree()
        >>> trie.insert("word")
        >>> trie.insert("water")
        >>> trie.insert("banana")
        >>> "word" in str(trie)
        True
        >>> "water" in str(trie)
        True
        >>> "bob" in str(trie)
        False
        >>> "banana" in str(trie)
        True
        '''
        curr = self
        for ch in word:
            if ch not in curr._children:
                curr._children[ch] = TrieTree(ch)
            
            curr = curr._children[ch]

        curr._value = word
            
    # TASK 2

    def __contains__(self, key: str):
        '''
        Returns True iff key is in tree, otherwise False
        >>> trie = TrieTree()
        >>> trie.insert("word")
        >>> "word" in trie
        True
        >>> "other" in trie
        False
        '''
        
        curr = self
        for ch in key:
            if ch not in curr._children:
                return False
            curr = curr._children[ch]
        return curr._value == key
            

    def helper(self, word, i):

        if i == len(word):
            # word not in trie
            if not self._value:
                return False

            self._value = ''
            return len(self._children) == 0

        ch = word[i]
        # word not in tire
        if ch not in self._children:
            return False

        need_to_del = self._children[ch].helper(word, i + 1)
        if need_to_del:
            self._children.pop(ch)
            return len(self._children) == 0

        # current node still has other chars
        return False

    # TASK 3
    def __delitem__(self, key: str):
        '''
        Deletes entry in tree and prunes unecessary branches if key exists, otherwise changes nothing
        >>> trie = TrieTree()
        >>> trie.insert("word")
        >>> "word" in trie
        True
        >>> del trie["word"]
        >>> "word" in trie
        False
        >>> str(trie)
        'TrieTree'
        >>> trie.insert('ab')
        >>> trie.insert('abs')
        >>> str(trie)
        'TrieTree\\n   `- a\\n      `- b : ab\\n         `- s : abs'
        >>> del trie['ab']
        >>> str(trie)
        'TrieTree\\n   `- a\\n      `- b\\n         `- s : abs'
        '''
        # key not exists, do nothing
        # if not self.__contains__(key):
        #     return

        # curr = self
        # for ch in key:
        #     next = curr._children[ch]
        #     if len(curr._children[ch]._children) <= 1:
        #         del curr._children[ch]
        #     curr = next

        return self.helper(key, 0)



        
            


    # TASK 4
    def sort(self, decreasing=False):
        '''
        Returns list of words in tree sorted alphabetically
        >>> trie = TrieTree()
        >>> trie.insert('banana')
        >>> trie.insert('cherry')
        >>> trie.insert('apple')
        >>> trie.sort()
        ['apple', 'banana', 'cherry']
        >>> trie.sort(decreasing=True)
        ['cherry', 'banana', 'apple']
        '''

        lst = []
        if self._value:
            lst.append(self._value)
        
        for child in self._children.values():
            lst += child.sort(decreasing)
        lst.sort(reverse=decreasing)
        return lst



    # TASK 5
    def autoComplete(self, prefix, N=10):
        '''
        if given a valid prefix, return a list containing N number of suggestions starting with that prefix in alphabetical order
        else return an empty list
        >>> trie = TrieTree()
        >>> trie.insert('apple')
        >>> trie.insert('dad')
        >>> trie.insert('apples')
        >>> trie.insert('application')
        >>> trie.insert('app')
        >>> trie.insert('about')
        >>> trie.autoComplete('a')
        ['about', 'app', 'apple', 'apples', 'application']
        >>> trie.autoComplete('a', N=2)
        ['about', 'app']
        >>> trie.autoComplete('app')
        ['app', 'apple', 'apples', 'application']
        >>> trie.autoComplete('c')
        []
        >>> trie.autoComplete('d')
        ['dad']
        '''
        curr = self
        for ch in prefix:
            if ch in curr._children:
                curr = curr._children[ch]
            else:
                return []
        
        return curr.sort()[:N]
    
 
    def editDistance(self, str1, str2, m, n):
 
        # If first string is empty, the only option is to
        # insert all characters of second string into first
        if m == 0:
            return n
    
        # If second string is empty, the only option is to
        # remove all characters of first string
        if n == 0:
            return m
    
        # If last characters of two strings are same, nothing
        # much to do. Ignore last characters and get count for
        # remaining strings.
        if str1[m-1] == str2[n-1]:
            return self.editDistance(str1, str2, m-1, n-1)
    
        # If last characters are not same, consider all three
        # operations on last character of first string, recursively
        # compute minimum cost for all three operations and take
        # minimum of three values.
        return 1 + min(self.editDistance(str1, str2, m, n-1),    # Insert
                       self.editDistance(str1, str2, m-1, n),    # Remove
                       self.editDistance(str1, str2, m-1, n-1)    # Replace
                    )

    # TASK 6
    def autoCorrect(self, word, errorMax=2):
        '''
        Given a word, if misspelt return a list of possible valid words 
        from the last valid prefix, with up to errorMax errors
        >>> trie = TrieTree()
        >>> trie.insert('dab')
        >>> trie.autoCorrect('dod')
        ['dab']
        >>> trie.autoCorrect('dod', errorMax=1)
        []
        >>> trie.autoCorrect('dad', errorMax=1)
        ['dab']
        >>> trie.insert('apple')
        >>> trie.insert('dad')
        >>> trie.insert('dude')
        >>> trie.insert('apples')
        >>> trie.insert('application')
        >>> trie.insert('app')
        >>> trie.insert('about')
        >>> trie.autoCorrect('aboot')
        ['about']
        >>> trie.autoCorrect('dea')
        ['dab', 'dad']
        >>> trie.autoCorrect('dod')
        ['dad', 'dude']
        >>> trie.autoCorrect('dea', errorMax=3)
        ['dab', 'dad', 'dude']
        '''

        prefix = ""
        curr = self
        for ch in word:
            if not ch in curr._children:
                break
            prefix += ch
            curr = curr._children[ch]

        res = []
        words = curr.sort()
        for w in words:
            if self.editDistance(w, word, len(w), len(word)) <= errorMax:
                res.append(w)
        return res
                
        

    # TASK 7
    def merge(self, otherTrie: TrieNodeAbstract):
        '''
        Merges another TrieTree into this one
        >>> trie1 = TrieTree()
        >>> trie2 = TrieTree()
        >>> trie1.insert('amazing')
        >>> trie2.insert('amazon')
        >>> trie1.merge(trie2)
        >>> 'amazon' in trie1
        True
        '''
        for word in otherTrie.sort():
            self.insert(word)


    def pPrint(self, _prefix="", _last=True, index=0):
        '''
        DONT CHANGE THIS
        '''
        ret = ''
        if index:
            ret = _prefix + ("`- " if _last else "|- ") + self._char
            _prefix += "   " if _last else "|  "
            if self._value:
                ret += ' : ' + self._value
            ret += '\n'
        else:
            ret = _prefix + "TrieTree"
            _prefix += "   " if _last else "|  "
            ret += '\n'
        child_count = len(self._children)
        for i, child in enumerate(self._children):
            _last = i == (child_count - 1)
            ret += self._children[child].pPrint(_prefix, _last, index+1)
        return ret

    def __str__(self):
        return self.pPrint().strip()


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # trie = TrieTree()
    # trie.insert("word")
    # trie.insert("water")
    # trie.insert("wall")
    # trie.insert("banana")
    # trie.insert("bob")

    # trie.insert("ab")
    # trie.insert("abs")
    # print(trie)

    # print(trie.sort(True))

    # print(trie.autoComplete("w", 1))

    # print("word" in str(trie))
    # print("water" in str(trie))
    # print("bob" in str(trie))
    # print("banana" in str(trie))

    # del trie["water"]
    # del trie["bo"]
    # # del trie["wall"]
    # del trie["ab"]
    # print(trie)


    # t2 = trie

    # print("------")
    # trie = TrieTree()
    # trie.insert('dab')
    # print(trie)
    # print(trie.autoCorrect('dod'))              # ['dab']
    # print(trie.autoCorrect('dod', errorMax=1))  # []
    # print(trie.autoCorrect('dad', errorMax=1))  #['dab']
    # trie.insert('apple')
    # trie.insert('dad')
    # trie.insert('dude')
    # trie.insert('apples')
    # trie.insert('application')
    # trie.insert('app')
    # trie.insert('about')
    # trie.insert('dube')
    # print(trie.autoCorrect('aboot'))            # ['about']
    # print(trie.autoCorrect('dea'))              # ['dab', 'dad']
    # print(trie.autoCorrect('dod'))              # ['dad', 'dude']
    # print(trie.autoCorrect('dea', errorMax=3))  # ['dab', 'dad', 'dude']

    # trie.insert("world")
    # t2.merge(trie)
    # print(t2)

    