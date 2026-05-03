# Problem: Word Ladder
# URL: https://leetcode.com/problems/word-ladder/
# Language: python3

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        nei=collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                curr=word[:j] + '*' + word[j+1:]
                nei[curr].append(word)
        
        visited=set([beginWord])
        q = deque([beginWord])
        step=1
        while q:
            for _ in range(len(q)):
                cur_word = q.popleft()
                if cur_word == endWord:
                    return step
                for j in range(len(cur_word)):
                    pattern=cur_word[:j] + '*' + cur_word[j+1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visited: 
                            visited.add(neiWord)
                            q.append(neiWord)
            step+=1
        return 0

        # Brute Force
        # visited=set()
        # wordSet = set(wordList)
        # q = deque([(beginWord, 1)])
        # visited.add(beginWord)
        # n = len(beginWord)

        # while q:
        #     cur_word,step = q.popleft()
        #     if cur_word == endWord:
        #         return step
        #     for i in range(n):
        #         for ch in 'abcdefghijklmnopqrstuvwxyz':
        #             word = cur_word[:i] + ch + cur_word[i+1:]
        #             if word in wordSet and word not in visited:
        #                     q.append([word,step+1])
        #                     visited.add(word)
        # return 0