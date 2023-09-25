import mimetypes
import os
import time
from PIL import Image
from celery import shared_task
from .models import File


@shared_task
def edit_file(file_id):
    try:
        file = File.objects.get(pk=file_id)
        file_extension = os.path.splitext(file.file.name)[1].lower()
        if file_extension in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']:
            with open(file.file.path, 'rb') as img_file:
                img = Image.open(img_file)
                img = img.convert('L')
                img.save(file.file.path)

        elif file_extension in ['.txt', '.text']:
            with open(file.file.path, 'r') as text_file:
                original_text = text_file.read()
            edited_text = "EDITED\n" + original_text + "\nEDITED"
            with open(file.file.path, 'w') as text_file:
                text_file.write(edited_text)

        file.processed = True
        file.save()
        return {'status': 'success', 'id': file_id}

    except Exception as e:
        return {'status': 'error', 'message': str(e)}

