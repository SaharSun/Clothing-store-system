#by "SAHAR KHORSHID"
class Node: 
  
    def __init__(self, data): 
        self.data = data  
        self.next = None  
  

class LinkedList_login: 

    def __init__(self): 
        self.head = None

    
    def insert_first(self, new_data): 

        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 


    def login(self, user_name , password): 

        current = self.head  
        while current != None: 
            if current.data['name'] == user_name:
                if current.data['password'] == password:
                    self.flag = True
                    return (current.data)
                
            current = current.next 


    def sing_up (self ,datauser):
        if self.login(datauser['name'] ,datauser['password'])is not True:
            new_node = Node(datauser) 
            if self.head is None: 
                self.head = new_node 
                return

            last = self.head 
            while (last.next): 
                last = last.next
            last.next =  new_node 
            return True

        return False

            


    


    def printListalluser(self): 
        temp = self.head 
        while (temp): 
            print (temp.data)
            temp = temp.next

