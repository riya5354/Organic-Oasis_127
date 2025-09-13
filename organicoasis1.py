import streamlit as st

# Website Title
st.title("Organic Oasis🥗")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Menu","Order", "Contact"])

# Home Page
if page == "Home":
    st.header("Welcome to Organic Oasis")
    st.write("Your favorite food, made organically and fresh.")
    

# Menu Page
elif page == "Menu":
    st.header("Our Menu")
    menu_items = [
        {
            "name": "Mango Pickle",
            "quantity":"200 gm",
            "price": "₹ 125",
            "description": "Desi Mango Delight,Made With Love And Care",
        },
        {
            "name": "Mango Pickle",
            "quantity":"400 gm",
            "price":"₹ 200",
            "description": "Desi Mango Delight,Made With Love And Care.",
        },
        {
            "name": " A2 Ghee",
            "quantity":"400 gm or 750 gm",
            "price": "₹1200 or ₹1900 ",
            "description": "A2 ghee.......Pure & Nourishing – Organic Ghee for Mind, Body & Soul",
        },
        {
            "name":"Cow Ghee",
            "quantity":"750gm",
            "price":"₹600",
            "description": "Cow ghee........Pure & Nourishing – Organic Ghee for Mind, Body & Soul",
        },
        {
            "name":"Buffalo Ghee",
            "quantity":"750 gm",
            "price":"₹700",
            "description":"Buffalo ghee........Pure & Nourishing – Organic Ghee for Mind, Body & Soul",
        },
        {
             "name": "Turmeric Powder",
             "quantity":"200 gm",
            "price":"₹100",
            "description": "From Farm to You: Organic Turmeric Powder Packed with Natural Goodness.",
        },
    ]
    for item in menu_items:
        st.subheader(f"{item['name']} - {item['price']}-{item['quantity']}")
        st.write(item["description"])
#Order Page
elif page=="Order":
    options = st.selectbox(
    "How would you like to be contacted?",
    ("Mobile Phone", "Email", "Instagram Page"),
    index=None,
    placeholder="Select contact method...",
    )
    st.write("You selected:", options)
    if options=="Mobile Phone":
       st.write("Contact Us: +91 9307946976")
    elif options=="Email":
        st.write("Email us: organicoasis127@gmail.com")
    elif options=="Instagram Page":
        st.write("Visit 'Organic Oasis_127' on Instagram")
    
       
# Contact Page
if page == "Contact":
    st.header("For More Information")
    st.write("📞 Phone: +91 9307946976")
    st.write("📧 Email: organicoasis127@gmail.com")
   
