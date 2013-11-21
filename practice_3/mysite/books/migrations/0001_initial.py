# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Author'
        db.create_table('books_author', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True)),
        ))
        db.send_create_signal('books', ['Author'])

        # Adding model 'Publisher'
        db.create_table('books_publisher', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('books', ['Publisher'])

        # Adding model 'Book'
        db.create_table('books_book', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('publisher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['books.Publisher'])),
            ('publication_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 11, 21, 0, 0))),
        ))
        db.send_create_signal('books', ['Book'])

        # Adding M2M table for field authors on 'Book'
        m2m_table_name = db.shorten_name('books_book_authors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('book', models.ForeignKey(orm['books.book'], null=False)),
            ('author', models.ForeignKey(orm['books.author'], null=False))
        ))
        db.create_unique(m2m_table_name, ['book_id', 'author_id'])

        # Adding model 'BooksImage'
        db.create_table('books_booksimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('small_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('large_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('img_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('link_book', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['books.Book'])),
            ('cont_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
        ))
        db.send_create_signal('books', ['BooksImage'])


    def backwards(self, orm):
        # Deleting model 'Author'
        db.delete_table('books_author')

        # Deleting model 'Publisher'
        db.delete_table('books_publisher')

        # Deleting model 'Book'
        db.delete_table('books_book')

        # Removing M2M table for field authors on 'Book'
        db.delete_table(db.shorten_name('books_book_authors'))

        # Deleting model 'BooksImage'
        db.delete_table('books_booksimage')


    models = {
        'books.author': {
            'Meta': {'object_name': 'Author'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'books.book': {
            'Meta': {'object_name': 'Book'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['books.Author']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publication_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 11, 21, 0, 0)'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['books.Publisher']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'books.booksimage': {
            'Meta': {'object_name': 'BooksImage'},
            'cont_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'large_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'link_book': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['books.Book']"}),
            'small_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'books.publisher': {
            'Meta': {'object_name': 'Publisher'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['books']