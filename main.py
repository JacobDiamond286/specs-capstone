from website import create_app

app = create_app()





if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.
    # db.create_all()
    app.run(debug=True, host="0.0.0.0")


