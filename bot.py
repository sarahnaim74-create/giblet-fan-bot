
import os
import random
from atproto import Client

HANDLE = os.environ["BSKY_HANDLE"]
PASSWORD = os.environ["BSKY_PASSWORD"]

client = Client()
client.login(HANDLE, PASSWORD)

posts = [
    "Giblet est mon favori. Je ne partage pas, c'est mon personnage préféré ! ❤️",
    "Je suis exclusivement fan de Giblet. Aucun autre personnage ne le remplace.",
    "Giblet est à moi dans mon univers de fan. ❤️",
    "Je ne fais pas de yumeship. Je suis simplement une fan exclusive de Giblet.",
    "Personne ne remplacera Giblet dans mon cœur de fan.",
    "Mon compte parle de Giblet et uniquement de Giblet !"
]

client.send_post(
    text=random.choice(posts),
    langs=["fr"]
)

print("Publication envoyé
e !")
