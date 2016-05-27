"""
 Insert Node at the end of a linked list
 head input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""
#This is a "method-only" submission.
#You only need to complete this method.
def InsertNth(head, data, position):
	if position == 0:
        new_node = node()
        new_node.data = data
        new_node.next = head.cur_node
        head.cur_node = new_node
    else:
    	current = head
        while (current.next != None):
            current = current.next
        current.next = Node(data)
    return head

