class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> lists = new ArrayList<>();
        for(int i = 1; i <= n; i++){
            if(i % 3 == 0){
                if(i % 5 == 0){
                    lists.add("FizzBuzz");
                }
                else{
                    lists.add("Fizz");
                }
            }
            else if (i % 5 == 0){
                lists.add("Buzz");
            }
            else{
                String s = String.valueOf(i);
                lists.add(s);
            }
        }
        System.out.println(lists);
        return(lists);
    }           
}
        