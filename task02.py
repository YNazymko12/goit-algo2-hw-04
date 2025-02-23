from trie import Trie

class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings) -> str:
        if not strings or not all(isinstance(word, str) for word in strings):
            print("Invalid input: Expected a list of strings.")
            return ""
        
        if len(strings) == 1:
            print(f"Only one word provided: {strings[0]}")
            return strings[0]
        
        for word in strings:
            self.put(word, True)
        
        # Шукаємо найдовший спільний префікс у Trie
        node = self.root
        prefix = ""
        
        while node and len(node.children) == 1 and node.value is None:
            char = next(iter(node.children))  
            prefix += char
            node = node.children[char]

        print(f"Longest common prefix found: '{prefix}'")
        return prefix

if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    print("Test 1: ", strings)
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    print("Test 2: ", strings)
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    print("Test 3: ", strings)
    assert trie.find_longest_common_word(strings) == ""
