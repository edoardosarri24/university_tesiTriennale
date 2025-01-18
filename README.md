# Titolo: L’etica nell’Intelligenza Artificiale: il problema di misurare la fairness nei sistemi governati dai dati.
### Relatrice: Maria Cecilia Verri - mariacecilia.verri@unifi.it
### Correlatore: Massimiliano Mancini - massimiliano.mancini@unifi.it
---
L’intelligenza artificiale è sempre più presente all’interno delle nostre vite, e spesso
le decisioni basate sugli agenti intelligenti determinano il futuro delle persone. Per
questo motivo, risulta normale chiederci se un sistema basato sul machine learning
agisca sempre in modo equo, onesto e rispettoso dell’uguaglianza e dell’imparzialità.
L’obiettivo della tesi è presentare le definizioni del concetto di fairness presenti
in letteratura, in modo da poter stabilire successivamente se un dataset risulta equo
oppure no.

I primi aspetti che sono stati introdotti sono i concetti di intelligenza artificiale e di
machine learning. Si è cercato di offrire una panoramica generale, esaminando la loro
evoluzione storica, esplorando le loro applicazioni attuali e cercando di spiegare come
avviene l’apprendimento automatico in sistemi di questo tipo.

Successivamente, sono stati presentati tre criteri di classificazione per il concetto di
fairness: indipendenza, separazione e sufficienza. Sono state analizzate otto definizio-
ni, ognuna appartenente a un preciso criterio. In particolare sono state approfondite
quelle relative al criterio di indipendenza: la parità statistica e il diverso impatto.
È stato poi presentato Adult, uno dei dataset più usati e studiati in letteratura. Sono
stati descritti tutti gli attributi che lo compongono, con particolare enfasi su quelli usati
per valutare la fairness.

L’ultima parte della tesi è mirata a capire se Adult è fair secondo le definizioni rela-
tive al principio di indipendenza, osservando gli attributi indicanti il sesso e la razza.
Per svolgere questa analisi è stato usato Python e la libreria Pandas. Il risultato che si è
ottenuto indica che Adult non risulta fair per nessuno dei due attributi considerati, e
in particolar modo per il genere.
