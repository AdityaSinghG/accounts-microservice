"""
REST API Routes
"""

from flask import Blueprint, jsonify, request

from service.models import Account

api = Blueprint("api", __name__)


@api.route("/")
def index():
    """
    Home Route
    """
    return jsonify(
        {
            "name": "Accounts Microservice",
            "version": "1.0.0",
            "status": "running",
        }
    )


##############################################################################
# CREATE AN ACCOUNT
##############################################################################
@api.route("/accounts", methods=["POST"])
def create_account():
    """
    Creates an account
    """
    data = request.get_json()

    account = Account()
    account.deserialize(data)
    account.create()

    return jsonify(account.serialize()), 201


##############################################################################
# LIST ALL ACCOUNTS
##############################################################################
@api.route("/accounts", methods=["GET"])
def list_accounts():
    """
    Returns all accounts
    """
    accounts = Account.all()

    results = []

    for account in accounts:
        results.append(account.serialize())

    return jsonify(results), 200


##############################################################################
# READ ACCOUNT
##############################################################################
@api.route("/accounts/<int:account_id>", methods=["GET"])
def get_account(account_id):
    """
    Returns one account
    """
    account = Account.find(account_id)

    if not account:
        return jsonify({"error": "Account not found"}), 404

    return jsonify(account.serialize()), 200


##############################################################################
# UPDATE ACCOUNT
##############################################################################
@api.route("/accounts/<int:account_id>", methods=["PUT"])
def update_account(account_id):
    """
    Updates an account
    """
    account = Account.find(account_id)

    if not account:
        return jsonify({"error": "Account not found"}), 404

    data = request.get_json()

    account.deserialize(data)
    account.update()

    return jsonify(account.serialize()), 200


##############################################################################
# DELETE ACCOUNT
##############################################################################
@api.route("/accounts/<int:account_id>", methods=["DELETE"])
def delete_account(account_id):
    """
    Deletes an account
    """
    account = Account.find(account_id)

    if not account:
        return jsonify({"error": "Account not found"}), 404

    account.delete()

    return "", 204
