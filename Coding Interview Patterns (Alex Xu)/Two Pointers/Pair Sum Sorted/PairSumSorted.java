import java.util.ArrayList;
import java.util.List;

public class PairSumSorted{
    public static void main(String[] args){
        // Arrays.asList converts an array into a list
        ArrayList<Integer> inputArr = new ArrayList<>(List.of(1, 2, 3, 4, 5, 6, 7, 8, 9));

        System.out.println(solution(inputArr, 5).equals(List.of(0, 3)) ? "Correct" : "Error");
        System.out.println(solution(inputArr, 18).equals(List.of(-1, -1)) ? "Correct" : "Error");

    }

    public static ArrayList<Integer> solution(ArrayList<Integer> inputArr, int target){

        // Sorted array allowed this two pointer method
        // For leftmost, current sum is the biggest, so if target is bigger, move right
        // For leftmost, changing the other operand can only result in smaller sums
        // 1 + 9 = 10, 1 + 8 = 9, 1 + 7 = 8

        // For rightmost, current sum is the smallest, so if target is smaller, move left
        // For rightmost, changing the other operand can only result in bigger sums
        // 9 + 1 = 10, 9 + 2 = 11, 9 + 3 = 12

        Integer left = 0, right = inputArr.size() - 1;
        // not including "=" solves the problem of adding the same number twice;eg. 5 + 5 = 10
        while (left < right){
            int currentSum = inputArr.get(left) + inputArr.get(right);
            if (currentSum == target){
                // System.out.println(left + ", " + right);
                return new ArrayList<>(List.of(left, right));
            }else if(currentSum < target){
                left++;
            }else{
                right--;
            }
        }
        
        // System.out.println(left + ", " + right);
        return new ArrayList<>(List.of(-1, -1));
    }
}