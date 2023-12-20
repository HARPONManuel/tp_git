import os
import subprocess
import json

def find_json_file(directory):
    # Utilisez la commande 'find' pour localiser les fichiers JSON dans le répertoire spécifié
    try:
        result = subprocess.check_output(['find', directory, '-name', '*.json'])
        # Décodez la sortie en UTF-8 et divisez-la en lignes
        files = result.decode('utf-8').split('\n')
        # Supprimez les éléments vides de la liste
        files = list(filter(None, files))
        return files
    except subprocess.CalledProcessError:
        print("Erreur lors de la recherche des fichiers JSON.")
        return []

def absolute_path(file_path):
    # Convertissez le chemin relatif en chemin absolu
    return os.path.abspath(file_path)

def read_and_parse_json(file_path):
    try:
        with open(file_path, 'r') as file:
            # Chargez le contenu JSON du fichier en tant que dictionnaire Python
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Le fichier {file_path} n'existe pas.")
        return None
    except json.JSONDecodeError:
        print(f"Erreur de décodage JSON dans le fichier {file_path}.")
        return None

def process_json_data(data):
    # Extrait et affiche la valeur associée à la clé 'name'
    if 'name' in data:
        print(f"Valeur associée à la clé 'name': {data['name']}")

    # Parcourt toutes les clés et valeurs du dictionnaire JSON
    print("Toutes les paires clé-valeur dans le fichier JSON :")
    for key, value in data.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    # Spécifiez le répertoire dans lequel vous souhaitez rechercher les fichiers JSON
    target_directory = '/home/formation/Bureau/tp_git/projet2'

    # Recherchez les fichiers JSON dans le répertoire cible
    json_files = find_json_file(target_directory)

    if not json_files:
        print(f"Aucun fichier JSON trouvé dans le répertoire {target_directory}.")
    else:
        # Choisissez le premier fichier JSON trouvé (vous pouvez itérer sur la liste si nécessaire)
        chosen_json_file = json_files[0]

        # Affichez le chemin du fichier JSON
        print(f"Chemin du fichier JSON : {chosen_json_file}")

        # Convertissez le chemin relatif en chemin absolu
        absolute_path_json = absolute_path(chosen_json_file)
        print(f"Chemin absolu vers le fichier JSON : {absolute_path_json}")

        # Lisez et analysez le fichier JSON
        json_data = read_and_parse_json(absolute_path_json)

        if json_data:
            # Traitez les données dans le fichier JSON
            process_json_data(json_data)
