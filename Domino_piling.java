import java.util.Scanner;
 
public class Main{
    public static void main(String[]args){
        Scanner scan = new Scanner(System.in);
        int m =scan.nextInt();
        int n = scan.nextInt();
        int amount = (m*n)/2;
        System.out.println(amount);
    }
}
