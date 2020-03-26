from flask import Flask, jsonify, request

app = Flask(__name__) # 임포트한 Flask 클래스를 객체화 (instantiate)
app.users = {}
app.tweets = []
app.follows = {}
app.id_count = 1

@app.route("/ping", methods=["GET"])
def ping():
    return "pong"

@app.route("/sign-up", methods=["POST"])
def sign_up():
    new_user = request.json
    new_user["id"] = app.id_count
    app.users[app.id_count] = new_user
    app.id_count += 1
    return jsonify(new_user)


@app.route("/tweet", methods=["POST"])
def tweet():
    payload = request.json
    user_id = int(payload['id'])
    tweet = payload['tweet']

    if user_id not in app.users:
        return '사용자가 존재하지 않습니다', 400
    
    if len(tweet) > 300:
        return '사용자가 존재하지 않습니다', 400

    tweet = {
        'id': user_id,
        'tweet': tweet
    }
    app.tweets.append(tweet)

    return '', 200


@app.route("/follow", methods=["POST"])
def follow():
    payload = request.json
    user_id = int(payload['id'])
    user_id_to_follow = int(payload['follow'])

    if user_id not in app.users or user_id_to_follow not in app.users:
        return "사용자가 존재하지 않습니다.", 400

    user = app.users[user_id]
    user.setdefault('follow', set()).add(user_id_to_follow)

    return jsonify(user)

# TODO: 커스텀 JSON 인코더 개발.