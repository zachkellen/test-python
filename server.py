from flask_app import app
from flask_app.controllers import interactions

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(threaded=True, debug = True)    # Run the app in debug mode.