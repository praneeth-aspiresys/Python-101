class User :
     data =[ 'test',2,[3,4]]
     def getData(self):
        print(User.data)
 

class Product(User):
    def product():
         #super is to call parent 
         super().getData()
#Inheritance  
user =  User()
user.getData()

product = Product()
product.getData()
it = iter(user.data)
it
print('strt')
next(it)
print(1)
print('inside 1')
next(it)
print(2)


