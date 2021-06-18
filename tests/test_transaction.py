import unittest
from app.models import User,Transaction,Wallet
from app import db

class WalletTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the class
    '''

    def setUp(self):
        self.user_wiko = User(username='wiko', password='banana', email='wiko@ms.com')  
        self.wallet = Wallet(total=1000,user_id=self.user_wiko.id)
        self.transaction = Transaction(type="credit",amount=1000,user_id=self.user_wiko.id,wallet_id=self.wallet.id)
      

    def tearDown(self):
       User.query.delete()
       Wallet.query.delete()
       Transaction.query.delete()
      
       
    def test_instance(self):
        self.assertTrue(isinstance(self.transaction,Transaction))
        
        
    def test_check_instance_variables(self):
        self.assertEquals(self.transaction.type,"credit")
        self.assertEquals(self.transaction.amount,1000)
        self.assertEquals(self.transaction.wallet_id,self.wallet.id)
        self.assertEquals(self.transaction.user_id,self.user_wiko.id)
       
    def test_save_transaction(self):
        self.transaction.save_transaction()
        self.assertTrue(len(Transaction.query.all()) > 0)