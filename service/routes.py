"""
Account Service Routes
"""
from flask import jsonify, request, abort
from service import app
from service.models import Account


@app.route("/health")
def health():
    """Health check endpoint"""
    return jsonify({"status": "OK"}), 200


@app.route("/accounts", methods=["POST"])
def create_account():
    """Create a new account"""
    data = request.get_json()
    if not data:
        abort(400, description="No data provided")

    account = Account()
    account.deserialize(data)
    account.create()

    return jsonify(account.serialize()), 201


@app.route("/accounts", methods=["GET"])
def list_accounts():
    """List all accounts"""
    accounts = Account.all()
    return jsonify([a.serialize() for a in accounts]), 200


@app.route("/accounts/<int:account_id>", methods=["GET"])
def read_account(account_id):
    """Read a single account"""
    account = Account.find(account_id)
    if not account:
        abort(404, description=f"Account {account_id} not found")
    return jsonify(account.serialize()), 200


@app.route("/accounts/<int:account_id>", methods=["PUT"])
def update_account(account_id):
    """Update an account"""
    account = Account.find(account_id)
    if not account:
        abort(404, description=f"Account {account_id} not found")

    data = request.get_json()
    account.deserialize(data)
    account.update()

    return jsonify(account.serialize()), 200


@app.route("/accounts/<int:account_id>", methods=["DELETE"])
def delete_account(account_id):
    """Delete an account"""
    account = Account.find(account_id)
    if not account:
        abort(404, description=f"Account {account_id} not found")

    account.delete()
    return "", 204


@app.errorhandler(400)
def bad_request(e):
    return jsonify({"error": str(e)}), 400


@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": str(e)}), 404
