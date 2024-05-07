from flask import Blueprint, flash, render_template, redirect, request, url_for
from neufmoisacroquer.components.search import custom_reverse

search_controller = Blueprint(
    "search_controller",
    __name__,
    static_folder="static",
    template_folder="templates"
)

@search_controller.route("/", methods=["POST", "GET"])
def index():
    # ici la méthode a été call par

    # en fonction de si on charge juste la page sans rechercher, ou si on fait une recherche
    # on va faire differentes opérations
    if request.method == "GET":
        # là on call juste la page, on fait pas de recherche
        # il ne se passe rien, mais on envoie quand même une "réponse vide"
        resultats = None
    elif request.method == "POST":
        # là on call la page avec une rercheche
        # le contenue de cette recherche est disponible dans la variable "query"
        recherche = request.form["query"]

        # et avec cette query, normalement on peut utiliser les functions du composant que tu as importé
        # je t'ai fait un composant "search.py" avec une fuction à la con pour l'exemple, mais tu peux remplacer par tes functions
        recherche_modifiee = custom_reverse(recherche)

        # il est aussi possible d'envoyer des variables à la vue
        # comme par exemple le résultat de la recherche
        # ces variables pourront êtes utilisé dans la vue grace au moteur de template jinja2
        # la vue elle fonctionne avec un tableau de réponse, s'il n'y a qu'une seule réponse, il faut quand même que ce soit un tableau de 1
        resultats = []

        resultats.append(f"ma recherche était : [{recherche_modifiee}]")
    else:
        # ni GET ni POST, c'est chelou, mais surtout c'est pas prévu

        # afficher un message sur la prochaine page pour dire qu'il y a eu un problème
        flash("Something went wrong...", "danger")

    # et on rend là vue, soit avec rien parce qu'on charge juste la page...
    # soit avec le résultat d'une recherche
    print(resultats)
    return render_template("search/index.html", resultats=resultats)


