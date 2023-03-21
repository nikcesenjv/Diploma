import shelve

def open_shelve(type_of_object):
    with shelve.open("objectsDB") as db:
        return db[type_of_object]

def shelve_objects(files, inner_folders, main_folders):
    with shelve.open("objectsDB") as db:
        db["file"], db["inner"], db["main"] = files, inner_folders, main_folders
