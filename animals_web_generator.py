import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

print(animals_data)
"""
for animal in animals_data:
    if 'name' in animal:
        print(f"Name: {animal.get('name')}")
    if 'diet' in animal['characteristics']:
        print(f"Diet: {animal['characteristics']['diet']}")
    if 'locations' in animal:
        print(f"Location: {animal['locations'][0]}")
    if 'type' in animal['characteristics']:
        print(f"Type: {animal['characteristics']['type']}")
    print()
"""
with open("animals_template.html", "r") as file:
    html_file = file.read()

output = ''  # define an empty string
for animal in animals_data:
    # append information to each string
    if 'name' in animal:
        output += f"Name: {animal['name']}\n"
    if 'diet' in animal['characteristics']:
        output += f"Diet: {animal['characteristics']['diet']}\n"
    if 'locations' in animal:
        output += f"Location: {animal['locations'][0]}\n"
    if 'type' in animal['characteristics']:
        output += f"Type: {animal['characteristics']['type']}\n"
    output += "\n"
print(output)


html_file.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w") as animals_html:
    animals_html.write(html_file)