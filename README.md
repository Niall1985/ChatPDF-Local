# 📄 ChatPDF-Local
**A locally running chatbot that lets you chat with your PDFs! 🚀**

## 📌 Features
✅ **Upload PDF Files** – Supports user-uploaded PDFs  
✅ **Chat with Your PDFs** – Ask questions and get human-like responses  
✅ **Powered by LLaMA** – Uses a local LLaMA model for response generation  

---

## 📥 Installation

First, clone the repository:

```sh
git clone https://github.com/Niall1985/ChatPDF-Local.git
cd ChatPDF-Local
```

Install the required dependencies:

```sh
pip install -r requirements.txt
```

Ensure you have the necessary LLaMA model weights downloaded and placed in the correct directory.

---

## 🚀 How to Run

Run the Streamlit app:

```sh
streamlit run pdf_chatbot.py
```

Now, open [localhost:8501](http://localhost:8501) in your browser! 🎉

---

## 🛠 How It Works

1. **Upload a PDF** 📄  
2. **Enter a question** ❓  
3. **Chatbot finds the most relevant answer using LLaMA** 🔍  
4. **Response is generated and displayed** 💬  

Under the hood, it:
- Extracts text using **PyMuPDF**  
- Splits the text into chunks for **efficient retrieval**  
- Uses a **LLaMA-based language model** to generate responses  
- Returns human-like responses based on the document's content  

---

## 🔧 Future Improvements
- [ ] **Memory** – Keep track of previous questions  
- [ ] **Better Search** – Implement **semantic search** for improved accuracy  
- [ ] **Deployment** – Deploy to **Streamlit Cloud**  

---

## 🛠 Technologies Used
- **Python** 🐍
- **Streamlit** 🎨
- **PyMuPDF (fitz)** 📄
- **LLaMA Model** 🧠

---

## 🤝 Contributing
Want to contribute? Feel free to **fork** the repository and submit a **pull request**!  

---

## 📜 License
This project is licensed under the **MIT License**.  

---

