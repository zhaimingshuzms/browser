from record_picture import app, db
from record_picture.models import User, Picture

db.drop_all()
db.create_all()
user = User()
picture = Picture()
db.session.add(picture)
db.session.add(user)
db.session.commit()
