public class ReverseLinkedListIterative {

    public static void main(String[] args) {
        ListNode head = new ListNode(1, null);
        System.out.println(solution(head));
    }

    public static ListNode solution(ListNode head) {
        // Iterative
        ListNode prev = null;
        ListNode curr = head;
        // Cannot read head.next here because head can be null (empty list)
        ListNode nxt;

        while(curr != null){
            // before next is replaced
            nxt = curr.next;

            // reverse the link
            curr.next = prev;

            // prepare for next step
            prev = curr;
            curr = nxt;
            // nxt = nxt.next;
        }

        return prev;
    }
}
