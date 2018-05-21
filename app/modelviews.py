from app import db, admin
from .models import WebColor
from flask_admin.contrib.sqla import ModelView

admin.add_view(ModelView(WebColor, db.session))
