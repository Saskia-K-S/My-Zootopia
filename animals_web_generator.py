import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

print(animals_data)

with open("animals_template.html", "r") as file:
    html_file = file.read()

    output = ''  # define an empty string
    for animal in animals_data:
        # append information to each string
        output += '<li class="cards__item">'
        if 'name' in animal:
            output += f"Name: {animal['name']}<br/>\n"
        if 'diet' in animal['characteristics']:
            output += f"Diet: {animal['characteristics']['diet']}<br/>\n"
        if 'locations' in animal:
            output += f"Location: {animal['locations'][0]}<br/>\n"
        if 'type' in animal['characteristics']:
            output += f"Type: {animal['characteristics']['type']}<br/>\n"
        output += '</li>'
        output += "\n"
    print(html_file)
    updated_html = html_file.replace("__REPLACE_ANIMALS_INFO__", output)


with open("animals.html", "w") as animals_html:
    animals_html.write(updated_html)