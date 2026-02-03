from flask import Flask, jsonify
import json
import os

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

@app.route('/users', methods=['GET'])
def list_users():
    """가입된 사용자 목록 조회"""
    try:
        users = load_users()
        return jsonify({
            'users': users,
            'count': len(users),
            'message': 'Users retrieved successfully'
        }), 200
    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'service': 'user-list'}), 200

@app.route('/', methods=['GET'])
def root():
    return jsonify({
        'service': 'User List Service',
        'endpoints': ['/users', '/health']
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=False)