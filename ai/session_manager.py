import json
import os


# Absolute path for session file
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

SESSION_FILE = os.path.join(
    BASE_DIR,
    "database",
    "session.json"
)



# ----------------------------
# Load Sessions
# ----------------------------

def load_sessions():

    if not os.path.exists(SESSION_FILE):

        return {}


    try:

        with open(
            SESSION_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)


    except Exception as e:

        print(
            "Session loading error:",
            e
        )

        return {}



# ----------------------------
# Save Sessions
# ----------------------------

def save_sessions(sessions):

    with open(
        SESSION_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            sessions,
            file,
            indent=4
        )



# Default Farmer Session

DEFAULT_SESSION_ID = "farmer_001"



# ----------------------------
# Get Session
# ----------------------------

def get_session(
        session_id=DEFAULT_SESSION_ID
):

    sessions = load_sessions()


    if session_id not in sessions:

        sessions[session_id] = {

            "language": "en",

            "crop": None,

            "intent": None,

            "history": []

        }

        save_sessions(sessions)


    return sessions[session_id]



# ----------------------------
# Update Session
# ----------------------------

def update_session(
        language,
        crop,
        intent,
        user,
        bot,
        session_id=DEFAULT_SESSION_ID
):


    sessions = load_sessions()



    if session_id not in sessions:

        sessions[session_id] = {

            "language": language,

            "crop": crop,

            "intent": intent,

            "history": []

        }



    # Update farmer information

    sessions[session_id]["language"] = language

    sessions[session_id]["crop"] = crop

    sessions[session_id]["intent"] = intent



    # Add conversation history

    sessions[session_id]["history"].append({

        "user": user,

        "bot": bot

    })


    # Keep only latest 10 conversations

    sessions[session_id]["history"] = (
        sessions[session_id]["history"][-10:]
    )


    save_sessions(sessions)


    print("Session saved successfully")