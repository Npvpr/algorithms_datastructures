public class RemoveNEnd {
    public static void main(String[] args) {
        ListNode head = new ListNode(1, null);
        System.out.println(solution(head, 1));
    }
    public static ListNode solution(ListNode head, int n) {
        ListNode dummyNode = new ListNode(0, head);

        // space left and right
        // start both from the dummy node
        // move right n times
        ListNode left = dummyNode;
        ListNode right = dummyNode;
        for(int i = 0; i < n; i++){
            right = right.next;
        }
        
        while(right.next != null){
            left = left.next;
            right = right.next;
        }

        // end
        // if right.next = null;
        // right = 1;

        // left = right - (n-1);
        // left = 1 - 2 - 1
        // left = 0
        left.next = left.next.next;

        return dummyNode.next;
        
    }
}
