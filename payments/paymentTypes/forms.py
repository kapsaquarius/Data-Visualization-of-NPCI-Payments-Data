from django import forms

PAYMENT= [
   ('UPI','UPI'),('POS','POS'),('NFS','NFS'),('NETC-VAL','NETC-VAL'),('NETC-VOL','NETC-VOL')
]

YEAR= [
   ('2017','2017'),('2018','2018'),('2019','2019'),('2020','2020')
]

MONTH=[
	('January','January'),('February','February'),('March','March'),('April','April'),('May','May'),
	('June','June'),('July','July'),('August','August'),('September','September'),('October','October'),
	('November','November'),('December','December')
]

class filterData(forms.Form):
	year = forms.ChoiceField(label='Select Year',choices=YEAR,widget=forms.Select(choices=YEAR), required=True)
	month = forms.ChoiceField(label='Select Month',choices=MONTH,widget=forms.Select(choices=MONTH), required=True)
	payment = forms.ChoiceField(label='Select Mode of Payment',choices=PAYMENT,widget=forms.Select(choices=PAYMENT), required=True)

