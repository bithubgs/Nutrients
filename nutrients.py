import streamlit as st
import pandas as pd

# საკვები პროდუქტების მონაცემები
products_data = {
    'პროდუქტი': [
        'საქონლის ხორცი (მჭლე)', 'ღორის ღვიძლი', 'ქათმის მკერდი', 'ქათმის ღვიძლი',
        'ორაგული (ველური)', 'თინუსი (დაკონსერვებული, წყალში)', 'სარდინი (ზეთში, ძვლებით)', 'კრევეტები', 'მიდიები',
        'ისპანახი', 'ბროკოლი', 'ავოკადო', 'სტაფილო', 'ბანანი', 'ტკბილი კარტოფილი', 'კომბოსტო', 'წითელი ბულგარული წიწაკა',
        'კარაქი', 'რძე (მთლიანი)', 'იოგურტი (ბერძნული)', 'ყველი (ჩედარი)', 'კვერცხი', 'ხაჭო',
        'შავი ლობიო', 'ნუში', 'ნიგოზი', 'ჩიას თესლი', 'მზესუმზირის თესლი', 'ოსპი', 'წიწიბურა',
        'ზღვის კალმახი', 'სპირულინა', 'ქლორელა', 'ყავისფერი ბრინჯი', 'კინოა', 'შვრია',
        'ვირთევზა', 'სკუმბრია', 'პორტობელო სოკო', 'ინდაურის ხორცი', 'ცხვრის ხორცი', 'ხბოს ხორცი',
        'ფორთოხალი', 'კივი', 'მარწყვი', 'მოცვი', 'ვაშლი',
        'სოიოს რძე (გამაგრებული)', 'ტოფუ', 'შავი შოკოლადი (70%+ კაკაო)', 'საფუარის ექსტრაქტი', 'ქატო',
        'მიწისთხილის კარაქი', 'ქოქოსის რძე', 'თეთრი ლობიო', 'მწვანე ლობიო', 'ხმელი გარგარი',
        'გოგრის თესლი', 'კეშიუ', 'ფიჭვის კაკალი', 'ჩიტიფეხა', 'ბარდა', 'კამა', 'ოხრახუში',
        'ფისტა', 'ბრაზილიური კაკალი', 'ნიორი', 'ჯანჯაფილი',
        # დამატებული პროდუქტები C და D ვიტამინებით
        'წითელი კომბოსტო', 'ლიმონი', 'გრეიპფრუტი', 'კალე', 'ბრიუსელის კომბოსტო',
        'თევზის ქონი (კოდის)', 'შამპინიონი (D ვიტამინით გამდიდრებული)', 'ძროხის რძე (D ვიტამინით გამდიდრებული)'
    ],
    'კატეგორია': [
        'ხორცი', 'ღვიძლი', 'ხორცი', 'ღვიძლი',
        'თევზი', 'თევზი', 'თევზი', 'ზღვის პროდუქტები', 'ზღვის პროდუქტები',
        'ბოსტნეული', 'ბოსტნეული', 'ხილი', 'ბოსტნეული', 'ხილი', 'ბოსტნეული', 'ბოსტნეული', 'ბოსტნეული',
        'რძის პროდუქტები', 'რძის პროდუქტები', 'რძის პროდუქტები', 'რძის პროდუქტები', 'კვერცხი', 'რძის პროდუქტები',
        'პარკოსნები', 'კაკალი და თესლი', 'კაკალი და თესლი', 'კაკალი და თესლი', 'კაკალი და თესლი', 'პარკოსნები', 'მარცვლეული',
        'თევზი', 'სუპერფუდი', 'სუპერფუდი', 'მარცვლეული', 'მარცვლეული', 'მარცვლეული',
        'თევზი', 'თევზი', 'სოკო', 'ხორცი', 'ხორცი', 'ხორცი',
        'ხილი', 'ხილი', 'ხილი', 'ხილი', 'ხილი',
        'მცენარეული რძე', 'სოიოს პროდუქტები', 'საკონდიტრო ნაწარმი', 'სუპერფუდი', 'მარცვლეული',
        'პარკოსნები', 'მცენარეული რძე', 'პარკოსნები', 'პარკოსნები', 'ხილი',
        'გოგრის თესლი', 'კეშიუ', 'ფიჭვის კაკალი', 'ბოსტნეული', 'პარკოსნები', 'ბოსტნეული', 'ბოსტნეული',
        'კაკალი და თესლი', 'კაკალი და თესლი', 'ბოსტნეული', 'ბოსტნეული',
        # დამატებული პროდუქტების კატეგორიები
        'ბოსტნეული', 'ხილი', 'ხილი', 'ბოსტნეული', 'ბოსტნეული',
        'თევზის პროდუქტები', 'სოკო', 'რძის პროდუქტები'
    ],
    'რკინა_მგ': [
        3.3, 30.5, 0.9, 13.0,
        0.8, 1.3, 2.9, 1.8, 6.7,
        2.7, 0.7, 0.6, 0.3, 0.3, 0.7, 0.5, 0.5,
        0.2, 0.03, 0.1, 0.4, 1.2, 0.4,
        6.2, 2.9, 2.7, 7.7, 5.2, 7.5, 2.2,
        90.0, 28.5, 58.0, 0.8, 4.6, 4.0,
        1.0, 1.6, 0.5, 2.5, 2.1, 3.5,
        0.1, 0.3, 0.3, 0.2, 0.2,
        0.5, 2.0, 3.0, 1.5, 10.0,
        1.5, 0.5, 6.0, 1.0, 1.5,
        3.3, 4.0, 5.0, 1.5, 1.5, 1.0, 2.0,
        3.9, 2.5, 1.7, 0.6,
        # დამატებული პროდუქტების მონაცემები
        0.5, 0.2, 0.2, 1.5, 0.5,
        0.1, 0.2, 0.1
    ],
    'B12_მკგ': [
        2.6, 83.1, 0.3, 16.6,
        4.9, 4.3, 8.9, 1.1, 24.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        0.2, 0.4, 0.5, 0.8, 0.6, 0.4,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        1.5, 175.0, 65.0, 0.0, 0.0, 0.0,
        5.4, 19.0, 0.0, 0.4, 2.1, 3.0,
        0.0, 0.0, 0.0, 0.0, 0.0,
        2.4, 0.0, 0.0, 5.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0,
        # დამატებული პროდუქტების მონაცემები
        0.0, 0.0, 0.0, 0.0, 0.0,
        100.0, 0.0, 1.2
    ],
    'ფოლატი_მკგ': [
        4, 290, 3, 588,
        26, 5, 10, 3, 76,
        194, 63, 81, 3, 20, 40, 107, 24,
        3, 5, 7, 27, 47, 24,
        394, 28, 45, 49, 227, 181, 30,
        180, 94, 23, 8, 184, 56,
        12, 2, 17, 4, 7, 5,
        30, 25, 20, 6, 3,
        50, 29, 30, 50, 160,
        60, 15, 200, 33, 10,
        15, 60, 80, 15, 30, 150, 170,
        70, 10, 15, 10,
        # დამატებული პროდუქტების მონაცემები
        30, 30, 20, 140, 60,
        0, 17, 5
    ],
    'C_ვიტამინი_მგ': [
        0, 1, 0, 17,
        0, 0, 0, 2, 8,
        28, 89, 10, 6, 9, 20, 36, 128,
        0, 0, 0, 0, 0, 0,
        2, 1, 1, 0, 1, 5, 0,
        3, 10, 9, 0, 0, 0,
        0, 0, 2, 0, 0, 0,
        53, 93, 59, 10, 4,
        0, 0, 0, 0, 0,
        0, 0, 0, 5, 1,
        0, 0, 0, 20, 10, 85, 133,
        0, 0, 5, 5,
        # დამატებული პროდუქტების მონაცემები
        60, 53, 40, 120, 110,
        0, 2, 1
    ],
    'D_ვიტამინი_IU': [
        3, 15, 0, 44,
        360, 154, 164, 5, 76,
        0, 0, 0, 0, 0, 0, 0, 0,
        142, 115, 5, 24, 82, 0,
        0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0,
        388, 388, 375, 6, 53, 7,
        0, 0, 0, 0, 0,
        100, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0,
        # დამატებული პროდუქტების მონაცემები
        0, 0, 0, 0, 0,
        1360, 1000, 100
    ],
    'კალციუმი_მგ': [
        12, 5, 8, 8,
        12, 4, 382, 70, 26,
        99, 47, 12, 6, 5, 30, 40, 10,
        24, 113, 110, 721, 50, 83,
        113, 37, 28, 177, 78, 35, 20,
        1170, 120, 74, 23, 47, 52,
        20, 12, 3, 10, 7, 12,
        40, 34, 13, 8, 7,
        300, 350, 100, 20, 200,
        20, 10, 150, 50, 5,
        50, 60, 10, 50, 30, 200, 170,
        100, 160, 20, 10,
        # დამატებული პროდუქტების მონაცემები
        40, 30, 20, 150, 60,
        10, 5, 120
    ],
    'მაგნიუმი_მგ': [
        20, 18, 29, 19,
        29, 64, 39, 39, 34,
        79, 21, 29, 12, 27, 25, 12, 10,
        2, 10, 11, 28, 10, 8,
        140, 158, 183, 335, 325, 36, 112,
        560, 195, 315, 143, 197, 138,
        27, 97, 9, 25, 17, 25,
        10, 15, 10, 12, 5,
        25, 50, 100, 15, 50,
        50, 15, 150, 20, 10,
        262, 292, 251, 20, 40, 50, 30,
        121, 197, 25, 18,
        # დამატებული პროდუქტების მონაცემები
        15, 10, 12, 30, 20,
        5, 10, 12
    ],
    'კალიუმი_მგ': [
        350, 320, 300, 290,
        363, 290, 397, 259, 290,
        558, 316, 487, 300, 358, 337, 250, 211,
        24, 150, 170, 90, 138, 150,
        644, 705, 440, 407, 894, 900, 380,
        990, 800, 700, 220, 170, 429,
        290, 360, 260, 300, 320, 380,
        180, 200, 150, 150, 100,
        150, 120, 100, 50, 250,
        350, 150, 600, 200, 300,
        500, 600, 700, 400, 450, 500, 450,
        700, 600, 400, 415,
        # დამატებული პროდუქტების მონაცემები
        250, 100, 150, 350, 280,
        0, 200, 150
    ],
    'თუთია_მგ': [
        4.0, 7.0, 0.4, 2.7,
        0.6, 0.8, 1.3, 0.6, 1.3,
        0.1, 0.2, 0.4, 0.1, 0.2, 0.2, 0.2, 0.1,
        0.1, 0.4, 0.5, 3.0, 1.1, 0.5,
        3.0, 0.9, 0.9, 3.5, 5.0, 1.3, 1.3,
        4.0, 0.7, 0.5, 0.8, 2.0, 2.0,
        0.5, 1.2, 0.5, 2.0, 2.5, 4.5,
        0.1, 0.1, 0.1, 0.1, 0.1,
        0.8, 0.8, 1.0, 0.5, 2.0,
        0.5, 0.1, 2.0, 0.3, 0.2,
        2.0, 1.5, 1.0, 0.5, 0.5, 0.5, 0.5,
        1.5, 2.0, 0.3, 0.3,
        # დამატებული პროდუქტების მონაცემები
        0.1, 0.1, 0.1, 0.2, 0.2,
        0.1, 0.5, 0.4
    ],
    'A_ვიტამინი_მკგ_RAE': [
        1, 1000, 10, 800,
        20, 20, 10, 10, 10,
        469, 31, 7, 835, 3, 709, 5, 47,
        100, 50, 10, 100, 50, 20,
        1, 0, 0, 0, 0, 1, 0,
        5, 300, 200, 0, 0, 0,
        10, 30, 0, 5, 5, 10,
        22, 23, 30, 10, 5,
        50, 0, 0, 0, 0,
        0, 0, 0, 10, 10,
        0, 0, 0, 10, 10, 50, 100,
        0, 0, 10, 0,
        # დამატებული პროდუქტების მონაცემები
        50, 10, 15, 500, 250,
        5, 0, 60
    ],
    'E_ვიტამინი_მგ_ATE': [
        0.5, 0.5, 0.2, 0.3,
        0.8, 0.2, 0.2, 0.1, 0.1,
        0.3, 0.8, 2.1, 0.7, 0.4, 0.3, 0.1, 1.6,
        0.8, 0.1, 0.1, 0.1, 0.5, 0.1,
        0.0, 7.7, 2.7, 0.5, 35.0, 0.1, 0.1,
        0.1, 0.1, 0.1, 0.0, 0.0, 0.1,
        0.1, 0.5, 0.1, 0.1, 0.1, 0.2,
        0.2, 0.1, 0.4, 0.2, 0.1,
        0.1, 0.0, 0.5, 0.0, 0.5,
        0.1, 0.1, 0.0, 0.1, 0.1,
        0.1, 2.0, 1.0, 0.5, 0.2, 0.5, 0.2,
        2.9, 0.5, 0.1, 0.1,
        # დამატებული პროდუქტების მონაცემები
        0.2, 0.1, 0.2, 0.5, 0.3,
        0.1, 0.1, 0.1
    ],
    'K_ვიტამინი_მკგ': [
        1, 3, 0, 5,
        5, 0, 0, 0, 0,
        483, 102, 21, 19, 0, 21, 109, 14,
        7, 0, 0, 0, 0, 0,
        4, 0, 0, 0, 0, 4, 0,
        0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        0, 0, 0, 25, 3, 160, 200,
        0, 0, 0, 0,
        # დამატებული პროდუქტების მონაცემები
        80, 0, 0, 681, 177,
        0, 0, 0
    ],
    'სელენი_მკგ': [
        35, 50, 20, 50,
        40, 90, 55, 30, 20,
        1, 1, 0.4, 0.2, 0.1, 0.6, 0.3, 0.1,
        1, 2, 2, 10, 15, 2,
        0.6, 0.2, 0.1, 0.4, 0.4, 0.6, 0.3,
        150, 4, 2, 10, 5, 10,
        100, 80, 0.5, 20, 25, 40,
        0.1, 0.1, 0.1, 0.1, 0.1,
        10, 10, 5, 20, 50,
        5, 1, 1, 1, 1,
        10, 1, 1, 0.5, 0.5, 1, 1,
        10, 544, 0.6, 0.2,
        # დამატებული პროდუქტების მონაცემები
        0.3, 0.1, 0.1, 0.5, 0.4,
        80, 5, 5
    ]
}

# DataFrame-ის შექმნა
df = pd.DataFrame(products_data)

# Callback ფუნქცია გასუფთავებისთვის
def clear_nutrients_multiselect_tab3():
    st.session_state.nutrients_multiselect_tab3 = []

# დამხმარე ფუნქცია ღილაკებისთვის (ძებნის პარამეტრების განახლება)
def set_search_and_min_amount(search_term_val, min_amount_val=0.0):
    st.session_state.search_term = search_term_val
    st.session_state.min_amount = min_amount_val

# --- დამხმარე ფუნქციები ---
def find_nutrient_column(search_term):
    """
    პოულობს შესაბამის სვეტს ძიების ტერმინის მიხედვით.
    ეს ფუნქცია გაუმჯობესებულია, რათა უკეთ მოძებნოს ვიტამინები,
    მაშინაც კი, თუ ტერმინი ზუსტად არ ემთხვევა სვეტის სახელს.
    """
    search_lower = search_term.lower()
    
    # სტანდარტული mappings ძიების ტერმინებისთვის
    # ეს mapping უნდა მოიცავდეს ყველა შესაძლო მომხმარებლის შეყვანის ვარიანტს
    # და მიუთითებდეს რეალურ სვეტის სახელს DataFrame-ში.
    nutrient_mapping = {
        'რკინა': 'რკინა_მგ',
        'iron': 'რკინა_მგ',
        'fe': 'რკინა_მგ', # დავამატე 'Fe' მოკლე დასახელებისთვის
        
        'b12': 'B12_მკგ',
        'ვიტამინი b12': 'B12_მკგ',
        'vitamin b12': 'B12_მკგ',
        'კობალამინი': 'B12_მკგ', # დავამატე ქართული სახელი
        
        'ფოლატი': 'ფოლატი_მკგ',
        'folate': 'ფოლატი_მკგ',
        'ფოლიუმის მჟავა': 'ფოლატი_მკგ', # დავამატე ქართული სახელი
        
        'c': 'C_ვიტამინი_მგ',
        'ვიტამინი c': 'C_ვიტამინი_მგ',
        'vitamin c': 'C_ვიტამინი_მგ',
        'c ვიტამინი': 'C_ვიტამინი_მგ',
        'ასკორბინის მჟავა': 'C_ვიტამინი_მგ', # დავამატე ქართული სახელი
        
        'd': 'D_ვიტამინი_IU',
        'ვიტამინი d': 'D_ვიტამინი_IU',
        'vitamin d': 'D_ვიტამინი_IU',
        'd ვიტამინი': 'D_ვიტამინი_IU',
        'კალციფეროლი': 'D_ვიტამინი_IU', # დავამატე ქართული სახელი
        
        'კალციუმი': 'კალციუმი_მგ',
        'calcium': 'კალციუმი_მგ',
        'ca': 'კალციუმი_მგ', # დავამატე მოკლე დასახელებისთვის
        
        'მაგნიუმი': 'მაგნიუმი_მგ',
        'magnesium': 'მაგნიუმი_მგ',
        'mg': 'მაგნიუმი_მგ', # დავამატე მოკლე დასახელებისთვის
        
        'კალიუმი': 'კალიუმი_მგ',
        'potassium': 'კალიუმი_მგ',
        'k (კალიუმი)': 'კალიუმი_მგ', # დავამატე, რადგან 'K' ასევე ვიტამინი K-ს ნიშნავს
        
        'თუთია': 'თუთია_მგ',
        'zinc': 'თუთია_მგ',
        'zn': 'თუთია_მგ', # დავამატე მოკლე დასახელებისთვის
        
        'a': 'A_ვიტამინი_მკგ_RAE',
        'ვიტამინი a': 'A_ვიტამინი_მკგ_RAE',
        'a ვიტამინი': 'A_ვიტამინი_მკგ_RAE',
        'vitamin a': 'A_ვიტამინი_მკგ_RAE',
        'რეტინოლი': 'A_ვიტამინი_მკგ_RAE', # დავამატე ქართული სახელი
        
        'e': 'E_ვიტამინი_მგ_ATE',
        'ვიტამინი e': 'E_ვიტამინი_მგ_ATE',
        'e ვიტამინი': 'E_ვიტამინი_მგ_ATE',
        'vitamin e': 'E_ვიტამინი_მგ_ATE',
        'ტოკოფეროლი': 'E_ვიტამინი_მგ_ATE', # დავამატე ქართული სახელი
        
        'k': 'K_ვიტამინი_მკგ', # ეს რჩება ვიტამინი K-სთვის
        'ვიტამინი k': 'K_ვიტამინი_მკგ',
        'k ვიტამინი': 'K_ვიტამინი_მკგ',
        'vitamin k': 'K_ვიტამინი_მკგ',
        'ფილოქვინონი': 'K_ვიტამინი_მკგ', # დავამატე ქართული სახელი
        
        'სელენი': 'სელენი_მკგ',
        'selenium': 'სელენი_მკგ',
        'se': 'სელენი_მკგ' # დავამატე მოკლე დასახელებისთვის
    }
    
    # 1. ვცდილობთ ზუსტი შესატყვისობა mapping-ში (უმთავრესი)
    if search_lower in nutrient_mapping:
        return nutrient_mapping[search_lower]
        
    # 2. თუ ზუსტი შესატყვისობა არ მოიძებნა, ვეძებთ ნაწილობრივ შესატყვისობას სვეტის სახელში.
    # ეს ხაზი კარგად მუშაობს იმისთვის, რომ მოძებნოს სვეტები, რომლებიც შეიცავს ძიების ტერმინს.
    # მაგალითად, "რკინა" მოძებნის "რკინა_მგ"-ს, თუ ის არ იყო mapping-ში (თუმცა ამ შემთხვევაში არის).
    # ეს უფრო მოქნილია, თუ მომავალში ახალი ნუტრიენტები დაემატება.
    for col in df.columns:
        if col not in ['პროდუქტი', 'კატეგორია']: # ვამოწმებთ მხოლოდ ნუტრიენტების სვეტებს
            if search_lower in col.lower():
                return col
            # დამატებითი ლოგიკა ვიტამინებისთვის:
            # თუ მომხმარებელმა ჩაწერა 'ვიტამინი C' და სვეტი არის 'C_ვიტამინი_მგ'
            # ან თუ ჩაწერა 'C' და სვეტი არის 'C_ვიტამინი_მგ'
            # ეს უკვე არსებობს და კარგად მუშაობს
            if 'ვიტამინი' in search_lower and search_lower.replace('ვიტამინი ', '') in col.lower():
                return col
            if 'vitamin' in search_lower and search_lower.replace('vitamin ', '') in col.lower():
                return col

    return None

def get_unit(column_name):
    """ვაბრუნებთ შესაბამის ზომის ერთეულს"""
    if 'მგ' in column_name:
        return 'მგ'
    elif 'მკგ' in column_name:
        return 'მკგ'
    elif 'IU' in column_name:
        return 'IU'
    elif 'RAE' in column_name:
        return 'მკგ RAE'
    elif 'ATE' in column_name:
        return 'მგ ATE'
    return ''

def get_daily_dose(nutrient_name):
    """ვაბრუნებთ დღიურ დოზას კონკრეტული ნუტრიენტისთვის"""
    daily_doses = {
        "რკინა": "18 მგ (ქალები), 8 მგ (მამაკაცები)",
        "B12": "2.4 მკგ",
        "ფოლატი": "400 მკგ",
        "C ვიტამინი": "90 მგ (მამაკაცები), 75 მგ (ქალები)",
        "D ვიტამინი": "600-800 IU",
        "კალციუმი": "1000-1200 მგ",
        "მაგნიუმი": "400-420 მგ (მამაკაცები), 310-320 მგ (ქალები)",
        "კალიუმი": "3500-4700 მგ",
        "თუთია": "11 მგ (მამაკაცები), 8 მგ (ქალები)",
        "A ვიტამინი": "700-900 მკგ RAE",
        "E ვიტამინი": "15 მგ",
        "K ვიტამინი": "90-120 მკგ",
        "სელენი": "55 მკგ"
    }
    
    # ვეძებთ დოზას
    for key, dose in daily_doses.items():
        if key.lower() in nutrient_name.lower():
            return dose
    return None

def calculate_daily_nutrition(selected_products, df):
    """გამოთვლის სულ დღიურ ნუტრიენტებს არჩეული პროდუქტებიდან"""
    if not selected_products:
        return None
    
    total_nutrition = {
        'რკინა_მგ': 0,
        'B12_მკგ': 0,
        'ფოლატი_მკგ': 0,
        'C_ვიტამინი_მგ': 0,
        'D_ვიტამინი_IU': 0,
        'კალციუმი_მგ': 0,
        'მაგნიუმი_მგ': 0,
        'კალიუმი_მგ': 0,
        'თუთია_მგ': 0,
        'A_ვიტამინი_მკგ_RAE': 0,
        'E_ვიტამინი_მგ_ATE': 0,
        'K_ვიტამინი_მკგ': 0,
        'სელენი_მკგ': 0
    }
    
    for item in selected_products:
        # ვპოულობთ პროდუქტს DataFrame-ში
        product_data = df[df['პროდუქტი'] == item['პროდუქტი']]
        
        if not product_data.empty:
            # გამოთვლა 100გ-ზე პროპორციულად
            multiplier = item['რაოდენობა'] / 100.0
            
            for nutrient in total_nutrition.keys():
                total_nutrition[nutrient] += product_data.iloc[0][nutrient] * multiplier
    
    return total_nutrition

def get_recommended_doses(gender):
    """რეკომენდებული დღიური დოზები სქესის მიხედვით"""
    if gender == "მამაკაცი":
        return {
            'რკინა_მგ': 8,
            'B12_მკგ': 2.4,
            'ფოლატი_მკგ': 400,
            'C_ვიტამინი_მგ': 90,
            'D_ვიტამინი_IU': 700,
            'კალციუმი_მგ': 1100,
            'მაგნიუმი_მგ': 410,
            'კალიუმი_მგ': 4000,
            'თუთია_მგ': 11,
            'A_ვიტამინი_მკგ_RAE': 900,
            'E_ვიტამინი_მგ_ATE': 15,
            'K_ვიტამინი_მკგ': 120,
            'სელენი_მკგ': 55
        }
    else:  # ქალი
        return {
            'რკინა_მგ': 18,
            'B12_მკგ': 2.4,
            'ფოლატი_მკგ': 400,
            'C_ვიტამინი_მგ': 75,
            'D_ვიტამინი_IU': 700,
            'კალციუმი_მგ': 1100,
            'მაგნიუმი_მგ': 315,
            'კალიუმი_მგ': 4000,
            'თუთია_მგ': 8,
            'A_ვიტამინი_მკგ_RAE': 700,
            'E_ვიტამინი_მგ_ATE': 15,
            'K_ვიტამინი_მკგ': 90,
            'სელენი_მკგ': 55
        }

def display_nutrition_analysis(total_nutrition, recommended_doses):
    """ვიზუალიზაცია დღიური ნორმის ანალიზისთვის"""
    
    nutrient_names = {
        'რკინა_მგ': '🔶 რკინა',
        'B12_მკგ': '🔷 B12',
        'ფოლატი_მკგ': '🟢 ფოლატი',
        'C_ვიტამინი_მგ': '🟡 C ვიტამინი',
        'D_ვიტამინი_IU': '🟠 D ვიტამინი',
        'კალციუმი_მგ': '⚪ კალციუმი',
        'მაგნიუმი_მგ': '🟣 მაგნიუმი',
        'კალიუმი_მგ': '🔵 კალიუმი',
        'თუთია_მგ': '⚫ თუთია',
        'A_ვიტამინი_მკგ_RAE': '⚪ A ვიტამინი',
        'E_ვიტამინი_მგ_ATE': '🟤 E ვიტამინი',
        'K_ვიტამინი_მკგ': '⚫ K ვიტამინი',
        'სელენი_მკგ': '⚪ სელენი'
    }
    
    # მთავარი ბარათები
    cols_per_row = 4
    num_nutrients = len(nutrient_names)
    num_rows = (num_nutrients + cols_per_row - 1) // cols_per_row
    
    for row_idx in range(num_rows):
        cols = st.columns(cols_per_row)
        for i in range(cols_per_row):
            nutrient_index = row_idx * cols_per_row + i
            if nutrient_index < num_nutrients:
                nutrient_key = list(nutrient_names.keys())[nutrient_index]
                nutrient_display_name = list(nutrient_names.values())[nutrient_index]

                current_amount = total_nutrition[nutrient_key]
                recommended = recommended_doses[nutrient_key]
                percentage = (current_amount / recommended) * 100
                
                with cols[i]:
                    # ფერის განსაზღვრა პროცენტის მიხედვით
                    if percentage < 50:
                        color = "🔴"
                    elif percentage < 100:
                        color = "🟡"
                    else:
                        color = "🟢"
                    
                    unit = get_unit(nutrient_key)
                    
                    st.metric(
                        label=f"{color} {nutrient_display_name}",
                        value=f"{current_amount:.1f} {unit}",
                        delta=f"{percentage:.1f}% ({current_amount - recommended:+.1f} {unit})"
                    )
    
    st.markdown("---")
    
    # დეტალური ანალიზი
    st.subheader("📈 დეტალური ანალიზი:")
    
    # პროგრეს ბარები
    for nutrient, name in nutrient_names.items():
        current_amount = total_nutrition[nutrient]
        recommended = recommended_doses[nutrient]
        percentage = min((current_amount / recommended), 2.0)  # მაქსიმუმ 200%
        
        unit = get_unit(nutrient)
        
        col1_detail, col2_detail, col3_detail = st.columns([2, 3, 2])
        
        with col1_detail:
            st.write(f"**{name}**")
        
        with col2_detail:
            # პროგრეს ბარი
            st.progress(min(percentage, 1.0))
        
        with col3_detail:
            st.write(f"{current_amount:.1f}/{recommended} {unit}")
    
    # რეკომენდაციები
    st.markdown("---")
    st.subheader("💡 რეკომენდაციები:")
    
    recommendations = []
    
    for nutrient, name in nutrient_names.items():
        current_amount = total_nutrition[nutrient]
        recommended = recommended_doses[nutrient]
        percentage = (current_amount / recommended) * 100
        
        if percentage < 50:
            recommendations.append(f"❗ **{name}**: ძალიან დაბალია ({percentage:.1f}%) - მეტი პროდუქტი დაამატეთ")
        elif percentage < 100:
            recommendations.append(f"⚠️ **{name}**: საშუალოზე დაბალია ({percentage:.1f}%) - კიდევ რამდენიმე პროდუქტი დაამატეთ")
        elif percentage > 200:
            recommendations.append(f"⚡ **{name}**: ძალიან მაღალია ({percentage:.1f}%) - შეამცირეთ რაოდენობა")
    
    if not recommendations:
        st.success("🎉 შესანიშნავია! ყველა ნუტრიენტი ნორმალურ ფარგლებშია!")
    else:
        for rec in recommendations:
            st.write(rec)

def search_by_nutrient(df, search_term, min_amount=0):
    """ვიძებთ პროდუქტებს კონკრეტული ნუტრიენტის მიხედვით"""
    # ვიყენებთ გაუმჯობესებულ ფუნქციას
    nutrient_col = find_nutrient_column(search_term)    
    
    if not nutrient_col:
        return pd.DataFrame()
    
    # ვფილტრავთ პროდუქტებს, რომლებიც შეიცავენ ამ ნუტრიენტს მინიმალური რაოდენობის ზემოთ
    if min_amount == 0.0:
        results = df[df[nutrient_col] > 0].copy()
    else:
        results = df[df[nutrient_col] >= min_amount].copy()
    
    # ვალაგებთ მაღალი შემცველობის მიხედვით
    results = results.sort_values(nutrient_col, ascending=False)
    
    return results
# --- სტრიმლიტის აპლიკაცია ---
def main():
    st.set_page_config(page_title="საკვები პროდუქტების ვიტამინ-მინერალური ძიება", layout="wide", """ <style> body { font-size: 8px; } </style> """)
    
    # session state-ის ინიციალიზაცია
    if 'search_term' not in st.session_state:
        st.session_state.search_term = ''
    if 'min_amount' not in st.session_state:
        st.session_state.min_amount = 0.0
    if 'selected_products' not in st.session_state:
        st.session_state.selected_products = []
    # Initialize session state for the multiselect in tab3
    if 'nutrients_multiselect_tab3' not in st.session_state:
        st.session_state.nutrients_multiselect_tab3 = []
    # Initialize session state for generated ration (new for tab4)
    if 'generated_ration' not in st.session_state:
        st.session_state.generated_ration = []

    # CSS სტაილი კომპაქტური ვიუსთვის
    st.markdown("""
    <style>
    .stApp {
        font-size: 14px;
    }
    .element-container {
        margin-bottom: 0.5rem !important;
    }
    .stMarkdown {
        margin-bottom: 0.5rem !important;
    }
    .nutrition-card {
        /* Default for light mode */
        background-color: #f8f9fa; 
        color: #333; /* Darker text for light background */
        padding: 0.5rem;
        border-radius: 0.25rem;
        margin-bottom: 0.5rem;
        border-left: 3px solid #007bff;
    }
    /* Dark mode adjustments */
    @media (prefers-color-scheme: dark) {
        .nutrition-card {
            background-color: #333333; /* Darker background for dark mode */
            color: #f8f9fa; /* Lighter text for dark background */
            border-left: 3px solid #66b3ff; /* A lighter blue for contrast */
        }
        .nutrition-card h4 {
            color: #f8f9fa !important; /* Ensure heading is light */
        }
        .nutrition-value {
            color: #99ccff !important; /* Lighter blue for values */
        }
        /* Adjusting Streamlit's default text color for general elements if needed */
        .stMarkdown, .stText, .stLabel {
            color: #f8f9fa; /* Light text for general markdown/text */
        }
    }

    .nutrition-value {
        font-weight: bold;
        color: #007bff; /* This will be overridden for dark mode by the @media query */
    }
    .dose-button {
        background-color: #e6f7ff;
        color: #007bff;
        border: 1px solid #007bff;
        padding: 0.25rem 0.5rem;
        border-radius: 0.25rem;
        cursor: pointer;
        font-weight: bold;
        display: inline-block;
        margin-right: 0.5rem;
        margin-bottom: 0.5rem;
    }
    .dose-button:hover {
        background-color: #007bff;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.title("🥗 საკვები პროდუქტების ვიტამინ-მინერალური ძიება")
    st.markdown("---")
    
    # დღიური დოზების ინფორმაცია მთავარ გვერდზე
    st.markdown("**📊 დღიური დოზები (ზრდასრული):**")
    
    col1, col2, col3, col4, col5 = st.columns([3, 3, 3, 3, 1]) # დამატებულია სვეტი გასუფთავებისთვის

    with col1:
        st.button("🔶 **რკინა:** 18 მგ (ქალები), 8 მგ (მამაკაცები)", key="dose_iron", use_container_width=True, on_click=set_search_and_min_amount, args=('რკინა', 0.0))
        st.button("🔷 **B12:** 2.4 მკგ", key="dose_b12", use_container_width=True, on_click=set_search_and_min_amount, args=('B12', 0.0))
        st.button("🟢 **ფოლატი:** 400 მკგ", key="dose_folate", use_container_width=True, on_click=set_search_and_min_amount, args=('ფოლატი', 0.0))
    with col2:
        st.button("🟡 **C ვიტამინი:** 90 მგ (მამაკაცები), 75 მგ (ქალები)", key="dose_c", use_container_width=True, on_click=set_search_and_min_amount, args=('C ვიტამინი', 0.0))
        st.button("🟠 **D ვიტამინი:** 600-800 IU", key="dose_d", use_container_width=True, on_click=set_search_and_min_amount, args=('D ვიტამინი', 0.0))
        st.button("⚪ **კალციუმი:** 1000-1200 მგ", key="dose_calcium", use_container_width=True, on_click=set_search_and_min_amount, args=('კალციუმი', 0.0))
    with col3:
        st.button("🟣 **მაგნიუმი:** 400-420 მგ (მამაკაცები), 310-320 მგ (ქალები)", key="dose_magnesium", use_container_width=True, on_click=set_search_and_min_amount, args=('მაგნიუმი', 0.0))
        st.button("🔵 **კალიუმი:** 3500-4700 მგ", key="dose_potassium", use_container_width=True, on_click=set_search_and_min_amount, args=('კალიუმი', 0.0))
        st.button("⚫ **თუთია:** 11 მგ (მამაკაცები), 8 მგ (ქალები)", key="dose_zinc", use_container_width=True, on_click=set_search_and_min_amount, args=('თუთია', 0.0))
    with col4:
        st.button("⚪ **A ვიტამინი:** 700-900 მკგ RAE", key="dose_a", use_container_width=True, on_click=set_search_and_min_amount, args=('A ვიტამინი', 0.0))
        st.button("🟤 **E ვიტამინი:** 15 მგ", key="dose_e", use_container_width=True, on_click=set_search_and_min_amount, args=('E ვიტამინი', 0.0))
        st.button("⚫ **K ვიტამინი:** 90-120 მკგ", key="dose_k", use_container_width=True, on_click=set_search_and_min_amount, args=('K ვიტამინი', 0.0))
        st.button("⚪ **სელენი:** 55 მკგ", key="dose_selenium", use_container_width=True, on_click=set_search_and_min_amount, args=('სელენი', 0.0))
    with col5:
        # გასუფთავების ღილაკი
        st.button("🗑️ გასუფთავება", key="clear_all_search", use_container_width=True, on_click=set_search_and_min_amount, args=('', 0.0))
            
    st.markdown("---")
    
    # ტაბების შექმნა
    tab1, tab2, tab3, tab4 = st.tabs(["🔍 ძიება", "🧮 დღიური ნორმის კალკულატორი", "📈 ნუტრიენტების მონაცემები", "✨ დღიური რაციონის შედგენა"])
    
    with tab1:
        # მხარეს პანელი ფილტრებისთვის
        with st.sidebar:
            st.header("🔍 ძიების პარამეტრები")
            
            # კატეგორიის ფილტრი
            categories = ['ყველა'] + sorted(df['კატეგორია'].unique().tolist())
            selected_category = st.selectbox("კატეგორია:", categories)
            
            # ძიების ტექსტური ველი
            st.session_state.search_term = st.text_input("მოძებნეთ ნუტრიენტი (მაგ. რკინა, ვიტამინი C):", 
                                                         value=st.session_state.search_term, 
                                                         key="main_search_input_text_field") # უნიკალური key
            
            # მინიმალური რაოდენობის ფილტრი
            if st.session_state.search_term:
                st.session_state.min_amount = st.number_input(f"მინიმალური რაოდენობა ({st.session_state.search_term}):", 
                                                               min_value=0.0, 
                                                               value=st.session_state.min_amount, # იყენებს session_state-ის მნიშვნელობას
                                                               step=0.1,
                                                               key="min_amount_input_field") # უნიკალური key
        
        # მთავარი კონტენტი (ძიების ტაბი)
        filtered_df = df.copy()
        
        # კატეგორიის ფილტრი
        if selected_category != 'ყველა':
            filtered_df = filtered_df[filtered_df['კატეგორია'] == selected_category]
        
        # ძიების ფუნქცია
        if st.session_state.search_term:
            search_results = search_by_nutrient(filtered_df, st.session_state.search_term, 
                                                st.session_state.min_amount)
            
            if not search_results.empty:
                st.subheader(f"🎯 ძიების შედეგები: '{st.session_state.search_term}'")
                
                # დღიური დოზის ინფორმაცია
                daily_dose = get_daily_dose(st.session_state.search_term)
                if daily_dose:
                    st.info(f"📊 **დღიური რეკომენდებული დოზა:** {daily_dose}")
                
                # კატეგორიების მიხედვით ჯგუფირება
                categories_found = search_results['კატეგორია'].unique()
                
                for category in sorted(categories_found):
                    with st.expander(f"📂 {category}", expanded=True):
                        category_data = search_results[search_results['კატეგორია'] == category]
                        
                        # ყველაზე მდიდარი პროდუქტების ჩვენება
                        nutrient_col = find_nutrient_column(st.session_state.search_term)
                        if nutrient_col:
                            category_data = category_data.sort_values(nutrient_col, ascending=False)
                            
                            for _, row in category_data.iterrows():
                                col1_display, col2_display = st.columns([3, 1])
                                with col1_display:
                                    st.write(f"**{row['პროდუქტი']}**")
                                with col2_display:
                                    value = row[nutrient_col]
                                    unit = get_unit(nutrient_col)
                                    # თუ მნიშვნელობა 0-ზე მეტია, ვაჩვენებთ, წინააღმდეგ შემთხვევაში - "0"
                                    if value > 0:
                                        st.write(f"`{value} {unit}`")
                                    else:
                                        st.write("`0`")
            else:
                st.warning(f"არ მოიძებნა პროდუქტები '{st.session_state.search_term}'-ით ამ კრიტერიუმებით.")
        
        else:
            # ყველა პროდუქტის ჩვენება კატეგორიების მიხედვით
            st.subheader("📋 ყველა პროდუქტი კატეგორიების მიხედვით")
            
            categories_to_show = filtered_df['კატეგორია'].unique()
            
            for category in sorted(categories_to_show):
                with st.expander(f"📂 {category}", expanded=False):
                    category_data = filtered_df[filtered_df['კატეგორია'] == category]
                    
                    # გრიდის ფორმატში ჩვენება
                    cols_grid = st.columns(2)  # 2 სვეტიანი გრიდი
                    
                    for idx, (_, row) in enumerate(category_data.iterrows()):
                        with cols_grid[idx % 2]:
                            # პროდუქტის ბარათი ყველა ვიტამინ-მინერალით
                            nutrition_info = f"""
                            <div class="nutrition-card">
                                <h4 style="margin: 0 0 0.5rem 0;">{row['პროდუქტი']}</h4>
                                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.25rem; font-size: 12px;">
                                    <div>🔶 რკინა: <span class="nutrition-value">{row['რკინა_მგ']} მგ</span></div>
                                    <div>🔷 B12: <span class="nutrition-value">{row['B12_მკგ']} მკგ</span></div>
                                    <div>🟢 ფოლატი: <span class="nutrition-value">{row['ფოლატი_მკგ']} მკგ</span></div>
                                    <div>🟡 C ვიტ.: <span class="nutrition-value">{row['C_ვიტამინი_მგ']} მგ</span></div>
                                    <div>🟠 D ვიტ.: <span class="nutrition-value">{row['D_ვიტამინი_IU']} IU</span></div>
                                    <div>⚪ კალციუმი: <span class="nutrition-value">{row['კალციუმი_მგ']} მგ</span></div>
                                    <div>🟣 მაგნიუმი: <span class="nutrition-value">{row['მაგნიუმი_მგ']} მგ</span></div>
                                    <div>🔵 კალიუმი: <span class="nutrition-value">{row['კალიუმი_მგ']} მგ</span></div>
                                    <div>⚫ თუთია: <span class="nutrition-value">{row['თუთია_მგ']} მგ</span></div>
                                    <div>⚪ A ვიტ.: <span class="nutrition-value">{row['A_ვიტამინი_მკგ_RAE']} მკგ RAE</span></div>
                                    <div>🟤 E ვიტ.: <span class="nutrition-value">{row['E_ვიტამინი_მგ_ATE']} მგ ATE</span></div>
                                    <div>⚫ K ვიტ.: <span class="nutrition-value">{row['K_ვიტამინი_მკგ']} მკგ</span></div>
                                    <div>⚪ სელენი: <span class="nutrition-value">{row['სელენი_მკგ']} მკგ</span></div>
                                </div>
                            </div>
                            """
                            st.markdown(nutrition_info, unsafe_allow_html=True)
    
    with tab2:
        st.header("🧮 დღიური ნორმის კალკულატორი")
        st.markdown("დაამატეთ პროდუქტები და მათი რაოდენობა (გრამებში), რათა გამოთვალოთ დღიური ნუტრიენტების ჯამური შემცველობა.")
        
        # სქესის არჩევა
        gender = st.radio("აირჩიეთ სქესი:", ["მამაკაცი", "ქალი"], key="gender_tab2") # Add unique key
        
        # პროდუქტის არჩევა
        product_options = df['პროდუქტი'].unique().tolist()
        selected_product_name = st.selectbox("აირჩიეთ პროდუქტი:", product_options, key="product_selector_tab2")
        
        # რაოდენობის შეყვანა
        amount_g = st.number_input("რაოდენობა (გრამებში):", min_value=1.0, value=100.0, step=10.0, key="amount_input_tab2")
        
        # პროდუქტის დამატება სიაში
        if st.button("➕ პროდუქტის დამატება", key="add_product_button_tab2"):
            if selected_product_name and amount_g > 0:
                # შემოწმება დუბლიკატებზე (შეცვლა თუ უკვე არსებობს)
                found = False
                for i, item in enumerate(st.session_state.selected_products):
                    if item['პროდუქტი'] == selected_product_name:
                        st.session_state.selected_products[i]['რაოდენობა'] = amount_g
                        found = True
                        break
                if not found:
                    st.session_state.selected_products.append({'პროდუქტი': selected_product_name, 'რაოდენობა': amount_g})
                st.success(f"'{selected_product_name}' დაემატა/განახლდა {amount_g} გრამით.")
            else:
                st.warning("გთხოვთ აირჩიოთ პროდუქტი და შეიყვანოთ დადებითი რაოდენობა.")
        
        st.markdown("---")
        
        st.subheader("🛒 თქვენი არჩეული პროდუქტები:")
        if st.session_state.selected_products:
            # ცხრილის ჩვენება და რედაქტირება
            
            # გადაყვანა DataFrame-ში დინამიური რედაქტირებისთვის
            selected_df = pd.DataFrame(st.session_state.selected_products)
            
            edited_df = st.data_editor(
                selected_df,
                num_rows="dynamic",
                use_container_width=True,
                column_config={
                    "პროდუქტი": st.column_config.Column(
                        "პროდუქტი",
                        help="პროდუქტის სახელი",
                        disabled=True,
                    ),
                    "რაოდენობა": st.column_config.NumberColumn(
                        "რაოდენობა (გრამებში)",
                        help="პროდუქტის რაოდენობა გრამებში",
                        min_value=1.0,
                        step=10.0,
                        format="%f გ",
                    ),
                },
                key="selected_products_editor"
            )
            
            # განვაახლოთ session state რედაქტირებული DataFrame-დან
            st.session_state.selected_products = edited_df.to_dict('records')
            
            if st.button("❌ სიის გასუფთავება", key="clear_selected_products"):
                st.session_state.selected_products = []
                st.success("პროდუქტების სია გასუფთავებულია.")
                st.rerun() # აუცილებელია ცვლილებების ასახვისთვის
            
            st.markdown("---")
            
            # ნუტრიენტების გაანგარიშება
            total_nutrition = calculate_daily_nutrition(st.session_state.selected_products, df)
            
            if total_nutrition:
                st.subheader("📊 დღიური ნუტრიენტების ანალიზი:")
                recommended_doses = get_recommended_doses(gender)
                display_nutrition_analysis(total_nutrition, recommended_doses)
            else:
                st.info("დაამატეთ პროდუქტები დღიური ნორმის სანახავად.")
        else:
            st.info("პროდუქტები არ არის დამატებული.")
    
    with tab3:
        st.header("📈 ნუტრიენტების სრული მონაცემები")
        st.markdown("იხილეთ ყველა პროდუქტის და ნუტრიენტის დეტალური მონაცემები.")
        
        # ფილტრები
        nutrient_columns = [col for col in df.columns if col not in ['პროდუქტი', 'კატეგორია']]
        selected_nutrients_to_display = st.multiselect(
            "აირჩიეთ ნუტრიენტები საჩვენებლად:",
            options=nutrient_columns,
            default=st.session_state.nutrients_multiselect_tab3, # Default value from session state
            key="nutrients_multiselect_tab3" # Set key for session state
        )
        
        # Category filter for the full data table
        categories_for_table = ['ყველა'] + sorted(df['კატეგორია'].unique().tolist())
        selected_category_for_table = st.selectbox("ფილტრი კატეგორიის მიხედვით:", categories_for_table, key="category_filter_tab3")

        # Clear selected nutrients button
        st.button("🗑️ არჩეული ნუტრიენტების გასუფთავება", on_click=clear_nutrients_multiselect_tab3, key="clear_multiselect_tab3")

        display_columns = ['პროდუქტი', 'კატეგორია'] + selected_nutrients_to_display

        filtered_df_tab3 = df.copy()
        if selected_category_for_table != 'ყველა':
            filtered_df_tab3 = filtered_df_tab3[filtered_df_tab3['კატეგორია'] == selected_category_for_table]

        if not selected_nutrients_to_display:
            st.warning("გთხოვთ აირჩიოთ მინიმუმ ერთი ნუტრიენტი მონაცემების საჩვენებლად.")
        else:
            st.dataframe(filtered_df_tab3[display_columns], use_container_width=True)

    with tab4:
        st.header("✨ დღიური რაციონის შედგენა")
        st.markdown("ამ ფუნქციის გამოყენებით შეგიძლიათ გენერირება დღიური რაციონი თქვენი სქესის მიხედვით, რომელიც დააბალანსებს აუცილებელ ნუტრიენტებს.")
        
        # სქესის არჩევა რაციონის გენერაციისთვის
        ration_gender = st.radio("აირჩიეთ სქესი რაციონის გენერაციისთვის:", ["მამაკაცი", "ქალი"], key="ration_gender_selector")
        
        st.markdown("---")

        if st.button("🛠️ რაციონის გენერაცია", key="generate_ration_button"):
            # Placeholder for ration generation logic
            st.info(f"რაციონის გენერაცია {ration_gender}ისთვის...")
            
            # --- აქ განთავსდება რაციონის გენერაციის ლოგიკა ---
            # ეს არის მხოლოდ მაგალითი, თქვენ უნდა შეიმუშაოთ ალგორითმი,
            # რომელიც შეარჩევს პროდუქტებს და მათ რაოდენობას
            # რეკომენდებული დღიური დოზების მისაღწევად.
            
            # მაგალითად, შეგიძლიათ:
            # 1. მიიღოთ რეკომენდებული დოზები 'ration_gender'-ისთვის.
            # 2. შეიმუშაოთ ალგორითმი, რომელიც შემთხვევით ან ოპტიმიზებულად შეარჩევს პროდუქტებს DataFrame-დან.
            # 3. გამოთვალოთ თითოეული შერჩეული პროდუქტის რაოდენობა, რათა მიაღწიოთ სამიზნე ნუტრიენტებს.
            # 4. შეინახოთ გენერირებული რაციონი `st.session_state.generated_ration`-ში.
            
            # ამ დროისთვის, უბრალოდ ვაჩვენებთ dummy მონაცემებს
            # 실제 რაციონის გენერაციის ფუნქცია უნდა იყოს აქ.
            
            st.session_state.generated_ration = [
                {'პროდუქტი': 'ქათმის მკერდი', 'რაოდენობა': 150},
                {'პროდუქტი': 'ბროკოლი', 'რაოდენობა': 200},
                {'პროდუქტი': 'ორაგული (ველური)', 'რაოდენობა': 100},
                {'პროდუქტი': 'ისპანახი', 'რაოდენობა': 100},
                {'პროდუქტი': 'ნუში', 'რაოდენობა': 30},
                {'პროდუქტი': 'იოგურტი (ბერძნული)', 'რაოდენობა': 150}
            ]
            st.success("🎉 რაციონი წარმატებით გენერირდა!")

        if st.session_state.generated_ration:
            st.subheader("📋 გენერირებული დღიური რაციონი:")
            generated_ration_df = pd.DataFrame(st.session_state.generated_ration)
            st.dataframe(generated_ration_df, use_container_width=True)

            # Display nutrition analysis for the generated ration (reusing existing function)
            total_nutrition_generated = calculate_daily_nutrition(st.session_state.generated_ration, df)
            if total_nutrition_generated:
                st.subheader("📊 გენერირებული რაციონის ნუტრიენტების ანალიზი:")
                recommended_doses_for_ration = get_recommended_doses(ration_gender)
                display_nutrition_analysis(total_nutrition_generated, recommended_doses_for_ration)
            
            if st.button("🗑️ გენერირებული რაციონის გასუფთავება", key="clear_generated_ration"):
                st.session_state.generated_ration = []
                st.success("გენერირებული რაციონი გასუფთავებულია.")
                st.rerun() # Refresh to clear display

        else:
            st.info("დააჭირეთ 'რაციონის გენერაცია' ღილაკს, რათა შექმნათ თქვენი დღიური რაციონი.")

if __name__ == "__main__":
    main()
