import unittest
from app.models import User,Wallet
from app import db

class WalletTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the class
    '''

    def setUp(self):
        self.user_wiko = User(username='wiko', password='banana', email='wiko@ms.com')  
        self.wallet = Wallet(total=1000,user_id=self.user_wiko.id)
      

    def tearDown(self):
       Wallet.query.delete()
       User.query.delete()
      
       
    def test_instance(self):
        self.assertTrue(isinstance(self.wallet,Wallet))
        
        
    def test_check_instance_variables(self):
        self.assertEquals(self.wallet.total,1000)
        self.assertEquals(self.wallet.user_id,self.user_wiko.id)
       
    def test_save_wallet(self):
        self.wallet.save_wallet()
        self.assertTrue(len(Wallet.query.all()) > 0)