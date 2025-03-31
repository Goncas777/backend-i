'''md
# Spotify Playback Statistics App

This project is a web application that analyzes and visualizes your Spotify playback history, similar to Spotify Wrapped. Users can upload their Spotify extended playback history files to generate statistics about their listening habits.

## Features
- Upload your **Spotify extended playback history** file.
- View detailed statistics about your listening habits.
- Use pre-loaded sample data if you don’t have a playback history file.
- Secure user authentication system.

## Installation & Setup

### 1. Clone the Repository
```bash
git https://github.com/Goncas777/backend-i/tree/main/spotifyapp.git
cd spotifyapp
```

### 2. Install Dependencies
Make sure you have **Poetry** installed. If not, install it with:
```bash
pip install poetry
```

Now, install the required dependencies:
```bash
poetry install
```

### 3. Start the Application
The app runs in Docker using `docker-compose`. Start it with:
```bash
make compose.start
```

### 4. Run Database Migrations
After starting the containers, apply migrations:
```bash
make compose.migrate
```

### 5. Create a Superuser (Optional)
If you want to create an admin user:
```bash
make create-superuser
```

### 6. Run Tests
To ensure everything is working correctly, run:
```bash
make pytest
```

## How to Use the App
1. Log in or create an account.
2. Upload your Spotify **extended playback history** file.
   - To get this file, go to your Spotify **Account Settings** → **Privacy Settings** → **Download Your Extended Playback History**.
3. If you don’t have a history file, you can use the preloaded sample data found in `media/uploads/` (3 real playback history `.zip` files).
4. View your listening statistics and insights!

## Notes
- Ensure that your environment variables for **PostgreSQL** are properly set.
- The app is meant to run inside Docker, so always use `make` commands for setup and execution.

'''

