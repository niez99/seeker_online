# Deployment Instructions for Heroku

This document provides step-by-step instructions to deploy the Flask app to Heroku.

## Prerequisites

- Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
- Have a Heroku account and be logged in via CLI (`heroku login`)
- Git installed and your project initialized as a git repository

## Deployment Steps

1. Initialize git repository (if not already done):
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```

2. Create a new Heroku app:
   ```bash
   heroku create
   ```

3. Push your code to Heroku:
   ```bash
   git push heroku main
   ```
   (If your default branch is `master`, use `git push heroku master`)

4. Scale the web dyno to run one instance:
   ```bash
   heroku ps:scale web=1
   ```

5. Open your deployed app in the browser:
   ```bash
   heroku open
   ```

## Notes

- Your `Procfile` uses `gunicorn` to run the app.
- `requirements.txt` includes necessary dependencies.
- `runtime.txt` specifies the Python version.
- SQLite database (`database.db`) will be created on the Heroku dyno filesystem but will not persist between restarts. For persistent data, consider using a Heroku Postgres add-on.
- To view logs, use:
  ```bash
  heroku logs --tail
  ```

## Troubleshooting

- If you encounter issues, check the logs with the command above.
- Ensure your local git branch matches the branch you push to Heroku.

---

Follow these steps to deploy your Flask app to Heroku successfully.
