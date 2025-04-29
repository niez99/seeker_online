# Deployment Instructions for Render.com (Free Tier)

This document provides step-by-step instructions to deploy your Flask app to Render.com, a free hosting platform that does not require payment information for basic usage.

## Prerequisites

- Create a free account on [Render.com](https://render.com/)
- Install Git and have your project in a Git repository
- Push your code to a GitHub, GitLab, or Bitbucket repository (Render connects to these)

## Deployment Steps

1. Push your local project to a Git repository (GitHub, GitLab, or Bitbucket):
   ```bash
   git init
   git add .
   git commit -m "Prepare for Render deployment"
   git remote add origin <your-repo-url>
   git push -u origin main
   ```
   Replace `<your-repo-url>` with your repository URL.

2. Log in to your Render.com account.

3. Click on **New** > **Web Service**.

4. Connect your GitHub/GitLab/Bitbucket account and select the repository containing your Flask app.

5. Configure the service:
   - **Name:** Choose a name for your app.
   - **Region:** Select a region close to your users.
   - **Branch:** Select the branch to deploy (e.g., main).
   - **Runtime:** Select **Python 3**.
   - **Build Command:** Leave empty or use `pip install -r requirements.txt`.
   - **Start Command:** Use the command from your Procfile:
     ```
     gunicorn app:app
     ```

6. Click **Create Web Service**.

7. Render will build and deploy your app. Once deployed, you will get a URL where your app is live.

## Notes

- Your SQLite database will be ephemeral on Render as well. For persistent storage, consider using a managed database service.
- You can view logs and redeploy from the Render dashboard.
- Render offers free SSL and custom domains.

## Troubleshooting

- If the app fails to start, check the logs in the Render dashboard.
- Ensure your `requirements.txt` and `Procfile` are correctly configured.

---

Follow these steps to deploy your Flask app quickly and for free on Render.com.
