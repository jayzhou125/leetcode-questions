# python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # build hash map ->  char : count
        count = collections.Counter(s)
        # find the index
        # enumerate() will return (idx, char) pair
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1
        

# Java
class Solution {
    public int firstUniqChar(String s) {
        // Hashmap
        // time complexity: o(n) loop through the length of the string for 2 times
        // space complexity: o(1) max 26 letters in english alphabet
        // int l = s.length();
        // Map<Character, Integer> map = new HashMap<>();
        // for(int i = 0; i < l; i++){
        //     char c = s.charAt(i);
        //     map.put(c, map.getOrDefault(c, 0) + 1);
        // }
        // for(int i = 0; i < l; i++){
        //     if (map.get(s.charAt(i)) == 1) 
        //         return i;
        // }
        // return -1;
        
        // easier to remember
        for (int i = 0; i < s.length(); i++) {
		    char ch = s.charAt(i);
		    if (s.indexOf(ch) == s.lastIndexOf(ch)) {
			    return i;
		    }
	    }
	    return -1;
    }
}
