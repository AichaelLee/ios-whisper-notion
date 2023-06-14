from flask import Flask, request
import os
import tempfile
from api import handle_transcript
import re
from datetime import datetime
import threading

app = Flask(__name__)


@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    auth_header = request.headers.get('auth')
    expected_password = os.environ.get('HEADER_AUTH_PASS')
    if auth_header != expected_password:
        return 'Unauthorized access', 401

    if 'file' not in request.files:
        return 'No file part in the request.', 400

    file = request.files['file']

    if file.filename == '':
        return 'No selected file.', 400

    if file:
        # Get the extension of the original file name
        file_extension = os.path.splitext(file.filename)[1]

        # Replace non-ASCII characters and spaces
        sanitized_filename = re.sub('[^\x00-\x7F]+', ' ', file.filename)
        sanitized_filename = sanitized_filename.replace(" ", "_")

        # Add a time-based prefix to the filename to ensure its uniqueness
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        sanitized_filename = f"{timestamp}_{sanitized_filename}"

        with tempfile.NamedTemporaryFile(delete=False, prefix=sanitized_filename, suffix=file_extension) as temp_file:
            temp_file.write(file.read())

        with open(temp_file.name, 'rb') as audio_file:
            completed = handle_transcript_with_timeout(audio_file)
            if not completed:
                return "Transcribing in the background..."

        return "Transcription complete"


# Executes transcription task with timeout
def handle_transcript_with_timeout(audio_file, timeout=2):
    transcript_thread = threading.Thread(target=handle_transcript.handle_transcript, args=(audio_file,))
    transcript_thread.start()
    transcript_thread.join(timeout)
    return not transcript_thread.is_alive()


if __name__ == '__main__':
    app.run(debug=True)
