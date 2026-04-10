# Flask Backend Setup

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
