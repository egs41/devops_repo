from flask import Flask, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

# 데이터 파일 경로
DATA_FILE = '/tmp/users.json'

def load_users():
    """사용자 데이터 로드"""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    return []

def save_users(users):
    """사용자 데이터 저장"""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(users, f, ensure_ascii=False, indent=2)

@app.route('/signup', methods=['POST'])
def signup():
    """신규 유저 회원가입"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'JSON data is required'}), 400
            
        username = data.get('username', '').strip()
        email = data.get('email', '').strip()
        
        if not username or not email:
            return jsonify({'error': 'Username and email are required'}), 400
        
        if '@' not in email:
            return jsonify({'error': 'Invalid email format'}), 400
        
        users = load_users()
        
        # 중복 체크
        for user in users:
            if user.get('username') == username:
                return jsonify({'error': 'Username already exists'}), 409
            if user.get('email') == email:
                return jsonify({'error': 'Email already exists'}), 409
        
        # 새 사용자 추가
        new_user = {
            'username': username,
            'email': email,
            'created_at': datetime.now().isoformat()
        }
        users.append(new_user)
        save_users(users)
        
        return jsonify({
            'message': 'User created successfully',
            'user': new_user
        }), 201
    
    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'service': 'signup'}), 200

@app.route('/', methods=['GET'])
def root():
    return jsonify({
        'service': 'User Signup Service',
        'endpoints': ['/signup', '/health']
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)