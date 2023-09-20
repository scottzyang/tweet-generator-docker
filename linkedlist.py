#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return f'Node({self.data})'


class LinkedList:

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list."""
        ll_str = ""
        for item in self.items():
            ll_str += f'({item}) -> '
        return ll_str

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(n) Why and under what conditions?"""
        # TODO: Loop through all nodes and count one for each
        length = 0
        current_node = self.head

        # loop until there is no current_node left
        while current_node is not None:
            length += 1
            current_node = current_node.next

        return length


    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        new_node = Node(item)
        # If list is empty, set new node as head and tail.
        if self.is_empty() == True:
            self.head = new_node
            self.tail = new_node
        # Set reference of last node to new node, and reset tail to new node.
        else:
            self.tail.next = new_node
            self.tail = new_node


    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        # eval is head exists, if it does change reference of curr node to head, reset head to new node
        if self.head is not None:
            new_node = Node(item)
            new_node.next = self.head
            self.head = new_node
        else:
            # if it is empty, simply append to list.
            self.append(item)

    def find(self, matcher):
        """Return an item from this linked list if it is present.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find item, if present return True otherwise False
        current_node = self.head

        while current_node is not None:
            if current_node.data == matcher:
                return True
            else:
                current_node = current_node.next
        return False

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find one whose data matches given item
        current_node = self.head

        # if head is empty
        if self.head is None:
            raise ValueError("List is empty.")

        # if item matches head
        if self.head and self.tail:
            if self.head.data is item:
                self.head = current_node.next

                if self.tail.data is item:
                    self.tail = None
                return

        # logic is always evaluating one node ahead, cannot loop until end of list.
        while current_node.next is not None:
            # check if next node data matches item
            if current_node.next.data == item:
                # check if last node is same as the next node
                if self.tail == current_node.next:
                    self.tail = current_node
                # set current node ref to ref from next node, if last element set to None.
                current_node.next = current_node.next.next
                return
            else:
                # change node to next node
                current_node = current_node.next

        raise ValueError('Item not found: {}'.format(item))

    def replace(self, match, replacement):
        current_node = self.head

        # loop to find match
        while current_node is not None:
            # if match, replace data
            if current_node.data is match:
                current_node.data = replacement
            else:
                # move to next node
                current_node = current_node.next



def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))
    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
