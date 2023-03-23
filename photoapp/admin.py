from django.contrib import admin
from .models import Image
from PIL import Image as PI

class ImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'content')

    def save_model(self, request, obj, form, change):
        obj.writer = request.user
        obj.save()

        img = PI.open(obj.image.path)

        maxSize = 2048

        if img.width > img.height:
            width = maxSize
            height = int(maxSize * img.height / img.width)
        else:
            width = int(maxSize * img.width / img.height)
            height = maxSize

        resized_image = img.resize((width, height))

        logo_img = PI.open('static/logo_white.png',)
        logo_img = logo_img.resize((120, 30))

        alpha = logo_img.split()[3]
        alpha = PI.eval(alpha, lambda a: int(a * 0.4))
        logo_img.putalpha(alpha)

        logo_width, logo_height = logo_img.size
        x = (resized_image.width - logo_width) // 2
        y = resized_image.height - logo_height - 70
        resized_image.paste(logo_img, (x, y), logo_img)

        resized_image.save(obj.image.path)

admin.site.register(Image, ImageAdmin)