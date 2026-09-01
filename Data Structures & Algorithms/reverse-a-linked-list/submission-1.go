/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func reverseList(head *ListNode) *ListNode {
	var prev *ListNode
	curr := head

	for {
		if curr == nil {
			break
		}

		temp := curr.Next
		curr.Next = prev
		prev = curr
		curr = temp
	}

	return prev
}
