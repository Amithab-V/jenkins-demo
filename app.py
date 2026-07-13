from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the main page
@app.route("/")
def home():
    # Return HTML content to display on the webpage
    return """
    <html>
        <head>
            <title>My Small Web Page</title>
            <style>
                body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
                h1 { color: #333366; }
            </style>
        </head>
        <body>
            <h1>Hello, World!</h1>
            <p>This simple web page is powered entirely by <strong>Python and Flask</strong>.</p>
        </body>
    </html>
    """

# Run the local development server
if __name__ == "__main__":
    app.run(debug=True)
