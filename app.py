import streamlit as st
import math
# -------------------------------
# PAGE CONFIG
# -------------------------------
# -------------------------------
# CUSTOM UI
# -------------------------------
st.markdown("""
    <style>
    body {
        background-color: #fafafa;
    }
    .stChatMessage {
        border-radius: 15px;
        padding: 10px;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)
# -------------------------------
# LOGIN SYSTEM
# -------------------------------
users = {
    "loyola": "loyola123",
    "student": "loyola123"
}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.header("Welcome to Loyola CS Digital Assistant")
    st.subheader("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in users and users[username] == password:
            st.session_state.logged_in = True
            st.success("Login successful!")
            st.rerun()
        else:
            st.error("Invalid username or password")

    st.stop()
# -------------------------------
# CUSTOM UI (ChatGPT style)
# -------------------------------
st.markdown("""
<style>
.main {
    background-color: #0e1117;
}
.stChatMessage {
    padding: 12px;
    border-radius: 10px;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# SIDEBAR (like ChatGPT)
# -------------------------------
with st.sidebar:

    st.markdown('<div class="sidebar-title"><b>⚙️ MENU</b></div>', unsafe_allow_html=True)
    if st.button(" Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")

    st.markdown('<div class="sidebar-title"><b>📌 TOPICS</b></div>', unsafe_allow_html=True)

    topics = [
        "Faculty", "Fees", "Courses",
        "Library", "Hostel", "Admission",
        "Principal", "HOD", "Scholarships","Creator","vice principal","student achievements",
    ]

    for t in topics:
        if st.button(t):
            st.session_state.quick_question = t.lower()

# -------------------------------
# DATA
# -------------------------------
# ALL KEYS IN lowercase
study_notes = {
    "hello": "Hello! I am your college assistant bot. How can I help you today?",
    "hi": "Hi there! What college info are you looking for?",
    "creator":"""<span style='color:blue; font-weight:bold;'>THIS APPLICATION WAS DEVELOPED BY SUHEL</span> He is a student currently studying in loyola college ysrr. He is really interested in coding and technology, especially Python and java. He building projects like chatbots and AI-based apps and me.He developed an AI-powered college assistant application using Python and the Streamlit framework. The application provides information about various academic and administrative aspects such as faculty details, fee structure, admission guidelines, scholarships, and eligibility criteria.

The system features an interactive chat-based interface inspired by ChatGPT, allowing users to input queries and receive relevant responses instantly. Additionally, He enhanced the user experience by incorporating features like dynamic content display, highlighted text formatting, and image integration for faculty profiles.

This project demonstrates by his skills in Python programming, UI design using Streamlit, and basic natural language processing techniques for handling user queries.
""",
    "admission": """
<h3>📌 Admission Guidelines</h3>

Loyola Degree College, affiliated to 
<b>Yogi Vemana University (YVU), Kadapa</b>, follows a 
<span style='color:#00ffcc; font-weight:bold;'>transparent, merit-based, and student-friendly</span> 
admission process.

<hr>

<h4>📋 General Guidelines</h4>

<ul>
<li><b>Eligibility:</b> Must meet YVU academic requirements</li>
<li><b>Application:</b> Online & Offline modes available</li>
<li><b>Selection:</b> Merit-based + Govt reservation policy</li>
<li><b>Documents:</b> Academic records, TC, certificates</li>
<li><b>Reservation:</b> As per Andhra Pradesh Govt norms</li>
<li><b>Code of Conduct:</b> Discipline & integrity required</li>
<li><b>Scholarships:</b> Financial support for deserving students</li>
<li><b>Jesuit Preference:</b> Support for underprivileged students</li>
</ul>

<hr>

<h4>🌟 Vision</h4>
To provide equitable and transparent admission opportunities aligned with YVU norms.

<h4>🎯 Mission</h4>
<ul>
<li>Ensure fair and merit-based admissions</li>
<li>Support marginalized communities</li>
<li>Guide students and parents clearly</li>
<li>Promote holistic student development</li>
<li>Follow university & government policies</li>
</ul>

<h4>💡 Taglines</h4>
<ul>
<li>“Admissions with Transparency, Education with Integrity”</li>
<li>“Equal Opportunities, Inclusive Education”</li>
<li>“Empowering Students, Enriching Futures”</li>
<li>“Fair Access to Quality Education”</li>
</ul>
""",
"eligibility": """
<h3>🎓 Eligibility Criteria</h3>

Loyola Degree College welcomes students who have successfully completed their 
<b>Intermediate (10+2)</b> education from a recognized board. Admissions follow 
<b>APSCHE guidelines</b> for web counselling and merit-based selection.

<h4>📘 Course-Wise Eligibility</h4>

<b>1. Computer Science:</b><br>
Students must have studied <span style='color:#00ffcc;'>Mathematics (MPC)</span>.<br><br>

<b>2. Life Sciences / B.Sc (Biology):</b><br>
Students should have completed <span style='color:#00ffcc;'>BiPC</span>.<br><br>

<b>3. Commerce Courses (B.Com):</b><br>
Students from <span style='color:#00ffcc;'>CEC or MEC</span> streams.<br><br>

<b>4. BBA:</b><br>
Open to <span style='color:#00ffcc;'>CEC or MEC</span> students.<br><br>

<b>5. Arts / Humanities:</b><br>
Students from <span style='color:#00ffcc;'>any stream</span> are eligible.<br><br>

<hr>

<h4>🌟 Vision</h4>
To provide equitable access to quality higher education and foster holistic learning.

<h4>🎯 Mission</h4>
<ul>
<li>Follow APSCHE & University guidelines</li>
<li>Provide clear course guidance</li>
<li>Ensure merit-based admissions</li>
<li>Help students choose right career path</li>
<li>Build confidence in higher education journey</li>
</ul>

<h4>💡 Taglines</h4>
<ul>
<li>“Eligibility Meets Opportunity at Loyola”</li>
<li>“Right Course, Bright Future”</li>
<li>“Your Stream, Your Strength, Your Success”</li>
<li>“Guiding You from Eligibility to Excellence”</li>
<li>“Merit-Based Access, Holistic Learning”</li>
</ul>
""",
"scholarships": """
<h3>🎓 Scholarship & Financial Support</h3>

Loyola Degree College is deeply committed to the <b>Jesuit tradition</b> of serving 
the poor and the marginalized.

In addition to <b>government scholarships</b>, the Management provides 
<span style='color:#00ffcc; font-weight:bold;'>financial aid and fee concessions</span> 
to ensure that <b>no deserving student is deprived of education</b> due to financial hardship.

This reflects Loyola vision of 
<b>inclusive and value-based education</b>, empowering students from underprivileged 
backgrounds to pursue their dreams with dignity.

<hr>

<h4>🌟 Vision</h4>
To ensure that every deserving student, regardless of financial background, 
has access to quality education and the opportunity to succeed.

<h4>🎯 Mission</h4>
<ul>
<li>Provide scholarships to deserving students</li>
<li>Bridge financial and academic gaps</li>
<li>Promote inclusivity in education</li>
<li>Support Jesuit value: <b>“option for the poor”</b></li>
<li>Build confident and responsible leaders</li>
</ul>

<h4>💡 Taglines</h4>
<ul>
<li>“Education for All, Support for the Needy”</li>
<li>“No Dream Too Distant, No Student Left Behind”</li>
<li>“Bridging Financial Gaps, Building Bright Futures”</li>
<li>“Compassion in Action, Education with Inclusion”</li>
</ul>
""",
 "courses": "We offer B.Sc, B.A and B.Com courses with single major.",
    "exam": "Final exams are in the third week of November.",
    "library": "Library is open from 8 AM to 5 PM.",
    "hostel": "Hostel is available on a first-come basis.",
    # Faculty data (ALL KEYS IN lowercase)
    "faculty": """ 
<span style='color:blue; font-weight:bold;'>SAMULURU SAMUEL</span>Mr. S. Samual – Computer Lecturer & NCC CTO.<br>
Technical skills:
• SQL
• C
• C++
• Java
• HTML,CSS
Strengths:
• Quick learner
• Good at communication
• Critical Thinking
• Versatility
Hobbies:
• Playing Sports
• Browsing social media
• Watching movies & Series
• Listening music
Personal details:
Name : S.Samuel
Father Name : S.Simon
Mother Name : S.Vimala
Marital status : Unmarried
Languages known : English and Telugu
Address : 2-2-257,
Christian line,
Pulivendula,
Y.S.R.Kadapa (dist), 516390(A.P).

<span style='color:blue; font-weight:bold;'>Mr.B. SUJITH KUMAR</span> – Programming expert, choreographer, social media admin.<br>
Professional Experience :
Worked as assistant professor in ANNAMACHARYA PG College of Computer
Studies, Rajampet
Worked as XML developer in MRV IT SOLUTIONS.
Technical Profiency:
WEB DEVELOPMENT
MACHINE LEARNING PROJECTS
C, JAVA, PYTHON PROGRAMMING LANGUAGES
MS-OFFICE
Professional Activites:
R&D incharge in APGCCs college-rajampet.
Culture coordinator at the university level.
List of Publications:
Paper titled “Detectiong fake identities on Instagram” at IJSRT in 2023.
Paper titled “Emotion-based detection of mental health risk in social meia” at
IJIRSET in 2025.
Workshops/FPDS/Webinars Attended:
Attended a faculty development program named “Enterprenuership management”
organized by Wadwani foundation held at JNTUA in march-2025.
Personal Profile
Name : B. SUJITH KUMAR
Date of Birth : 24-06-2001
Gender : MALE
Contact Address : 2-5-249/1, SIYONPURAM,
PULIVENDULA-516390
Languages Knows : ENGLISH, TELUGU

<span style='color:blue; font-weight:bold;'>Mr. L. Karthik</span> – Friendly teaching style, social media admin.<br>
Professional Experience :
Technical Profiency:
WEB DEVELOPMENT
MACHINE LEARNING PROJECTS
C, JAVA, PYTHON PROGRAMMING LANGUAGES
MS-OFFICE
Professional Activites:
List of Publications:
Paper titled “BINARY MULTILINGUAL MACHINE GENERATOR TEST
DETECCTION” at in 2025.
Workshops/FPDS/Webinars Attended:
Personal Profile
Name : L. KARTHIK
Date of Birth : 3-8-2002
Gender : MALE
Contact Address : 1-10-315, CHRISTIAN
LINE PULIVENDULA516390
Languages Knows : ENGLISH, TELUGU

<span style='color:blue; font-weight:bold;'>Mrs. D. HIMAJA<a href="https://loyoladegreecollegeysrr.ac.in/admin/uploads/staff/8272himaja.pdf" target="_blank">Profile</a></span>– Teaching programming, DB, OS since 2017,SASA.<br>
Professional Experience:
I have been working as the Computer Science lecturer at Loyola Degree College
(YSRR), Pulivendula, from 2017 to the present.
Technical Profiency:
Languages : C, C++, JAVA, Python, Ms-Office
Operating systems : windows XP, 7, 8.1, 10,11
Database : Oracle
Professional Activities:
I have been working as the SASA Coordinator at Loyola Degree College since June
2025.
Workshops/FDPS/Webinars Attended\n
Data Analytics Using Power BI and Tableau Organized by Faculty of IT and CS -Parul
University - Gujarat, Atria Institute of Technology- Karnataka & Amity Pune – Maharashtra
in in Collaboration with ExcelR Edtech Pvt.Ltd. 11th to 15th March 2024
Business Analytics Organized by AISSMS College of Engineering, SJC Institute of Technology
and Matrusri Engineering College in Collaboration with ExcelR Edtech Pvt.Ltd. 5th to 9th Sep
2024
Block Chain Technology Organized by D Y Patil Deemed to be university 8
TH TO 12 Jan
024
Data Visualization using Tableau by MOHAN BABU UNIVERSITY &
EXCELR EDTTECH PVT LTD 16th to 20th Sep2024
Gen-AI and Prompt Engineering Using Microsoft Co-Pilot. By BNM Institute of
Technology Bangalore (BNMIT) – Karnataka,D.Y. Patil Agriculture and
Technical University Talsande – Maharashtra, and Marwadi University Rajkot -
Gujarat in Collaboration with ExcelR Edtech Pvt. Ltd. 15th to B.  19 Nov 2024
Cloud Architect By Vardhaman Engineering College, Shamshabad - Hyderabad,
AVS Engineering College, Salem – Tamil Nadu, 18th-22nd Nov 2024.
Data Visualization Using Tableau By Department of Computer Science and
Engineering, Mohan Babu University, Tirupati, Andhra Pradesh & EXCELR
EDTECH PVT. LTD.1st to 5th April 2024\n
Personal Profile
Name : D. Himaja
Date of Birth : 10-06-1994
Gender : Fe- Male
Contact Address : Peddakondappa Colony -2
pulivendula, YSR Kadapa
Languages Knows : English, Telugu,
""",

"fee structure": """
B.Sc computer science – 15,000 only.

B.Sc data science – 15,000 only.

B.Sc quantum technology – 15,000 only.

Students are eligible for scholarships.
""",

"hod": """
<span style='color:blue; font-weight:bold;'>M. Ramana Reddy<a href="https://loyoladegreecollegeysrr.ac.in/admin/uploads/staff/7099facultyRamana%20Resume2025.pdf" target="_blank">Profile</a></span>– Teaching programming, DB, OS since 2017,SASA.<br>M. Ramana Reddy (MCA, MBA) – HOD & Assistant Professor<br>  
Department of Computer Science  
the Department of Computer Science at Loyola Degree College, established a few years ago, is dedicated to training students as techno-savvy professionals equipped with skills for the digital age. The department focuses on building strong foundations in computer systems, programming languages, databases, and emerging technologies that prepare students for higher studies, research, and industry careers.\n
Professional Experience:
I have been working as the Head of the Department of Computer Science at Loyola
Degree College (YSRR), Pulivendula, from August 2021 to the present.
I worked as a Lecturer in Computer Science at Loyola Degree College (YSRR),
Pulivendula, from July 2012 to July 2021.
I served as the Head of the Department of Computer Science at Vivekananda Degree
College, Vempalli, from August 2010 to May 2012.
I worked as an IT Associate at the Institute for Electronic Governance from August
2008 to July 2010.
""",

"principal": """
<span style='color:blue; font-weight:bold;'>Prof . Fr. Dr. L. Joji Reddy, S.J. M.Sc., M.B.A., M.Phil., Ph.D., Postdoc.(USA)<a href="https://loyoladegreecollegeysrr.ac.in/content.php?type=college&id=principal-s-message" target="_blank">Profile</a></span> - Principal, Loyola Degree College.<br>
Loyola Degree College is more than an institution—it is a global centre of learning with world-class facilities and a commitment to excellence in every sphere of life. Our vision goes beyond academics, embracing the all-round development of every student and nurturing in them a lifelong thirst for knowledge. Here, education is not confined to classrooms; it is value-driven, activity-based, and respect-centered, preparing our students to adapt, excel, and lead in any environment. Loyola imparts not only knowledge but also values—by teaching, by example, and by inspiring students to serve the poorest of the poor with compassion and patriotism. In this way, we cultivate visionary leaders who dream fearlessly, live purposefully, and leave behind a legacy for generations to come. As Principal, I am proud to be a Loyolite and to lead our student community as they unravel their true potential and move confidently toward their aspiring, futuristic goals.
""",

"vana father": """
<span style='color:blue; font-weight:bold;'>Dr. Vana Chinnappa <a href="https://loyoladegreecollegeysrr.ac.in/admin/uploads/staff/8756Fr.Vana%20Chinnappa%20(2).pdf" target="_blank">Profile</a></span>  - Vice Principal, Loyola Degree College.<br>
Technical Profiency:
Microscopy
Atomic Force Microscopy (AFM)
Scanning Electron Microscopy (SEM)
Spectroscopy
UV-Vis Spectroscopy (UV-Vis)
Reflectron Time of Flight Mass Spectroscopy
Deposition
Cluster Beam deposition (CBD) – Cluster Synthesis through physical method.
Photo (electro)catalytic tests – Stearic acid degradation, solar water splitting tests,
FTIR
Computer and Scientific Softwares
MS word and Excel
Origin, QPlot
Professional Activites:
List of Publications
1. Chinnabathini, V.C., Dingenen, F., Borah, R., Abbas, I., van der Tol, J., Zarkua, Z.,
D'Acapito, F., Nguyen, T.H T., Lievens, P., Grandjean, D., Verbruggen, S.W., Janssens,
E. with Grandjean, D. (corresp. author) (2023). Gas phase deposition of well-defined
bimetallic gold-silver clusters for photocatalytic applications. NANOSCALE, 15 (14),
6696-6708. doi: 10.1039/d2nr07287d.
2. Vana Chinnappa Chinnabathini, Karthick Raj Ag, Thi Hong Trang Nguyen, Zviadi
Zarkua, Imran Abbas, Thi Hang Hoang, Peter Lievens, Didier Grandjean, Sammy W.
Verbruggen, Ewald Janssens. AuCu bimetallic nanocluster-modified titania nanotubes for
photoelectrochemical water splitting: composition-dependent atomic arrangement and
activity. NANOSCALE, 2025, 17, 833-845. doi : https://doi.org/10.1039/D4NR03219E.
3. Thi Hong Trang Nguyen, Zviadi Zarkua, Chinnabathini Vana Chinnappa, Wenjian
Hu, Sreeprasanth Pulinthanathu Sree, Didier Grandjean, Deepak Pant and Ewald
Janssens (2023). Co3−xFexO4 inverse opals with tunable catalytic activity for highperformance overall water splitting. NANOSCALE, 15, 10306-10318
doi : 10.1039/D2NR07300E.
4. Franceschini, Filippo; Chinnabathini, Vana Chinnappa; Papamichail, Dimitra;
Nguyen, Trang; Deschaume, Olivier; Pham, Hung; Bartic, Carmen; Escudero, Daniel;
Vantomme, André; Janssens, Ewald; Taurino, Irene Manuscript "Gold Nanoclusters
on Anodized Glassy Carbon as an Electrocatalytic Glucose Sensing Platform." ACS
APPL, Nano.Mater. 2025, 8, 27, 13914-13923.
Publications in progress
1. Karthick Raj AG, Antony Charles Minja, Vana Chinnappa Chinnabathini, Rajeshreddy
Ninakanti, Sara Bals, Ewald Janssens, Roel van de Krol and Sammy W. Verbruggen.
“Atomically Precise Nickel-Iron Clusters on Bismuth Vanadate for Efficient
Photoelectrochemical Water Splitting” (under progress).
2. Thi Hong Trang Nguyen, Jing Shen, Chandani Singh, Dimitra Papamichail, Vana
Chinnappa Chinnabathini, Oriol Gutiérrez Sanchez, Didier Grandjean, Deepak Pant,
and Ewald Janssens. “The Tunable C 2 Products on Pd Nanocluster-modified
Mesoporous Copper Oxide Inverse Opals Toward CO 2 Electrochemical Reduction
Reaction” (under progress).
Workshops/FPDS/Webinars Attended:
1. Participation and oral and oral presentation at “International Meeting on Nanoalloys
(IMN)”, 9-11 May 2023, held in Orleans, France
2. Participation and poster presentation at "Thematic Workshop - Non-Equilibrium and
Environment Effects on Nanoalloys" 7-9 December 2022, held in Paris, France
3. Participation and poster presentation at “Nanoalloys: Recent developments and
future perspectives Faraday Discussion”, 21–23 September 2022, held in London,
United Kingdom.
4. Participation and poster presentation at Belgian Physical Society (BPS) scientific
meeting on 18th May 2022 held in Dessel, Belgium.
5. Participation in “International Meeting on Nanoalloys (IMN)”, 14-16 April 2021,
Leuven, Belgium, virtual conference
6. Participation and poster presentation at “International Cluster Meeting”, 18-23 July
2021, held in Prague, Czech Republic
7. Catchy kick-off training, September 15-17, 2021, Leuven (Belgium)
8. Spring school on nanoalloys 24-30 April 2022, Corsica Islands, France in Cargese and
presented a poster
9. Participated in the national seminar on “Advances in Biomaterials and
characterization Techniques” held at Andhra Loyola College, Vijayawada, Andhra
Pradesh, India on 20 - 21 January, 2017
10. Participated in the international conference on “Recent Trends in Sensor
development for the Assessment and Management of the Environment” organized
by Loyola Institute of frontier energy, Loyola College, Chennai, India, on 8th to 10th
January 2010.
Personal Profile
Name : Ch. Vana Chinnappa
Date of Birth : 27-02-1980
Gender : Male
Contact Address : Jesuit Residence, Loyola
degree and poly colleges,
Pulivendula, Kadap Dt
Languages Knows : Telugu, English, Tamil,
Hindi and Dutch
""",

"sujitha":"""
<span style='color:blue; font-weight:bold;'>L.Sujitha<a href="https://loyoladegreecollegeysrr.ac.in/admin/uploads/staff/8271sujitha.pdf" target="_blank">Profile</a></span><br>
Professional Experience :
Head of the department of physics,Loyola degree college(YSRR), pulivendula
 (2023-present)
Lecturer in Sri Chaitanya junior college,Hyderabad(2020-2021)
Lecturer in Narayana Pu college, Bangalore (2015-2019)
Technical Profiency:
Softwares knowns like
Ms office
Programming languages
C,C++
Oracle, HTML
Typing in lower got a certificate
Professional Activites:
Coordinator,Dean of academics
Actively engaged in result analysis
Organized National science day events
Supervised and guided CSP projects
Mentor of physics club
List of Publications:
No publications
\n Workshops/FDPS/Webinars Attended:
1) Attended FDPs on “ Generative AI tools for smart teaching " organized
by AIACHE on june9th-june13, 2025\n
Personal Profile
Name : L.Sujitha
Date of Birth : 22-09-1991
Gender : Female
Contact Address : H.No:4-7-317/33,
Brahmanapalliroad,
Pulivendula
Languages Knows : Telugu, English
""",

#DATA GREETINGS
"how are you":"I'm just a bot,I dont have any Feelings,I’m here to help you with any college information you need!",
"bye": "Goodbye! Feel free to ask me anything about your college anytime.",
"good bye": "Goodbye! Feel free to ask me anything about your college anytime.",
"good morning": "Good morning! How can I assist you with your college information today?",
"good afternoon": "Good afternoon! What college info are you looking for?",
"good evening": "Good evening! How can I help you with your college information today?",
"good night": "Good night! If you have any questions about your college, feel free to ask anytime.",
" i love you": "I’m just a bot, but I’m here to help you with any college information you need!",
"who created you": "I was created by a student named <span style='color:blue; font-weight:bold;'>Suhel</span>, who is passionate about coding and technology. He developed this AI-powered college assistant application using Python and the Streamlit framework to provide information about various academic and administrative aspects of the college.",
"pora puka": "pora erri puka🤣. I’m here to help you with any college information you need.",

#all subjects syllabus
"major computer science syllabus": """
<button>click here https://apsche.ap.gov.in/Pdf/major_minor1/Computer%20Science%20Major.pdf</button> 
""",

"minor quantum technology syllabus": """
<button>click here https://apsche.ap.gov.in/Pdf/major_minor1/Quantum%20Technologies%20Minor.pdf</button>
""",

"major data science syllabus": """
<button>click here https://apsche.ap.gov.in/Pdf/major_minor1/Data%20Science%20Major.pdf</button>
""",

"major physics syllabus": """
<button>click here https://apsche.ap.gov.in/Pdf/major_minor1/Physics%20Major.pdf</button>
""",

"minor data science syllabus": """
<button>click here https://apsche.ap.gov.in/Pdf/major_minor1/Data%20Science%20Minor.pdf</button>
""",

"minor physics syllabus": """
<button>click here https://apsche.ap.gov.in/Pdf/major_minor1/Physics%20Minor.pdf</button>
""",

# Study data (ALL KEYS IN lowercase)
    # Your Questions
    "what activities are available in your college": "Our college offers real-time project-based learning with an advanced computing lab. Students also participate in sports, NCC, NSS, and cultural activities.",

    "what type of learning environment does your college provide": "The college provides a real-time project-based learning environment with advanced computing labs.",

    "who is the hod of your department": "Mr. M. Ramana Reddy is the HOD of Computational Sciences.",

    "since when has the hod been serving": "He has been serving since 2012.",

    "who is mrs d himaja": "Mrs. D. Himaja is a Computer Lecturer serving since 2017.",

    "what are the timings of the library": "The library is open from 8 AM to 8 PM.",

    "who is the viceprincipal": "The Vice Principal of Loyola Degree College is <span style='color:blue; font-weight:bold;'>Dr. Vana Chinnappa</span>.",

    "student achievements": """📄 PROJECT REPORT: SMART DUSTBIN SEGREGATOR
1. Abstract

Waste management is a major issue in modern society. Improper segregation of waste leads to environmental pollution and inefficient recycling. This project presents a Smart Dustbin Segregator, an automated system that separates waste into categories such as wet, dry, and metal using sensors and a microcontroller. The system reduces human effort and promotes efficient waste management.

2. Introduction

With increasing urbanization, waste generation has increased significantly. Manual segregation is time-consuming and unhygienic. This project aims to design an automated system that can:

Identify waste type
Segregate waste automatically
Improve recycling efficiency
3. Objectives
To design an automated waste segregation system
To reduce manual labor
To promote eco-friendly waste management
To implement sensor-based classification
4. Components Used
Hardware:
Arduino Uno (microcontroller)
Moisture Sensor
Metal Sensor
Servo Motor
Ultrasonic/IR Sensor
Power Supply
Dustbin with compartments
Software:
Arduino IDE
Embedded C programming
5. System Architecture
Block Description:
Input: Waste material
Sensors detect type
Microcontroller processes data
Servo motor directs waste
Output: Segregated waste bins
6. Working Principle
Waste is placed into the input section
Sensors analyze the waste:
Metal sensor detects metal
Moisture sensor detects wet waste
Arduino processes sensor data
Servo motor rotates to the correct bin
Waste falls into the appropriate compartment
7. Algorithm
START
Read sensors

IF metal detected:
    Rotate servo to metal bin

ELSE IF moisture > threshold:
    Rotate servo to wet bin

ELSE:
    Rotate servo to dry bin

END
8. Circuit Description
Moisture sensor connected to analog pin (A0)
Metal sensor connected to digital pin (D2)
Servo motor connected to PWM pin (D9)
Power supply provides required voltage
9. Advantages
Reduces manual work
Improves recycling process
Low-cost implementation
Easy to operate
10. Applications
Smart cities
Public places
Schools and colleges
Railway stations
11. Limitations
Cannot detect mixed waste accurately
Sensor errors possible
Limited classification (only basic types)
12. Future Enhancements
AI-based waste detection using camera
IoT integration for monitoring
Mobile app notifications
Automatic bin level detection
13. Conclusion

The Smart Dustbin Segregator is an effective solution for automated waste management. It reduces human effort and improves efficiency in waste segregation. With further improvements, it can be implemented in real-world smart city systems.

14. References
Arduino official documentation
Embedded systems textbooks
Waste management research articles
""",


}

# -------------------------------
# SMART RESPONSE
# -------------------------------
def get_answer(user_input):
    user_input = user_input.lower()

    # -------------------------------
    # MATH CALCULATIONS
    # -------------------------------
    try:
        # Power support
        user_input = user_input.replace("^", "**")

        # Square root
        if "sqrt" in user_input:
            num = float(user_input.split("sqrt")[-1])
            return "The " + user_input + f"🧮Answer is: {math.sqrt(num)}"

        # Basic operations
        if any(op in user_input for op in ["+", "-", "*", "/"]):
            result = eval(user_input)
            return "The " + user_input + f"🧮Answer is: {result}"
    except:
        pass

    # -------------------------------
    # YOUR EXISTING LOGIC
    # -------------------------------
    if "fee" in user_input:
        return study_notes["fee structure"]

    if "scholarship" in user_input:
        return study_notes["scholarships"]
    
    if "student achievements" in user_input:
        return study_notes["student achievements"]
    
    # Default
    for key in study_notes:
        if key in user_input:
            return study_notes[key]
        
    return "🤖 I’m still learning. Try asking about fees, faculty, or courses."

# -------------------------------
# CHAT MEMORY
# -------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------------------
# TITLE
# -------------------------------

if st.session_state.logged_in:
    col1, col2 = st.columns([1,10])

with col1:
    st.image("loyola_logo.png", width=60)

with col2:
    st.markdown("<h2 style='color:#9ca3af;'>Loyola CS Digital Assistant</h2>", unsafe_allow_html=True)

# -------------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):

        # show images if exist
        if "images" in msg:
            for img in msg["images"]:
                st.image(img, width=120)

        # show text
        st.markdown(msg["content"], unsafe_allow_html=True)
# -------------------------------
# INPUT (ChatGPT style)
# -------------------------------
user_input = st.chat_input("Ask anything about your college...")

# Handle quick button click
if "quick_question" in st.session_state:
    user_input = st.session_state.quick_question
    del st.session_state.quick_question

# -------------------------------
# RESPONSE FLOW
# -------------------------------
if user_input:
    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    st.chat_message("user").write(user_input)

    # Get answer
    answer = get_answer(user_input)

    #Decide images
    images = []

    if "hod" in user_input.lower():
        images = ["ramana.jpg"]

    elif "faculty" in user_input.lower():
        images = ["samuel.jpg", "sujith.jpg", "karthik.jpg", "himaja.jpg"]

    elif "principal" in user_input.lower():
        images = ["joji.jpg"]
    
    elif "creator" in user_input.lower():
        images = ["suhel.jpg"] 
    
    elif "vana father" in user_input.lower():
        images = ["vana.jpg"]

    elif "sujitha" in user_input.lower():
        images = ["sujitha.jpg"]

    elif "who created you" in user_input.lower():
        images = ["suhel.jpg"]

    elif "student achievements" in user_input.lower():
        images = ["achievement.jpg", "physics.jpg"]
        width = 600
    
    # Save assistant message WITH images
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer,
        "images": images
    })

    # Show immediately
    with st.chat_message("assistant"):
        for img in images:
            st.image(img, width=width if 'width' in locals() else 120)
            st.write("")  # Add spacing after images
        st.markdown(answer, unsafe_allow_html=True)
