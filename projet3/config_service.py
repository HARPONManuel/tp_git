"""

import subprocess
import shutil
import os

def configure_services():
    # Chemin du fichier de configuration Apache
    apache_config_path = '/chemin/vers/votre/fichier/apache.conf'

    # Modifier le fichier de configuration Apache
    # update_apache_config(apache_config_path)

    # Redémarrer le service Apache
    restart_apache()

    # Commit des changements dans la branche 'develop'
    commit_changes()

    # Fusion avec la branche 'master'
    merge_with_master()

    # Pousser sur GitHub
    push_to_github()

#def update_apache_config(config_path):
    # Effectuer les modifications nécessaires dans le fichier de configuration Apache
    # Par exemple, vous pouvez utiliser un éditeur de texte ou la bibliothèque configparser
    # pour mettre à jour les paramètres du fichier de configuration.
    # Assurez-vous d'avoir les permissions nécessaires pour écrire dans le fichier.
    # ...

def restart_apache():
    # Redémarrer le service Apache
    subprocess.run(['service', 'apache2', 'restart'])  # Adapté à un système Ubuntu/Debian, ajustez selon votre distribution.

def commit_changes():
    # Commit des changements dans la branche 'develop'
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', 'Configurer les services'])

def merge_with_master():
    # Fusion avec la branche 'master'
    subprocess.run(['git', 'checkout', 'master'])
    subprocess.run(['git', 'merge', 'develop'])
    subprocess.run(['git', 'checkout', 'develop'])

def push_to_github():
    # Pousser sur GitHub
    subprocess.run(['git', 'push', 'origin', 'develop'])
    subprocess.run(['git', 'push', 'origin', 'master'])

if __name__ == "__main__":
    configure_services()


"""

"""
import subprocess

def install_apache():
    subprocess.run(["sudo", "apt-get", "update"])
    subprocess.run(["sudo", "apt-get", "install", "-y", "apache2"])

def install_ssh():
    subprocess.run(["sudo", "apt-get", "install", "-y", "opensshserver"])
    if __name__ == "__master__":
        install_apache()
        install_ssh()
"""

import os

def install_apache():
    os.system('sudo apt-get update')
    os.system('sudo apt-get install apache2')
 
def install_ssh():
    os.system('sudo apt-get update')
    os.system('sudo apt-get install -y openssh-server')

install_apache()
install_ssh()
              
