class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        news = s.strip(' ')
        newsarr = news.split(" ")
        return len(newsarr[-1])