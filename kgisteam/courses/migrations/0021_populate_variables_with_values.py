# Generated by Django 3.0.2 on 2020-02-02 00:24

from django.db import migrations
from django.db.utils import OperationalError

from courses.maths import sn_round
from courses.models import Problem


def update_problem_variables(apps, schema_editor):
    """Data migration."""
    try:
        for problem in Problem.objects.all():
            if problem.variable_names and problem.variable_default_values:
                current_variables = dict(
                    zip(
                        problem.variable_names.split(','),
                        problem.variable_default_values.split(',')
                    )
                )
                current_variables = { 
                    key.strip(): sn_round(float(value.strip()))
                    for key, value in variables.items()
                }
                problem.variables_with_values = ', '.join( 
                    [ '{name}[{default_value}]'.format(name=key, default_value=value) 
                        for key, value in current_variables.items()  ]   
                )    
                problem.save()
    except OperationalError:
        """Suppress this error when the data migration is reapplied."""
        pass
    except AttributeError:
        """Suppress this error when the data migration is reapplied."""
        pass
    
def revert_problem_variables(apps, schema_editor):
    """Data migration."""
    try:
        for problem in Problem.objects.all():
            if problem.variables_with_values:
                problem.variables_with_values = ''
                problem.save()
    except OperationalError:
        """Suppress this error when the data migration is reapplied."""
        pass


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0020_problem_variables_with_values'),
    ]

    operations = [
        migrations.RunPython(update_problem_variables, revert_problem_variables),
    ]
