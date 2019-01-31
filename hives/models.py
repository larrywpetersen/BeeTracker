from django.db import models

import datetime
import pytz

from django.urls import reverse

class Hive(models.Model):
    id = models.AutoField(primary_key=True)
    date_entered = models.DateTimeField(auto_now=True)
    label = models.CharField(max_length=50 ,default='')
    hive_from = models.CharField(max_length=50 ,default='')
    queen_year = models.IntegerField(default=2019)
    queen_breed = models.ForeignKey('Breed', on_delete=models.PROTECT)
    queen_from = models.CharField(max_length=50 ,default='')
    location = models.CharField(max_length=50 ,default='')
    brood_boxes = models.IntegerField(default=1)
    supers = models.IntegerField(default=1)

    def __str__(self):
        # https://howchoo.com/g/ywi5m2vkodk/working-with-datetime-objects-and-timezones-in-python
        de = self.date_entered.astimezone(pytz.timezone('US/Mountain'))
        return '<%s> Hive "%s", from %s, '  \
               'Queen(%i, %s, from %s), ' \
               'at %s, %i brood box(es), %i super(s), entered on %s.' \
               % (self.id, self.label, self.hive_from,
               self.queen_year, self.queen_breed.name, self.queen_from,
               self.location, self.brood_boxes, self.supers, de.strftime('%c'))



class Breed(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default='')

    def __str__(self):
        return '<%s> %s' % (self.id, self.name)




# class HiveLog(models.Model):
    # id = models.AutoField(primary_key=True)






#  dates  Tues - Fri Apr 16 - 19 6:30 - 9:00   Sat 20th  2:00 - 7:00

#  exit  through NW door


