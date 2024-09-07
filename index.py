import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu


with st.sidebar:
	selected=option_menu(
		menu_title="Python World",
		options=["Introduction to Python","Installation to Python","Sample Code", "Contact"],
		icons=["book-fill","arrow-down","code-slash","person-lines-fill"],
		menu_icon="list-task",
		)

#----------------------------------------------------------------
if selected == "Introduction to Python":
	st.title("Welcome to Python World!!")
	img=Image.open("Python.png")
	st.image(img,width=300)		
	st.header("What is Python?")
	st.markdown("Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. It 	was created by Guido van Rossum, and released in 1991. Its high-level built in data structures, combined with 	dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use 	as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax 	emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and 	packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard 	library are available in source or binary form without charge for all major platforms, and can be freely 	distributed.")

	st.subheader("Features of Python:")
	st.markdown(""" 
	Python is a versatile and powerful programming language, known for its simplicity and readability. 	Here are 	some of its key features:

	1) Easy to Learn and Use: Python has a simple syntax that is similar to English, making it easy to 	learn and 	write code. This simplicity allows developers to focus on solving problems rather than struggling with 	complex 	syntax.

	2) Interpreted Language: Python is an interpreted language, meaning that the code is executed line by line. This 	makes debugging easier and allows for more interactive coding and testing.

	3) High-Level Language: Python abstracts away many of the complexities of the machine-level details, such as 	memory management, making it easier to write and understand.

	4) Cross-Platform Compatibility: Python is cross-platform, meaning it can run on various operating systems, 	including Windows, macOS, and Linux, without requiring changes to the code.

	5) Extensive Standard Library: Python comes with a vast standard library that provides modules and functions for 	many common programming tasks, such as file handling, regular expressions, and web development, reducing the need 	for external libraries. """)

	st.subheader("Applications of Python:")
	st.markdown("""
	1. Web Development
	2. Data Science
	3. Machine Learning & AI
	4. Automation & Scripting
	5. Scientific Computing
	6. Game Development
	7. Finance
	8. Networking & Cybersecurity
	9. Education
	10. IoT & Robotics
	11. Blockchain & Embedded Systems """)

#-----------------------------------------------------------------------
if selected == "Installation to Python":
	st.header("Installation of Python")
	st.divider()
	st.markdown(""" This is how you can install python on your system:-""")

	st.markdown("### 1. Windows- ")

	st.markdown(""" 
	a. Download Python Installer:
	Visit the official Python website and download the latest Python installer for Windows.

	b. Run the Installer: Double-click the downloaded installer.

	c. Important: Check the box that says "Add Python to PATH."
	Click "Install Now" to begin the installation. 

	d. Verify Installation:
	Open Command Prompt and type python --version or python to verify Python is installed correctly. """)

	st.markdown("### 2. macOS- ")

	st.markdown(""" 
	a. Download Python Installer:
	Go to the Python website and download the macOS installer. 

	b. Run the Installer:
	Open the downloaded .pkg file and follow the installation prompts.

	c. Verify Installation:
	Open Terminal and type python3 --version or python3 to check the installation. """)

	st.markdown("### 3. Linux- ")

	st.markdown(""" 
	a. Check Pre-installed Version:
	Most Linux distributions come with Python pre-installed. You can check by opening Terminal and typing python3 --	version.

	b. Install Python (if not installed or for a different version):
	Update your package list: sudo apt update.
	Install Python: sudo apt install python3.

	c. Verify Installation:
	In Terminal, type python3 --version to confirm the installation. """)

	st.markdown("### 4. Install Python Packages-")
	st.markdown(""" Use pip, Python's package manager, to install packages: pip install package_name. """)

	st.markdown("### 5. Integrated Development Environment (IDE)-")
	st.markdown(""" Optionally, install an IDE like PyCharm, VS Code, or use the built-in IDLE to start coding in 	Python. """)

#------------------------------------------------------------------------------
if selected == "Sample Code":
	st.header("Sample Code")
	st.divider()
	st.write("You can start your journey with python by trying out these simple programs: ")
	st.caption("Program 1: Program to show use print statement")
	st.code(""" print("Hello World!!") """)
	st.caption("OUTPUT:-")
	st.code(""" Hello World """)
	
	st.caption("Program 2: Program to declare a variable and do simple arithmetic")
	st.code(""" 
		a=10
		b=15
		print("Addition= ",a+b)
		print("Subtraction= ",a-b)
		print("Multiplication= "a*b)
		print("Division= "a/b)
		 """)
	st.caption("OUTPUT:-")
	st.code(""" 
		Addition= 25
		Subtraction= -5
		Multiplication= 150
		Division= 0
		""")

	st.caption("Program 3: Program to swap two variables")
	st.code("""
		A = int( input("Please enter value for A: "))  
		B = int( input("Please enter value for B: "))  
    
		temp = A  
		A = B  
		B = temp  
   
		print ("The Value of A after swapping: ", A)  
		print ("The Value of B after swapping: ", B)  
		""")
	st.caption("OUTPUT:-")
	st.code("""
		Please enter value for A:  10
		Please enter value for B:  50
		The Value of A after swapping: 50
		The Value of B after swapping: 10
		""")

	st.write("Explore more programs by yourself:")
	st.link_button("Find out more","https://www.geeksforgeeks.org/python-programming-examples/")	


#------------------------------------------------------------------------------
if selected == "Contact":
	st.header("How was your experience?")
	st.write("Was this information helpful? Let us know by giving us a quick rating!")
	st.select_slider("Rating-",["Satisfactory","Average","Good","Excellent"])
	st.divider()
	st.header("Contact Me Here")
	uname=st.text_input("Enter your Name: "," ")
	eaddr=st.text_input("Enter your Email Address: "," ")
	suggest=st.text_area("Your valuable suggestions: "," ")
	if st.button("Submit"):
		if uname == " ":
			st.warning("Please enter your name!!!")
		elif eaddr == " ":
			st.warning("Please enter your email address!!!")
		elif suggest == " ":
			st.warning("Please give your suggestions!!!")
		else:
			st.balloons()
			st.success("Form submitted Successfully!!!")
