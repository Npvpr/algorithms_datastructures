// package algorithms.hashmaps_sets;

import java.util.HashSet;

public class LongestConsecutiveNumbers {
    public static void main(String[] args) {
        
        System.out.println(solution(new int[] {1, 2, 3, 4, 5})); // 5
        System.out.println(solution(new int[] {})); // 0
        System.out.println(solution(new int[] {1})); // 1
        System.out.println(solution(new int[] {1, 1, 1})); // 1
        System.out.println(solution(new int[] {1, 3, 2, 6, 9, 5, 7, 8})); // 5

    }

    public static int solution(int[] inputArr){
        int longestChain = 0;
        // Cannot directly convert from int[] to HashSet<Integer>, Integer[] would work
        // HashSet<Integer> inputHash = new HashSet<>(Arrays.asList(inputArr)); => this doesn't work
        HashSet<Integer> inputHash = new HashSet<>();
        for (int num: inputArr){
            inputHash.add(num);
        }

        for(int currentNum: inputHash){
            if(!inputHash.contains(currentNum-1)){
                int currentChain = 1; 
                while(inputHash.contains(currentNum+1)){
                    currentChain++;
                    currentNum++;
                }
                longestChain = Math.max(currentChain, longestChain);
            }
        }
        return longestChain;

    }
}
