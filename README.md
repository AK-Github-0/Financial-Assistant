# LLM Chatbot with Docker Support

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
   git clone https://github.com/your-username/llm-chatbot.git
   cd llm-chatbot
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
   docker build -t llm-chatbot .
   ```

2. **Run the Docker Container**
   ```bash
   docker run -it --rm llm-chatbot
   ```

3. **Optional:** Run with Port Mapping (if serving via API)
   ```bash
   docker run -it --rm -p 8000:8000 llm-chatbot
   ```

## Project Structure
```
├── Dockerfile
├── llm.py
├── main.py
├── requirements.txt
└── README.md
```

## Dockerfile (Example)
```Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
```

## Troubleshooting
- **SSL Warning:** `NotOpenSSLWarning` due to LibreSSL. Install OpenSSL 1.1.1+ if needed.
- **Device Error:** Use `device="cpu"` if no GPU is detected.

## License
This project is licensed under the MIT License.

---

**Happy coding!** 🚀

