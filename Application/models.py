from __future__ import unicode_literals
from django.db import models
from datetime import date
from django.contrib.auth.models import User


class BloodGroup(models.Model):
	blood_group=models.CharField(max_length=250, verbose_name="Blood Group")
	def __str__(self):
		return self.blood_group

class DonarRegistation(User):

	# blood_id=models.ForeignKey(BloodGroup)
	name=models.CharField(max_length=250, verbose_name='Name')
	addrees=models.CharField(max_length=250, verbose_name='Address')
	cell_no=models.CharField(max_length=250, verbose_name='Phone Number')
	blood_group=models.CharField(max_length=250, verbose_name='Blood Group')

	# pic=models.FileField()

class Post(models.Model):
	name=models.CharField(max_length=225)
	location=models.CharField(max_length=225)
	blood_id=models.ForeignKey(BloodGroup)
	date = models.DateField(default=date.today)
