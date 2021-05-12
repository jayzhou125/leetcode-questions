class Solution {
    public String countAndSay(int n) {
        // iterative
        // String result = "1";
        // for (int i = 2; i <= n; i++){
        //     result = say(result);             
        // }
        // return result;
        
        // recursive
        return n == 1 ? "1": say(countAndSay(n-1));
    }
    
    private String say(String s){
        int i = 0, j = 0;
        StringBuilder sb = new StringBuilder();
        while (j <= s.length()){
            while(j < s.length() && s.charAt(i) == s.charAt(j)) 
                j++;
            sb.append(j - i).append(s.charAt(i));
            i = j;
            j++;
        }
        return sb.toString();
    }
}
