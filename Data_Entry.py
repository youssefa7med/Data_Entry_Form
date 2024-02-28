import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

st.set_page_config(page_title="Google Sheets App", page_icon="📄")


# Display Title & Description

st.title("Google Sheets App",help = "You can add, edit, delete, search and view clients in Google Sheets")


st.markdown("You can access the google sheet from here: [Google Sheets](https://docs.google.com/spreadsheets/d/1YkL8ZwK3bCdwlywd9Dcd3F6o_tW4xqMOyuflgEAu2iY/edit?usp=sharing)")
st.divider()

# Establish a connection with your Google Sheet
conn = st.connection("gsheets",type = GSheetsConnection)

# Fetch data from Google Sheet
existing_data = conn.read(worksheet="Sheet1",usecols =list(range(9)),ttl =5)
existing_data = existing_data.dropna(how = "all")

# list of columns
columns = existing_data.columns.tolist()


# Constants
Gender = ["Male","Female"]

action = st.selectbox("Action",["Add New Client","Edit Existing Client","Delete Client","Search Client","View All Clients"])

if action == "Add New Client":

    st.subheader("Add New Client")
    # Onboarding New Client
    with st.form("Client Form"):
        first_name = st.text_input("First Name*",max_chars = 15,help = "Enter your first name")
        last_name = st.text_input("Last Name*",max_chars = 15,help = "Enter your last name")
        gender = st.radio("Gender*",["Male","Female"],index = None,horizontal = True,help = "Enter your gender")
        age = st.number_input("Age*",min_value = 0,max_value = 100,step = 1,help = "Enter your age")
        phone = st.text_input("Phone*",max_chars = 11,help = "Enter your phone number")
        email = st.text_input("Email*",max_chars = 30,help = "Enter your email")
        country = st.text_input("Country*",max_chars = 15,help = "Enter your country")
        address = st.text_input("Address",max_chars = 30,help = "Enter your address")
        notes = st.text_area("Notes",help = "Enter any notes")

        # Submit
        st.markdown("**Required*")


        submit = st.form_submit_button("Submit")

        if submit:
            if not first_name or not last_name or not gender or not age or not phone or not email or not country:
                st.warning("Ensure all fields are filled")
                st.stop()
            elif existing_data['Email'].str.contains(email).any():
                st.error("Email already exists")
                st.stop()
            else :
                client_data = pd.DataFrame(
                    [
                        {
                            "First Name": first_name,
                            "Last Name": last_name,
                            "Gender": gender,
                            "Age": age,
                            "Phone": phone,
                            "Email": email,
                            "Country": country,
                            "Address": address,
                            "Notes": notes
                        }
                    ]
                )

                # Add new data to Google Sheet
                updated_df = pd.concat([existing_data,client_data],ignore_index = True)

                # Update Google Sheet
                conn.update(worksheet="Sheet1",data = updated_df)
                
                st.success("Client added successfully !")

elif action == "Edit Existing Client":
    st.subheader("Edit Existing Client")

    client_to_edit = st.selectbox("Select Client",existing_data["Email"].tolist())

    client_data = existing_data[existing_data["Email"] == client_to_edit].iloc[0]

    with st.form(key="update_form"):
        first_name = st.text_input("First Name*",max_chars = 15,value = client_data["First Name"],help = "Enter your first name")
        last_name = st.text_input("Last Name*",max_chars = 15,value = client_data["Last Name"],help = "Enter your last name")
        gender = st.radio("Gender*",["Male","Female"],index = Gender.index(client_data["Gender"]),horizontal = True,help = "Enter your gender")
        age = st.number_input("Age*",value = client_data["Age"],help = "Enter your age")
        phone = st.text_input("Phone*",max_chars = 11,value = client_data["Phone"],help = "Enter your phone number")
        email = st.text_input("Email*",max_chars = 30,value = client_data["Email"],help = "Enter your email")
        country = st.text_input("Country*",max_chars = 15,value = client_data["Country"],help = "Enter your country")
        address = st.text_input("Address",max_chars = 30,value = client_data["Address"],help = "Enter your address")
        notes = st.text_area("Notes",value = client_data["Notes"],help = "Enter any notes")

        st.markdown("**required*")
        update_button = st.form_submit_button(label="Update Client Details")

        if update_button:
            if not first_name or not last_name or not gender or not age or not phone or not email or not country :
                st.warning("Ensure all mandatory fields are filled With correct values.")
            else:
                # Removing old entry from the dataframe
                existing_data.drop(existing_data[existing_data["Email"] == client_to_edit].index,inplace = True)
                # Creating updated data entry
                updated_client_data = pd.DataFrame(
                    [
                        {
                            "First Name": first_name,
                            "Last Name": last_name,
                            "Gender": gender,
                            "Age": age,
                            "Phone": phone,
                            "Email": email,
                            "Country": country,
                            "Address": address,
                            "Notes": notes
                        }
                    ]
                )
                # Adding updated data to the dataframe
                updated_df = pd.concat(
                    [existing_data, updated_client_data], ignore_index=True
                )
                conn.update(worksheet="Sheet1", data=updated_df)
                st.success("Client details successfully updated!")

elif action == "View All Clients":
    st.dataframe(existing_data)

# Delete Vendor
elif action == "Delete Client":
    client_to_delete = st.selectbox(
        "Select a client to Delete", options=existing_data["Email"].tolist()
    )

    if st.button("Delete"):
        existing_data.drop(
            existing_data[existing_data["Email"] == client_to_delete].index,
            inplace=True,
        )
        conn.update(worksheet="Sheet1", data=existing_data)
        st.success("Client successfully deleted!")

elif action == "Search Client":
    client_to_search = st.selectbox("Select Client",existing_data["Email"].tolist())

    if st.button("Search"):
        st.dataframe(existing_data[existing_data["Email"].str.contains(client_to_search)])

