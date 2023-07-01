class Node:
    def __init__(self,data):
        self.data=data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head=None

    def append(self, data):
        if self.head is None:
            new_node=Node(data)
            new_node.prev =None
            self.head = new_node
        else:
            new_node = Node(data)
            current = self.head
            while current.next:
                current= current.next
            current.next = new_node
            new_node.prev= current
            new_node.next=None

    def prepend(self, data):
        if self.head is None:
            new_node= Node(data)
            new_node.prev = None
            self.head= new_node
        else:
            new_node= Node(data)
            new_node.prev= new_node
            new_node.next=self.head
            self.head= new_node
            new_node.prev= None 
    def add_after_node(self,key,data):
        curr=self.head
        while curr:
            if curr.next is None and curr.data==key:
                self.append(data)
                return
            elif curr.data==key:
                new_node=Node(data)
                next=curr.next
                curr.next=new_node
                new_node.next=next
                new_node.prev=curr
                next.prev=new_node
            curr=curr.next
    def add_before_node(self,key, data):
        curr=self.head
        while curr:
            if curr.prev is None and curr.data==key:
                self.prepend(data)
            elif curr.data==key:
                new_node=Node(data)
                prev=curr.prev
                curr.prev=new_node
                new_node.next=curr
                new_node.prev=prev
                prev.next=new_node
            curr=curr.next
    def delete(self,key):
        curr= self.head
        while curr:
            if curr.data==key and curr==self.head:
                #case1
                if not curr.next:
                    curr=None
                    self.head=None
                    return
                #case2
                else:
                    next=curr.next
                    curr.next=None
                    curr.prev=None
                    self.head=next
                    next.next=None
                    next.prev=None
                    return
            elif curr.data==key:
                #case3
                if curr.next:
                    next=curr.next
                    prev=curr.prev
                    prev.next=next
                    next.prev=prev
                    curr.next=None
                    curr.prev= None
                #case4
                #Its a last Node and we want to delete the last Node with next None
                else:
                    prev=curr.prev
                    curr.prev=None
                    prev.next=None
                    curr=None
                    return
            curr=curr.next
    def reverse(self):
        tmp=None
        curr=self.head
        while curr:
            tmp=curr.prev
            curr.prev=curr.next
            curr.next=tmp
            curr=curr.prev
        if tmp:
            self.head=tmp.prev
    def delete_node(self,node):
        curr= self.head
        while curr:
            if curr == node and curr == self.head:
                #case1
                if not curr.next:
                    curr=None
                    self.head=None
                    return
                #case2
                else:
                    next=curr.next
                    curr.next=None
                    curr.prev=None
                    self.head=next
                    next.next=None
                    next.prev=None
                    return
            elif curr == node:
                #case3
                if curr.next:
                    next=curr.next
                    prev=curr.prev
                    prev.next=next
                    next.prev=prev
                    curr.next=None
                    curr.prev= None
                #case4
                #Its a last Node and we want to delete the last Node with next None
                else:
                    prev=curr.prev
                    curr.prev=None
                    prev.next=None
                    curr=None
                    return
            curr=curr.next

    def remove_duplicates(self):
        curr= self.head
        seen= dict()
        while curr:
            if curr.data not in seen:
                seen[curr.data]=1
                curr= curr.next
            else:
                next= curr.next
                self.delete_node(curr)
                curr=next



    def pairs_with_sum(self, sum_val):
        pairs=list()
        p=self.head
        q= None
        while p:
            q= p.next
            while q:
                if p.data + q.data == sum_val:
                    pairs.append("(" + str(p.data) + "," + str(q.data)+ ")")
                q=q.next
            p= p.next
        return pairs
    

    def print_self(self):
        cur=self.head
        while cur:
            print(cur.data)
            cur=cur.next

dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.append(5)





print(dllist.pairs_with_sum(0))
dllist.print_self()