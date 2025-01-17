# Financial-Asssistant

This project leverages advanced language models to generate text-based responses. It integrates efficient model handling using vLLM and offers flexibility in model selection, including lightweight models for CPU execution.

---

## 📂 Project Structure

```
├── main.py             # Entry point of the application
├── llm.py              # Model loading and response generation
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── .venv/              # Python virtual environment
```

---

## 🛠 Installation

1. **Clone the Repository:**

```bash
git clone https://github.com/your-username/ai-text-generation.git
cd ai-text-generation
```

2. **Set Up Virtual Environment:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. **Install Dependencies:**

```bash
pip install -r requirements.txt
```

4. **Install OpenSSL (MacOS users):**

```bash
brew install openssl
```

---

## 🚀 Running the Project

### **Run the App:**

```bash
python main.py
```

---

## ⚙️ Configuration

### **Model Configuration (llm.py):**

```python
from vllm import LLM

llm = LLM(
    model="facebook/opt-125m",
    device="cpu",
    enforce_eager=True,
    disable_log_stats=True  # Disable async logging for stability
)
```

---

## 📝 Usage

### **Generating Responses:**

```python
from llm import generate_response

prompt = "Tell me a story about AI."
response = generate_response(prompt)
print(response)
```

---

## 🐞 Troubleshooting

### **Common Issues:**

1. **LibreSSL Warning:**
   - Install OpenSSL: `brew install openssl`

2. **NotImplementedError:**
   - Set `disable_log_stats=True` in `llm.py`.

3. **Async Output Errors:**
   - Replace vLLM with Hugging Face Transformers if needed.

---

## 📦 Dependencies

- Python 3.9+
- vLLM
- Transformers
- PyTorch

Install all dependencies with:

```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a Pull Request

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 💬 Contact

**Abdullah Khan**  
📧 Email: abdullah@example.com  
🔗 LinkedIn: [linkedin.com/in/abdullahkhan](https://linkedin.com/in/abdullahkhan)

---

## 🌟 Acknowledgments

- [vLLM](https://github.com/vllm-project/vllm)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers)

---

**Give this project a ⭐ if you find it useful!**


