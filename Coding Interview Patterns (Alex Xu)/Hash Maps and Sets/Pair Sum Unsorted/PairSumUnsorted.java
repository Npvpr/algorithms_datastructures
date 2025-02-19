import java.util.Arrays;
import java.util.HashMap;

public class PairSumUnsorted {
    public static void main(String[] args) {
        // Arrays.equals(array1, array2) -> Content Comparison Methods
        // arraylist1.equals(arraylist2) -> Content Comparison Methods
        // array1.equals(array2) -> Reference Comparison Methods
        // arraylist1 == arraylist2 -> Reference Comparison Methods :'(
        System.out.println(Arrays.equals(solution(new int[] { 2, 7, 11, 15 }, 9), new int[] { 0, 1 })); // [0, 1]
        System.out.println(Arrays.equals(solution(new int[] { 3, 2, 4 }, 6), new int[] { 1, 2 })); // [1, 2]
        System.out.println(Arrays.equals(solution(new int[] { 3, 3 }, 6), new int[] { 0, 1 })); // [0, 1]
    }

    public static int[] solution(int[] nums, int target) {
        // Frequency doesn't matter here because there is only one solution
        HashMap<Integer, Integer> nMap = new HashMap<>();

        int complement;
        for (int i = 0; i < nums.length; i++) {
            complement = target - nums[i];

            // if found, current num doesn't need to be put into the HashMap anymore
            // just return them
            if (nMap.containsKey(complement)) {
                return new int[] { nMap.get(complement), i };
            }
            nMap.put(nums[i], i);
        }
        return new int[] {};
    }

}
