from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from ..requests import get_currencies,get_currency_rates
from .forms import UpdateProfile, ConversionForm,TransactForm
from ..models import User,Wallet,Transaction
from .. import db,photos

from flask_login import login_required,current_user

@main.route('/')

def index():

    '''
    View root page function that returns the index page and its data
    '''
 
    title = 'Home - CurrencyApp'
   

    return render_template('main/index.html')

@main.route('/convert',methods=["POST","GET"])

def conversion():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - CurrencyApp'
    result = 0.00
    
   
    form = ConversionForm()

    if form.validate_on_submit():   
   
        amount = form.amount.data
        fromCurr = form.fromCurr.data
        toCurr = form.toCurr.data
         
        rates = get_currency_rates(fromCurr,toCurr)
        rate = rates.get(f"{fromCurr}_{toCurr}")
       
        result = (int(amount) * rate)
        print(rate)
        print(result)
        
                
              
        return render_template('main/convert.html',result=result,rates=rates,form=form)
   
    return render_template('main/convert.html',result=result, form=form)

@main.route('/transactions')
@login_required
def transaction():
    
  
   
    return render_template('main/transact.html')


@main.route('/send_funds',methods=["POST","GET"])
def send_funds():
    
    people = []
    users = User.query.filter(User.username!=current_user.username)
    for user in users:
        people.append(user.username)
  
    
    if request.method == "POST":
        name = request.form.get('user')
        
        amount = request.form.get('amount')
        user_id= current_user._get_current_object().id
     
       
        
        user_current = User.query.get(user_id)
      
        wallet = Wallet.query.get(user_current.id)
        first_amount = (wallet.total - int(amount))
        wallet.total = first_amount
        db.session.commit()
       
        
        transaction_amount = int(amount)
        wallet = Wallet.query.get(user_current.id)
        transaction = Transaction(type="debit",amount=transaction_amount,user_id=user_current.id,wallet_id=wallet.id)
        db.session.add(transaction)
        db.session.commit()
       
        
        user_receiver = User.query.filter_by(username=name).first()
        wallet = Wallet.query.get(user_receiver.id)
        rates = get_currency_rates(user_current.currency,user_receiver.currency)
        rate = rates.get(f"{user_current.currency}_{user_receiver.currency}")
        second_amount = (rate * int(amount)) + wallet.total
        wallet.total = second_amount
        db.session.commit()
       
       
        wallet = Wallet.query.get(user_receiver.id)
        transaction = Transaction( type="credit",amount = (rate * int(amount)),user_id= user_receiver.id,wallet_id=wallet.id)
        db.session.add(transaction)
        db.session.commit()
        
        
        
        return redirect(url_for('main.profile',uname=user_current.username))
 
    return render_template('main/send.html',people=people)

@main.route('/credit',methods=["POST","GET"])
def credit():
     
    form =TransactForm()
    
    if form.validate_on_submit():  
                
        amount = form.amount.data
        form_currency = form.currency.data
        
        user_id= current_user._get_current_object().id     
        user_current = User.query.get(user_id)
        
        rates = get_currency_rates(form_currency, user_current.currency)
        rate = rates.get(f"{form_currency}_{ user_current.currency}")
       
        result = (int(amount) * rate)
        
        
        
        wallet = Wallet.query.get(user_current.id)
        total_amount = (wallet.total + int(result))
        wallet.total = total_amount
        db.session.commit()
       
        
        transaction_amount = int(amount)
        wallet = Wallet.query.get(user_current.id)
        transaction = Transaction(type="credit",amount=transaction_amount,user_id=user_current.id,wallet_id=wallet.id)
        db.session.add(transaction)
        db.session.commit()
      
       
        
        
        return redirect(url_for('main.profile',uname=user_current.username))
 
    return render_template('main/credit.html',form=form)


@main.route('/debit',methods=["POST","GET"])
def debit():
      
    form =TransactForm()
    if form.validate_on_submit(): 
             
        amount = form.amount.data
        form_currency = form.currency.data
        
        
        user_id= current_user._get_current_object().id     
        user_current = User.query.get(user_id)
        
        
        rates = get_currency_rates(form_currency, user_current.currency)
        rate = rates.get(f"{form_currency}_{ user_current.currency}")
       
        result = (int(amount) * rate)
        
        wallet = Wallet.query.get(user_current.id)
        total_amount = (wallet.total - int(result))
        wallet.total = total_amount
        db.session.commit()
       
        transaction_amount = int(amount)
        wallet = Wallet.query.get(user_current.id)
        transaction = Transaction(type="debit",amount=transaction_amount,user_id=user_current.id,wallet_id=wallet.id)
        db.session.add(transaction)
        db.session.commit()
      
        
        return redirect(url_for('main.profile',uname=user_current.username))
 
    return render_template('main/debit.html',form=form)







@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)
    wallet = Wallet.query.filter_by(user_id = user.id).first()
  

    return render_template("profile/profile.html", user = user,wallet=wallet)




@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        wallet = Wallet.query.get(user.id)
        amount = wallet.total
        
        rates = get_currency_rates(user.currency,form.currency.data)
        rate = rates.get(f"{user.currency}_{form.currency.data}")
       
        result = (int(amount) * rate)
        wallet.total = result
        db.session.commit()
                
        user.bio = form.bio.data
        user.currency = form.currency.data

        db.session.add(user)
        db.session.commit()
        
        

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
