from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SelectField,SubmitField,IntegerField
from wtforms.fields.core import DecimalField
from wtforms.validators import Required
from ..requests import get_currencies

CURRENCY_CHOICES = [('ALL','ALL'),('XCD','XCD'),('EUR','EUR'),('BBD','BBD'),('BTN','BTN'),('BND','BND'),('XAF','XAF'),('CUP','CUP'),('USD','USD'),('FKP','FKP'),('GIP','GIP'),('HUF','HUF'),('IRR','IRR'),('JMD','JMD'),('AUD','AUD'),('LAK','LAK'),('LYD','LYD'),('MKD','MKD'),('XOF','XOF'),('NZD','NZD'),('OMR','OMR'),('PGK','PGK'),('RWF','RWF'),('WST','WST'),('RSD','RSD'),('SEK','SEK'),('TZS','TZS'),('AMD','AMD'),('BSD','BSD'),('BAM','BAM'),('CVE','CVE'),('CNY','CNY'),('CRC','CRC'),('CZK','CZK'),('ERN','ERN'),('GEL','GEL'),('HTG','HTG'),('INR','INR'),('JOD','JOD'),('KRW','KRW'),('LBP','LBP'),('MWK','MWK'),('MRO','MRO'),('MZN','MZN'),('ANG','ANG'),('PEN','PEN'),('QAR','QAR'),('STD','STD'),('SLL','SLL'),('SOS','SOS'),('SDG','SDG'),('SYP','SYP'),('AOA','AOA'),('AWG','AWG'),('BHD','BHD'),('BZD','BZD'),('BWP','BWP'),('BIF','BIF'),('KYD','KYD'),('COP','COP'),('DKK','DKK'),('GTQ','GTQ'),('HNL','HNL'),('IDR','IDR'),('ILS','ILS'),('KZT','KZT'),('KWD','KWD'),('LSL','LSL'),('MYR','MYR'),('MUR','MUR'),('MNT','MNT'),('MMK','MMK'),('NGN','NGN'),('PAB','PAB'),('PHP','PHP'),('RON','RON'),('SAR','SAR'),('SGD','SGD'),('ZAR','ZAR'),('SRD','SRD'),('TWD','TWD'),('TOP','TOP'),('VEF','VEF'),('DZD','DZD'),('ARS','ARS'),('AZN','AZN'),('BYR','BYR'),('BOB','BOB'),('BGN','BGN'),('CAD','CAD'),('CLP','CLP'),('CDF','CDF'),('DOP','DOP'),('FJD','FJD'),('GMD','GMD'),('GYD','GYD'),('ISK','ISK'),('IQD','IQD'),('JPY','JPY'),('KPW','KPW'),('LVL','LVL'),('CHF','CHF'),('MGA','MGA'),('MDL','MDL'),('MAD','MAD'),('NPR','NPR'),('NIO','NIO'),('PKR','PKR'),('PYG','PYG'),('SHP','SHP'),('SCR','SCR'),('SBD','SBD'),('LKR','LKR'),('THB','THB'),('TRY','TRY'),('AED','AED'),('VUV','VUV'),('YER','YER'),('AFN','AFN'),('BDT','BDT'),('BRL','BRL'),('KHR','KHR'),('KMF','KMF'),('HRK','HRK'),('DJF','DJF'),('EGP','EGP'),('ETB','ETB'),('XPF','XPF'),('GHS','GHS'),('GNF','GNF'),('HKD','HKD'),('XDR','XDR'),('KES','KES'),('KGS','KGS'),('LRD','LRD'),('MOP','MOP'),('MVR','MVR'),('MXN','MXN'),('NAD','NAD'),('NOK','NOK'),('PLN','PLN'),('RUB','RUB'),('SZL','SZL'),('TJS','TJS'),('TTD','TTD'),('UGX','UGX'),('UYU','UYU'),('VND','VND'),('TND','TND'),('UAH','UAH'),('UZS','UZS'),('TMT','TMT'),('GBP','GBP'),('ZMW','ZMW'),('BTC','BTC'),('BYN','BYN'),('BMD','BMD'),('GGP','GGP'),('CLF','CLF'),('CUC','CUC'),('IMP','IMP'),('JEP','JEP'),('SVC','SVC'),('ZMK','ZMK'),('XAG','XAG'),('ZWL','ZWL')]

class ConversionForm(FlaskForm):

    amount = DecimalField('Amount',validators=[Required()])
    fromCurr = SelectField('Click to select your currency',choices=CURRENCY_CHOICES,validators=[Required()])
    toCurr = SelectField('Click to select your currency',choices=CURRENCY_CHOICES,validators=[Required()])
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    currency = SelectField('Click to select your currency',choices=CURRENCY_CHOICES,validators=[Required()])
    
    submit = SubmitField('Submit')
    
    
class TransactForm(FlaskForm):
    amount = DecimalField('Amount',validators=[Required()])
    currency = SelectField('Click to select your currency',choices=CURRENCY_CHOICES,validators=[Required()])
    submit = SubmitField('Submit')
    
    
