from django import forms
from django.conf import settings
import os


class TemplateChoiceWidget(forms.Select):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.choices = self.get_template_choices()

    def get_template_choices(self):
        templates_dir = os.path.join(settings.BASE_DIR, "templates")
        choices = []
        for root, dirs, files in os.walk(templates_dir):
            for file in files:
                if file.endswith(".html"):
                    relative_path = os.path.relpath(
                        os.path.join(root, file), templates_dir
                    )
                    choices.append((relative_path, relative_path))
        return choices
