from django.db.models import *
from datetime import datetime
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from mysite.settings import MEDIA_ROOT

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

class BooksImage(Model):
    small_image = ImageField(upload_to=MEDIA_ROOT)
    large_image = ImageField(blank=True, null=True, upload_to=MEDIA_ROOT)
    img_id = PositiveIntegerField()
    link_book = ForeignKey(Book)
    cont_type = ForeignKey(ContentType)
    cont_obj = generic.GenericForeignKey("cont_type", "img_id")

    def __unicode__(self):
        return '%s' % self.id

    def img_count(self):
        count = 0
        if self.small_img:
            count += 1
        if self.large_img:
            count += 1
        return '%s' % count

    def view_small_image(self):
        return u'<img src="%s"/>' % (self.small_image.url)

    view_small_image.allow_tags = True

    def view_large_image(self):
        return u'<img src="%s"/>' % (self.large_image.name)

    view_large_image.allow_tags = True
