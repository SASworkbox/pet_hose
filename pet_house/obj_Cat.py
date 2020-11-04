from Pet_house import Animal

cats = [dict(animal_name="Барон", animal_sex="мальчик", animal_age="2 года"),
        dict(animal_name="Сэм", animal_sex="мальчик", animal_age="2 года"), ]

for cat in cats:
    cat_obj = Animal(animal_name=cat.get("animal_name"), animal_sex=cat.get("animal_sex"),
                     animal_age=cat.get("animal_age"))

    print(cat_obj.animal_name, cat_obj.animal_sex, cat_obj.animal_age)
