from django.db import models

# Create your models here.

class register(models.Model):
	username=models.Charfield(max_length=8)
	atmpin=models.IntegerField(max_length=4)
def _str_(self):
	return self.name

class authentication(models.Model):
	username=models.ForeignKey(register, on delete=models.CASCADE)
	atmpin=models.ForeignKey(register, on delete=models.CASCADE)

class deposit(models.Model):
	bank_account_no=models.IntegerField(max_length=10)
	deposit_amount=models.IntegerField(max_length=10)
	atmpin=models.ForiegnKey(register, on delete=models.CASCADE)
def _str_(self):
	return self.name

class withdraw(models.Model):
       withdraw_amount=models.IntegerField(max_length=10)
       bank_account_no=ForiegnKey(deposit, on delete=models.CASCADE)	

	