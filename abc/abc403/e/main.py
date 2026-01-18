class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_end = False
        self.count = 1

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            else: 
                node.children[ch].count += 1
            node = node.children[ch]
        node.is_end = True
    
    def has_prefix(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
            if node.is_end:
                return True
        return False
    
    def erase_with_prefix(self, prefix):
        def dfs_count(node):
            count = 1 if node.is_end else 0
            for child in node.children.values():
                count += dfs_count(child)
            return count
        
        def dfs_erase(node):
            for ch in list(node.children.keys()):
                dfs_erase(node.children[ch])
                del node.children[ch]
            node.is_end = False
            node.count = 0
        
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return 0
            node = node.children[ch]

        count = dfs_count(node)
        dfs_erase(node)
        return count

import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

trie_x=Trie()
trie_y=Trie()
ans=0
for _ in range(int(input())):
    t,s=input().split()
    if t=="1":
        trie_x.insert(s)
        node=trie_y.root
        node = trie_y.root
        ans -= trie_y.erase_with_prefix(s)
    else:
        if not trie_x.has_prefix(s):
            ans+=1
            trie_y.insert(s)
    print(ans)
