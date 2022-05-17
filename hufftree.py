class Tree:

    def __init__ (self,left,right,mid):

        self.left=left
        self.right=right
        self.mid=mid
 # getter and setter functions for mid node
    def get_mid(self):
        return self.mid
    
    def set_mid(self,val):
        self.mid = val

 # getter setter functions for right node
    def get_right(self):
        return self.right

    def set_right(self,val):
        self.right=val

 # getter setter functions for left node
    def get_left(self):
        return self.left

    def set_left(self,val):
        self.left = val

