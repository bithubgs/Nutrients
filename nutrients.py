import streamlit as st

st.set_page_config(
    page_title="🍏 თქვენი პირადი ნუტრიციოლოგი",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={
        'About': "ეს აპლიკაცია შექმნილია თქვენი პირადი კვებითი რეკომენდაციების მოსაწოდებლად. გთხოვთ, გაითვალისწინოთ, რომ ეს არ არის პროფესიონალური სამედიცინო რჩევა."
    }
)

# --- Custom CSS Styles for enhanced mobile responsiveness and DARK MODE adaptation ---
st.markdown(
    """
    <style>
    /* General body and app styling for LIGHT MODE */
    body {
        font-family: 'Open Sans', sans-serif;
        color: #333; /* Dark text for light mode */
        line-height: 1.6;
    }
    .main {
        background-color: #fefefe; /* Very light, clean background for content */
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.1);
        margin-top: 20px;
        margin-bottom: 20px;
    }
    .stApp {
        background: linear-gradient(to right, #e0f5f7, #c1e7ed); /* Subtle gradient background */
    }

    /* Headings styling for LIGHT MODE */
    h1 {
        color: #1a7a4f; /* Deeper green for main title */
        text-align: center;
        font-family: 'Merriweather', serif;
        font-size: 2.4em;
        margin-bottom: 20px;
        padding-bottom: 15px;
        border-bottom: 3px solid #66bb6a;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.05);
    }
    h2, h3, h4 {
        color: #2b6b55; /* Darker, richer green for subheadings */
        font-family: 'Merriweather', serif;
        border-bottom: 1px solid #c8e6c9;
        padding-bottom: 5px;
        margin-top: 25px;
        font-size: 1.4em;
    }
    h4 {
        font-size: 1.2em;
    }

    /* Button styling for LIGHT MODE */
    .stButton>button {
        background-color: #66bb6a; /* Medium green button */
        color: white;
        border-radius: 10px;
        border: none;
        padding: 12px 25px;
        font-size: 17px;
        cursor: pointer;
        transition: all 0.3s ease;
        display: block;
        margin: 25px auto;
        width: 85%;
        max-width: 350px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .stButton>button:hover {
        background-color: #5cb85c;
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.2);
    }

    /* Input field styling for LIGHT MODE */
    .stSelectbox, .stNumberInput, .stRadio {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 8px;
        border: 1px solid #a7d9e7;
        box-shadow: inset 0 1px 4px rgba(0,0,0,0.05);
        margin-bottom: 12px;
    }

    /* Alert messages styling for LIGHT MODE */
    .stAlert {
        border-radius: 10px;
        padding: 15px;
        font-size: 0.98em;
        line-height: 1.5;
        margin-top: 15px;
        margin-bottom: 15px;
    }
    .stAlert.warning {
        background-color: #fff8e1;
        border-color: #ffecb3;
        color: #e69100;
    }
    .stAlert.info {
        background-color: #e0f7fa;
        border-color: #b2ebf2;
        color: #00796b;
    }

    /* Sidebar styling for LIGHT MODE */
    .css-1d391kg { /* Streamlit sidebar background */
        background-color: #e0f8f8;
        border-right: 1px solid #b2e0e0;
        box-shadow: 3px 0 8px rgba(0,0,0,0.05);
    }

    /* Expander styling for LIGHT MODE */
    .st-emotion-cache-1r6dm7m { /* Expander header color */
        color: #2b6b55;
        font-weight: bold;
        font-size: 1.15em;
    }
    .st-emotion-cache-eczf16 { /* Expander content background */
        background-color: #f8fcfc;
        border-radius: 10px;
        padding: 15px;
        margin-top: 10px;
        border: 1px dashed #d5f2f5;
        box-shadow: inset 0 1px 5px rgba(0,0,0,0.02);
    }

    /* Markdown list styling */
    ul {
        padding-left: 25px;
        list-style-type: disc;
    }
    li {
        margin-bottom: 8px;
    }

    /* --- DARK MODE specific styles --- */
    @media (prefers-color-scheme: dark) {
        body {
            color: #e0e0e0; /* Light grey text for dark mode */
        }
        .main {
            background-color: #2c2c2c; /* Darker background for content */
            box-shadow: 0 8px 20px rgba(0,0,0,0.4); /* More pronounced shadow */
        }
        .stApp {
            background: linear-gradient(to right, #1a1a1a, #2a2a2a); /* Dark gradient background */
        }

        /* Headings styling for DARK MODE */
        h1 {
            color: #90ee90; /* Lighter green for main title in dark mode */
            border-bottom-color: #4CAF50; /* More vibrant green line */
            text-shadow: 1px 1px 2px rgba(0,0,0,0.4);
        }
        h2, h3, h4 {
            color: #a0e6a0; /* Lighter green for subheadings */
            border-bottom-color: #3e8e41;
        }

        /* Button styling for DARK MODE */
        .stButton>button {
            background-color: #4CAF50; /* Green button remains vibrant */
            box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        }
        .stButton>button:hover {
            background-color: #3e8e41;
            box-shadow: 0 6px 12px rgba(0,0,0,0.5);
        }

        /* Input field styling for DARK MODE */
        .stSelectbox, .stNumberInput, .stRadio {
            background-color: #3c3c3c; /* Darker background for inputs */
            border-color: #555; /* Softer border */
            color: #e0e0e0; /* Light text in inputs */
        }
        /* Ensure text in selectbox/numberinput is light */
        .stSelectbox div[data-baseweb="select"] {
            color: #e0e0e0 !important;
        }
        .stNumberInput input {
            color: #e0e0e0 !important;
        }
        .stRadio label {
            color: #e0e0e0 !important;
        }


        /* Alert messages styling for DARK MODE */
        .stAlert {
            background-color: #444; /* Darker background for alerts */
            border-color: #666;
            color: #e0e0e0;
        }
        .stAlert.warning {
            background-color: #5c4700; /* Darker warning background */
            border-color: #8c6e00;
            color: #ffe082; /* Lighter warning text */
        }
        .stAlert.info {
            background-color: #1a4f66; /* Darker info background */
            border-color: #3a7a92;
            color: #81d4fa; /* Lighter info text */
        }


        /* Sidebar styling for DARK MODE */
        .css-1d391kg {
            background-color: #222; /* Darker sidebar background */
            border-right-color: #333;
            box-shadow: 3px 0 8px rgba(0,0,0,0.2);
        }

        /* Expander styling for DARK MODE */
        .st-emotion-cache-1r6dm7m { /* Expander header color */
            color: #90ee90;
        }
        .st-emotion-cache-eczf16 { /* Expander content background */
            background-color: #333; /* Darker content background */
            border-color: #555;
            box-shadow: inset 0 1px 5px rgba(0,0,0,0.2);
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("👨‍⚕️🍏 თქვენი პირადი ნუტრიციოლოგი")
st.write("შეიყვანეთ თქვენი მონაცემები და მიიღეთ დეტალური კვებითი რეკომენდაციები თქვენი ინდივიდუალური საჭიროებების გათვალისწინებით.")

st.sidebar.header("📝 შეიყვანეთ მონაცემები")

# --- User data input ---
gender = st.sidebar.radio("🧍 **სქესი:**", ("მამრობითი", "მდედრობითი"))
weight = st.sidebar.number_input("⚖️ **წონა (კგ):**", min_value=1.0, max_value=300.0, value=70.0, step=0.1)
height = st.sidebar.number_input("📏 **სიმაღლე (სმ):**", min_value=50.0, max_value=250.0, value=170.0, step=0.1)
age = st.sidebar.number_input("🎂 **ასაკი (წელი):**", min_value=1, max_value=120, value=30)

activity_level = st.sidebar.selectbox(
    "🏃 **ფიზიკური აქტივობა:**",
    (
        "მინიმალური (მჯდომარე ცხოვრება)",
        "მსუბუქი (კვირაში 1-3-ჯერ ვარჯიში)",
        "ზომიერი (კვირაში 3-5-ჯერ ვარჯიში)",
        "მაღალი (კვირაში 6-7-ჯერ ვარჯიში)",
        "ძალიან მაღალი (ყოველდღიური, ინტენსიური ვარჯიში)"
    )
)

meal_frequency = st.sidebar.number_input("🍽️ **ჭამის სიხშირე (დღეში):**", min_value=2, max_value=6, value=3)

body_type = st.sidebar.selectbox(
    "🧍 **აღნაგობა:**",
    ("გამხდარი", "საშუალო", "მსუქანი")
)

goal = st.sidebar.selectbox(
    "🎯 **კვებითი მიზანი:**",
    ("წონის დაკლება", "წონის შენარჩუნება", "წონის მომატება")
)

# --- Blood type selection with both international and Georgian designations ---
st.sidebar.markdown("---")
st.sidebar.subheader("🩸 სისხლის ჯგუფი")
blood_abo_options = [
    "არ ვიცი",
    "0 (I ჯგუფი)",
    "A (II ჯგუფი)",
    "B (III ჯგუფი)",
    "AB (IV ჯგუფი)"
]
blood_abo_selection = st.sidebar.selectbox(
    "**ABO სისტემა / ქართული სტანდარტი:**",
    blood_abo_options
)

blood_rh = st.sidebar.selectbox(
    "**Rh ფაქტორი:**",
    ("არ ვიცი", "+ (დადებითი)", "- (უარყოფითი)")
)

# Extracting the ABO part for internal logic if needed
blood_abo = blood_abo_selection.split(' ')[0] if blood_abo_selection != "არ ვიცი" else "არ ვიცი"
standard_blood_group = blood_abo_selection if blood_abo_selection != "არ ვიცი" else "უცნობი"

st.sidebar.markdown("---")
calculate_button = st.sidebar.button("✨ მიიღე რეკომენდაციები")

# --- Calorie calculation (Harris-Benedict formula) ---
def calculate_bmr(weight, height, age, gender):
    if gender == "მამრობითი":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else: # მდედრობითი
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    return bmr

def calculate_tdee(bmr, activity_level):
    activity_factors = {
        "მინიმალური (მჯდომარე ცხოვრება)": 1.2,
        "მსუბუქი (კვირაში 1-3-ჯერ ვარჯიში)": 1.375,
        "ზომიერი (კვირაში 3-5-ჯერ ვარჯიში)": 1.55,
        "მაღალი (კვირაში 6-7-ჯერ ვარჯიში)": 1.725,
        "ძალიან მაღალი (ყოველდღიური, ინტენსიური ვარჯიში)": 1.9
    }
    return bmr * activity_factors[activity_level]

if calculate_button:
    bmr_val = calculate_bmr(weight, height, age, gender)
    tdee_val = calculate_tdee(bmr_val, activity_level)

    daily_calories = tdee_val
    if goal == "წონის დაკლება":
        daily_calories -= 500 # Calorie deficit
    elif goal == "წონის მომატება":
        daily_calories += 500 # Calorie surplus

    st.subheader("📊 თქვენი პერსონალური რეკომენდაციები")
    st.markdown("---")

    with st.expander("✨ **ენერგეტიკული მოთხოვნილება**", expanded=True): # Default expanded for initial view
        st.write(f"თქვენი საბაზისო მეტაბოლური მაჩვენებელი (BMR) არის: **{bmr_val:.2f} კალორია/დღეში**")
        st.write(f"თქვენი დღიური ენერგეტიკული ხარჯი (TDEE) ფიზიკური აქტივობის გათვალისწინებით არის: **{tdee_val:.2f} კალორია/დღეში**")
        st.markdown(f"თქვენი მიზანია **{goal}**, ამიტომ სავარაუდო დღიური კალორიული ნორმაა: **{daily_calories:.2f} კალორია**")

    st.markdown("---")
    with st.expander("💪 **მაკროელემენტების განაწილება და წყაროები**"):

        # Macronutrient ratios based on goal and body type (can be further refined)
        protein_ratio, carbs_ratio, fats_ratio = 0, 0, 0

        if goal == "წონის დაკლება":
            protein_ratio = 0.35 # 35% protein
            carbs_ratio = 0.40  # 40% carbs
            fats_ratio = 0.25   # 25% fat
        elif goal == "წონის შენარჩუნება":
            protein_ratio = 0.25
            carbs_ratio = 0.50
            fats_ratio = 0.25
        else: # Weight gain
            protein_ratio = 0.30
            carbs_ratio = 0.55
            fats_ratio = 0.15

        protein_grams = (daily_calories * protein_ratio) / 4 # 1g protein = 4 calories
        carbs_grams = (daily_calories * carbs_ratio) / 4     # 1g carbs = 4 calories
        fats_grams = (daily_calories * fats_ratio) / 9       # 1g fat = 9 calories

        st.write(f"თქვენი დღიური კვება უნდა შედგებოდეს დაახლოებით:")
        st.markdown(f"""
        * **ცილა:** **{protein_grams:.2f} გრამი** ({protein_ratio*100:.0f}% კალორიებიდან)
            * **ძირითადი წყაროები:** 🥩 მჭლე ხორცი (ქათმის მკერდი, ინდაური, უცხიმო საქონლის ხორცი), 🐟 თევზი (ორაგული, კალმახი, თინუსი), 🥚 კვერცხი, 🥛 რძის პროდუქტები (ხაჭო, ბერძნული იოგურტი, ყველი), 🌱 პარკოსნები (ოსპი, ლობიო, მუხუდო), ტოფუ, თხილეული.
        * **ნახშირწყლები:** **{carbs_grams:.2f} გრამი** ({carbs_ratio*100:.0f}% კალორიებიდან)
            * **წყაროები (კომპლექსური):** 🌾 მთელმარცვლოვანი პური, ყავისფერი ბრინჯი, ქინოა, შვრია, ტკბილი კარტოფილი, პარკოსნები.
            * **მარტივი (ჯანსაღი):** 🍎 ხილი (ვაშლი, ბანანი, კენკრა).
        * **ცხიმები:** **{fats_grams:.2f} გრამი** ({fats_ratio*100:.0f}% კალორიებიდან)
            * **წყაროები (ჯანსაღი):** 🥑 ავოკადო, 🌰 თხილი (ნუში, კაკალი), 🥜 არაქისის კარაქი (ნატურალური), 🐟 ცხიმიანი თევზი, 🥣 ზეითუნის ზეთი, ჩიას თესლი.
        """)

    st.markdown("---")
    with st.expander("🍽️ **კვების სიხშირე და რაციონების მაგალითები**"):
        st.write(f"თქვენ გირჩევნიათ იკვებოთ **{meal_frequency}**-ჯერ დღეში. ეს კარგი მიდგომაა სტაბილური ენერგიის შესანარჩუნებლად.")

        st.markdown("##### რეკომენდებული რაციონები:")
        st.markdown("""
        * **🌅 საუზმე:**
            * შვრიის ფაფა კენკრით და ნუშით.
            * ომლეტი ბოსტნეულით და მთელმარცვლოვანი პურით.
            * ბერძნული იოგურტი ხილით და გრანოლით.
        * **☀️ სადილი:**
            * გამომცხვარი ქათმის მკერდი ყავისფერი ბრინჯით და ბროკოლით.
            * ორაგულის სტეიკი ტკბილი კარტოფილით და სალათით.
            * ოსპის წვნიანი მთელმარცვლოვანი პურით.
        * **🌙 ვახშამი:**
            * შემწვარი ინდაური და ბოსტნეული (ყვავილოვანი კომბოსტო, მწვანე ლობიო).
            * თინუსის სალათი მწვანე ფოთლოვანი სალათით და ავოკადოთი.
            * ხაჭო კენკრით და თხილით.
        * **🍎 შუალედური კვება:**
            * ხილი, მუჭა თხილი, იოგურტი, სტაფილოს ჩხირები ჰუმუსით.
        """)

    st.markdown("---")
    with st.expander("🏋️‍♀️ **კვებითი რეკომენდაციები აქტივობის დონის მიხედვით**"):
        st.write(f"თქვენი აქტივობის დონეა: **{activity_level}**.")

        if "მინიმალური" in activity_level:
            st.markdown("""
            **მინიმალური აქტივობა (მჯდომარე ცხოვრება):**
            * **ფოკუსი:** დაბალანსებული, ადვილად მოსანელებელი საკვები, მაღალი ბოჭკოვანით. მოერიდეთ ჭარბ კალორიებს.
            * **რეკომენდებულია:**
                * **საუზმე:** შვრიის ფაფა ხილით, ან კვერცხის ცილის ომლეტი ბოსტნეულით.
                * **სადილი:** ბოსტნეულის სალათი ქათმის გრილზე მომზადებული მკერდით ან თევზით. მსუბუქი სუპები.
                * **ვახშამი:** ორთქლზე მოხარშული თევზი ან მჭლე ხორცი, ბევრი მწვანე ბოსტნეულით.
                * **შუალედური კვება:** ხილი, იოგურტი.
            * **მოერიდეთ:** ტკბილეული, ცხიმიანი საკვები, გადამუშავებული ნახშირწყლები (თეთრი პური, მაკარონი).
            """)
        elif "მსუბუქი" in activity_level:
            st.markdown("""
            **მსუბუქი აქტივობა (კვირაში 1-3-ჯერ ვარჯიში):**
            * **ფოკუსი:** კარგი ბალანსი მაკროელემენტებს შორის. აქტიური ცხოვრებისთვის საჭირო ენერგია.
            * **რეკომენდებულია:**
                * **საუზმე:** მთელმარცვლოვანი ფაფები, კვერცხი, ბერძნული იოგურტი.
                * **სადილი:** მჭლე ხორცი/თევზი, ყავისფერი ბრინჯი/ქინოა, ბევრი ბოსტნეული.
                * **ვახშამი:** მსუბუქი ცილოვანი კვება ბოსტნეულით.
                * **შუალედური კვება:** თხილი, ხილი, ბოსტნეულის ჩხირები.
            * **ყურადღება მიაქციეთ:** ვარჯიშის წინ (1-2 სთ) მიიღეთ მცირე რაოდენობით სწრაფი ნახშირწყლები (ბანანი), ვარჯიშის შემდეგ - ცილა და კომპლექსური ნახშირწყლები.
            """)
        elif "ზომიერი" in activity_level:
            st.markdown("""
            **ზომიერი აქტივობა (კვირაში 3-5-ჯერ ვარჯიში):**
            * **ფოკუსი:** გაზრდილი ნახშირწყლებისა და ცილის მიღება კუნთების აღდგენისა და ენერგიის შესანარჩუნებლად.
            * **რეკომენდებულია:**
                * **საუზმე:** შვრიის ფაფა პროტეინის ფხვნილით ან კვერცხით, მთელმარცვლოვანი პური.
                * **სადილი:** ქათამი/თევზი/საქონლის ხორცი, მეტი რაოდენობით ყავისფერი ბრინჯი/ტკბილი კარტოფილი, უამრავი ბოსტნეული.
                * **ვახშამი:** ცილოვანი კვება (ორაგული, ინდაური) და მწვანე ბოსტნეული.
                * **შუალედური კვება:** პროტეინ ბარი, ხაჭო, თხილი, ხილი.
            * **მნიშვნელოვანია:** ვარჯიშის შემდგომი კვება ცილებითა და კომპლექსური ნახშირწყლებით (მაგ. ქათამი და ბრინჯი) კუნთების სწრაფი აღდგენისთვის.
            """)
        elif "მაღალი" in activity_level:
            st.markdown("""
            **მაღალი აქტივობა (კვირაში 6-7-ჯერ ვარჯიში):**
            * **ფოკუსი:** მაღალი კალორიული მიღება, ნახშირწყლები, როგორც ენერგიის ძირითადი წყარო, და მაღალი ცილის მიღება კუნთების ზრდისა და აღდგენისთვის.
            * **რეკომენდებულია:**
                * **საუზმე:** დიდი პორცია შვრია თხილით, კენკრით, პროტეინის ფხვნილით. ომლეტი ბევრი კვერცხით.
                * **სადილი:** ორმაგი პორცია მჭლე ხორცი/თევზი, დიდი პორცია ბრინჯი/კარტოფილი/პასტა, ბოსტნეული.
                * **ვახშამი:** ცილით მდიდარი და კომპლექსური ნახშირწყლების შემცველი კვება (მაგალითად, საქონლის ხორცი წიწიბურათი).
                * **შუალედური კვება:** ხილი, პროტეინ შეიკი, სენდვიჩები მთელმარცვლოვანი პურით.
            * **განსაკუთრებული ყურადღება:** ვარჯიშის წინ და შემდგომ კვებას. შესაძლოა საჭირო გახდეს სპორტული დანამატები (კრეატინი, BCAA).
            """)
        elif "ძალიან მაღალი" in activity_level:
            st.markdown("""
            **ძალიან მაღალი აქტივობა (ყოველდღიური, ინტენსიური ვარჯიში):**
            * **ფოკუსი:** ძალიან მაღალი კალორიული მიღება, ენერგიის მუდმივი შევსება და კუნთების მაქსიმალური აღდგენა.
            * **რეკომენდებულია:**
                * **მრავალჯერადი კვება:** 5-6 დიდი კვება დღეში, მდიდარი ნახშირწყლებითა და ცილებით.
                * **კვების მაგალითები:** რთული ნახშირწყლები (ბრინჯი, ტკბილი კარტოფილი, პასტა), მჭლე ცილები (ქათამი, ინდაური, საქონლის ხორცი, თევზი), ჯანსაღი ცხიმები (ავოკადო, თხილი).
                * **მუდმივი შევსება:** ვარჯიშის დროს და მის შემდეგ ელექტროლიტებითა და სწრაფი ნახშირწყლებით მდიდარი სასმელები.
            * **სპეციალური მიდგომა:** შესაძლოა საჭირო გახდეს პროფესიონალი სპორტული დიეტოლოგის კონსულტაცია. დანამატების როლი (კრეატინი, პროტეინი, გეინერები) უფრო მნიშვნელოვანი ხდება.
            """)

    st.markdown("---")
    with st.expander("⚖️ **ერთჯერადი კვების მიახლოებითი ნორმა**"):
        st.markdown(f"""
        თქვენი **{daily_calories:.0f} კალორიის** გათვალისწინებით და **{meal_frequency} კვებაზე** გადანაწილებით, თითოეული კვება უნდა იყოს დაახლოებით **{daily_calories / meal_frequency:.0f} კალორია**.
        საშუალო ერთჯერადი კვება შეიძლება შეიცავდეს:
        * **ცილა:** **{protein_grams / meal_frequency:.0f} გრამი** (დაახლ. ხელისგულის ზომის პორცია ქათამი/თევზი, ან 2-3 კვერცხი).
        * **ნახშირწყლები:** **{carbs_grams / meal_frequency:.0f} გრამი** (დაახლ. მუჭის ზომის პორცია ბრინჯი/ქინოა, ან 1 საშუალო კარტოფილი).
        * **ცხიმები:** **{fats_grams / meal_frequency:.0f} გრამი** (დაახლ. ცერა თითის ზომის პორცია ავოკადო/თხილი).
        * **ბოსტნეული:** 🥦🥕 იმდენი, რამდენიც გსურთ!
        """)

    st.markdown("---")
    with st.expander("🌱 **მნიშვნელოვანი მინერალები და ვიტამინები: დეტალური წყაროები**"):
        st.markdown("""
        * **ვიტამინი C:** 🍊 ციტრუსები, 🥝 კივი, 🍓 მარწყვი, 🌶️ წიწაკა, ბროკოლი.
        * **ვიტამინი D:** ☀️ მზის სინათლე, 🐟 ცხიმიანი თევზი, 🥚 კვერცხის გული.
        * **რკინა:** 🥩 წითელი ხორცი, 🍗 ქათამი, 🐟 თევზი, 🌱 ოსპი, ისპანახი, გოგრის თესლი.
        * **კალციუმი:** 🥛 რძის პროდუქტები, 🌱 ისპანახი, ბროკოლი, ტოფუ.
        * **მაგნიუმი:** 🌰 თხილი, 🌻 თესლეული, 🌱 ისპანახი, ავოკადო, შავი შოკოლადი.
        * **კალიუმი:** 🍌 ბანანი, 🥔 კარტოფილი, 🥑 ავოკადო, 🌱 ისპანახი, ლობიო.
        * **ვიტამინი B12:** 🥩 ხორცი, 🐟 თევზი, 🥚 კვერცხი, 🥛 რძის პროდუქტები.
        * **ფოლიუმის მჟავა:** 🥬 მწვანე ფოთლოვანი ბოსტნეული, პარკოსნები, ციტრუსები.
        """)

    st.markdown("---")
    with st.expander("💧 **დამატებითი ჯანსაღი ჩვევები**"):
        st.markdown("""
        * **წყლის მიღება:** დალიეთ **2-2.5 ლიტრი** წყალი დღეში.
        * **ძილი:** ეცადეთ გეძინოთ **7-9 საათი**.
        * **სტრესის მართვა:** იპოვეთ თქვენთვის შესაფერისი გზები (იოგა, მედიტაცია, გასეირნება).
        * **ფიზიკური აქტივობა:** რეგულარული ვარჯიში აუცილებელია.
        * **ჯანსაღი არჩევანი:** შეზღუდეთ გადამუშავებული, შაქრიანი და ცხიმებით მდიდარი საკვები.
        * **მრავალფეროვნება:** მიირთვით მრავალფეროვანი საკვები.
        * **მოუსმინეთ სხეულს:** იკვებეთ შიმშილის დროს, შეწყვიტეთ დანაყრებისას.
        """)

    # --- Blood type specific advice (general) ---
    selected_blood_type_display = standard_blood_group
    if blood_rh != "არ ვიცი":
        selected_blood_type_display += f" {blood_rh}"

    if blood_abo != "არ ვიცი" and "არ ვიცი" not in blood_abo_selection:
        st.markdown("---")
        with st.expander(f"🩸 **რეკომენდაცია სისხლის ჯგუფისთვის ({selected_blood_type_display})**"):
            if "0" in blood_abo: # 0 (I Group)
                st.write("""
                **ჯგუფი 0 (I):** ზოგადი რეკომენდაციით, ამ ჯგუფისთვის ხშირად რეკომენდებულია **მაღალცილოვანი დიეტა** მჭლე ხორცით, ფრინველით, თევზით.
                * **უპირატესობა:** 🥩 წითელი ხორცი (უცხიმო), 🍗 ქათამი, 🐟 თევზი, ხილი, ბოსტნეული.
                * **შეზღუდეთ:** 🥛 რძის პროდუქტები, 🌾 მარცვლეული (ხორბალი), 🥔 კარტოფილი.
                """)
            elif "A" in blood_abo: # A (II Group)
                st.write("""
                **ჯგუფი A (II):** სასარგებლოა ძირითადად **მცენარეული კვება**.
                * **უპირატესობა:** 🍎 ხილი, 🥦 ბოსტნეული, 🌾 მთელმარცვლოვანი (შვრია, ბრინჯი), 🌱 პარკოსნები, 🐟 თევზი (ზომიერად).
                * **შეზღუდეთ:** 🥩 წითელი ხორცი, 🥛 რძის პროდუქტები.
                """)
            elif "B" in blood_abo: # B (III Group)
                st.write("""
                **ჯგუფი B (III):** რეკომენდებულია **დაბალანსებული და მრავალფეროვანი დიეტა**.
                * **უპირატესობა:** 🍗 მჭლე ხორცი, 🐟 თევზი, 🥛 რძის პროდუქტები, 🌾 მარცვლეული, 🍎 ხილი, 🥦 ბოსტნეული.
                * **შეზღუდეთ:** 🌽 სიმინდი, წიწიბურა, არაქისი.
                """)
            elif "AB" in blood_abo: # AB (IV Group)
                st.write("""
                **ჯგუფი AB (IV):** ეს ჯგუფი A და B ჯგუფების ნაზავია. რეკომენდებულია **ზომიერი, შერეული დიეტა**.
                * **უპირატესობა:** 🐟 თევზი, 🍤 ზღვის პროდუქტები, ტოფუ, 🥬 მწვანე ბოსტნეული, 🥛 რძის პროდუქტები, 🌱 პარკოსნები.
                * **შეზღუდეთ:** 🥩 წითელი ხორცი (მცირე რაოდენობით), 🌽 სიმინდი, წიწიბურა.
                """)
        st.info("""
        **შენიშვნა სისხლის ჯგუფზე:** სისხლის ჯგუფის მიხედვით კვების დიეტა პოპულარულია, თუმცა მისი ეფექტურობა მეცნიერულად სრულად დადასტურებული არ არის.
        """)

    st.markdown("---")
    st.warning("""
    **🚨 მნიშვნელოვანი გაფრთხილება:** ეს ზოგადი რეკომენდაციებია და არ წარმოადგენს პროფესიონალურ სამედიცინო ან დიეტოლოგიურ კონსულტაციას.
    ინდივიდუალური კვების გეგმისთვის მიმართეთ ლიცენზირებულ დიეტოლოგს ან ექიმს, განსაკუთრებით თუ გაქვთ ქრონიკული დაავადებები, ალერგიები ან სპეციალური კვებითი საჭიროებები.
    """)
