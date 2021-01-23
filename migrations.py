from django.db import migrations
import uuid

class MyRouter:

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if 'target_db' in hints:
            return db == hints['target_db']
        return True

def forwards(apps, schema_editor):
    if schema_editor.connection.alias != 'default':
        return
    # Your migration code goes here

class Migration(migrations.Migration):

    dependencies = ['*app이름', '*migration 이름'
        # Dependencies to other migrations
    ]

    operations = [
        #이전
        migrations.RunPython(forwards),

        #삭제 : 예시는 UUID
        # migrations.AlterField(
        #     model_name='mymodel',
        #     name='uuid',
        #     field=models.UUIDField(default=uuid.uuid4, unique=True),
        #),

        
    ]