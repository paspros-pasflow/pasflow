from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # To allow cross-origin requests from your frontend

# Team member data with their areas of expertise
team_members = [
    {"name": "Alice Johnson", "expertise": ["leads", "follow up", "client relations"]},
    {"name": "Bob Smith", "expertise": ["data analysis", "report", "analytics"]},
    {"name": "Charlie Brown", "expertise": ["marketing", "campaign", "advertisement"]},
    {"name": "Diana Prince", "expertise": ["project management", "deadline", "planning"]},
    {"name": "Ethan Hunt", "expertise": ["security", "audit", "compliance"]}
]

def find_best_match(task):
    """Find the best team member based on the task description."""
    task = task.lower()
    for member in team_members:
        for keyword in member["expertise"]:
            if keyword in task:
                return member["name"]
    # Fallback to a random member if no keyword matches
    import random
    return random.choice(team_members)["name"]

@app.route('/assign_task', methods=['POST'])
def assign_task():
    """Endpoint to handle task assignment."""
    data = request.get_json()
    task_description = data.get("task", "").strip()

    if not task_description:
        return jsonify({"status": "error", "message": "Task description is required."}), 400

    assigned_member = find_best_match(task_description)
    return jsonify({"status": "success", "assigned_member": assigned_member})

if __name__ == '__main__':
    app.run(debug=True)
