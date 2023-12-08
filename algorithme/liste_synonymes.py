# liste_synonymes.py
def dico_syno ():
    dictionnaire_synonymes = {'mots':[["produit","article","élément","bien","actif","avoir","ressource",["élément","physique"],["bien","physique"]],
    ["ensemble","réserve","quantité","nombre","accumulation","agrégat"],
    ["stocker","stockage","garder","emmagasiner","accumuler","conserver"],
    ["utilisation","utiliser",],
    ["vente","vendre","revendre","revente","commercialisation","cession"],
    ["entreprise","organisation",["organisme","activité","marchand"]],
    ["acheter","achat"],
    ["fabriquer"],
    ["final","dernier"],
    ["rester","demeurer"],
    ["patrimoine"],
    ["entité"],
    ["financer","fianncement","payer","paiement","financier"],
    ["processus","fonctionnement",["pilotage","quotidien"]],
    ["trouver","recherche","rechercher"]
    ,["final","dernier"]
    ,["ultérieur"]
    ,["collecte"]
    ,["actionnaire"]
    ,["banque","bancaire"]
    ,["fondateur"]
    ,["source"]
    ,["externe","extérieur"]
    ,["créer","établir"]
    ,["capital"]
    ,["regrouper","réunion","réunir","obtenir","obtention","percevoir","toucher","recevoir","acquérir","acquisition"]#
    ,["contribution","apport"]
    ,["opération","transaction"]
    ,["immobilisation"]
    ,["obligation","devoir","impératif","responsable","responsabilité"]
    ,["service"]
    ,["consommer"]
    ,["disparaitre","partir"]
    ,["exploitation"]
    ,["affecter"]
    ,["répartir","partager","distribuer","diviser"]
    ,["charge"]
    ,["montant","valeur","prix","somme"]
    ,["niveau"]
    ,["activité","projet"]
    ,["système"]
    ,["enregistrement"]
    ,["flux"]
    ,["environnement"]
    ,["règle"]
    ,["méthode"]
    ,["encadrer"]
    ,["légal"]
    ,["produire","production"]
    ,["document","tableau"]
    ,["représentation","image","photographie","modèle"]
    ,["fidèle","exact","précis","correct"]
    ,["partie"]
    ,["principe"]
    ,["gestion","gérer","organisation","organiser"]
    ,["améliorer","amélioration","perfectionner"]
    ,["comprendre"]
    ,["dirigeant","chef","supérieur"]
    ,["interne"]
    ,["synthétiser","synthèse","résumer","résumé","présentation","présenter"]
    ,["encaissement","encaisser"]
    ,["décaissement"]
    ,["établir",["mettre","place"],"réaliser",]
    ,["budget"]
    ,["recette","gain"]
    ,["dépense","coût",["sortie","ressource"]]
    ,["calculer","calcul",["processus","mathématique"],["procédé","mathématique"]]
    ,["réalité"]
    ,["prévision"]
    ,["différent","différence","écart"]
    ,["emprunt","emprunter"]
    ,["créancier"]
    ,["rembourser"]
    ,["échéancier",["registre","paiement"]]
    ,["fournisseur"]
    ,["administration"]
    ,["taxe"]
    ,["impôt"]
    ,["lié","rapport","relative"]
    ,[["non","lié"]]
    ,["solde"]
    ,["analyser","observer","constater","voir"]
    ,["richesse"]
    ,["définitivement"]
    ,["bénéficiaire","bénéfice","bénéficier","intérêt"]
    ,["générer"]
    ,["mesure"]
    ,["perte","perdre"]
    ,["indicateur"]
    ,["posséder","avoir","disposer"]
    ,["démontrer",["faire","preuve"],"prouver","montrer","démonstration"]
    ,["autonomie"]
    ,["comptable"]
    ,["situation","état"]
    ,["passif","dette",["obligation","financier"],"endettement"]
    ,["période","moment","durée","date"]
    ,["spécifique","donner","particulier","fixer","prévoir",["varier", "pas"],["pas","variation"],"invariant","fixe","stable","invariable"]
    ,["forme","état"]
    ,["classique","typique","conventionnel"]
    ,["institution","établissement","institut"]
    ,["taux"]
    ,["variable","varier"]
    ,["contrat"]
    ,["négociation"]
    ,["sans transformation","finis","pas de modification","tel quel"],
    [["sans","transformation"],["pas","modification"],["tel","quel"],"finir"],
    ["durablement",["période","prolonger"],["long","terme"],["façon","durable"],["durée","prolonger"],["long","période"],["manière","permanent"]],
    [["autre","opération","courant"],["pas", "opération" ,"courant"],["autre","courant"],["pas","courant"]],
    ["immédiatement","directement",["sans","calcul","intermédiaire"]],
    [["période","donner"],["durée","spécifique"],["moment","donner"],["date","spécifique"]],
    [["charge","courant"]],[["cycle","production"]],[["cycle","exploitation"]],[["cycle","financement"]],[["cycle","investissement"]],["argent","capital","fond","somme"],[["collecte","fond"]],[["agent","économique"]],[["valeur","économique","positif"]],[["valeur","économique","négatif"]],
    [["avantage","économique","futur"],"contrepartie"],[["sortie","ressource"]],[["sans","contrepartie"],["pas","contrepartie"]],["clé","repartition"],["boite","outil"]
    ]}
    return dictionnaire_synonymes

#exemple_dico = {["stocker","stockage","garder","emmagasiner","accumuler","conserver"]:["vente","vendre","revendre","revente","commercialisation","cession"]}

def dico_anto ():
    dictionnaire_anto = {
        
        'stocker':["vente","vendre","revendre","revente","commercialisation","cession","utilisation","utiliser"]
        ,'vente':["stocker","stockage","garder","emmagasiner","accumuler","conserver","acheter","achat"]

        ,'premier':["final","dernier","ultérieur"]
        ,"final":["premier"]

        ,"rester":["disparaitre","partir"]
        ,"disparaitre":["rester","demeurer"]

        ,"interne":["externe","extérieur","étranger","périphérique"]
        ,"externe":["interne","intérieur"]

        ,"répartir":["regrouper","réunion","réunir","obtenir","obtention","percevoir","toucher","recevoir","acquérir","acquisition"]
        ,"regrouper":["répartir","partager","distribuer","diviser"]

        ,"service":["produit","article","élément","bien","actif","avoir","ressource"]
        ,"produit":["service","passif","dette",["obligation","financier"],"endettement"]

        ,"détruire":["fabriquer"]
        ,"fabriquer":["détruire"]

        ,"décaissement":["encaissement","encaisser"]
        ,"encaissement":["décaissement"]

        ,"rembourser":["emprunt","emprunter"] 
        ,"emprunt":["rembourser"]

        ,"dépense":["recette","gain","gagner"]
        ,"recette":["dépense","coût",["sortie","ressource"],"perte","perdre"]
        
        ,"variable":["spécifique","donner","particulier","fixer","prévoir",["varier", "pas"],["pas","variation"],"invariant","fixe","stable","invariable"]
        ,"spécifique":["variable","varier"]

        ,"inexact":["fidèle","exact","précis","correct"]
        ,"fidèle":["inexact","vague","imprécis","flou","vague"]

        ,"gagner" : ["perte","perdre"]
        ,"perte":["gagner","gain"]
    }
    return dictionnaire_anto

"""
"stock = ensemble de biens destinés à être achetés"
BUT = ["être","acheter"]
>c'est faux<
le dictionnaire correct : 
'BUT': {'S': 'stock', 'O': [['utilisation', 'utiliser'], ['vente', 'vendre', 'revendre', 'revente', 'commercialisation', 'cession'], ['utiliser'], ['processus', 'fonctionnement', ['pilotage', 'quotidien']], ['produire', 'production'], ['vendre'], ['marché']]}
#donc on va regarder les termes qu'il y a dans le but, dans ce cas-ci on voit la liste contenant les synonymes de "vente" 
-> on va donc créer un deuxième dictionnaire/liste contenant des antonymes, en regardant le dictionnaire d'antonyme et les mots dans le dictionnaire du prof 
-> si dans la définition de l'élève on y voit un de ces mots - > on retourne /!\ contresens

#Un problème qu'on peut déjà soulever -> les termes à plusieurs parties





["posséder","avoir","disposer"]
[["avantage","économique","futur"],"contrepartie"]
[["sans","contrepartie"],["pas","contrepartie"]]

["lié","rapport","relative"]
[["non","lié"]]

[["valeur","économique","positif"]]
[["valeur","économique","négatif"]]
    


    [
    ["stocker","stockage","garder","emmagasiner","accumuler","conserver"],
    ["utilisation","utiliser"],

    ,["consommer"]
    ,["obligation","devoir","impératif","responsable","responsabilité"]

    ["entreprise","organisation",["organisme","activité","marchand"]],
    ["agrégat"],
    
    ["patrimoine"],
    ["entité"],
    ["financer","fianncement","payer","paiement","financier"],
    ["processus","fonctionnement",["pilotage","quotidien"]],
    ["trouver","recherche","rechercher"]

    ,["activité"]
    ,["collecte"]
    ,["actionnaire"]
    ,["banque","bancaire"]
    ,["fondateur"]
    ,["source"]
    ,["créer","établir"]
    ,["capital"]
    ,["contribution","apport"]
    ,["opération","transaction"]
    ,["immobilisation"]
    
    ,["exploitation"]
    ,["affecter"]
    
    ,["charge"]
    ,["montant","valeur","prix","somme"]
    ,["niveau"]
    ,["activité","projet"]
    ,["système"]
    ,["enregistrement"]
    ,["flux"]
    ,["environnement"]
    ,["règle"]
    ,["méthode"]
    ,["encadrer"]
    ,["légal"]
    ,["produire","production"]
    ,["document","tableau"]
    ,["représentation","image","photographie","modèle"]
    
    ,["partie"]
    ,["principe"]
    ,["gestion","gérer","organisation","organiser"]
    ,["améliorer","amélioration","perfectionner"]
    ,["comprendre"]
    ,["dirigeant","chef","supérieur"]
    ,["interne"]
    ,["synthétiser","synthèse","résumer","résumé","présentation","présenter"]

    ,["établir",["mettre","place"],"réaliser"]
    ,["budget"]
    
    ,["calculer","calcul",["processus","mathématique"],["procédé","mathématique"]]
    ,["réalité"]
    ,["prévision"]
    ,["différent","différence","écart"]
    
    ,["créancier"]
    
    ,["échéancier",["registre","paiement"]]
    ,["fournisseur"]
    ,["administration"]
    ,["taxe"]
    ,["impôt"]
    
    ,["solde"]
    ,["analyser","observer","constater","voir"]
    ,["richesse"]
    ,["définitivement"]
    ,["bénéficiaire","bénéfice","bénéficier","intérêt"]
    ,["générer"]
    ,["mesure"]

    ,["indicateur"]
    
    ,["démontrer",["faire","preuve"],"prouver","montrer","démonstration"]
    ,["autonomie"]
    ,["comptable"]
    ,["situation","état"]
    
    ,["période","moment","durée","date"]
    

    ,["forme","état"]
    ,["classique","typique","conventionnel"]
    ,["institution","établissement","institut"]
    ,["taux"]
    ,["contrat"]
    ,["négociation"]
    ,["sans transformation","finis","pas de modification","tel quel"],

    [["sans","transformation"],["pas","modification"],["tel","quel"],"finir"],

    ["durablement",["période","prolonger"],["long","terme"],["façon","durable"],["durée","prolonger"],["long","période"],["manière","permanent"]],
    [["autre","opération","courant"],["pas", "opération" ,"courant"],["autre","courant"],["pas","courant"]],
    ["immédiatement","directement",["sans","calcul","intermédiaire"]],
    [["période","donner"],["durée","spécifique"],["moment","donner"],["date","spécifique"]],
    [["charge","courant"]],
    [["cycle","production"]],
    [["cycle","exploitation"]],
    [["cycle","financement"]],
    [["cycle","investissement"]],
    ["argent","capital","fond","somme"],
    [["collecte","fond"]],
    [["agent","économique"]],
    
    ,["clé","repartition"],["boite","outil"]
    ]
"""