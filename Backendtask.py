from flask import Flask, request, jsonify
import datetime
import pytz

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def my_endpoint():
    # Get query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Check if slack_name and track parameters are provided
    if not slack_name or not track:
        return jsonify({'error': 'Both slack_name and track are required'}), 400

    # Get the current day of the week
    current_day = datetime.datetime.now(pytz.utc).strftime('%A')

    # Get the current UTC time
    utc_time = datetime.datetime.now(pytz.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    # Construct the GitHub URLs based on your project
    github_repo_url = 'https://github.com/nikitadjadhav31/seeker'
    github_file_url = f'{github_repo_url}/blob/main/BAckendtask'

    # Create the JSON response
    response = {
        'slack_name': slack_name,
        'current_day': current_day,
        'utc_time': utc_time,
        'track': track,
        'github_file_url': github_file_url,
        'github_repo_url': github_repo_url,
        'status_code': 200
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
