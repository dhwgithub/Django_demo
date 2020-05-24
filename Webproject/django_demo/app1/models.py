from django.db import models


class CreateUpdate(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:  # 这样设置使得生成数据库表时不会生成该类
        abstract = True


class Person(CreateUpdate):
    # first_name, last_name, created_at, updated_at
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Order(CreateUpdate):
    # order_id, order_desc, created_at, updated_at
    order_id = models.CharField(max_length=30, db_index=True)
    order_desc = models.CharField(max_length=120)
