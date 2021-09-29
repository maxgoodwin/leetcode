/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode ReverseList(ListNode head) {
        return ReverseList(head, null);
    }
    
    public ListNode ReverseList(ListNode head, ListNode newHead) {
        if (head == null) {
            return newHead;
        }
        
        ListNode next = head.next;
        head.next = newHead;
        return ReverseList(next, head);
    }
}