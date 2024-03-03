# PostItRipper

This Python-based project facilitates the batch processing of images for text extraction using OpenAI's GPT-4 Vision API. It serves images from a specified directory via an HTTP server and utilizes the API to extract and print readable text from those images. This tool is especially useful for projects requiring optical character recognition (OCR) on multiple files - my use case is post it notes from workshops and user research but it will work with any text in images.

## Features

- **Local HTTP Server**: Hosts images from a specified directory for processing (via ngrok free)
- **Integration with OpenAI GPT-4 Vision API**: Leverages advanced AI for accurate text extraction from images.
- **Batch Processing Capability**: Processes all images in the specified directory automatically.
- **Efficient Text Extraction**: Directly extracts readable text from images, ideal for OCR tasks.
- **Robust Error Handling**: Designed to handle and silently recover from errors to ensure uninterrupted processing.

## Prerequisites

To use this project, you'll need:

- Python 3.6 or newer.
- `requests` library installed in your Python environment.
- An OpenAI API key.
- A running instance of `ngrok` or similar service to expose your local server to the internet.
