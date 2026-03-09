from typing import TypeVar, Generic, Optional
# en esta seccion se estudiara a nivel conceptual lo que son los nodos y como implementarlos

T = TypeVar("T")

# A node is a container of data, together with one or more links to other nodes. A link is a pointer


# there is a problem with this structure and is explained next to this:
# imagine this list: 10 -> 20 -> 30 -> 40
#
# if you are at node 30, you can move: 30 -> 40
#
# but you cannot go back to 20, because there is no reference to it.
#
# the only way to reach 20 again would be: start from the head 10 -> 20 -> 30
# this can be inefficient
#
#
# the solution to this is add a new variable that is previous pointer and contains the value previous to the current node


# implementing a node
class Node(Generic[T]):
    def __init__(self, data: T) -> None:
        self.data = data
        self.next: Optional[Node] = (
            None  # pointer is initialized to None, meaning that unless you chage the value of next, the node is going to be an end-point.
            # we use Optional Node because we point to another node, not to the data itself
        )

    # we could also add other methods like __str__
    def __str__(self) -> str:
        return str(self.data)

    def __repr__(self) -> str:
        return f"Node(data: {self.data}, next: Node(data: {self.next}))"


if __name__ == "__main__":
    node1 = Node(data=20)
    node2 = Node(data="samuel")
    node3 = Node(data="colombia")

    # the reference of this nodes is empty
    print(f"Reference of the nodes: \n{repr(node1)}\n{repr(node2)}\n{repr(node3)}")

    # to give this reference a value we link the values and this the part when a conceptually concept appears that is
    # linkendlist
    node1.next = node2
    node2.next = node3

    # and now if we look for those reference we're gonna se the next
    print(
        f"\nReference of the nodes (changed): \n{repr(node1)}\n{repr(node2)}\n{repr(node3)}"
    )
