# Piton Dialog System

Chatbot che impersona il personaggio di Severus Piton, insegnante di Pozioni alla scuola di Magia e Stregoneria di Hogwarts.  
La relazione del progetto è disponibile [qui](pdf/Relazione.pdf).

## Utilizzo

Per provare il bot consiglio di utilizzare un virtual environment, per installare le dipendenze è sufficiente eseguire il comando `pip install -r requirements.txt`.  
Per avviarlo conviene aprire il file `dialog_manager.py` in modo da poter settare a piacimento il parametro `can_listen` che permette di attivare o meno la funzione di riconoscimento vocale.  
Per un corretto funzionamento del programma:

- Modalità con riconoscimento vocale: parlare solamente dopo che viene stampato "...ready to listen..."
- Modalità standard: scrivere solamente dopo che viene stampato "Student: "

## Nota

Forse la funzione di Text-to-Speech non funziona su computer che non siano Apple, o anche forse Apple più datati del mio dispositivo. Questo perchè utilizzo una voce sintetizzata disponibile localmente sul mio computer, in particolare: `com.apple.voice.compact.en-GB.Daniel`.
Se non dovesse funzionare, si può provare a commentare le prime due righe della funzione `speak`, in quel modo dovrebbe funzionare con la voce di default del sistema, sempre che sia disponibile.  
Se anche in questo caso non dovesse funzionare, consiglio di commentare tutto il contenuto della funzione `speak` in modo da non avere nessun output vocale.
