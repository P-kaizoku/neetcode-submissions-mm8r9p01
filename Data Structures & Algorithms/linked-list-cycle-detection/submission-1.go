/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func hasCycle(head *ListNode) bool {
    slow := head
	fast := head

	for {
		if fast == nil || fast.Next == nil {
			break
		}

		slow = slow.Next
		fast = fast.Next.Next

		if fast == slow{
			return true
		}
	}
	return false
}
