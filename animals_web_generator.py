import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def skin_type_finder(animals_data):
    # present list of skin types
    skin_types = []
    for animal in animals_data:
        if 'skin_type' in animal['characteristics']:
            skin_types.append(animal['characteristics']['skin_type'])
    skin_types_distinct = set(skin_types)
    print(f"This is the List of available skin types: ")
    for skin_type in skin_types_distinct:
        print(skin_type)
    user_input_skintypes = input(f"Please choose and enter a skin type from the above list: ")

    return user_input_skintypes


def serialize_animal(animals_data, user_input_skintypes):
    output = ''  # define an empty string
    for animal in animals_data:
        # only the specific skin TYPE
        if user_input_skintypes == animal['characteristics']['skin_type']:
            # append information to each string
            output += '<li class="cards__item">'
            output += f"<div class='card__title'>{animal['name']}</div>"
            output += ' <p class="card__text">'
            output += '<ul>'
            if 'name' in animal:
                output += f"<li><strong>Name</strong>: {animal['name']}</li>\n"
            if 'diet' in animal['characteristics']:
                output += f"<li><strong>Diet</strong>: {animal['characteristics']['diet']}</li>\n"
            if 'locations' in animal:
                output += f"<li><strong>Location</strong>: {animal['locations'][0]}</li>\n"
            if 'type' in animal['characteristics']:
                output += f"<li><strong>Type</strong>: {animal['characteristics']['type']}</li>\n"
            if 'distinctive_feature' in animal['characteristics']:
                output += f"<li><strong>Distinctive Feature</strong>: {animal['characteristics']['distinctive_feature']}</li>\n"
            output += '</ul>'
            output += '</p>'
            output += '</li>'

    return output


def main():
    animals_data = load_data('animals_data.json')
    user_input_skintypes = skin_type_finder(animals_data)

    with open("animals_template.html", "r") as file:
        html_file = file.read()

    output = serialize_animal(animals_data, user_input_skintypes)
    updated_html = html_file.replace("__REPLACE_ANIMALS_INFO__", output)

    with open("animals.html", "w") as animals_html:
        animals_html.write(updated_html)


if __name__ == "__main__":
    main()
