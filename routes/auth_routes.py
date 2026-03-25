from flask import Blueprint, request, jsonify
from models.user_model import db, User
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity
from utils.email_service import send_email

auth_bp = Blueprint('auth', __name__)

# ✅ REGISTER
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json

    # 🔍 Check existing user
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"msg": "Email already exists"}), 400

    # ✅ Create user
    user = User(
        first_name=data['first_name'],
        middle_name=data.get('middle_name'),  # optional
        last_name=data['last_name'],
        email=data['email'],
        phone=data.get('phone'),
        created_by=data.get('created_by')  # optional (admin use)
    )

    user.set_password(data['password'])

    db.session.add(user)
    db.session.commit()

    return jsonify({"msg": "User Registered Successfully"})


# ✅ LOGIN
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json

    user = User.query.filter_by(email=data['email']).first()

    if user and user.check_password(data['password']):
        token = create_access_token(identity=user.id)

        return jsonify({
            "access_token": token,
            "user": {
                "id": user.id,
                "name": user.full_name(),
                "email": user.email,
                "is_admin": user.is_admin
            }
        })

    return jsonify({"msg": "Invalid credentials"}), 401

@auth_bp.route('/profile', methods=['GET'])
@jwt_required()
def get_profile():
    user_id = get_jwt_identity()

    user = User.query.get(user_id)

    if not user:
        return jsonify({"msg": "User not found"}), 404

    return jsonify({
        "id": user.id,
        "first_name": user.first_name,
        "middle_name": user.middle_name,
        "last_name": user.last_name,
        "full_name": user.full_name(),
        "email": user.email,
        "phone": user.phone,
        "image": user.image,
        "is_admin": user.is_admin,
        "created_at": str(user.created_at)
    })

@auth_bp.route('/edit-profile', methods=['PUT'])
@jwt_required()
def update_profile():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    if not user:
        return jsonify({"msg": "User not found"}), 404

    data = request.json

    # ✅ Update fields (only if provided)
    user.first_name = data.get('first_name', user.first_name)
    user.middle_name = data.get('middle_name', user.middle_name)
    user.last_name = data.get('last_name', user.last_name)
    user.phone = data.get('phone', user.phone)
    user.image = data.get('image', user.image)

    db.session.commit()

    return jsonify({"msg": "Profile updated successfully"})