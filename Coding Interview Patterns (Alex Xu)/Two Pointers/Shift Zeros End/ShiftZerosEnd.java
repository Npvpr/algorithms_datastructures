import java.util.Arrays;

public class ShiftZerosEnd {
    // Shift Zeros to the end
    // Non-zeros have to stay in the same order
    // Modify the given array (making new array to return is not allowed)

    public static void main(String[] args) {

        System.out.println(Arrays.equals(solution(new int[] {}), new int[] {}));
        System.out.println(Arrays.equals(solution(new int[] { 0 }), new int[] { 0 }));
        System.out.println(Arrays.equals(solution(new int[] { 1 }), new int[] { 1 }));
        System.out.println(Arrays.equals(solution(new int[] { 0, 0, 0 }), new int[] { 0, 0, 0 }));
        System.out.println(Arrays.equals(solution(new int[] { 1, 3, 2 }), new int[] { 1, 3, 2 }));
        System.out.println(Arrays.equals(solution(new int[] { 1, 1, 1, 0, 0 }), new int[] { 1, 1, 1, 0, 0 }));
        System.out.println(Arrays.equals(solution(new int[] { 0, 0, 1, 1, 1 }), new int[] { 1, 1, 1, 0, 0 }));
        System.out.println(Arrays.equals(solution(new int[] { 1, 0, 1, 0, 1 }), new int[] { 1, 1, 1, 0, 0 }));

    }

    public static int[] solution(int[] inputArr) {

        int left = 0, right = 0;
        // System.out.println("Before: ");
        // printArr(inputArr);

        while (right < inputArr.length) {
            if (inputArr[right] != 0) {
                int temp = inputArr[left];
                inputArr[left] = inputArr[right];
                inputArr[right] = temp;
                left++;
            }
            right++;
        }
        // System.out.println("After: ");
        // printArr(inputArr);

        return inputArr;
    }

    public static void printArr(int[] inputArr) {
        for (int i : inputArr) {
            System.out.print(i + " ");
        }
        System.out.println();
    }
}
