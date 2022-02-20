from django.db import models
import reversion
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE
from django.contrib.auth.models import User

@reversion.register()
class KeyPairsTraining(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    class Meta:
        db_table = 'key_pairs_trining'

    keys = models.CharField( blank=False, null=False,unique=True,max_length=16)
    flight_time = models.IntegerField(blank=True, null=True)
    hold_time1 =models.IntegerField( blank=True, null=True)
    presure_up1 = models.DecimalField( blank=True, null=True,max_digits=20,decimal_places=4)
    presure_down2 = models.DecimalField( blank=True, null=True,max_digits=20,decimal_places=4)
    presure_size_up1 = models.DecimalField( blank=True, null=True,max_digits=20,decimal_places=4)
    presure_size_down2 = models.DecimalField( blank=True, null=True,max_digits=20,decimal_places=4)
    coordinateX_up1 = models.DecimalField( blank=True, null=True,max_digits=20,decimal_places=4)
    coordinateY_up1 = models.DecimalField( blank=True, null=True,max_digits=20,decimal_places=4)
    coordinateX_down2 = models.DecimalField( blank=True, null=True,max_digits=20,decimal_places=4)
    coordinateY_down2 = models.DecimalField( blank=True, null=True,max_digits=20,decimal_places=4)

    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE,
                                       related_name="fk_key_pairs_training_user")

    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_edited = models.DateTimeField(auto_now=True, null=True)
   
    def __str__(self):
        return self.keys

@reversion.register()
class KeyTraining(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    class Meta:
        db_table = 'key_trining'

    key = models.CharField( blank=False, null=False,unique=True,max_length=16)
    hold_time = models.IntegerField(blank=True, null=True)
    presure_up = models.DecimalField( blank=True, null=True,max_digits=20,decimal_places=4)
    presure_down = models.DecimalField( blank=True, null=True,max_digits=20,decimal_places=4)
    finger_size_up = models.DecimalField( blank=True, null=True,max_digits=20,decimal_places=4)
    finger_size_down = models.DecimalField( blank=True, null=True,max_digits=20,decimal_places=4)
    coordinateX_up = models.DecimalField( blank=True, null=True,max_digits=20,decimal_places=4)
    coordinateY_up = models.DecimalField( blank=True, null=True,max_digits=20,decimal_places=4)
    coordinateX_down = models.DecimalField( blank=True, null=True,max_digits=20,decimal_places=4)
    coordinateY_down = models.DecimalField( blank=True, null=True,max_digits=20,decimal_places=4)

    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE,
                                       related_name="fk_key_training_user")

    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_edited = models.DateTimeField(auto_now=True, null=True)
   
    def __str__(self):
        return self.key