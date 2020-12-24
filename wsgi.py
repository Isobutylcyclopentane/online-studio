"""
major flask app create and entry point

Author: Jerry Cheng
Last update: November 12, 2020
"""

from controller import create_app



app = create_app()

if __name__ == "__main__":
    app.run(host="localhost", port=5000)