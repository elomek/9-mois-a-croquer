"""
CLEF et MISE en place
dans un powershell

$headers = @{
    'Content-Type' = 'application/json'
    'Authorization' = 'Bearer meili'  # Utilisation de la clé maître
}
$body = @{
    'name' = 'MaCleAvecToutesLesAutorisations'
    'description' = 'DescriptionDeVotreCle'
    'actions' = @('search', 'documents.*', 'indexes.*', 'tasks.*', 'settings.*', 'stats.*', 'metrics.*', 'dumps.*', 'snapshots.*', 'version', 'keys.create', 'keys.get', 'keys.update', 'keys.delete', 'experimental.get', 'experimental.update')
    'indexes' = @('*')
    'expiresAt' = '2023-12-31T23:59:59Z'
}
$response = Invoke-RestMethod -Uri 'http://localhost:7700/keys' -Method Post -Headers $headers -Body ($body | ConvertTo-Json)
#Afficher la réponse (la clé générée)
$response 

autorisation secondaire 

$headers = @{
    'Content-Type' = 'application/json'
    'Authorization' = 'Bearer meili' 
}

$indexes = Invoke-RestMethod -Uri "http://localhost:7700/indexes" -Method Get -Headers $headers

foreach ($index in $indexes) {
    $indexName = $index.name
    Invoke-WebRequest -Uri "http://localhost:7700/indexes/$indexName" -Method Delete -Headers $headers
}

si jamais besoin en json file
   
if json_file:
    file_stop_words = open('stopwords-fr.json')
    stop_words = json.load(file_stop_words)

client.index(table_name).update_stop_words(stop_words)

### pour verifier le nom des colum d'une table

engine = create_engine(f"mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# Créez un objet Inspector pour inspecter la base de données
inspector = inspect(engine)

# Remplacez 'nom_de_table' par le nom de votre table
table_name = 'recipes'

# Obtenez les informations sur les colonnes de la table
columns = inspector.get_columns(table_name)

# Affichez les noms des colonnes
for column in columns:
    print(column['name'])

"""

# liste stopword
custom_stop_words = {"à", "au", "aux", "avec", "ce", "ces", "dans", "de", "des", "du", "elle",
    "en", "et", "eux", "il", "je", "la", "le", "leur", "lui", "ma", "mais", "me",
    "même", "mes", "moi", "mon", "ne", "nos", "notre", "nous", "on", "ou", "par",
    "pas", "pour", "qu", "que", "qui", "sa", "se", "ses", "son", "sur", "ta", "te",
    "tes", "toi", "ton", "tu", "un", "une", "vos", "votre", "vous", "c", "d", "j",
    "l", "à", "m", "n", "s", "t", "y", "été", "étée", "étées", "étés", "étant",
    "suis", "es", "est", "sommes", "êtes", "sont", "serai", "seras", "sera", "serons",
    "serez", "seront", "serais", "serait", "serions", "seriez", "seraient", "étais",
    "était", "étions", "étiez", "étaient", "fus", "fut", "fûmes", "fûtes", "furent",
    "sois", "soit", "soyons", "soyez", "soient", "serais", "serait", "serions", "seriez",
    "seraient", "eusse", "eusses", "eût", "eussions", "eussiez", "eussent",
    "a", "ai", "as", "avait", "avoir", "avons", "ayant", "cet", "cette", "déjà", 
    "dit", "donc", "elle", "en", "être", "fait", "il", "ils", "leur", "leurs", 
    "là", "ma", "maintenant", "mon", "nos", "notre", "nous", "ont", "ou", "parce",
    "parce que", "parce qu", "pourquoi", "quand", "que", "quel", "quelle", 
    "quelles", "quels", "qui", "se", "ses", "si", "sont", "sous", "soyez", 
    "suis", "sur", "ton", "tous", "tout", "toutes", "tu", "un", "une", 
    "voient", "vont", "vos", "votre", "vous", "ça",
    "abord", "absolument", "afin", "ah", "ai", "aie", "ainsi", "allaient", "allo", "allons", 
    "allô", "alors", "anterieur", "anterieure", "anterieures", "apres", "après", "as", "assez", 
    "attendu", "au", "aucun", "aucune", "aujourd", "aujourd'hui", "aupres", "auquel", "aura", 
    "auront", "aussi", "autre", "autres", "aujourd'hui", "auprès", "auquel", "aussitôt", 
    "autant", "autre", "autres", "auxquelles", "auxquels", "aujourd'hui", "auprès", 
    "auquel", "aussitôt", "autant", "autre", "autres", "auxquelles", "auxquels", "avaient", 
    "avais", "avait", "avant", "avec", "avoir", "avons", "ayant", "bah", "bas", "basee", 
    "bat", "beau", "beaucoup", "bien", "bigre", "boum", "bravo", "brrr", "c", "car", "ce", 
    "ceci", "cela", "celle", "celle-ci", "celle-là", "celles", "celles-ci", "celles-là", 
    "celui", "celui-ci", "celui-là", "cent", "cependant", "certain", "certaine", "certaines", 
    "certains", "certes", "ces", "cet", "cette", "ceux", "ceux-ci", "ceux-là", "chacun", "chacune",
    "chaque", "cher", "chère", "chères", "chers", "chez", "chiche", "chut", "chère", "chères", 
    "chers", "chez", "chiche", "chut", "chère", "chères", "chers", "chez", "chiche", "chut",
    "chères", "chers", "chez", "chiche", "chut", "chère", "chères", "chers", "chez", "chiche",
    "chut", "ci", "cinq", "cinquantaine", "cinquante", "cinquantième", "cinquième", "clac", 
    "clic", "comme", "comment", "comparable", "comparables", "compris", "concernant", "contre",
    "couic", "crac", "d", "da", "dans", "de", "debout", "dedans", "dehors", "depuis", "derrière", 
    "des", "dès", "désormais", "desquelles", "desquels", "dessous", "dessus", "deux", "deuxième", 
    "deuxièmement", "devant", "devers", "devra", "différent", "différente", "différentes", "différents",
    "dire", "divers", "diverse", "diverses", "dix", "dix-huit", "dix-neuf", "dix-sept", "dixième", 
    "doit", "doivent", "donc", "dont", "douze", "douzième", "dring", "du", "duquel", "durant", "e", 
    "effet", "eh", "elle", "elle-même", "elles","elle-même", "elles", "elles-mêmes", "en", "encore", "entre", "envers", "environ", "es", "ès",
    "est", "et", "etant", "étaient", "être", "eu", "euh", "eux", "eux-mêmes", "excepté", "f", 
"fais", "faisaient", "faisant", "fait", "feront", "fi", "flac", "floc", "fois", "font", 
"force", "furent", "g", "générale", "généralement", "gens", "h", "ha", "haut", "hein", 
"hé", "hélas", "hem", "hep", "hi", "ho", "holà", "hop", "hormis", "hors", "hou", "houp", 
"hue", "hui", "huit", "huitième", "hum", "hurrah", "hé", "hélas", "i", "ici", "il", "ils", 
"importe", "j", "je", "jusqu", "jusque", "k", "l", "la", "là", "laquelle", "las", "le", 
"lequel", "les", "lès", "lesquelles", "lesquels", "leur", "leurs", "longtemps", "lors", 
"lorsque", "lui", "lui-même", "m", "ma", "maint", "mais", "malgré", "me", "même", "mêmes", 
"merci", "mes", "mien", "mienne", "miennes", "miens", "mille", "mince", "moi", "moi-même", 
"moins", "mon", "moyennant", "n", "na", "ne", "néanmoins", "neuf", "neuvième", "ni", "nombreux", 
"non", "nos", "notre", "nôtre", "nôtres", "nous", "nous-mêmes", "nul", "o", "ô", "oh", "ohé", 
"ole", "olé", "on", "ont", "onze", "onzième", "ore", "ou", "où", "ouf", "ouias", "oust", "ouste", 
"outre", "p", "paf", "pan", "par", "parce", "parce que", "parce qu", "par-delà", "parfois", 
"parle", "parlent", "parler", "parmi", "parole", "parce", "parce que", "parce qu", "par-delà", 
"parfois", "parle", "parlent", "parler", "parmi", "parole", "pense", "permet", "plouf", "plus", 
"plusieurs", "plutôt", "pour", "pourquoi", "près", "proche", "psitt", "puisque", "q", "qu", "quand", 
"quant", "quanta", "quant-à-soi", "quarante", "quatorze", "quatre", "quatre-vingt", "quatrième", "que", 
"quel", "quelle", "quelles", "quelque", "quelques", "quelqu'un", "quels", "qui", "quiconque", "quinze", 
"quoi", "quoique", "r", "revoici", "revoilà", "rien", "s", "sa", "sacrebleu", "sans", "sapristi", 
"sauf", "se", "seize", "selon", "sept", "septième", "sera", "serai", "seraient", "serais", "serait", 
"seras", "serez", "seriez", "serions", "serons", "seront", "ses", "si", "sien", "sienne", "siennes", 
"siens", "sinon", "six", "sixième", "soi", "soi-même", "soient", "sois", "soit", "soixante", "son", 
"sont", "sous", "soyez", "soyons", "suis", "suite", "sur", "sus", "t", "ta", "tac", "tandis", "tant", 
"te", "té", "tel", "telle", "tellement", "telles", "tels", "tenant", "tes", "tic", "tien", "tienne", 
"tiennes", "tiens", "toc", "toi", "toi-même", "ton", "touchant", "toujours", "tous", "tout", "toute", 
"toutes", "treize", "trente", "très", "trois", "troisième", "trop", "u", "un", "une", "unes", "uns", 
"v", "va", "vais", "vas", "vé", "vers", "via", "vif", "vifs", "vingt", "vivat", "vive", "vives", "vlan", 
"voici", "voilà", "vont", "vos", "votre", "vous", "vous-mêmes", "vu", "w", "x", "y", "z", "zut",
"ça", "ès", "étaient", "être", "eu", "euh", "eux", "eux-mêmes", "f", "feront", "fi", "floc", 
"font", "g", "gens", "h", "ha", "haut", "hein", "hé", "hélas", "hem", "hep", "hi", "ho", "holà", 
"hop", "hormis", "hors", "hou", "houp", "hue", "hui", "huit", "huitième", "hum", "hurrah", "hé", 
"hélas", "i", "ici", "il", "ils", "importe", "j", "je", "jusque", "k", "l", "la", "là", "laquelle", 
"las", "le", "lequel", "les", "lesquelles", "lesquels", "leur", "leurs", "longtemps", "lors", 
"lorsque", "lui", "lui-même", "m", "ma", "mais", "malgré", "me", "même", "mêmes", "merci", 
"mes", "mien", "mienne", "miennes", "miens", "mille", "mince", "moi", "moi-même", "moins", 
"mon", "moyennant", "n", "na", "ne", "néanmoins", "neuf", "ni", "nombreux", "non", "nos", 
"notre", "nôtre", "nôtres", "nous", "nous-mêmes", "o", "ô", "oh", "ohé", "olé", "on", "ont", 
"onze", "ore", "ou", "où", "ouais", "ouf", "ouias", "outre", "p", "pan", "par", "parce", 
"parce que", "parce qu", "par-delà", "parfois", "parmi", "parole", "pense", "permet", "plouf", 
"plus", "plusieurs", "plutôt", "pour", "pourquoi", "près", "proche", "psitt", "puisque", "q", 
"qu", "quand", "quant", "quinze", "quoi", "quoique", "r", "revoici", "revoilà", "rien", "s", 
"sa", "sapristi", "sauf", "se", "seize", "selon", "sept", "sera", "serai", "seraient", "serais", 
"serait", "seras", "seriez", "serions", "serons", "seront", "ses", "si", "sien", "sienne", 
"siennes", "siens", "sinon", "six", "soi", "soi-même", "soient", "sois", "soit", "soixante", 
"son", "sont", "sous", "soyez", "soyons", "suis", "suite", "sur", "sus", "t", "tandis", "tant", 
"te", "té", "tel", "telle", "telles", "tels", "tenant", "tes", "tic", "tien", "tienne", "tiennes", 
"tiens", "toc", "toi", "toi-même", "ton", "touchant", "toujours", "tous", "tout", "toute", "toutes", 
"treize", "trente", "très", "trois", "troisième", "u", "un", "une", "unes", "v", "va", "vais", "vas", 
"vé", "vers", "via", "vif", "vifs", "vingt", "vivat", "vive", "vives", "voici", "voilà", "vont", 
"vos", "votre", "vous", "vous-mêmes", "w", "x", "y", "z", "zut"}




# Import des bibliothèques nécessaires
from sqlalchemy import create_engine, MetaData, Table, text, inspect
from meilisearch.client import Client
from datetime import date
import spacy
import requests

def serialize_date(obj):
    """
    Sérialise un objet de type date au format ISO (YYYY-MM-DD).

    Args:
        obj (date): Objet de type date à sérialiser.

    Returns:
        str: Date sérialisée au format ISO.
    """
    if isinstance(obj, date):
        return obj.strftime("%Y-%m-%d")

def get_stop_words():
    """
    Obtient la liste des mots vides (stop words) de la langue française à partir de spaCy.

    Returns:
        list: Liste des mots vides.
    """
    nlp = spacy.load("fr_core_news_sm")

    return list(nlp.Defaults.stop_words)

def extract_keywords(text):
    """
    Extrait les mots clés d'un texte à l'aide de spaCy.

    Args:
        text (str): Texte à traiter.

    Returns:
        list: Liste des mots clés extraits.
    """
    doc = nlp(text)
    return [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]

def filter_stop_words(text, stop_words):
    """
    Filtre les mots vides (stop words) d'un texte.

    Args:
        text (str): Texte à filtrer.
        stop_words (list): Liste des mots vides.

    Returns:
        str: Texte filtré.
    """
    if isinstance(text, str):
        doc = nlp(text)
        return ' '.join(token.lemma_ for token in doc if token.is_alpha and token.lemma_ not in stop_words)
    return str(text)

def transform_code_to_id(row, column):
    """
    Transforme le code en ID dans certaines conditions.

    Args:
        row: Objet de ligne provenant de la base de données.
        column (dict): Dictionnaire représentant les informations sur la colonne.

    Returns:
        dict: Dictionnaire avec l'ID ou la valeur de la colonne, selon la condition.
    """
    if 'code' in row._fields and column['name'] == 'code':
        return {'id': getattr(row, 'code')}
    return {column['name']: getattr(row, column['name'])}

def setup_meilisearch_indexes():
    """
    Fonction principale qui gère la mise en place des index MeiliSearch pour différentes tables de la base de données.

    Note:
        Assurez-vous d'avoir les bibliothèques requises et les dépendances installées avant d'exécuter cette fonction.
    """
    ###MISE EN PLACE 
   
    DB_USERNAME = 'root'
    DB_PASSWORD = 'root'
    DB_HOST = 'localhost'
    DB_PORT = 3306
    DB_NAME = '9mois'

    MEILI_HOST = 'http://localhost:7700'
    MEILI_API_KEY = '6f435ceaafdfb71a7ed47b3376400a87c883ecd9eb12598b652a5f37cb634da3'

    db_engine = create_engine(f"mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

    metadata = MetaData()
    metadata.reflect(bind=db_engine)
    inspector = inspect(db_engine)
    
    # ARTICLE
    MEILI_INDEX_NAME = 'Articles'

    columns = inspector.get_columns('articles')
    selected_columns = ['id', 'title', 'content']

    client = Client(MEILI_HOST, MEILI_API_KEY)

    index = client.create_index(uid=MEILI_INDEX_NAME)

    with db_engine.connect() as connection:
        query = text(f"SELECT {', '.join(selected_columns)} FROM articles")
        result = connection.execute(query)
        data = result.fetchall()

    documents = []
    for row in data:
        document = {}
        for i, column in enumerate(selected_columns):
            if column == 'content':
                document['keywords'] = extract_keywords(row[i])
            else:
                document[column] = serialize_date(row[i]) if isinstance(row[i], date) else row[i]
        documents.append(document)


    index_url = f'{MEILI_HOST}/indexes/{MEILI_INDEX_NAME}/documents'
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {MEILI_API_KEY}'}
    response = requests.post(index_url, headers=headers, json=documents)

    if response.status_code == 202:
        print(f"{len(documents)} documents ajoutés à l'index MeiliSearch avec stop words et mots clés.")
    else:
        print(f"Erreur lors de l'ajout des documents : {response.text}")


    ## RECETTE

    recipes_engine = create_engine(f"mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
    recipes_metadata = MetaData()
    recipes_metadata.reflect(bind=recipes_engine)

    recipes_inspector = inspect(recipes_engine)
    recipes_columns = recipes_inspector.get_columns('recipes')

    recipes_client = Client(MEILI_HOST, MEILI_API_KEY)
    RECIPES_INDEX_NAME = 'Recipes'

    with recipes_engine.connect() as recipes_connection:
        recipes_query = text(f"SELECT * FROM recipes")
        recipes_result = recipes_connection.execute(recipes_query)
        recipes_data = recipes_result.fetchall()

    recipes_index_info = recipes_client.create_index(uid=RECIPES_INDEX_NAME, options={"primaryKey": "id"})
    recipes_index = recipes_client.index(uid=RECIPES_INDEX_NAME)

    stop_words = get_stop_words()
    recipes_documents = [
        {
            recipes_columns[i]['name']: serialize_date(row[i]) if isinstance(row[i], date) else filter_stop_words(row[i], stop_words)
            for i in range(len(recipes_columns))
        }
        for row in recipes_data
    ]

    recipes_index.update_documents(recipes_documents)

    print(f"{len(recipes_documents)} documents ajoutés à l'index MeiliSearch (recipes).")

    ## FOOD

    FOOD_INDEX_NAME = 'Food'

    food_engine = create_engine(f"mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

    with food_engine.connect() as food_connection:
        food_query = text(f"SELECT code AS id, name FROM food")
        food_result = food_connection.execute(food_query)
        food_data = food_result.fetchall()

    food_columns = [
        {'name': 'id', 'type': 'VARCHAR(length=15)'},
        {'name': 'name', 'type': 'VARCHAR(length=191)'}
    ]

    food_client = Client(MEILI_HOST, MEILI_API_KEY)
    food_index_info = food_client.create_index(uid=FOOD_INDEX_NAME, options={"primaryKey": "id"})
    food_index = food_client.index(uid=FOOD_INDEX_NAME)

    stop_words = get_stop_words()
    food_documents = [
        {
            food_columns[i]['name']: filter_stop_words(row[i], stop_words) if isinstance(row[i], str) else str(row[i])
            for i in range(len(food_columns))
        }
        for row in food_data
    ]

    food_index.update_documents(food_documents)

    print(f"{len(food_documents)} documents ajoutés à l'index MeiliSearch (food).")


    ## QUESTIONS


    QUESTIONS_INDEX_NAME = 'questions'

    questions_engine = create_engine(f"mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
    questions_metadata = MetaData()
    questions_metadata.reflect(bind=questions_engine)

    questions_inspector = inspect(questions_engine)
    questions_columns = questions_inspector.get_columns('questions')

    questions_selected_columns = ['id', 'question', 'answer']

    questions_client = Client(MEILI_HOST, MEILI_API_KEY)
    questions_index_info = questions_client.create_index(uid=QUESTIONS_INDEX_NAME, options={"primaryKey": "id"})
    questions_index = questions_client.index(uid=QUESTIONS_INDEX_NAME)

    with questions_engine.connect() as questions_connection:
        questions_query = text(f"SELECT {', '.join(questions_selected_columns)} FROM questions")
        questions_result = questions_connection.execute(questions_query)
        questions_data = questions_result.fetchall()

    questions_columns = [
        {'name': 'id', 'type': 'INTEGER'},
        {'name': 'question', 'type': 'VARCHAR(length=255)'},
        {'name': 'answer', 'type': 'TEXT'}
    ]

    stop_words = get_stop_words()
    questions_documents = [
        {
            questions_columns[i]['name']: filter_stop_words(row[i], stop_words) if isinstance(row[i], str) else str(row[i])
            for i in range(len(questions_columns))
        }
        for row in questions_data
    ]

    questions_index.update_documents(questions_documents)

    print(f"{len(questions_documents)} documents ajoutés à l'index MeiliSearch (questions).")

    ## ALL

    ALL_INDEX_NAME = 'all'
    all_client = Client(MEILI_HOST, MEILI_API_KEY)
    all_index_info = all_client.create_index(uid=ALL_INDEX_NAME)

    questions_selected_columns = ['id', 'question', 'answer']
    recipes_selected_columns = ['id', 'name','time','difficulty','budget','side_food','steps','food']
    articles_selected_columns = ['id', 'title', 'content']
    food_selected_columns = ['code', 'name']  

    tables_columns = {
        'questions': questions_selected_columns,
        'recipes': recipes_selected_columns,
        'articles': articles_selected_columns,
        'food': food_selected_columns
    }

    all_columns = []
    for table, selected_columns in tables_columns.items():
        engine = create_engine(f"mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
        metadata = MetaData()
        metadata.reflect(bind=engine)
        inspector = inspect(engine)
        columns = inspector.get_columns(table)
        all_columns.extend([col for col in columns if col['name'] in selected_columns])

    unique_columns = {column['name']: column for column in all_columns}.values()

    all_index = all_client.index(uid=ALL_INDEX_NAME)




    for table, selected_columns in tables_columns.items():
        engine = create_engine(f"mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
        with engine.connect() as connection:
            query = text(f"SELECT {', '.join(selected_columns)} FROM {table}")
            result = connection.execute(query)
            data = result.fetchall()

        documents = []
        for row in data:
            document = {}
            for column in unique_columns:
                if hasattr(row, column['name']):
                    if table == 'food':
                        document.update(transform_code_to_id(row, column))
                    else:
                        document[column['name']] = serialize_date(getattr(row, column['name'])) if isinstance(getattr(row, column['name']), date) else getattr(row, column['name'])
            documents.append(document)

        all_index.update_documents(documents)
        print(f"{len(documents)} documents ajoutés à l'index MeiliSearch ({table}).")


    print(f"{len(all_index.get_primary_key())} documents ajoutés à l'index MeiliSearch (all).")


# nlp 
nlp = spacy.load("fr_core_news_sm")

# Exécution de la fonction principale
setup_meilisearch_indexes()
