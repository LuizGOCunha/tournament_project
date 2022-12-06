def upload_to_db(fighters_name, fighters_weight, fighters_belt):
    db = open("fighterdb.csv", "a")
    db.write(f"{fighters_name}, {fighters_weight}, {fighters_belt}\n")

upload_to_db("george", "76", "purple")