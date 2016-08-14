from app import app, db

import os

port = int(os.environ.get('PORT', 54624))
app.run(host='0.0.0.0', port=port, debug=False)

