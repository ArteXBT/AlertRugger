# ⏰ Telegram Notification Alarm

Un bot Telegram basé sur Python qui surveille un canal ou un groupe spécifique et déclenche une action (comme un appel via IFTTT) en réponse à chaque nouveau message détecté. Le bot utilise la bibliothèque **Telethon** pour fonctionner et peut être hébergé gratuitement sur **Railway**.

## 🛠️ Fonctionnalités

- 🔔 Surveille un canal ou groupe Telegram pour détecter de nouveaux messages.
- 📤 Envoie automatiquement une commande `/ifttt@IFTTT` à un bot pour déclencher une action.
- 📞 Active un appel vocal via le service IFTTT VoIP Calls.
- ⏳ Attente de 5 secondes après chaque message pour éviter les boucles infinies.
- 💻 Fonctionne 24h/24 et peut être hébergé gratuitement.

---

## 📋 Prérequis

Avant de commencer, assurez-vous d'avoir :

1. **Un compte Telegram** avec accès au canal ou groupe que vous voulez surveiller.
2. **Un compte sur [Telegram Developers](https://my.telegram.org/)** pour obtenir votre `API ID` et `API Hash`.
3. **Un compte IFTTT** (abonnement à 4€/mois requis pour les automatisations avancées).
4. Python 3.7+ installé sur votre machine.

---

## 🚀 Installation

### 1. Clonez ce dépôt

``` bash
git clone https://github.com/votre-utilisateur/telegram-notification-alarm.git
cd telegram-notification-alarm
```

### 2. Installez les dépendances

``` bash
pip install -r requirements.txt
```

### 3. Configurez le script

Dans le fichier Python principal (`main.py`), remplacez les valeurs suivantes :

- `VOTRE_API_ID` : Votre **API ID** obtenu depuis Telegram.
- `VOTRE_API_HASH` : Votre **API Hash** obtenu depuis Telegram.
- `USERNAME_CANAL` : Le `@username` du canal ou groupe Telegram à surveiller.

---

## ⚙️ Configuration IFTTT

Pour que le bot déclenche un appel vocal via IFTTT, procédez comme suit :

1. **Créer un compte IFTTT** sur [ifttt.com](https://ifttt.com/). Souscrivez à l’abonnement à 4€/mois pour débloquer les automatisations avancées.
2. **Créer une applet Telegram → VoIP Call** :
   - Dans IFTTT, cliquez sur **Create** pour créer une nouvelle applet.
   - Configurez le déclencheur (**IF This**) :
     1. Choisissez **Telegram** comme service.
     2. Sélectionnez **Message envoyé dans un groupe**.
     3. Connectez le bot Telegram d'IFTTT au même groupe où votre bot envoie `/ifttt@IFTTT`.
   - Configurez l'action (**Then That**) :
     1. Choisissez **VoIP Calls** comme service.
     2. Configurez l’action **Call this device** pour que votre téléphone reçoive un appel.
3. Activez l’applet pour qu’elle fonctionne dès que votre bot envoie le message.

---

## 🌐 Hébergement sur Railway (Gratuit)

Pour exécuter le bot 24h/24, vous pouvez l’héberger gratuitement sur Railway :

1. Créez un compte gratuit sur [Railway.app](https://railway.app/).
2. Importez ce projet directement depuis GitHub.
3. Configurez la commande de démarrage :
   - Accédez à votre service Railway.
   - Cliquez sur **Settings**.
   - Dans **Start Command**, entrez :

     ``` plaintext
     python alertRugger.py
     ```

5. Ajoutez vos variables d’environnement dans Railway :
   - `API_ID` : Votre **API ID**.
   - `API_HASH` : Votre **API Hash**.
   - `CHANNEL_USERNAME` : Le `@username` du canal ou groupe.

6. Déployez le projet ! Votre bot sera désormais actif en permanence.

---

## 📢 Intégrer les Alertes FOMO dans votre Groupe

1. **Commencer une discussion avec le bot [FOMO](https://t.me/fomo)**

2. **Configurer un profil sur FOMO** :
   - Tapez la commande `/menu` pour accéder au menu principal.
   - Sélectionnez **Profiles**.
   - Cliquez sur **New Profile** pour créer un nouveau profil d'alerte.
   
3. **Ajouter le bot à votre groupe** :
   - Après avoir créé un profil, cliquez sur **Add bot to group**.
   - Sélectionnez le groupe dans lequel se trouve également le bot IFTTT.
   - Suivez les instructions de **@fomo** pour finaliser la configuration et l'intégrer correctement.

Une fois cette étape terminée, les alertes de FOMO seront envoyées dans le groupe et pourront être utilisées en combinaison avec le bot IFTTT pour déclencher les actions appropriées.

---

## 📚 Contribuer

Les contributions sont les bienvenues ! Si vous souhaitez ajouter des fonctionnalités ou améliorer ce projet :

1. Forkez ce dépôt.
2. Créez une branche pour vos modifications (`git checkout -b feature/amélioration`).
3. Faites un commit (`git commit -m "Ajout d'une nouvelle fonctionnalité"`).
4. Faites un push sur la branche (`git push origin feature/amélioration`).
5. Ouvrez une Pull Request !
