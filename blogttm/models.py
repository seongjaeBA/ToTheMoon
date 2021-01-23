from django.db import models
from django.conf import settings
from django.urls import reverse
# import uuid

# Create your models here.
'''
Common field arguments
help_text: Provides a text label for HTML forms (e.g. in the admin site), as described above.
verbose_name: A human-readable name for the field used in field labels. If not specified, Django will infer the default verbose name from the field name.
default: The default value for the field. This can be a value or a callable object, in which case the object will be called every time a new record is created.
null: If True, Django will store blank values as NULL in the database for fields where this is appropriate (a CharField will instead store an empty string). The default is False.
blank: If True, the field is allowed to be blank in your forms. The default is False, which means that Django's form validation will force you to enter a value. This is often used with null=True , because if you're going to allow blank values, you also want the database to be able to represent them appropriately.
choices: A group of choices for this field. If this is provided, the default corresponding form widget will be a select box with these choices instead of the standard text field.
primary_key: If True, sets the current field as the primary key for the model (A primary key is a special database column designated to uniquely identify all the different table records). If no field is specified as the primary key then Django will automatically add a field for this purpose.
'''

''' Field Types(OneToOneField, ForeignKey, ManyToManyField)
CharField is used to define short-to-mid sized fixed-length strings. You must specify the max_length of the data to be stored.
TextField is used for large arbitrary-length strings. You may specify a max_length for the field, but this is used only when the field is displayed in forms (it is not enforced at the database level).
IntegerField is a field for storing integer (whole number) values, and for validating entered values as integers in forms.
DateField and DateTimeField are used for storing/representing dates and date/time information (as Python datetime.date in and datetime.datetime objects, respectively). These fields can additionally declare the (mutually exclusive) parameters auto_now=True (to set the field to the current date every time the model is saved), auto_now_add (to only set the date when the model is first created) , and default (to set a default date that can be overridden by the user).
EmailField is used to store and validate email addresses.
FileField and ImageField are used to upload files and images respectively (the ImageField adds additional validation that the uploaded file is an image). These have parameters to define how and where the uploaded files are stored.
AutoField is a special type of IntegerField that automatically increments. A primary key of this type is automatically added to your model if you don’t explicitly specify one.
ForeignKey is used to specify a one-to-many relationship to another database model (e.g. a car has one manufacturer, but a manufacturer can make many cars). The "one" side of the relationship is the model that contains the "key" (models containing a "foreign key" referring to that "key", are on the "many" side of such a relationship).
ManyToManyField is used to specify a many-to-many relationship (e.g. a book can have several genres, and each genre can contain several books). In our library app we will use these very similarly to ForeignKeys, but they can be used in more complicated ways to describe the relationships between groups. These have the parameter on_delete to define what happens when the associated record is deleted (e.g. a value of models.SET_NULL would set the value to NULL).
'''

''' 기본 모델
class MyModelName(models.Model):
    """A typical class defining a model, derived from the Model class."""
    # Fields
    my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')
    ...
    # Metadata : (-) 기호는 default sorting attribute
    class Meta:
        ordering = ['-my_field_name']
    # Methods : view 등록 해야함
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.my_field_name
'''
class BlogTTM(models.Model):
    my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')
    ...
    class Meta:
        ordering = ['-my_field_name']
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.my_field_name

class PostSubject(models.Model):
    name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

    """글쓰기 모델"""
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,verbose_name='작성자' )
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    post_subject = models.ManyToManyField(PostSubject)   

    class Meta:
        abstract = True
        ordering = ['-created_date']
    
    def get_absolute_url(self):
        return reverse("post-list", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.title

class DjangoContents(Post):
    ...

class Git(Post):
    ...

class DataAnalysis(Post):
    SUBJECT = (
    ('db', 'DataBase'),
    ('v', 'Visualization'),
    ('i', 'IBM'),
    ('o', 'Oracle'),
    ('b', 'Basic'),
    )

    subject = models.CharField(
        max_length=2,
        choices=SUBJECT,
        blank=True,
        default='b',
    )


class CaseStudy(Post):
    ...
    
class Cloud(Post):
    SUBJECT = (
    ('a', 'AWS'),
    ('g', 'GCP'),
    ('i', 'IBM'),
    ('o', 'Oracle'),
    ('c', 'Container'),
    ('b', 'Basic'),
    )

    subject = models.CharField(
        max_length=2,
        choices=SUBJECT,
        blank=True,
        default='b',
    )    