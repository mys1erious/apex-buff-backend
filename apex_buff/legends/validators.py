from django.core.exceptions import ValidationError

from abilities.models import Ability


def restrict_abilities_amount_in_legend(slug):
    max_abilities = 4

    if Ability.objects.filter(slug=slug).count() >= max_abilities:
        raise ValidationError('Legend already has maximum number of abilities')
