public class GetIntersectionNode {
    public static void main(String[] args) {
        
    }

    public static ListNode solution(ListNode headA, ListNode headB) {
        ListNode left = headA;
        ListNode right = headB;

        while(left != right){
            left = (left != null) ? left.next : headB;
            right = (right != null) ? right.next : headA;
        }
        
        return left;
    }
}
