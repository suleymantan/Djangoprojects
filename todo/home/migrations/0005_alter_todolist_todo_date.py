# Generated by Django 4.2.19 on 2025-02-18 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_alter_todolist_todo_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todolist",
            name="todo_date",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
