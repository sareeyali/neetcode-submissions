class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        q = collections.deque([(beginWord, 1)])
        seen = set([beginWord])

        while q:
            trial_word, count = q.popleft()
            if trial_word == endWord:
                return count
            for i in range(len(trial_word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    new_word = trial_word[:i] + c + trial_word[i+1:]
                    if new_word in wordSet and new_word not in seen:
                        seen.add(new_word)
                        q.append((new_word, count + 1))
        return 0
                        