from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class LikeItem(models.Model):
    # whose likeitem
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # generic type for likeditems
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE) # tpye of liked object
    content_id = models.PositiveIntegerField() # referencing that object 
    content_object = GenericForeignKey() # reading actual object 