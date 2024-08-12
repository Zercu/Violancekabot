# Violancekabot

## Suraj Heroku de
:

```markdown
# Telegram Music Bot

A Telegram bot that plays music in voice chats, using YouTube as a source. The bot supports commands for admins, including playing music, stopping playback, sending announcements, and providing support and donation links.

## Features

- **Play music**: Search and play songs from YouTube in a Telegram voice chat.
- **Admin Controls**: Only designated admins can control music playback, make announcements, and manage the bot.
- **Support and Donation**: Provides users with a support group link and a donation link.

## Commands

- **/start**: Start interacting with the bot.
- **/play <song name>**: Search for a song on YouTube and play it in the voice chat (admin only).
- **/stop**: Stop the current song (admin only).
- **/announce <message>**: Make an announcement in the chat (admin only).
- **/support**: Get a link to the support group.
- **/donate**: Get a link to make a donation.

## Deployment on Mobile (Using Termux)

### 1. Install Termux

- Download and install Termux from [Google Play Store](https://play.google.com/store/apps/details?id=com.termux) or [F-Droid](https://f-droid.org/en/packages/com.termux/).

### 2. Install Required Packages

Open Termux and run the following commands to install the necessary packages:

```bash
pkg update
pkg install git python nodejs ffmpeg
pip install yt-dlp
npm install -g heroku
```

### 3. Set Up GitHub Repository

1. **Clone Your Repository**:

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Add and Edit Files**:

   - Use a text editor (`nano`, `vim`) to edit `app.py`, `requirements.txt`, `Procfile`, etc.
   - Commit and push your changes:

   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin master
   ```

### 4. Deploy to Heroku from Mobile

1. **Log In to Heroku**:

   ```bash
   heroku login
   ```

2. **Create a New Heroku App**:

   ```bash
   heroku create your-app-name
   ```

3. **Set Environment Variables**:

   ```bash
   heroku config:set API_ID=your_api_id
   heroku config:set API_HASH=your_api_hash
   heroku config:set BOT_TOKEN=your_bot_token
   heroku config:set SESSION_NAME=your_session_name
   heroku config:set ADMIN_IDS=1234567890,9876543210
   heroku config:set SUPPORT_GROUP_LINK=https://t.me/your_support_group
   heroku config:set DONATION_LINK=https://www.paypal.com/your_donation_link
   ```

4. **Deploy the App**:

   ```bash
   git push heroku master
   ```

### 5. Monitor the Bot

- **View Logs**:

   ```bash
   heroku logs --tail -a your-app-name
   ```

- **Interact with the Bot**: Use the commands in your Telegram group or chat to control the bot.

## Additional Information

- **File Management**: Remember that Heroku’s file system is ephemeral. Persistent storage should be handled using external storage services.
- **Contributing**: Contributions are welcome! Feel free to fork the repository and submit a pull request.
- **License**: This project is licensed under the MIT License.

```

### **Summary of What’s Included**

- **Bot Features**: Highlights the key features of the bot.
- **Commands**: Lists the bot commands and their descriptions.
- **Deployment on Mobile**:

Provides detailed steps on how to deploy the bot from a mobile device using Termux, GitHub, and Heroku. This includes installing necessary packages, setting up a GitHub repository, and deploying the bot to Heroku.

### **How to Use This Documentation**

1. **Create the `README.md`**:
   - Copy the content provided above into a `README.md` file in your project directory.

2. **Commit and Push**:
   - After creating or editing the `README.md`, commit and push it to your GitHub repository:

   ```bash
   git add README.md
   git commit -m "Added README.md with deployment instructions and commands"
   git push origin master
   ```

3. **Deploy to Heroku**:
   - Follow the instructions in the README to deploy your bot to Heroku directly from your mobile device.

This documentation ensures that anyone with access to the repository, including you, can easily set up, deploy, and manage the Telegram music bot, even from a mobile device. The commands section provides clear guidance on how to interact with the bot once it’s deployed.