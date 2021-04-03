class Cart:
    def __init__(self,request):
        self.request=request
        self.session=request.session
        cart=self.session.get('cart')
        if not cart:
            cart=self.session['cart']={}
        else:
            self.cart=cart

    def add(self, product):
        if str(product.id) not in self.cart.keys():
            self.cart[product.id]={
                'id':product.id,
                'name':product.name,
                'price':str(product.price),
                'image':product.image.url,
                'quantity':1,
            }
        else:
            self.cart[product.id]['quantity']+=1
            '''for key, value in self.cart.items():
                if key==product.id:
                    value['quantity']=value['quantity']+1
                    break'''
        self.save_cart()

    def save_cart(self):
        self.session['cart']=self.cart
        self.session.modified=True

    def delete(self, product):
        if str(product.id) in self.cart.keys():
            del self.cart[product.id]
            self.save_cart()

    def remove_unit(self, product):
        if str(product.id) in self.cart.keys():
            if self.cart[product.id]['quantity'] == 1:
                del self.cart[product.id]
            else:
                self.cart[product.id]['quantity']-=1
            self.save_cart()

    def clear(self):
        cart=self.session['cart']={}
        self.session.modified=True
