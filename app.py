from flask import Flask, jsonify, request


def create_app():
    """Create and configure the ACEest Fitness & Gym web application."""
    app = Flask(__name__)
    members = []

    @app.get("/")
    def health_check():
        return jsonify({"service": "ACEest Fitness & Gym", "status": "healthy"})

    @app.get("/members")
    def list_members():
        return jsonify({"count": len(members), "members": members})

    @app.post("/members")
    def add_member():
        payload = request.get_json(silent=True)
        if not payload or not isinstance(payload.get("name"), str) or not payload["name"].strip():
            return jsonify({"error": "A non-empty member name is required."}), 400

        member = {
            "id": len(members) + 1,
            "name": payload["name"].strip(),
            "plan": payload.get("plan", "standard"),
        }
        members.append(member)
        return jsonify(member), 201

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)