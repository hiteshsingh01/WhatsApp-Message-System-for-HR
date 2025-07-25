import streamlit as st
import pandas as pd
import pywhatkit as kit
import time
import os

st.set_page_config("📲 HR WhatsApp Notifier", layout="centered")

st.title("📲 Automated WhatsApp Message System for HR")

CSV_FILE = "employees.csv"

# Ensure CSV file exists
if not os.path.exists(CSV_FILE):
    pd.DataFrame(columns=["Employee ID", "Name", "Phone Number", "Reporting Time"]).to_csv(CSV_FILE, index=False)

# Step 1: Upload CSV
st.subheader("📤 Upload Existing Employee CSV")
csv_file = st.file_uploader("Upload CSV file", type=["csv"])

if csv_file:
    df = pd.read_csv(csv_file)
else:
    df = pd.read_csv(CSV_FILE)

if all(col in df.columns for col in ["Employee ID", "Name", "Phone Number", "Reporting Time"]):
    st.success("✅ CSV loaded successfully!")
    st.dataframe(df)

    # Step 2: Add New Entry
    st.subheader("➕ Add New Employee Entry")
    with st.form("add_form"):
        emp_id = st.text_input("Employee ID")
        name = st.text_input("Name")
        phone = st.text_input("Phone Number")
        reporting_time = st.text_input("Reporting Time")
        submit = st.form_submit_button("Add Entry")

        if submit:
            if emp_id and name and phone and reporting_time:
                new_row = pd.DataFrame([[emp_id, name, phone, reporting_time]], columns=df.columns)
                df = pd.concat([df, new_row], ignore_index=True)
                df.to_csv(CSV_FILE, index=False)
                st.success("✅ Entry added to CSV.")
                st.experimental_rerun()
            else:
                st.error("❌ Please fill all fields.")

    # Step 3: Message Template
    st.subheader("✉️ Message Format")
    msg_template = st.text_area("Customize your message", 
        "Hello {name},\n\nThis is a reminder that your reporting time is at {time}.\n\n- HR Team")

    same_msg_toggle = st.checkbox("🔁 Send same message to everyone (ignore names and times)")

    if same_msg_toggle:
        common_msg = st.text_area("Enter the common message to send")

    # Step 4: Send Messages
    if st.button("🚀 Send Messages"):
        st.info("📤 Starting message sending...")

        for index, row in df.iterrows():
            name = row["Name"]
            number = str(row["Phone Number"])
            time_slot = row["Reporting Time"]

            if same_msg_toggle:
                msg = common_msg
            else:
                msg = msg_template.format(name=name, time=time_slot)

            try:
                st.write(f"📞 Sending to {name} ({number})...")
                kit.sendwhatmsg_instantly(f"+{number}", msg, wait_time=10, tab_close=True)
                time.sleep(10)  # wait 10 seconds between messages to avoid ban
                st.success(f"✅ Sent to {name}")
            except Exception as e:
                st.error(f"❌ Error sending to {name}: {e}")
else:
    st.error("CSV must contain columns: Employee ID, Name, Phone Number, Reporting Time")
