import java.util.HashMap;

public class GeometricSequenceTriplets {
    public static void main(String[] args) {
        // Original sample test case:
        System.out.println(solution(new int[] { 2, 1, 2, 4, 8, 8 }, 2)); // Expected output: 5

        // Edge Case 1: Empty Array
        System.out.println(solution(new int[] {}, 2)); // Expected output: 0

        // Edge Case 2: Single Element Array
        System.out.println(solution(new int[] { 1 }, 2)); // Expected output: 0

        // Edge Case 3: Two Elements Only
        System.out.println(solution(new int[] { 1, 2 }, 2)); // Expected output: 0

        // Edge Case 4: All Identical Elements with r = 1
        System.out.println(solution(new int[] { 1, 1, 1, 1 }, 1)); // Expected output: 4

        // Edge Case 5: Larger Set of Identical Elements with r = 1
        System.out.println(solution(new int[] { 1, 1, 1, 1, 1 }, 1)); // Expected output: 10

        // Edge Case 6: No Valid Triplets (Different Ratio)
        System.out.println(solution(new int[] { 1, 2, 3, 4, 5 }, 3)); // Expected output: 0

        // Edge Case 7: Valid Triplets with Mixed Order and Duplicates
        System.out.println(solution(new int[] { 1, 3, 9, 9, 27, 81 }, 3)); // Expected output: 6

        // Edge Case 8: Case with r = 0
        // Here, we catch and print the exception.
        try {
            System.out.println(solution(new int[] { 0, 0, 0 }, 0));
        } catch (Exception e) {
            System.out.println("Error for r=0: " + e);
        }

        // Edge Case 9: Negative Numbers with a Negative Ratio
        System.out.println(solution(new int[] { 1, -1, 1, -1, 1 }, -1)); // Expected output: Depends on array order

        // Edge Case 10: Duplicates in a Non-r = 1 Geometric Progression
        System.out.println(solution(new int[] { 2, 2, 2, 4, 4, 8 }, 2)); // Expected output: 6

    }

    public static int solution(int[] inputArr, int commonRatio) {
        HashMap<Integer, Integer> leftMap = new HashMap<>();
        HashMap<Integer, Integer> rightMap = new HashMap<>();

        // can use 'getOrDefault' built-in
        // rightMap.put(x, rightMap.getOrDefault(x, 0) + 1);

        for (int currentNum : inputArr) {
            if (!rightMap.containsKey(currentNum)) {
                rightMap.put(currentNum, 1);
                leftMap.put(currentNum, 0);
            } else {
                rightMap.put(currentNum, rightMap.get(currentNum) + 1);
            }
        }

        int count = 0;

        // I think int x is automatically converted to Integer while doing
        // HashMap.get(x) or HashMap.put(x, int)
        // because of keys of HashMaps are Integers
        for (int x : inputArr) {

            rightMap.put(x, rightMap.get(x) - 1);

            if (x % commonRatio == 0) {
                if (leftMap.containsKey(x / commonRatio) && rightMap.containsKey(x * commonRatio)) {
                    count += leftMap.get(x / commonRatio) * rightMap.get(x * commonRatio);
                }
            }

            leftMap.put(x, leftMap.get(x) + 1);

        }

        return count;
    }
}
