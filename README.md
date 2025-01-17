# Financial Assistant

This project uses the `vllm` library to load and run large language models (LLMs) like Facebook's OPT for generating text responses. Docker support ensures consistent deployment across environments.

## Features
- Fast and efficient text generation using `vllm`
- Supports models like `facebook/opt-125m`
- Dockerized setup for easy deployment

## Prerequisites
- Python 3.9+
- Docker installed and running

## Local Setup (Without Docker)

1. **Clone the Repository**
   ```bash
   git clone https://github.com/AK-Github-0/Financial-Assistant
   ```

2. **Create and Activate Virtual Environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # For macOS/Linux
   .venv\Scripts\activate     # For Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   python main.py
   ```

## Running with Docker

1. **Build the Docker Image**
   ```bash
   docker build -t Financial-Assistant .
   ```

2. **Run the Docker Container**
   ```bash
   docker run -it --rm Financial-Assistant
   ```

3. **Optional:** Run with Port Mapping (if serving via API)
   ```bash
   docker run -it --rm -p 8000:8000 Financial-Assistant
   ```

## Project Structure
```
├── Dockerfile
├── llm.py
├── main.py
├── requirements.txt
└── README.md
```




