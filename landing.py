import streamlit as st

#-----------------------
#       navbar
#-----------------------


st.markdown("""
            <link
              rel="stylesheet"
              href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/7.3.0/css/all.min.css"
              integrity="sha512-ApSLB1Pd3/bZN8fWB/RG9YhN/7bd9Hkf3AGaE2mPfebjrxagjuBtx2GcgdqIlJkUzwylBo61r9Xa9NmgBI0swA=="
              crossorigin="anonymous"
              referrerpolicy="no-referrer"
            />

            <div class = "nav">
                    
            <div class="title">
                <a href="#"> CareerCompass</a>
            </div>
            
            <div class="nav-items">
                <a href="/" class="Home">
                    <i class="fa-solid fa-house"></i> 
                    Home 
                </a>
                <a href="/Resume_uploader" class="resume">     
                    <i class="fa-sharp fa-solid fa-file-import"></i>
                    Resume Upload 
                </a>
                <a href="/Dashboard" class="ATS">    
                    <i class="fa-solid fa-tachograph-digital"></i>
                    ATS Dashnoard
                </a>
                <a href="/Mock_Interview">    
                    <i class="fa-solid fa-microphone"></i>
                    Mock Interview 
                </a>
                <a href="/About"> 
                    <i class="fa-solid fa-circle-info"></i>
                    About
                </a>
                <div class="login">
                    <i class="fa-regular fa-user"></i>
                    <a href="/login"> Login/Sign Up </a>
                </div>
            </div>
            
            </div> """, unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.image("logo.png")    
    
with col2:    
    st.markdown("""
            <div class="hero-section">
                    <div class="main">
                    <h1>
                        Your career, <br>
                        powered by smarter preparation. 
                    </h1>
                    <p class="description">
                        Prepare for your next opportunity with powerful resume
                        analysis, ATS scoring, and realistic mock interviews —
                        all in one place.
                    </p>
                </div>
            </div>
            """, unsafe_allow_html=True)

st.markdown("""
                <style>
                        
            /* Remove Streamlit top area */
            
            header {
                display: none !important;
            }

            [data-testid="stHeader"] {
                display: none !important;
            }

            #MainMenu {
                display: none !important;
            }

            footer {
                display: none !important;
            }

            .block-container {
                padding: 0 !important;
                margin: 0 !important;
                max-width: 100% !important;
                max-height: 100% !important;
            }

            [data-testid="stVerticalBlock"] {
                gap: 10px !important;
            }

            .stMarkdown {
                margin: 0 !important;
                padding: 0 !important;
            }

            .nav{
                display:flex;
                justify-content: space-between;
                align-items:flex-end;
                background: linear-gradient(
                90deg,
                #8B4CF5 0%,
                #B957C9 45%,
                #FF8A4C 100%
            );
                text-decoration: none;

            }

            .Home{
                color:#FFFFFF !important;
            }

            .title a{ 
                padding-left:20px;
                padding-top:15px;
                font-size: 35px;
                background: linear-gradient(
                90deg,
                #2E005D,
                #8E008B,
                #EF2E78
                );

                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;

                text-decoration: none;
                font-weight:700;
            }

            .nav-items {
                display: flex;
                gap: 50px;    
            }

            .nav-items a {
                color: #2E005D;
                text-decoration: none;
                font-size: 15px;
            }

            .login {
                color: #2E005D;
                border: 1px solid transparent;
                padding-right:12px;
            }

            .nav-items a:hover {
                color: #ffffff;
                transform: translateY(-2px);
            }

            .login:hover{
                color: #ffffff;
                transform: translateY(-2px);
            }

           
            
             /* HERO SECTION */

            [data-testid="stHorizontalBlock"] {
                min-height: 800px !important;

                background: linear-gradient(
                    90deg,
                    #8B4CF5 0%,
                    #B957C9 45%,
                    #FF8A4C 100%
                );

                padding-left:200px;
                padding-right:900px;
                padding-bottom:300px;
                padding-top:200px;
                box-sizing: border-box;

                align-items: center;
            }
            .main {
                color: #FFFFFF;
                line-height: 1.15;
                font-weight: 800;
                width:400px;
                margin-bottom: 25px;
            }
            .main h1 {
                font-size:32px;
            }
            .description {
                font-size:20px !important;
                font-weight:200;
                width:550px;
                color: #FFFFFF;
                line-height: 1.6;
            }

            /* IMAGE */

            [data-testid="stHorizontalBlock"] img {
                width: auto !important;
                height: auto !important;
                display: block;
            }
           
           </style>

            """, unsafe_allow_html=True)


