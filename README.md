# 📄 ChatPDF-Local
**A locally running chatbot that lets you chat with your PDFs! 🚀**

## 📌 Features
✅ **Upload PDF Files** – Supports user-uploaded PDFs  
✅ **Chat with Your PDFs** – Ask questions and get human-like responses  
✅ **No External AI Required** – Uses TF-IDF for efficient retrieval  
✅ **Fast & Lightweight** – Runs completely offline  

---

## 📥 Installation

First, clone the repository:

```sh
git clone https://github.com/Niall1985/ChatPDF-Local.git
cd ChatPDF-Local
```

Install the required dependencies:

```sh
pip install streamlit PyMuPDF scikit-learn
```

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
3. **Chatbot finds the most relevant answer** 🔍  
4. **Response is humanized and displayed** 💬  

Under the hood, it:
- Extracts text using **PyMuPDF**
- Splits the text into chunks for **efficient retrieval**
- Uses **TF-IDF similarity search** to find relevant content
- Humanizes responses to make them more conversational  

---

## 🔧 Future Improvements
- [ ] **Memory** – Keep track of previous questions  
- [ ] **Better Search** – Implement **BM25** for improved accuracy  
- [ ] **Multi-PDF Support** – Allow chatting with multiple PDFs  
- [ ] **Deployment** – Deploy to **Streamlit Cloud**  

---

## 🛠 Technologies Used
- **Python** 🐍
- **Streamlit** 🎨
- **PyMuPDF (fitz)** 📄
- **TF-IDF (Scikit-Learn)** 🔍  

---

## 🤝 Contributing
Want to contribute? Feel free to **fork** the repository and submit a **pull request**!  

---

## 📜 License
This project is licensed under the **MIT License**.  

---