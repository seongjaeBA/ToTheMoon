from genericpath import exists
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
        # migrations.RunPython(forwards),

        #삭제 : 예시는 UUID
        # migrations.AlterField(
        #     model_name='mymodel',
        #     name='uuid',
        #     field=models.UUIDField(default=uuid.uuid4, unique=True),
        #),

        
    ]

class UtilCommand:
    class QeuryCheckingCommand:
        def dbchecker(__name__):
            """장고 서버 확인

            Args:
                __name__ (str): [장고 앱 이름]
            """
            import os
            import inspect
            from runpy import run_module 

            
            djangoappname = ".".join([str(__name__), "models"])
            print(djangoappname)
            run_module(djangoappname)
            print(inspect.getmembers(djangoappname))

            # cur_path = os.path.join(os.getcwd(), str(__name__), "models.py")
            # if os.path.exists(cur_path):
            #     # print(__name__, inspect.getmembers(cur_path))
            #     for i in dir(cur_path):
            #         if type(i) == "class":
            #             print(__name__, dir(cur_path))
            # else:
            #     print("파일 없음")

    class UserCommand:
        def userlist():
            from django.contrib.auth import get_user_model
            Users = get_user_model()
            Users.objects.all()


if __name__ ==  "__main__":
    UtilCommand.QeuryCheckingCommand.dbchecker("blogttm")