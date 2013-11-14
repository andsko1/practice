from books.models import Book
from books.models import Publisher
from books.models import Author
from django.contrib import admin
from books.models import BooksImage

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name', 'email')
	list_daisplay_links = ('last_name', 'first_name')
	ordering = ('last_name', 'first_name')

class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'publisher', 'publication_date')
	list_daisplay_links = ('title')
	search_fields = ['title']
	date_hierarchy = 'publication_date'
	fieldsets = (('Output data', {'classes': ('collapse'), 'fields': ('publisher', 'publication_date')}),)

	def image_count(self, img):
	        cnt = 0
	        for c in BooksImage.objects.filter(id=img.id):
	    		if c.small_image:
        	        	cnt += 1
            		if c.large_image:
                		cnt += 1
            	return cnt
	image_count.allow_tags = True

	def view_small_img(self, img):
        	link = ""
        	for c in BooksImage.objects.filter(id=img.id):
            		link = c.view_small_image()
            	return link
	view_small_img.allow_tags = True

	def view_large_img(self, img):
        	link = ""
        	for c in BooksImage.objects.filter(id=img.id):
            		link = c.view_large_image()
            	return link
	view_large_img.allow_tags = True

class PubAdmin(admin.ModelAdmin):
	fieldsets = (('Contact info', {'classes': ('collapse'), 'fields': ('country', 'city', 'address')}),)
	list_display = ('title', 'country', 'city')
	ordering = ('title',)
	list_filter = ('country', 'city')

class BooksImageAdmin(admin.ModelAdmin):
	list_display = ('id', 'link_book', 'view_small_image', 'view_large_image')
	

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PubAdmin)
admin.site.register(BooksImage, BooksImageAdmin)
