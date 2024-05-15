from flask_marshmallow import Marshmallow
from db.database import get_mysql_connection as db

ma = Marshmallow()

class Position(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_time = db.Column(db.DateTime, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

# Esquema Marshmallow para serialização
class PositionSchema(ma.Schema):
    class Meta:
        fields = ("id", "date_time", "latitude", "longitude")

position_schema = PositionSchema()
positions_schema = PositionSchema(many=True)
