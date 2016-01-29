from django.db import models
from django.contrib.auth.models import User
import datetime


class Thread(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    participants = models.ManyToManyField(User)
    last_message = models.DateTimeField(null=True, blank=True, auto_now_add=True)

    def save(self, *args, **kwargs):
        super(Thread, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name if self.name else '%s %s' % (self.id, self.last_message)


class Message(models.Model):
    text = models.TextField()
    sender = models.ForeignKey(User)
    thread = models.ForeignKey(Thread)
    datetime = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super(Message, self).save(*args, **kwargs)
        self.thread.last_message = datetime.datetime.now()
        self.thread.save()

    def __unicode__(self):
        return '%s ***[%s]*** %s' % (self.sender, self.thread, self.datetime)

