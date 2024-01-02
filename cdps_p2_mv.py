import os
from subprocess import call, CalledProcessError

grupo = "2"
ruta_app = "practica_creativa2/bookinfo/src/productpage"

def clonarRepositorio():
    try:
        print("-----------------------------------Entra en clonarRepositorio---------------------------------------")
        call(["sudo", "rm", "-r", "practica_creativa2"])
        call(["git", "clone", "https://github.com/CDPS-ETSIT/practica_creativa2.git"])
        call(["sudo", "apt", "update"])
        #call(["sudo", "apt", "install", "git"])
        call(["sudo", "apt", "install", "python3-pip", "-y"])
        #call(["pip", "install", "--upgrade pip"])
        #call(["pip", "install", "--upgrade setuptools"])
    except CalledProcessError as e:
        print(f"Error al ejecutar el comando: {e}")

def dependencias():
    print("-----------------------------------Entra en dependencias--------------------------------------") 
    ruta_requirements = f"{ruta_app}/requirements.txt"
    with open(ruta_requirements, "r") as requirements:
        file = requirements.read()
        new_file = file.replace("requests==2.21.0","requests")
    with open(ruta_requirements, "w") as requirements:
        requirements.write(new_file)
    call(["pip3", "install", "-r", f"{ruta_app}/requirements.txt"])
    #call(['pip', 'install', '--force-reinstall', '-v', "urllib3==1.21.1"])
    #call(['pip', 'install', '--force-reinstall', '-v', "chardet==3.0.2"])

def getGrupo():
    print("-----------------------------------Entra en getGrupo--------------------------------------")
    os.environ["GROUP_NUMBER"]= grupo

def editHTML():
    print("------------------------------------Entra en editHTML--------------------------------------")
    ruta_html = f"{ruta_app}/templates/productpage.html"

    with open(ruta_html, "r") as html:
        file = html.read()
        new_file = file.replace("{% block title %}Simple Bookstore App{% endblock %}",
            "{% block title %}" + str(os.environ.get('GROUP_NUMBER')) + "{% endblock %}")

    with open(ruta_html, "w") as html:
        html.write(new_file)

def editPuerto():
    print("------------------------------------Entra en editPuerto--------------------------------------")
    call(["python3", f"{ruta_app}/productpage_monolith.py", "9080"])

def main():
    clonarRepositorio()
    dependencias()
    getGrupo()
    editHTML()
    editPuerto()

if __name__ == "__main__":
    main()


