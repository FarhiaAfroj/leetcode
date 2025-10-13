class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        target = {}
        for char in licensePlate:
            if char.isalpha():
                char_lower = char.lower()
                target[char_lower] = target.get(char_lower, 0) + 1
        
        shortest_word = None
        for word in words:
            word_count = {}
            for char in word:
                word_count[char] = word_count.get(char, 0) + 1
            
            valid = True
            for char, count in target.items():
                if word_count.get(char, 0) < count:
                    valid = False
                    break
            
            if valid:
                if shortest_word is None or len(word) < len(shortest_word):
                    shortest_word = word
        
        return shortest_word