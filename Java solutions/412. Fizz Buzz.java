class Solution {
    public List<String> fizzBuzz(int n) {
        // Naive Approach
        // time complexity: o(n)
        // space complexity: o(1)
        // List<String> answer = new ArrayList<>();
        // for (int i = 1; i <= n; i++){
        //     if (i % 3 == 0 && i % 5 == 0) answer.add("FizzBuzz");
        //     else if (i % 3 == 0) answer.add("Fizz");
        //     else if (i % 5 == 0) answer.add("Buzz");
        //     else answer.add(Integer.toString(i));
        // }
        // return answer;
        
        // String concatenation, neater solution if the game rule changes
        // time complexity: o(n)
        // space complexity: o(n)
        // List<String> answer = new ArrayList<>();
        // for (int i = 1; i <= n; i++){
        //     String cur = "";
        //     if (i % 3 == 0) cur += "Fizz";
        //     if (i % 5 == 0) cur += "Buzz";
        //     if (cur.equals("")) cur += Integer.toString(i);
        //     answer.add(cur);
        // }
        // return answer;
        
        // hash table, for dealing with too many mappings
        List<String> answer = new ArrayList<>();
        HashMap<Integer, String> hm = new HashMap<>();
        hm.put(3, "Fizz");
        hm.put(5, "Buzz");
        for (int i = 1; i <= n; i++){
            String cur = "";
            for (Integer key: hm.keySet()){
                if (i % key == 0) cur += hm.get(key);
            }
            if (cur.equals("")) cur += Integer.toString(i);
            answer.add(cur);
        }
        return answer;
    }
}
