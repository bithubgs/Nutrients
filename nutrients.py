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

# --- დამხმარე ფუნქციები ---
def find_nutrient_column(search_term):
    """
    პოულობს შესაბამის სვეტს ძიების ტერმინის მიხედვით.
    ეს ფუნქცია გაუმჯობესებულია, რათა უკეთ მოძებნოს ვიტამინები,
    მაშინაც კი, თუ ტერმინი ზუსტად არ ემთხვევა სვეტის სახელს.
    """
    search_lower = search_term.lower()
    
    # სტანდარტული mappings ძიების ტერმინებისთვის
    nutrient_mapping = {
        'რკინა': 'რკინა_მგ',
        'iron': 'რკინა_მგ',
        'b12': 'B12_მკგ',
        'ვიტამინი b12': 'B12_მკგ',
        'ფოლატი': 'ფოლატი_მკგ',
        'folate': 'ფოლატი_მკგ',
        'c': 'C_ვიტამინი_მგ',
        'ვიტამინი c': 'C_ვიტამინი_მგ',
        'vitamin c': 'C_ვიტამინი_მგ',
        'c ვიტამინი': 'C_ვიტამინი_მგ',
        'd': 'D_ვიტამინი_IU',
        'ვიტამინი d': 'D_ვიტამინი_IU',
        'vitamin d': 'D_ვიტამინი_IU',
        'd ვიტამინი': 'D_ვიტამინი_IU',
        'კალციუმი': 'კალციუმი_მგ',
        'calcium': 'კალციუმი_მგ',
        'მაგნიუმი': 'მაგნიუმი_მგ',
        'magnesium': 'მაგნიუმი_მგ',
        'კალიუმი': 'კალიუმი_მგ',
        'potassium': 'კალიუმი_მგ',
        'თუთია': 'თუთია_მგ',
        'zinc': 'თუთია_მგ',
        'a': 'A_ვიტამინი_მკგ_RAE',
        'ვიტამინი a': 'A_ვიტამინი_მკგ_RAE',
        'a ვიტამინი': 'A_ვიტამინი_მკგ_RAE',
        'vitamin a': 'A_ვიტამინი_მკგ_RAE',
        'e': 'E_ვიტამინი_მგ_ATE',
        'ვიტამინი e': 'E_ვიტამინი_მგ_ATE',
        'e ვიტამინი': 'E_ვიტამინი_მგ_ATE',
        'vitamin e': 'E_ვიტამინი_მგ_ATE',
        'k': 'K_ვიტამინი_მკგ',
        'ვიტამინი k': 'K_ვიტამინი_მკგ',
        'k ვიტამინი': 'K_ვიტამინი_მკგ',
        'vitamin k': 'K_ვიტამინი_მკგ',
        'სელენი': 'სელენი_მკგ',
        'selenium': 'სელენი_მკგ'
    }
    
    # 1. ვცდილობთ ზუსტი შესატყვისობა mapping-ში (უმთავრესი)
    if search_lower in nutrient_mapping:
        return nutrient_mapping[search_lower]
        
    # 2. თუ ზუსტი შესატყვისობა არ მოიძებნა, ვეძებთ ნაწილობრივ შესატყვისობას სვეტის სახელში
    # (მაგალითად, "C" მოიძიებს "C_ვიტამინი_მგ"-ს)
    for col in df.columns: # ვამოწმებთ ყველა სვეტს, გარდა 'პროდუქტი' და 'კატეგორია'
        if col not in ['პროდუქტი', 'კატეგორია']:
            if search_lower in col.lower():
                return col
            # დამატებითი ლოგიკა ვიტამინებისთვის:
            # თუ მომხმარებელმა ჩაწერა 'ვიტამინი C' და სვეტი არის 'C_ვიტამინი_მგ'
            # ან თუ ჩაწერა 'C' და სვეტი არის 'C_ვიტამინი_მგ'
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
    st.set_page_config(page_title="საკვები პროდუქტების ვიტამინ-მინერალური ძიება", layout="wide")
    
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
        background-color: #f8f9fa;
        padding: 0.5rem;
        border-radius: 0.25rem;
        margin-bottom: 0.5rem;
        border-left: 3px solid #007bff;
    }
    .nutrition-value {
        font-weight: bold;
        color: #007bff;
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
        if st.button("🔶 **რკინა:** 18 მგ (ქალები), 8 მგ (მამაკაცები)", key="dose_iron", use_container_width=True):
            st.session_state.search_term = 'რკინა'
            st.session_state.min_amount = 0.0
            st.rerun()
        if st.button("🔷 **B12:** 2.4 მკგ", key="dose_b12", use_container_width=True):
            st.session_state.search_term = 'B12'
            st.session_state.min_amount = 0.0
            st.rerun()
        if st.button("🟢 **ფოლატი:** 400 მკგ", key="dose_folate", use_container_width=True):
            st.session_state.search_term = 'ფოლატი'
            st.session_state.min_amount = 0.0
            st.rerun()
    with col2:
        if st.button("🟡 **C ვიტამინი:** 90 მგ (მამაკაცები), 75 მგ (ქალები)", key="dose_c", use_container_width=True):
            st.session_state.search_term = 'C ვიტამინი'
            st.session_state.min_amount = 0.0
            st.rerun()
        if st.button("🟠 **D ვიტამინი:** 600-800 IU", key="dose_d", use_container_width=True):
            st.session_state.search_term = 'D ვიტამინი'
            st.session_state.min_amount = 0.0
            st.rerun()
        if st.button("⚪ **კალციუმი:** 1000-1200 მგ", key="dose_calcium", use_container_width=True):
            st.session_state.search_term = 'კალციუმი'
            st.session_state.min_amount = 0.0
            st.rerun()
    with col3:
        if st.button("🟣 **მაგნიუმი:** 400-420 მგ (მამაკაცები), 310-320 მგ (ქალები)", key="dose_magnesium", use_container_width=True):
            st.session_state.search_term = 'მაგნიუმი'
            st.session_state.min_amount = 0.0
            st.rerun()
        if st.button("🔵 **კალიუმი:** 3500-4700 მგ", key="dose_potassium", use_container_width=True):
            st.session_state.search_term = 'კალიუმი'
            st.session_state.min_amount = 0.0
            st.rerun()
        if st.button("⚫ **თუთია:** 11 მგ (მამაკაცები), 8 მგ (ქალები)", key="dose_zinc", use_container_width=True):
            st.session_state.search_term = 'თუთია'
            st.session_state.min_amount = 0.0
            st.rerun()
    with col4:
        if st.button("⚪ **A ვიტამინი:** 700-900 მკგ RAE", key="dose_a", use_container_width=True):
            st.session_state.search_term = 'A ვიტამინი'
            st.session_state.min_amount = 0.0
            st.rerun()
        if st.button("🟤 **E ვიტამინი:** 15 მგ", key="dose_e", use_container_width=True):
            st.session_state.search_term = 'E ვიტამინი'
            st.session_state.min_amount = 0.0
            st.rerun()
        if st.button("⚫ **K ვიტამინი:** 90-120 მკგ", key="dose_k", use_container_width=True):
            st.session_state.search_term = 'K ვიტამინი'
            st.session_state.min_amount = 0.0
            st.rerun()
        if st.button("⚪ **სელენი:** 55 მკგ", key="dose_selenium", use_container_width=True):
            st.session_state.search_term = 'სელენი'
            st.session_state.min_amount = 0.0
            st.rerun()
    with col5:
        # გასუფთავების ღილაკი
        if st.button("🗑️ გასუფთავება", key="clear_all_search", use_container_width=True):
            st.session_state.search_term = ''
            st.session_state.min_amount = 0.0
            st.rerun()
            
    st.markdown("---")
    
    # ტაბების შექმნა
    tab1, tab2, tab3 = st.tabs(["🔍 ძიება", "🧮 დღიური ნორმის კალკულატორი", "📈 ნუტრიენტების მონაცემები"])
    
    with tab1:
        # მხარეს პანელი ფილტრებისთვის
        with st.sidebar:
            st.header("🔍 ძიების პარამეტრები")
            
            # კატეგორიის ფილტრი
            categories = ['ყველა'] + sorted(df['კატეგორია'].unique().tolist())
            selected_category = st.selectbox("კატეგორია:", categories)
            
            # მინიმალური რაოდენობის ფილტრი
            # ეს ინფუთი მხოლოდ მაშინ გამოჩნდება, თუ რამეა საძიებო ველში
            if st.session_state.search_term:
                st.session_state.min_amount = st.number_input(f"მინიმალური რაოდენობა ({st.session_state.search_term}):", 
                                                              min_value=0.0, 
                                                              value=st.session_state.get('min_amount', 0.0), 
                                                              step=0.1)
        
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
                                <h4 style="margin: 0 0 0.5rem 0; color: #333;">{row['პროდუქტი']}</h4>
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
        # დღიური ნორმის კალკულატორი
        st.subheader("🧮 დღიური ნორმის კალკულატორი")
        st.write("აირჩიეთ პროდუქტები და მიუთითეთ რაოდენობა (გრამებში), თქვენი დღიური ნორმა გამოითვლება:")
        
        # ახალი პროდუქტის დამატება
        col1_calc, col2_calc, col3_calc = st.columns([3, 2, 1])
        
        with col1_calc:
            product_to_add = st.selectbox("აირჩიეთ პროდუქტი:", 
                                         options=[''] + sorted(df['პროდუქტი'].tolist()),
                                         key="product_selector")
        
        with col2_calc:
            if product_to_add:
                amount = st.number_input("რაოდენობა (გრამი):", 
                                         min_value=0.0, value=100.0, step=10.0,
                                         key="amount_input")
        
        with col3_calc:
            if product_to_add and st.button("➕ დამატება"):
                st.session_state.selected_products.append({
                    'პროდუქტი': product_to_add,
                    'რაოდენობა': amount
                })
                st.rerun()
        
        # არჩეული პროდუქტების ჩვენება
        if st.session_state.selected_products:
            st.subheader("📝 არჩეული პროდუქტები:")
            
            # პროდუქტების სია
            for i, item in enumerate(st.session_state.selected_products):
                col1_item, col2_item, col3_item = st.columns([3, 2, 1])
                
                with col1_item:
                    st.write(f"**{item['პროდუქტი']}**")
                
                with col2_item:
                    # რაოდენობის რედაქტირება
                    new_amount = st.number_input(f"რაოდენობა (გ):", 
                                                 value=item['რაოდენობა'],
                                                 min_value=0.0, step=10.0,
                                                 key=f"edit_amount_{i}")
                    if new_amount != item['რაოდენობა']:
                        st.session_state.selected_products[i]['რაოდენობა'] = new_amount
                        st.rerun()
                
                with col3_item:
                    if st.button("🗑️", key=f"remove_{i}"):
                        st.session_state.selected_products.pop(i)
                        st.rerun()
            
            # ყველა პროდუქტის გასუფთავება
            if st.button("🗑️ ყველას გასუფთავება", key="clear_all_selected_products"):
                st.session_state.selected_products = []
                st.rerun()
            
            # დღიური ნორმის გამოთვლა
            st.markdown("---")
            st.subheader("📊 დღიური ნორმის ანალიზი:")
            
            # გამოთვლა
            total_nutrition = calculate_daily_nutrition(st.session_state.selected_products, df)
            
            if total_nutrition:
                # სქესის არჩევა უკეთესი გამოთვლისთვის
                gender = st.radio("სქესი:", ["მამაკაცი", "ქალი"], horizontal=True)
                
                # რეკომენდებული დოზების მიღება
                recommended_doses = get_recommended_doses(gender)
                
                # ვიზუალიზაცია
                display_nutrition_analysis(total_nutrition, recommended_doses)

    with tab3:
        st.subheader("📊 ნუტრიენტების მონაცემები პროდუქტების მიხედვით")
        st.write("აირჩიეთ მინერალები და ვიტამინები, რათა ნახოთ რომელი პროდუქტები შეიცავს მათ დიდი რაოდენობით.")

        # ნუტრიენტების მრავალჯერადი არჩევა
        all_nutrients = [col for col in df.columns if col not in ['პროდუქტი', 'კატეგორია']]
        # Use the value from session_state for multiselect
        selected_nutrients_tab3 = st.multiselect("აირჩიეთ ნუტრიენტები:", all_nutrients, 
                                                 default=st.session_state.nutrients_multiselect_tab3, 
                                                 key="nutrients_multiselect_tab3")

        # გასუფთავების ღილაკი
        # გამოიყენეთ on_click callback ფუნქცია
        st.button("🗑️ არჩევის გასუფთავება", key="clear_selected_nutrients_tab3", on_click=clear_nutrients_multiselect_tab3)

        if selected_nutrients_tab3:
            st.markdown("---")
            st.subheader("📝 შერჩეული ნუტრიენტების შემცველი პროდუქტები")

            # შექმენით დროებითი DataFrame მხოლოდ შერჩეული ნუტრიენტებით
            display_cols = ['პროდუქტი', 'კატეგორია'] + selected_nutrients_tab3
            display_df = df[display_cols].copy()

            # კატეგორიების მიხედვით დაჯგუფება და ჩვენება
            for category in sorted(display_df['კატეგორია'].unique()):
                with st.expander(f"📂 {category}", expanded=True):
                    category_data = display_df[display_df['კატეგორია'] == category]
                    
                    # დალაგება თითოეული ნუტრიენტის მიხედვით (შეგიძლიათ შეცვალოთ ლოგიკა)
                    # მაგალითად, დაალაგოთ პირველი შერჩეული ნუტრიენტის მიხედვით
                    if selected_nutrients_tab3:
                        sort_nutrient = selected_nutrients_tab3[0]
                        category_data = category_data.sort_values(sort_nutrient, ascending=False)
                    
                    # ცხრილის ჩვენება hide_index-ით
                    st.dataframe(category_data, use_container_width=True, hide_index=True)


    # სტატისტიკა
    st.markdown("---")
    col1_stats, col2_stats, col3_stats = st.columns(3)
    
    with col1_stats:
        if 'filtered_df' in locals():
            st.metric("სულ პროდუქტები", len(filtered_df))
        else:
            st.metric("სულ პროდუქტები", len(df))
    
    with col2_stats:
        if 'filtered_df' in locals():
            st.metric("კატეგორიები", len(filtered_df['კატეგორია'].unique()))
        else:
            st.metric("კატეგორიები", len(df['კატეგორია'].unique()))
    
    with col3_stats:
        if 'search_results' in locals() and not search_results.empty:
            st.metric("ძიების შედეგები", len(search_results))
        else:
            st.metric("ძიების შედეგები", 0)

if __name__ == "__main__":
    main()