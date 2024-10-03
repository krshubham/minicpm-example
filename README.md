# Image and Prompt Processor

This project is a FastAPI-based web application that processes images and text prompts using the Ollama API with the minicpm-v model.

## Prerequisites

- Python 3.7+
- Ollama installed and running with the minicpm-v model

## Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up Ollama:
   - Install Ollama from [https://ollama.ai/](https://ollama.ai/)
   - Run the following command to pull and run the minicpm-v model:
     ```
     ollama run minicpm-v
     ```

## Running the Server

1. Start the FastAPI server:
   ```
   python app.py
   ```

2. Open your web browser and navigate to `http://localhost:8000`

## Usage

1. On the home page, you'll see a form where you can enter a prompt and upload an image.
2. Fill in the prompt and select an image file.
3. Click "Process" to submit the form.
4. The server will process your input using the Ollama API and display the result.

## Project Structure

- `app.py`: Main FastAPI application file
- [templates/](cci:7://file:///Users/kumarshubham/personal/minicpm-server/templates:0:0-0:0): Directory containing HTML templates
  - `index.html`: Home page template
  - `result.html`: Result page template
- `requirements.txt`: List of Python dependencies

## Dependencies

Key dependencies include:
- FastAPI
- Uvicorn
- Jinja2
- Requests

For a full list of dependencies, see `requirements.txt`.