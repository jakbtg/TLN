# Piton Dialog System

Chatbot che impersona il personaggio di Severus Piton, insegnante di Pozioni alla scuola di Magia e Stregoneria di Hogwarts.  
La relazione del progetto è disponibile [qui](pdf/Relazione.pdf).

## Utilizzo

Per provare il bot consiglio di utilizzare un virtual environment, per installare le dipendenze è sufficiente eseguire il comando `pip install -r requirements.txt`.  
Per avviarlo conviene aprire il file `dialog_manager.py` in modo da poter settare a piacimento il parametro `can_listen` che permette di attivare o meno la funzione di riconoscimento vocale.

### Importante

Per un corretto funzionamento del programma:

- Modalità con riconoscimento vocale: parlare solamente dopo che viene stampato "...ready to listen..."
- Modalità standard: scrivere solamente dopo che viene stampato "Student: "
