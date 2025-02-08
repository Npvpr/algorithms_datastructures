public class Naive{
    public static void main(String[] args){
        int a = 8;
        int b = 12;

        int best = 0;
        for(int d = 1; d <= a+b; d++){
            if((a%d == 0) && (b%d == 0)){
                best = d;
            }
        }
        System.out.println(best);
    }
}