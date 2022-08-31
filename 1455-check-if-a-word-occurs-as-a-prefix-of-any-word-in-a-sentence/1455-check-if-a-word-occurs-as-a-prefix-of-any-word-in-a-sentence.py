class Solution:
    def isPrefixOfWord(self, sentence: str, sword: str) -> int:
        words=sentence.split()
        for i,word in enumerate(words):
            # print(i,word)
            if len(word)>=len(sword):
                if sword == word[:len(sword)]:
                    return i+1
        return -1