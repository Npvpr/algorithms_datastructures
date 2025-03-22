public class Palindrome {
    // skip non-alphanumeric characters
    public static void main(String[] args) {
        System.out.println(solution("") == true);
        System.out.println(solution("a") == true);
        System.out.println(solution(",:") == true);
        System.out.println(solution("AbBa") == true);
        System.out.println(solution("defeda") == false);
    }

    public static boolean solution(String inputStr) {
        int left = 0, right = inputStr.length() - 1;
        while (left < right) {
            while (left < right && !Character.isAlphabetic(inputStr.charAt(left))) {
                left++;
            }
            while (left < right && !Character.isAlphabetic(inputStr.charAt(right))) {
                right--;
            }
            if (Character.toLowerCase(inputStr.charAt(left)) != Character.toLowerCase(inputStr.charAt(right))) {
                // System.out.println("Not equal: " + inputStr.charAt(left) + " vs " + inputStr.charAt(right));
                return false;
            }
            // System.out.println("Equal: " + inputStr.charAt(left) + " vs " + inputStr.charAt(right));

            left++;
            right--;
        }
        return true;
    }
}
