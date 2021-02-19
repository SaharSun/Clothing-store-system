#by "SAHAR KHORSHID"

import sys
import os
from login import LinkedList_login
class Node: 
  
    def __init__(self, data): 
        self.data = data  
        self.next = None  
  

class LinkedList: 

    def __init__(self): 
        self.head = None
  


    def insert_first(self, new_data): 

        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
  
  
    
    def search_id_foradding(self, x): 
        self.flag = False
        current = self.head  
        while current != None: 
            if current.data['id'] == x: 
                self.flag = True
                return current
                
            current = current.next 
        return None



    def adding(self, prev_id, new_data): 

        if self.search_id_foradding(prev_id):
        
            prev_node = self.search_id_foradding(prev_id)
            
            new_node = Node(new_data)
            new_node.next = prev_node.next
            prev_node.next = new_node
                 
        return None



    def insert_end(self, new_data):  
        new_node = Node(new_data) 
        if self.head is None: 
            self.head = new_node 
            return

        last = self.head 
        while (last.next): 
            last = last.next
        last.next =  new_node 
  

    def search_id(self, x): 
        current = self.head 
        self.flag = False
        while current != None: 
            if current.data['id'] == x: 
                self.flag = True 
                return current.data 

            current = current.next
       
      

    def search_name(self, x): 
        name_list = []
        self.flag = False
        current = self.head  
        while current != None: 
            if current.data['name'] == x: 
                self.flag = True
                name_list.append(current.data)    
            current = current.next 
        return name_list    
        


    def search_color(self, x): 
        color_list = []
        self.flag = False
        current = self.head  
        while current != None: 
            if current.data['color'] == x: 
                self.flag = True
                color_list.append(current.data)    
            current = current.next 
        return color_list 


    def search_money(self,x): 
        mony_list = []
        self.flag = False
        current = self.head  
        while current != None: 
            if current.data['money'] == x: 
                self.flag = True
                mony_list.append(current.data)    
            current = current.next 
        return mony_list



    def search_sort_money (self , first , end):
        money_list = []
        self.flag = False
        current = self.head  
        while current != None: 
            if current.data['money'] >= first:
                if current.data['money'] <= end:
                    self.flag = True
                    money_list.append(current.data)    
            current = current.next 


        for i in range(len(money_list)):
            cursor = money_list[i]
            pos = i
            while (pos > 0) and (money_list[pos - 1]['money'] > cursor['money']):
                money_list[pos] = money_list[pos - 1]
                pos = pos - 1
            money_list[pos] = cursor
        return money_list


    def search_size(self , x):
        size_list = []
        self.flag = False
        current = self.head  
        while current != None: 
            if x in current.data['size']: 
                self.flag = True
                size_list.append(current.data)    
            current = current.next 
        return size_list



    def deleteNode(self, key):
        temp = self.head  
        if (temp is not None):  
            if (temp.data['id'] == key):  
                self.head = temp.next
                temp = None
                return
        while(temp is not None):  
            if temp.data['id'] == key:  
                break
            prev = temp  
            temp = temp.next
        if(temp == None):  
            return
        prev.next = temp.next
        temp = None


    def shopping(self, x , size):
        self.flag = False
        current = self.head  
        while current != None: 
            if current.data['id'] == x: 
                if size in current.data['size']is True:
                    self.flag = True
                    current.data['size'] = current.data['size'].replace(size, '')
                    return (current.data)
                
            current = current.next 


    def printListall(self): 
        temp = self.head 
        while (temp): 
            
            print (temp.data)
            temp = temp.next
    



a = {'id':1 , 'name':"coat", 'money':440 , 'color':'black' , 'size': '44,46,48,50,52'}
b = {'id':2 , 'name':"T-shirt" , 'money':280 , 'color':'red' , 'size': '44,46,48,50,52'}
c = {'id':3 , 'name':"suit", 'money': 990 , 'color':'gray' , 'size': '44,46,48,50,52'}
d = {'id':4 , 'name':"Pants", 'money': 170 , 'color':'black' , 'size': '44,45,46,47,48,49,50,51,52'}
e = {'id':5 , 'name':"Shirt", 'money': 180 , 'color':'white' , 'size': '44,46,48,50,52'}
k = {'id':6 , 'name':"Shirt", 'money': 150 , 'color':'red' , 'size': '44,46,48,50,52'}

if __name__=='__main__': 
    user1 = {'name':'s' ,'password': 's'}
    user2 = {'name':'saba' ,'password': 's456'}
    manage_user = LinkedList_login()
    manage_user.insert_first(user1)
    manage_user.insert_first(user2)
    while True :
        os.system("cls")
        print('~~~~~~~~~~~~ by Team 6 ~~~~~~~~~~~~~~ '+ '\n')
        print('\n  1) Log in'+ '\n  2) sing Up' +'\n  3) Exite')
        key1 = input("Choose one(1,2,3): ")
        if key1 == '1':
            os.system("cls")
            usr = input("User name:")
            password = input("password:")
            if manage_user.login(usr, password) is not None:
                os.system("cls")
                llist = LinkedList()
                llist.insert_first(a); 
                llist.insert_first(c); 
                llist.insert_first(d); 
                llist.insert_first(b); 
                llist.insert_first(e)
                while True :
                    os.system("cls")
                    print(f'you are log in ~{usr}~ account')
                    print("   -------MENU-------"+ '\n'+'  --1) Show all'+'\n  --2) Adding'+ '\n  --3) Searching'+ '\n  --4) Deleting')
                    key2 = input("\nChoose one(1,2,3,4): ")
                    

                    if key2 == '1' :
                        os.system("cls")
                        llist.printListall()
                        
                        print('\n')
                        go_back = input('Go Back white(b): ')
                        if go_back == "b":
                            continue



                    elif key2 == '2':
                        os.system("cls")
                        print("Which option do you want to choose?")
                        print('  1) insert first list'+ '\n  2) adding between two data'+ '\n  3) insert End list')
                        key3 = input("option:")


                        if key3 == '1':
                            os.system("cls")
                            id_data = int(input ("write id number: "))
                            name = input("write name of clothing: ")
                            color = input('write color: ')
                            money = int(input("write Money: "))
                            size = input("write range of size: ")
                            new_data = {'id':id_data ,'name':name, 'money':money , 'color':color , 'size':size }

                            if llist.search_id(id_data) is None:
                                llist.insert_first(new_data)
                                llist.printListall()
                            else:
                                print("~ There is already such an ID. So you can not save the same ID")
                            go_back = input('\nGo Back white(b): ')
                            if go_back == "b":
                                continue

                        
                        elif key3 == '2':
                            os.system("cls")
                            prev_id = int(input("write the desired ID:"))
                            id_data = int(input ("write id number: "))
                            name = input("write name of clothing: ")
                            color = input('write color: ')
                            money = int(input("write Money: "))
                            size = input("write range of size: ")
                            new_data = {'id':id_data ,'name':name, 'money':money , 'color':color , 'size':size }
                            if llist.search_id(id_data) is None:
                                llist.adding(prev_id , new_data)
                                llist.printListall()
                            else:
                                print("~ There is already such an ID. So you can not save the same ID")
                            go_back = input('\nGo Back white(b): ')
                            if go_back == "b":
                                continue
                                
                        

                        elif key3 == '3':
                            os.system("cls")
                            id_data = int(input ("write id number: "))
                            name = input("write name of clothing: ")
                            color = input('write color: ')
                            money = int(input("write Money: "))
                            size = input("write range of size: ")
                            new_data = {'id':id_data ,'name':name, 'money':money , 'color':color , 'size':size }
                            if llist.search_id(id_data) is None:
                                llist.insert_end(new_data)
                                llist.printListall()
                            else:
                                print("~ There is already such an ID. So you can not save the same ID")
                            go_back = input('\nGo Back white(b): ')
                            if go_back == "b":
                                continue


                                
                    elif key2 == '3':
                        os.system("cls")
                        print("Which option do you want to choose?")
                        print('  1) Search by ID'+ '\n  2) Search by name'+ '\n  3) Search by color' + '\n  4) Search by money' + '\n  5) Search by range of money' +
                        '\n  6) Search by size' )
                        key4 = input("option:")
                        if key4 == '1':
                            os.system("cls")
                            search_id = int(input("write 'ID' for searching: "))
                            if llist.search_id(search_id):
                                print(llist.search_id(search_id))
                            else :
                                print("There is no such ID :( ")
                            go_back = input('\nGo Back white(b): ')
                            if go_back == "b":
                                continue


                        elif key4 == '2':
                            os.system("cls")
                            name = input("write 'Name' for searching: ")
                            if llist.search_name(name):
                                print(llist.search_name(name))
                            else :
                                print("There is no such Name :(")
                            go_back = input('\nGo Back white(b): ')
                            if go_back == "b":
                                continue

                        elif key4 == '3':
                            os.system("cls")
                            color = input("write 'Color' for searching: ")
                            if llist.search_color(color):
                                print(llist.search_color(color))
                            else :
                                print("There is no such color :(")
                            go_back = input('\nGo Back white(b): ')
                            if go_back == "b":
                                continue

                        elif key4 == '4':
                            os.system("cls")
                            money = int(input("write 'Money' for searching: "))
                            if llist.search_money(money):
                                print(llist.search_money(money))
                            else :
                                print("There is no such Money :(")
                            go_back = input('\nGo Back white(b): ')
                            if go_back == "b":
                                continue

                        elif key4 == '5':
                            os.system("cls")
                            first = int(input("write first for searching range: "))
                            end = int(input("write end for searching range: "))
                            if llist.search_sort_money(first,end):
                                print(llist.search_sort_money(first , end))
                            else :
                                print("There is no such Money :(")
                            go_back = input('\nGo Back white(b): ')
                            if go_back == "b":
                                continue

                        elif key4 == '6':
                            os.system("cls")
                            size = input("write 'Size' for searching: ")
                            if llist.search_size(size):
                                print(llist.search_size(size))
                            else :
                                print("There is no such Size :(")
                            go_back = input('\nGo Back white(b): ')
                            if go_back == "b":
                                continue


                    elif key2 == '4':
                        os.system("cls")
                        print('   1) Deleting' + '\n   2) Shopping')
                        key5 = input("option:")
                        if key5 == '1':
                            os.system("cls")
                            llist.printListall()
                            print('\n\n')
                            id_delet = int(input("write 'ID' for Delete: "))
                            print('\n\n')
                            if llist.search_id(id_delet):
                                llist.deleteNode(id_delet)
                                print("It was successful")
                                print('\n\n')
                                llist.printListall()
                            else:
                                print('~ Sorry, We do not have such a ID :(')
                            go_back = input('\nGo Back white(b): ')
                            if go_back == "b":
                                continue


                        elif key5 == '2':
                            os.system("cls")
                            llist.printListall()
                            print('\n\n')
                            id_shop = int(input("write 'ID' for Delete: "))
                            size = input("wite 'Size' for buying")
                            if llist.search_size(size):
                                llist.shopping(id_shop , size)
                                print("It was successful")
                                print('\n\n')
                                llist.printListall()
                            else:
                                print('~ Sorry, We do not have such a size :(')
                            go_back = input('\nGo Back white(b): ')
                            if go_back == "b":
                                continue
                    
                    
        
        
        elif key1 == '2':
            usr = input("User name:")
            password1 = input("password:")
            password2 = input("wite agine password:")
            if password1 == password2:
                new_user = {'name': usr , 'password': password2}
                if manage_user.sing_up(new_user):
                    print("\nwelcome your Accunt\n")
                else:
                    print("\nplz write another user\n")
                
                print()
                
            else:
                print("\nwrite the password correctly!!\n\n")
            go_back = input('Go Back white(b): ')
            if go_back == "b":
                continue

        elif key1 == '3':
            exit()
             