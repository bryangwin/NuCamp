from flask import Blueprint, jsonify, abort, request
from flask_login import login_user, logout_user, login_required, current_user
from ..models import User, db
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route('', methods=['GET']) # decorator takes path and list of HTTP verbs
def index():
    users = User.query.all() # ORM performs SELECT query
    result = []
    for u in users:
        result.append(u.serialize()) # build list of Users as dictionaries
    return jsonify(result) # return JSON response

@bp.route('/register', methods=['POST'])
def register():
    # Check that the required fields are in the request
    if 'username' not in request.json or 'password' not in request.json or 'email' not in request.json:
        return abort(400)

    # Check that the username is not already taken
    if User.query.filter_by(username=request.json['username']).first() is not None:
        return jsonify({'message': 'Username already taken.'}), 400
    
    if User.query.filter_by(username=request.json['email']).first() is not None:
        return jsonify({'message': 'Email already taken.'}), 400

    # Create a new User instance
    user = User(
        username=request.json['username'],
        email=request.json['email'],
        password=generate_password_hash(request.json['password'])
    )

    # Add the new user to the database
    db.session.add(user)
    db.session.commit()

    return jsonify(user.serialize()), 201

@bp.route('/login', methods=['POST'])
def login():
    # Check that the required fields are in the request
    if 'username' not in request.json or 'password' not in request.json:
        return abort(400)

    # Query the database for the User
    user = User.query.filter_by(username=request.json['username']).first()

    # Check if the User was found and the password is correct
    if user is None or not check_password_hash(user.password, request.json['password']):
        return jsonify({'message': 'Invalid username or password.'}), 401

    # Log the user in
    login_user(user)

    return jsonify(user.serialize())

@bp.route('/logout', methods=['POST'])
@login_required
def logout():
    # Log the user out
    logout_user()
    return jsonify({'message': 'Logged out.'})

@bp.route('/<int:id>/follow', methods=['POST'])
@login_required
def follow(id):
    # Get the user to follow
    user_to_follow = User.query.get(id)
    if user_to_follow is None:
        return jsonify({'message': 'User not found.'}), 404

    # Check that the current user is not the same as the user to follow
    if current_user.id == user_to_follow.id:
        return jsonify({'message': 'Cannot follow yourself.'}), 400

    # Add the follow relationship
    current_user.follow(user_to_follow)

    return jsonify({'message': 'Followed user.'})

@bp.route('/<int:id>/unfollow', methods=['POST'])
@login_required
def unfollow(id):
    # Get the user to unfollow
    user_to_unfollow = User.query.get(id)
    if user_to_unfollow is None:
        return jsonify({'message': 'User not found.'}), 404

    # Check that the current user is not the same as the user to unfollow
    if current_user.id == user_to_unfollow.id:
        return jsonify({'message': 'Cannot unfollow yourself.'}), 400

    # Remove the follow relationship
    current_user.unfollow(user_to_unfollow)

    return jsonify({'message': 'Unfollowed user.'})

@bp.route('/<int:id>/followers', methods=['GET'])
def followers(id):
    # Get the user
    user = User.query.get(id)
    if user is None:
        return jsonify({'message': 'User not found.'}),
