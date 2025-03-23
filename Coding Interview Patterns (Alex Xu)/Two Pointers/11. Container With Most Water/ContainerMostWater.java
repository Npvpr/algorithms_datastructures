public class ContainerMostWater {
    public static void main(String[] args) {
        System.out.println(solution(new int[] {1,8,6,2,5,4,8,3,7}) == 49);
        System.out.println(solution(new int[] {5,5,5,5}) == 15);
        System.out.println(solution(new int[] {4,3,2,1}) == 4);
        System.out.println(solution(new int[] {1,2}) == 1);
    }

    public static int solution(int[] inputArr){
        int left = 0, right = inputArr.length - 1, max = 0;
        while(left < right){
            int currentMax = Math.min(inputArr[left], inputArr[right]) * (right - left);

            if(currentMax > max){
                // System.out.println(inputArr[left] + " " + inputArr[right]);
                max = currentMax;
            }

            if(inputArr[left] < inputArr[right]){
                left++;
            }else if(inputArr[right] < inputArr[left]){
                right--;
            }else{
                left++;
                right--;
            }
        }
        // System.out.println(max);
        return max;
    }
}
