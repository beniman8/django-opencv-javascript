from random import choices
from django.db import models
from .utils import get_filtered_image
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO  # we use this to make the processe faster 
from django.core.files.base import ContentFile

ACTION_CHOICE = (
    ("NO_FILTER", "no filter"),
    ("COLORIZED", "colorized"),
    ("GRAYSCALE", "grayscale"),
    ("BLURRED", "blurred"),
    ("BINARY", "binary"),
    ("INVERT", "invert"),
)


class Upload(models.Model):

    image = models.ImageField(upload_to="images")
    action = models.CharField(max_length=50,choices=ACTION_CHOICE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.id}"

    def save(self, *args, **kwargs) -> None:

        # open image
        pil_img = Image.open(self.image)

        # convert the image to array and do some processing
        cv_img = np.array(pil_img)
        img = get_filtered_image(cv_img, self.action)

        #convert back to pil image

        im_pil = Image.fromarray(img)


        #save
        buffer = BytesIO()
        im_pil.save(buffer,format='png')


        image_png = buffer.getvalue()

        self.image.save(f"{self.image}",ContentFile(image_png),save=False)

        super().save(*args, **kwargs)

 
