class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        queue = [(beginWord,1)]
        while queue:
            cur,length = queue.pop(0)
            for i in range(len(cur)):
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = cur[:i]+j+cur[i+1:]
                    if next_word in wordList:
                        if next_word == endWord:
                            return length+1
                        else:
                            queue.append((next_word,length+1))
                            wordList.remove(next_word)
        return 0
s = Solution()
print(s.ladderLength('hot','got',['hot','got']))
