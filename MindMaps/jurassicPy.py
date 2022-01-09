import requests
import json

# -------------------------
# Jinja2
# -------------------------
from jinja2 import Environment, FileSystemLoader
template_dir = 'Templates/'
env = Environment(loader=FileSystemLoader(template_dir))
allDinosaurs_template = env.get_template('allDinosaurs.j2')
dinosaur_template = env.get_template('dinosaur.j2')

# -------------------------
# Headers
# -------------------------
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
}

# -------------------------
# All Dinosaurs
# -------------------------

allDinosaurs = requests.request("GET", "https://dinosaur-facts-api.shultzlab.com/dinosaurs", headers=headers)
allDinosaursJSON = allDinosaurs.json()

parsed_all_output = allDinosaurs_template.render(allDinosaurs = allDinosaursJSON)

with open("Dinosaurs/All_Dinosaurs/All_Dinosaurs.md", "w") as fh:
    fh.write(parsed_all_output)               
    fh.close()

# -------------------------
# Each Dinosaur
# -------------------------
for dinosaur in allDinosaursJSON:
    oneDinosaur = dinosaur
    parsed_all_output = dinosaur_template.render(dinosaur = oneDinosaur)

    with open(f"Dinosaurs/{ oneDinosaur['Name'] }.md", "w") as fh:
        fh.write(parsed_all_output)               
        fh.close()    