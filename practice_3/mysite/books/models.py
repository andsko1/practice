from django.db.models import *
from datetime import datetime
# Create your models here.
class Author(Model):
  first_name = CharField(max_length=32)
  last_name = CharField(max_length=32)
  email = EmailField(null=True)

  def __unicode__(self):
    return u'%s %s' % (self.first_name, self.last_name)
  def get_absolute_url(self):
    return reverse('mysite.books.views.author', args=[str(self.id)])
 
class Publisher(Model):
  title = CharField(max_length=32)
  address = TextField()
  city = CharField(max_length=64)
  country = CharField(max_length=64)
  website = URLField()

  def __unicode__(self):
    return u'%s (%s, %s)' % (self.title, self.city, self.country)


class Book(Model):
  title = CharField(max_length=128)
  authors = ManyToManyField(Author)
  publisher = ForeignKey(Publisher)
  publication_date = DateField('Publication_date', default=datetime.now())

  def __unicode__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('mysite.books.views.book', args=[str(self.id)])
