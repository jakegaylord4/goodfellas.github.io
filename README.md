# PolarGigs

## GitHub Link: https://github.com/jakegaylord4/goodfellas.github.io/tree/non-auth

## How to Start the Server

1. **(Recommended) Create and activate a virtual environment:**
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Set environment variables (optional):**
   - Edit `.env` to set your `PORT` or `SECRET_KEY` if needed.

4. **Run the Flask server:**
   ```
   python app.py
   ```

- The server will start on the port specified in `.env` (default is 5000 or 5001 if 5000 is in use).
- Access the server at `http://localhost:<PORT>` in your browser.

---

**Note:** If you see an error about the port being in use, either stop the other process or change the `PORT` in `.env`.

## App Usage

1. Create an account with the Sign-Up button.

2. Login with your new account details.

3. Find or create a service with their respective pages.

## App Notes

- The app comes prepopulated with two example services to view.
- Data does not persist between server restarts. Images are saved to disk, but all other data will be lost.
