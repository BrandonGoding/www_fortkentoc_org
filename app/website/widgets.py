from django import forms


class OpacitySliderWidget(forms.NumberInput):
    def __init__(self, attrs=None):
        final_attrs = {"type": "range", "min": 0, "max": 100, "step": 5}
        if attrs:
            final_attrs.update(attrs)
        super().__init__(attrs=final_attrs)
