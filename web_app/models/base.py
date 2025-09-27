from datetime import datetime, timezone
from peewee import Model, SQL, DateTimeField

class BaseModel(Model):
    created_at = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    class Meta:
        database = db

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super().save(*args, **kwargs)