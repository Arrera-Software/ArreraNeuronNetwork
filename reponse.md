3. Dans self.__reponse_frame (Lié à reply_mail(objet, mail_recu, consigne_reponse))
Cette vue sert à répondre à un mail reçu en tenant compte de ses consignes. Elle demande 3 champs d'entrée :
1.
Un Titre :
◦
Un aLabel en haut à gauche (ex. : "Répondre à un mail").
2.
Section Objet d'origine :
◦
Un aLabel (ex. : "Objet du mail reçu :").
◦
Un champ de saisie simple aEntry (qui servira à générer le Re: ...).
3.
Section Mail reçu :
◦
Un aLabel (ex. : "Mail reçu :").
◦
Une zone de texte aText (moyenne ou scrollable) pour y coller le message de l'expéditeur.
4.
Section Consignes de réponse :
◦
Un aLabel (ex. : "Vos instructions de réponse :").
◦
Une zone aText (ou une aEntry large) pour expliquer ce qu'il faut répondre (ex. : "Refuser poliment et proposer jeudi à 10h").