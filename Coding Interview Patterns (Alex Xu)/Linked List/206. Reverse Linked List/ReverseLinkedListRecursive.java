public class ReverseLinkedListRecursive {

    public static void main(String[] args) {
        ListNode head = new ListNode(1, null);
        System.out.println(solution(head));
    }

    public static ListNode solution(ListNode head) {

        // Recursive
        if (head == null || head.next == null) {
            return head;
        }

        ListNode newHead = solution(head.next);

        // The reverse process doesn't depend on the newHead
        head.next.next = head;

        // Head is last node for each list/sublist
        head.next = null;

        // NewHead is the last node of original list which needs to carried to the final
        // recursion
        return newHead;

    }

}
