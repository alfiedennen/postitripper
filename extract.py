import http.server
import socketserver
import threading
import os
import requests

# Your OpenAI API Key
api_key = "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"  # Replace this with your actual API key

# Folder containing images - adjust to your images' directory
image_folder = 'D:\\Visual Studio Code Projects\\Batch OCR\\images\\'

# Port for the HTTP server (choose a port that is not in use)
PORT = 3128

def start_server(path, port=3128):
    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=path, **kwargs)
        
        def log_message(self, format, *args):
            pass  # Override to prevent printing access log messages to the terminal

    with socketserver.TCPServer(("", port), Handler) as httpd:
        httpd.serve_forever()

def run_server():
    server_thread = threading.Thread(target=start_server, args=(image_folder, PORT), daemon=True)
    server_thread.start()

def extract_text_gpt4(image_filename):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    # Construct image URL using ngrok URL
    ngrok_url = "https://bada-5-64-156-198.ngrok-free.app"  # You need to replace this with your actual ngrok URL
    image_url = f"{ngrok_url}/{image_filename}"

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": "Extract all readable text from this image. If text is obscured or cannot be read, do not tell me, just extract and print what can be read. Similary, do not preprend extractions with any preamble, only provide the extracted text. Where there are multiple postits,exract the text from each in turn."
            },
            {
                "role": "system",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_url,
                        }
                    }
                ]
            }
        ],
        "max_tokens": 300
    }
    
    # API call
    return requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload).json()

def process_images(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            try:
                response = extract_text_gpt4(filename)
                extracted_text = response['choices'][0]['message']['content'] if 'choices' in response and len(response['choices']) > 0 else ""
                print(f"File: {filename}\n{extracted_text}\n")  # Modified print statement
            except:
                pass  # Silently handle errors to avoid printing them

if __name__ == '__main__':
    run_server()
    process_images(image_folder)