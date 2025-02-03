import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ThreeSum {
    public static void main(String[] args) {
        System.out.println(solution(new int[] {-1,0,1,2,-1,-4}).equals(Arrays.asList(Arrays.asList(-1,-1,2),Arrays.asList(-1,0,1))) ? "Correct" : "Error");
        System.out.println(solution(new int[] {0,1,1}).equals(Arrays.asList()) ? "Correct" : "Error");
        System.out.println(solution(new int[] {0,0,0}).equals(Arrays.asList(Arrays.asList(0,0,0))) ? "Correct" : "Error");
    }

    public static List<List<Integer>> solution(int[] nums) {

        Arrays.sort(nums);

        // List interface is flexible for Arrays.asList()
        List<List<Integer>> triplets = new ArrayList<>();
        
        // - 2 => leave rooms for second and third ints
        for(int i = 0; i < nums.length - 2; i++){
            
            // optimization: triplets consisting of only positive numbers will never sum to 0
            if(nums[i] > 0) break;

            // correct arrays of first -1 and correct arrays of second -1 can become duplicates
            // if(nums[i] == nums[i+1]) continue; // if last correct triplet is [-1, -1, 2], this code would skip
            if(i > 0 && nums[i] == nums[i-1]) continue;

            int left = i+1, right = nums.length -1;
            while(left < right){
                int sum = nums[i] + nums[left] + nums[right];
                if(sum == 0){
                    triplets.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    left++;
                    while(left < right && nums[left] == nums[left - 1]) left++;
                }else if(sum < 0){
                    left++;
                }else{
                    right--;
                }
            }
        }

        return triplets;
    }
}
