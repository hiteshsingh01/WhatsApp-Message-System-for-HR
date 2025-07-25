
# 📲 Automated WhatsApp Messaging System for HR & Teams

A simple yet powerful **Python + Streamlit** app to automate personalized WhatsApp messaging for HR departments, clinics, coaching institutes, and more.

---

## 🚀 Features

- Upload a CSV file with employee **Name**, **Phone Number**, and **Reporting Time**  
- Send personalized WhatsApp messages with dynamic placeholders (`{name}`, `{time}`)  
- Option to send the **same message to all** contacts  
- Automatically sends messages with a **10-second delay** between each to avoid bans  
- User-friendly Streamlit dashboard for uploading, editing, and previewing data  

---

## 📋 How It Works

1. Prepare a CSV with columns: `name`, `number`, `time` (or your custom columns)  
2. Upload the CSV in the app  
3. Enter your message template with placeholders like `{name}` and `{time}`  
4. Start sending — messages will be sent automatically via WhatsApp Web with delays  
5. Monitor progress on the dashboard  

---

## 🛠️ Built With

- Python  
- Streamlit  
- pandas  
- pywhatkit  

---

## 📂 Folder Structure

```

WhatsApp-Message-System-for-HR/
├── main.py               # Streamlit app entry point
├── README.md             # Project documentation
└── sample\_data.csv       # Example CSV for testing

````

---

## ⚙️ Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/jayant77778/WhatsApp-Message-System-for-HR.git
   cd WhatsApp-Message-System-for-HR
````

2. Install dependencies (you can install manually as needed):

   ```bash
   pip install streamlit pandas pywhatkit
   ```

3. Run the Streamlit app:

   ```bash
   streamlit run main.py
   ```

---

## 💡 Ideal Use Cases

* HR teams sending reporting time or salary alerts
* Clinics or hospitals sending shift reminders
* Coaching institutes sending class or batch updates
* Any organization needing bulk personalized WhatsApp messaging

---

## 🔗 GitHub Repository

👉 [https://github.com/jayant77778/WhatsApp-Message-System-for-HR](https://github.com/jayant77778/WhatsApp-Message-System-for-HR)

---

## 🙌 Acknowledgments

This project was developed during my learning journey at **LinuxWorld Informatics Pvt Ltd** under the mentorship of **Vimal Daga Sir**, a visionary in AI and automation.

---

## 🤝 Connect With Me

* 💼 [LinkedIn – Jayant Bhati](https://www.linkedin.com/in/jayantbhati77/)

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


