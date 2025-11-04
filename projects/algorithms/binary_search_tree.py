'''
Create a data structure that can store 100 million records and perform
insertion
search
update 
list
i/p's username, name and email.
'''



from logging_config import get_logger

logger = get_logger(__name__)

class User:
    counter = 0
    def __init__(self,username,name,email):
        self.counter += 1
        self.username = username
        self.name = name
        self.email = email
        print('user created')

    def __repr__(self):
        return "User(username = {}, name = {}, email = {})".format(self.username,self.name,self.email)
    
    def __str__(self):
        return "User(name = {}, email = {})".format(self.name,self.email)

class UserDatabase:

    def __init__(self):
        self.users = []
        print('DB created')

    def insert(self, user):
        i = 0
        while i < len(self.users):
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)

    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user
            
    def update(self, user):
        target = self.find(user.username)
        target.name , target.email = user.name, user.email
    
    def list_all(self):
        return self.users


'''Binary Tree for optimization as the above algorithm is O(N) and can be optimized.
Has two child nodes if not leaf node
left side smaller values and vice versa at every node
Tree map: keys with values
Balanced tree - both sided have a node
Height of tree k , the no of nodes at each level  - 2^k nodes, k <= log(N+1)'''

class BinaryTree():
    def __init__(self, key=None, value = None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    @staticmethod
    def parse_tuple(data):
        if isinstance(data, tuple) and len(data) == 3:
            node = BinaryTree(data[1])
            node.left = BinaryTree.parse_tuple(data[0])
            node.right = BinaryTree.parse_tuple(data[2])
            return node
        elif data is None:
            return None
        else:
            return BinaryTree(data)

    def to_tuple(self):
        if self is None:
            return None
        left_subtree = self.left.to_tuple() if self.left else None
        right_subtree = self.right.to_tuple() if self.right else None

        if left_subtree is None and right_subtree is None:
            return self.key
        return (left_subtree, self.key, right_subtree)

    def inorder_traversal(self,  result=[]):
        if result is None:
            result = []
        if self:
            
            if self.left:
                self.left.preorder_traversal(result)
            result.append(self.key)
            if self.right:
                self.right.preorder_traversal(result)
        return result

    def postorder_traversal(self):
        if self:
            if self.left:
                self.left.postorder_traversal()
            if self.right:
                self.right.postorder_traversal()
            print(self.key, end=' ')

    def preorder_traversal(self, result=None):
        if result is None:
            result = []
        if self:
            result.append(self.key)
            if self.left:
                self.left.preorder_traversal(result)
            if self.right:
                self.right.preorder_traversal(result)
        return result

    def print_tree(self, level=0, prefix="Root: "):
        if self is not None:
            print(" " * (level * 4) + prefix + str(self.key))
            if self.left:
                self.left.print_tree(level + 1, f"level {level}: - L--- ")
            if self.right:
                self.right.print_tree(level + 1, f"level {level}: - R--- ")

    def height(self):
        if self is None:
            return -1
        left_height = self.left.height() if self.left else -1
        right_height = self.right.height() if self.right else -1
        return 1 + max(left_height, right_height)
    
    def height_min(self):
        if self is None:
            return -1
        left_height = self.left.height() if self.left else -1
        right_height = self.right.height() if self.right else -1
        return 1 + min(left_height, right_height)

    def count_nodes(self):
        if self is None:
            return 0
        left_count = self.left.count_nodes() if self.left else 0
        right_count = self.right.count_nodes() if self.right else 0
        return 1 + left_count + right_count
    
    def is_bst(self, min_key=None, max_key=None):
        if self is None:
            return True
        current_key = str(self.key).lower()
        min_key = str(min_key).lower() if min_key is not None else None
        max_key = str(max_key).lower() if max_key is not None else None
        # Compare as strings if both keys are not None
        if min_key is not None and str(self.key) <= str(min_key):
            return False, None, None
        if max_key is not None and str(self.key) >= str(max_key):
            return False, None, None
        left_is_bst, left_min, left_max = self.left.is_bst(min_key, current_key) if self.left else (True, current_key, current_key)
        right_is_bst, right_min, right_max = self.right.is_bst(current_key, max_key) if self.right else (True, current_key, current_key)
        is_bst = left_is_bst and right_is_bst
        min_key = left_min if self.left else current_key
        max_key = right_max if self.right else current_key
        return is_bst, min_key, max_key
    
    def insert(self,key,value):
        if self is None:
            node = BinaryTree(key,value)
        elif self.key > key:
            if self.left is None:
                self.left = BinaryTree(key, value)
                self.left.parent = self
            else:
                self.left.insert(key, value)
        elif self.key < key:
            if self.right is None:
                self.right = BinaryTree(key, value)
                self.right.parent = self
            else:
                self.right.insert(key, value)
        return self
    
    '''
    Search the binary tree and determine the position of the key locate it and print the corresponding contents.

    Check the key with the node key and determine its position left / right tree.
    Recursively check the same until a match is found, if found print both the key and value.
    if nothing found print nothing.
    '''
    
    def find(self, key):
        if self.key is None:
            return 'No match'
        elif key == self.key:
            return self.value
        elif key < self.key:
            if self.left is None:
                return 'No match'
            return self.left.find(key)
        else:
            if self.right is None:
                return 'No match'
            return self.right.find(key)
        
    '''
    update the binary search tree:
    Check the binary search tree and find a ket and update its value accordingly and print the result.
    To do:

    '''
    def update(self, key, value):
        if self.key is None:
            print('No match')
        elif key == self.key:
             self.value = value
             return self.value
        elif key < self.key:
            if self.left is None:
                return 'No match'
            return self.left.update(key, value)
        else:
            if self.right is None:
                return 'No match'
            return self.right.update(key, value)
    '''
    Delete key:
    Check the BST if the key exists then delete the key and its corresponding value
    check the key and depending on the same subtree
    1. To be deleted node has no nodes - simply delete.
    2. To be deleted node has only one tree either left or right - delete the node and move it up the 
    '''
    def delete( self, key):
        if self.key is None:
            print('No match')
        elif self.key == key and self.key.left == None and self.key.right == None:
            self.key = None
            return self.key
        elif self.key == key and self.key.left == None and self.key.right != None:
            self.key = self.key.right
            self.value = self.right.value
            self.left = self.right.left
            self.right = self.right.right
        elif self.key == key and self.key.left != None and self.key.right == None:
            self.key = self.key.left
            self.value = self.left.value
            self.right = self.left.right
            self.left = self.left.left
        elif self.key == key and self.key.left != None and self.key.right != None:
            self.key = self.right.key
            self.value = self.right.value
            self.left = self.right.left
            self.right = self.right.right
        else:
            if key < self.key:
                self.left.delete(key)
            else:
                self.right.delete(key)

    def list_all(self):
        result = []
        self.inorder_traversal(result)
        return result
    
    '''
    Function to determine whether a BST is balanced or not
    1. Left subtree is balanced
    2. Right subtree is balanced
    3. Difference of heights b/n both the tree is not more than 1
    '''
    def is_balanced(self):
        def check_balance(node):
            if node is None:
                return 0, True
            left_height, left_balanced = check_balance(node.left)
            right_height, right_balanced = check_balance(node.right)
            current_height = 1 + max(left_height, right_height)
            is_balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
            return current_height, is_balanced

        _, balanced = check_balance(self)
        return balanced
    

        

raman = User('raman','v l r ramanraj','ramanraj33')
raman1 = User('raman1','v l r raman1raj','raman1raj33')
vydehi = User('vydehi','puppy','vydehio')
aakash = User('aakash','aaka','aakas')
#x = UserDatabase()
#x.insert(raman)
#x.insert(raman1)
#print(x.list_all())
#print(raman)
#tree_tuple = ((2, 3, None), 2, ((1, 2, None), 3, (6, 7, 8)))

'''
Lexiographical order, capital letters are always lesser than smaller case letters.
'''
tree_tuple_text = (('aakash', 'bvenkat', None),
    'cathila',
    (
        ('dbscina', 'evelyn', 'fascina'),
        'gilgamesh',
        ('hayagreeva', 'india', 'japan')
    )
)
bt = BinaryTree(raman.username,raman)
#text = bt.parse_tuple(tree_tuple_text)
bt.left = BinaryTree(aakash.username,aakash)
bt.left.parent = bt
bt.right = BinaryTree(raman1.username,raman1)
bt.right.parent = bt
bt.insert(vydehi.username,vydehi)
print(bt.height())
print(bt.find('sandeep'))
vydehi = User('vydehi','erri_puppy','vydehio')
bt.update('vydehi',vydehi)
print(bt.find('vydehi'))
#print(text.is_bst())
print(bt.is_balanced())
bt.print_tree()
















