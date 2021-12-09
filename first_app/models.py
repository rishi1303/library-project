from django.contrib.auth.models import User
from django.db import models
from datetime import datetime, date, timedelta

class Fine(models.Model):
    book=models.CharField(max_length=100)
    book_id=models.CharField(max_length=10, unique=True)
    issue_date=models.DateField(auto_now_add=False, auto_now=False, blank=True)
    cur_date=models.DateField(auto_now_add=True, auto_now=False, blank=True)
    user_name = models.ForeignKey(User,on_delete=models.CASCADE)

    @property
    def total(self):
        t=date.today()
        r=t-self.issue_date
        if r.days > 15:
            f = r.days - 15
            return f
        else:
            f=0
            return f

    @property
    def tplus(self):
        a = self.issue_date + timedelta(days=15)
        return a
