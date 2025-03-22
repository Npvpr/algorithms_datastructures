public class LexicographicalSequence {
    public static void main(String[] args) {
        System.out.println(solution("a").equals("a"));
        System.out.println(solution("aaaa").equals("aaaa"));
        System.out.println(solution("dcba").equals("abcd"));
        System.out.println(solution("abcedda").equals("abdacde"));
        System.out.println(solution("ynitsed").equals("ynsdeit"));
    }

    public static String solution(String inputStr) {
        char[] letters = inputStr.toCharArray();
        
        // this is copied by reference, editing "copy" will effect the "letters"
        // char[] copy = letters;

        // Copied by value
        // char[] copy = letters.clone();

        int pivot = letters.length - 2;
        int right = letters.length - 1;

        while (pivot >= 0) {
            if (letters[pivot] < letters[pivot + 1]) {
                break;
            }
            pivot--;
        }

        if (pivot == -1) {
            // StringBuilder.reverse() is an instance method, not a static method
            // To use this, first create StringBuilder object first, reverse second, and finally convert back to String
            // return new StringBuilder(inputStr).reverse().toString();

            // "letters" array is passed by reference(actually, value of memory address)
            // can modify the original array
            // but method cannot change the reference itself
            // meaning -> inside method
            reverse(letters, 0, right);

            return new String(letters);
        }

        while(right > pivot){
            if(letters[right] > letters[pivot]){
                char temp = letters[right];
                letters[right] = letters[pivot];
                letters[pivot] = temp;
                break;
            }
            right--;
        }

        reverse(letters, pivot + 1, letters.length - 1);

        return new String(letters);
    }

    public static void reverse(char[] arr, int start, int end){
        // method cannot change the reference itself
        // this will only effect 'arr' array in this scope, not 'letters' array itself
        // arr = new char[] {'X', 'Y', 'Z'}
        
        while(end > start){
            char temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            end--;
            start++;
        }
    }
}
