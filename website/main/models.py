from django.db import models
from datetime import date
from django.contrib.auth.models import User

class Day(models.Model):
      date = models.DateField(default=date.today)
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      def __str__(self):
            return f'{self.date}'



class Task(models.Model):
      title = models.CharField(max_length=200)
      completed = models.BooleanField(default=False)
      day = models.ForeignKey(Day, on_delete=models.CASCADE)

      def __str__(self):
            return self.title

class DefaultDay(models.Model):
      WEEK_DAYS = (
      (0, 'Monday'),
      (1, 'Tuesday'),
      (2, 'Wednesday'),
      (3, 'Thursday'),
      (4, 'Friday'),
      (5, 'Saturday'),
      (6, 'Sunday'),
      )
      week_day = models.IntegerField(choices=WEEK_DAYS)
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      def __str__(self):
            return self.get_week_day_display()




class DefaultTask(models.Model):
      title = models.CharField(max_length=200)
      defaultday = models.ForeignKey(DefaultDay, on_delete=models.CASCADE)

      def __str__(self):
            return self.title

