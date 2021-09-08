from cx_Freeze import setup, Executable

includefiles=[
    "image",
    "son",
    "initialisation",
    "police",
    "score",
    "lock",
    "contenu.txt"
    ]
    
    

target = Executable(
    script="snake.py",
    icon="logo_snake.ico"
    )

setup(
    name="Snake",
    version="1.17",
    description="le snake le plus complet de 2020!!!",
    author="Noailles Valentin, Vuillaume Axel",
    options = {'build_exe' : {'include_files':includefiles}},
    executables=[target]
    )
