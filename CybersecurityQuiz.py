import random

# Networking Basics
def networking_basics():
    print("Networking Basics\n")
    print("Question 1: What does TCP stand for?")
    print("a) Transmission Control Protocol")
    print("b) Transfer Control Protocol")
    print("c) Transport Control Protocol")
    print("d) Technical Control Protocol")
    answer_1 = input("Enter your answer (a, b, c, or d): ")
    if answer_1.lower() == "a":
        print("Correct!")
    else:
        print("Incorrect. The correct answer is a) Transmission Control Protocol.")

# Operating Systems
def operating_systems():
    print("Operating Systems\n")
    print("Question 1: Which operating system is based on the Linux kernel?")
    print("a) Windows")
    print("b) macOS")
    print("c) Linux")
    print("d) Android")
    answer_1 = input("Enter your answer (a, b, c, or d): ")
    if answer_1.lower() == "c":
        print("Correct!")
    else:
        print("Incorrect. The correct answer is c) Linux.")

# Security Concepts
def security_concepts():
    print("Security Concepts\n")
    print("Question 1: What does CIA stand for in the context of cybersecurity?")
    print("a) Confidentiality, Integrity, Availability")
    print("b) Control, Identify, Authenticate")
    print("c) Cybersecurity Information Agency")
    print("d) Computer Intrusion Analysis")
    answer_1 = input("Enter your answer (a, b, c, or d): ")
    if answer_1.lower() == "a":
        print("Correct!")
    else:
        print("Incorrect. The correct answer is a) Confidentiality, Integrity, Availability.")

# Threats and Vulnerabilities
def threats_and_vulnerabilities():
    print("Threats and Vulnerabilities\n")
    print("Question 1: What is a common example of social engineering?")
    print("a) Virus")
    print("b) Phishing")
    print("c) Firewall")
    print("d) Encryption")
    answer_1 = input("Enter your answer (a, b, c, or d): ")
    if answer_1.lower() == "b":
        print("Correct!")
    else:
        print("Incorrect. The correct answer is b) Phishing.")

# Cryptography
def cryptography():
    print("Cryptography\n")
    print("Question 1: What is the purpose of a digital signature?")
    print("a) Encrypt data")
    print("b) Verify the integrity of data")
    print("c) Authenticate a user")
    print("d) Establish a secure connection")
    answer_1 = input("Enter your answer (a, b, c, or d): ")
    if answer_1.lower() == "b":
        print("Correct!")
    else:
        print("Incorrect. The correct answer is b) Verify the integrity of data.")

# Network Security
def network_security():
    print("Network Security\n")
    print("Question 1: What is the primary function of a firewall?")
    print("a) Encrypt network traffic")
    print("b) Monitor network activity")
    print("c) Block unauthorized access")
    print("d) Authenticate users")
    answer_1 = input("Enter your answer (a, b, c, or d): ")
    if answer_1.lower() == "c":
        print("Correct!")
    else:
        print("Incorrect. The correct answer is c) Block unauthorized access.")

# Identity and Access Management
def identity_and_access_management():
    print("Identity and Access Management\n")
    print("Question 1: What is multi-factor authentication?")
    print("a) Using multiple passwords")
    print("b) Authenticating with biometrics")
    print("c) Verifying identity through social media")
    print("d) Using a username only")
    answer_1 = input("Enter your answer (a, b, c, or d): ")
    if answer_1.lower() == "b":
        print("Correct!")
    else:
        print("Incorrect. The correct answer is b) Authenticating with biometrics.")

# Risk Management
def risk_management():
    print("Risk Management\n")
    print("Question 1: What is the first step in the risk management process?")
    print("a) Identify risks")
    print("b) Analyze risks")
    print("c) Mitigate risks")
    print("d) Monitor risks")
    answer_1 = input("Enter your answer (a, b, c, or d): ")
    if answer_1.lower() == "a":
        print("Correct!")
    else:
        print("Incorrect. The correct answer is a) Identify risks.")

# Security Policies and Procedures
def security_policies_and_procedures():
    print("Security Policies and Procedures\n")
    print("Question 1: Why is it important to regularly update software and apply patches?")
    print("a) To increase system performance")
    print("b) To prevent unauthorized access")
    print("c) To improve user experience")
    print("d) To reduce network bandwidth usage")
    answer_1 = input("Enter your answer (a, b, c, or d): ")
    if answer_1.lower() == "b":
        print("Correct!")
    else:
        print("Incorrect. The correct answer is b) To prevent unauthorized access.")

# Security Tools
def security_tools():
    print("Security Tools\n")
    print("Question 1: What is the purpose of a vulnerability scanner?")
    print("a) Encrypt network traffic")
    print("b) Monitor network activity")
    print("c) Identify security vulnerabilities")
    print("d) Block unauthorized access")
    answer_1 = input("Enter your answer (a, b, c, or d): ")
    if answer_1.lower() == "c":
        print("Correct!")
    else:
        print("Incorrect. The correct answer is c) Identify security vulnerabilities.")

# Main menu and program loop
def main_menu():
    print("Welcome to the Cybersecurity Learning Program!")
    print("Please select a topic to explore:")
    print("1. Networking Basics")
    print("2. Operating Systems")
    print("3. Security Concepts")
    print("4. Threats and Vulnerabilities")
    print("5. Cryptography")
    print("6. Network Security")
    print("7. Identity and Access Management")
    print("8. Risk Management")
    print("9. Security Policies and Procedures")
    print("10. Security Tools")
    print("0. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        networking_basics()
    elif choice == "2":
        operating_systems()
    elif choice == "3":
        security_concepts()
    elif choice == "4":
        threats_and_vulnerabilities()
    elif choice == "5":
        cryptography()
    elif choice == "6":
        network_security()
    elif choice == "7":
        identity_and_access_management()
    elif choice == "8":
        risk_management()
    elif choice == "9":
        security_policies_and_procedures()
    elif choice == "10":
        security_tools()
    elif choice == "0":
        print("Thank you for using the Cybersecurity Learning Program. Goodbye!")
        exit()
    else:
        print("Invalid choice. Please try again.")

# Main program loop
while True:
    main_menu()
