from django.core.exceptions import ValidationError

from abilities.models import Ability


MAX_ABILITIES = 4


def validate_num_of_abilities_in_legend(legend):
    if Ability.objects.filter(legend=legend).count() >= MAX_ABILITIES:
        raise ValidationError(f'Legend `{legend.name}` already has maximum number of abilities.')
