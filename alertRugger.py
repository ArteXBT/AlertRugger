import asyncio
from telethon import TelegramClient, events

# Informations de connexion
api_id = 'API_ID'         # Remplacez par votre API ID
api_hash = 'API_Hash'     # Remplacez par votre API Hash
channel_username = '@canal'  # Le @username du canal à surveiller

# Créez un client Telegram
client = TelegramClient('ruggeralrt', api_id, api_hash)

# Variable de contrôle pour éviter l'envoi répété
message_sent = False

async def main():
    # Se connecter et surveiller les nouveaux messages dans le canal
    await client.start()

    # Définir l'événement de surveillance du canal
    @client.on(events.NewMessage(chats=channel_username))
    async def handler(event):
        global message_sent
        # Si le message a déjà été envoyé récemment, ne pas répondre à nouveau
        if message_sent:
            return

        print("Nouveau message détecté dans le canal !")
        
        # Envoyer le message souhaité à IFTTT bot
        await client.send_message(channel_username, '/ifttt@IFTTT')
        
        # Mettre à jour la variable pour indiquer que le message a été envoyé
        message_sent = True
        
        # Attendre un peu avant de permettre l'envoi de nouveaux messages
        await asyncio.sleep(60)

        # Réinitialiser la variable pour permettre à nouveau l'envoi de messages
        message_sent = False

    print("Bot en cours d'exécution. En attente de messages dans le canal...")

    # Recommencer à surveiller après chaque message
    await client.run_until_disconnected()

# Démarrage du client
with client:
    client.loop.run_until_complete(main())
