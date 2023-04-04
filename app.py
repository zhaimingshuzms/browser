from record_picture import app
from flask_frozen import Freezer

# freezer = Freezer(app)

if __name__ == '__main__':
    app.run(debug=True)
    # freezer.freeze()