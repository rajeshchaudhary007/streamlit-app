import streamlit as st 
import requests
from streamlit_lottie import st_lottie
from PIL import Image
from streamlit_option_menu import option_menu



st.set_page_config(page_title="My Website", page_icon=":sunglasses:", layout="wide")



image = Image.open('pic.png')

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#load assets 

lottie_coding = load_lottieurl("https://lottie.host/3f7365fb-77a3-4cfb-b954-5b1fba85ccfd/DACOb4lKkq.json")
lottie_contact = load_lottieurl("https://lottie.host/e31b2e0a-0140-484f-8242-870fc17b5ce5/rBPLo42RXv.json")

#----header section---


with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
            st.subheader("Hi i am Rajesh Chaudhary :wave:")
            st.title("An introvert who code a little bit ")
            st.write("I am passionate about finding ways to use Python to be more efficient")
            st.write("📄 [Resume (1 page)](https://drive.google.com/file/d/1jDD9FoXdgS-DF5dib4ihZLh8-9Fm1cBj/view?usp=drive_link")
        
            
                
    with right_column:
         st_lottie(lottie_coding, width=500, height=200, key="coding")
       




    
#-----What i do -----
with st.container():
    st.write("----")
    st.header("What I do ")
    st.write("##")
    st.write(
            
        """
**About Me**

As a passionate and highly skilled Python Developer, I thrive on turning innovative ideas into practical solutions. My love for coding and problem-solving has been the driving force behind my career in software development. With a solid foundation in Python and a deep understanding of software design principles, I am dedicated to creating efficient, maintainable, and scalable applications.

**Technical Expertise**

- Proficient in Python and its ecosystem, including popular frameworks such as Django and Flask.
- Strong understanding of object-oriented programming (OOP) and design patterns.
- Experience with database management systems, particularly MySQL and PostgreSQL.
- Familiarity with front-end technologies such as HTML, CSS, and JavaScript.
- Knowledge of version control systems like Git for collaborative development.
- Skilled in integrating third-party APIs and web services to enhance application functionality.
- Ability to optimize code for performance and scalability.

**Problem-Solving Approach**

I approach challenges with a logical and analytical mindset, seeking elegant solutions that address both short-term requirements and long-term maintainability. I am detail-oriented and value clean, well-documented code that ensures seamless collaboration with other team members.


**Passion for Learning**

As a firm believer in continuous learning, I am always eager to explore emerging technologies and stay updated with the latest trends in the Python ecosystem. I regularly participate in online coding challenges and open-source projects to sharpen my skills and contribute to the developer community.

        """
)
        



with st.container():
    st.write("----")
    left_column,right_column = st.columns(2)
    with left_column:
        st.title("Contact")
        
        Name = st.text_input("Enter your Name", "")
        message = st.text_input("Message", "")
        email = st.text_input("Email", "")
    
        st.markdown(
                """
                
                <style>
                .styled-button {
                    background-color: #4CAF50;
                    color: white;
                    padding: 8px 15px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                }
                .styled-button:hover {
                    background-color: #45a049;
                }
                </style>
                """,
                unsafe_allow_html=True
            )
        st.markdown(
                f'<button class="styled-button" type="submit">Submit</button>',
                unsafe_allow_html=True
            )
       
    
    with right_column:
        st_lottie(lottie_contact, height=400, key="contact")
        
        



