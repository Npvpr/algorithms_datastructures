import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ThreeSum {
    public static void main(String[] args) {
        // For lists compare with list1.equals(list2)
        // For arrays compare with Arrays.equals(array1, array2)
        System.out.println(solution(new int[] { -1, 0, 1, 2, -1, -4 })
                .equals(Arrays.asList(Arrays.asList(-1, -1, 2), Arrays.asList(-1, 0, 1))));
        System.out.println(solution(new int[] { 0, 1, 1 }).equals(Arrays.asList()));
        System.out.println(
                solution(new int[] { 0, 0, 0 }).equals(Arrays.asList(Arrays.asList(0, 0, 0))));
    }

    public static List<List<Integer>> solution(int[] nums) {

        Arrays.sort(nums);

        // List interface is flexible for Arrays.asList()
        List<List<Integer>> triplets = new ArrayList<>();

        // - 2 => leave rooms for second and third ints
        for (int i = 0; i < nums.length - 2; i++) {

            // optimization: triplets consisting of only positive numbers will never sum to
            // 0
            if (nums[i] > 0)
                break;

            // correct arrays of first -1 and correct arrays of second -1 can become
            // duplicates
            // if(nums[i] == nums[i+1]) continue; // if last correct triplet is [-1, -1, 2],
            // this code would skip
            if (i > 0 && nums[i] == nums[i - 1])
                continue;

            int left = i + 1, right = nums.length - 1;
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum == 0) {
                    triplets.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    left++;
                    // assume here the array from left to right is: [-2, -2, 0, 0, 2, 2], left =
                    // 0:-2, right = 5:2
                    // this left skipping will end in 2:0
                    while (left < right && nums[left] == nums[left - 1])
                        left++;

                    // this right skipping will end in 4:2
                    // this is not mandatory because left skipping would just reject 0+2 > 0
                    // tip: there could only be one possible answer for required operand in sum
                    // eg. to get 3 = 1 + a; 'a' can only 2 and there are no other possible integers
                    // but this could optimize some cases with too much rightmost duplicates
                    while (left < right && nums[right] == nums[right - 1])
                        right--;
                } else if (sum < 0) {
                    left++;
                } else {
                    right--;
                }
            }
        }

        return triplets;
    }
}
