from typing import Protocol

class PaymentMethod (Protocol):

    def authorize_payment(self , amount : float) -> bool :
        ...
    def process_payment(self , amount : float) -> bool :
        ...

class CreditCardPayment :

    def authorize_payment(self , amount : float) -> bool :
        print (f"Authorizing credit card payment of $ {amount}")

        return True
    
    def process_payment(self , amount : float) -> bool :
        print(f"Processing credit card payment of $ {amount}")

        return True

class PayPalPayment :

    def authorize_payment(self , amount : float) -> bool :
        print (f"Authorizing PayPal payment of $ {amount}")

        return True
    
    def process_payment(self , amount : float) -> bool :
        print(f"Processing PayPal payment of $ {amount}")
        
        return True
    

def process_order (payment : PaymentMethod , amount : float):

    if payment.authorize_payment(amount):

        payment.process_payment(amount)
        print("succes")

    else :

        print("autorized fail")

credit_card_payment = CreditCardPayment()

pay_pal = PayPalPayment()

process_order(credit_card_payment , 1000.0 )

process_order(pay_pal , 2000.0)

