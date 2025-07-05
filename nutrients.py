import streamlit as st
import pandas as pd

# ... (Your existing products_data and DataFrame creation remain the same) ...
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
    /* Define CSS variables for colors that adapt to theme */
    :root {
        --primary-text-color: #333;
        --secondary-text-color: #666;
        --card-background-color: #f8f9fa;
        --card-border-color: #007bff;
        --button-background-color: #e6f7ff;
        --button-text-color: #007bff;
        --hover-background-color: #007bff;
        --hover-text-color: white;
    }

    /* Dark mode adjustments using the data-theme attribute */
    [data-theme="dark"] {
        --primary-text-color: #f0f2f6; /* Lighter text for dark mode */
        --secondary-text-color: #bbb;
        --card-background-color: #26272e; /* Darker background for cards */
        --card-border-color: #007bff; /* Keep primary blue border */
        --button-background-color: #31333f; /* Darker button background */
        --button-text-color: #8bb4ff; /* Lighter blue for button text */
        --hover-background-color: #007bff;
        --hover-text-color: white;
    }

    .stApp {
        font-size: 14px;
        color: var(--primary-text-color); /* Use variable for app text color */
    }
    .element-container {
        margin-bottom: 0.5rem !important;
    }
    .stMarkdown {
        margin-bottom: 0.5rem !important;
    }
    .nutrition-card {
        background-color: var(--card-background-color); /* Use variable */
        padding: 0.5rem;
        border-radius: 0.25rem;
        margin-bottom: 0.5rem;
        border-left: 3px solid var(--card-border-color); /* Use variable */
    }
    .nutrition-card h4 {
        color: var(--primary-text-color); /* Use variable */
        margin: 0 0 0.5rem 0;
    }
    .nutrition-value {
        font-weight: bold;
        color: var(--button-text-color); /* Use a more appropriate variable or keep original blue */
    }
    .dose-button {
        background-color: var(--button-background-color); /* Use variable */
        color: var(--button-text-color); /* Use variable */
        border: 1px solid var(--button-text-color); /* Use variable for border */
        padding: 0.25rem 0.5rem;
        border-radius: 0.25rem;
        cursor: pointer;
        font-weight: bold;
        display: inline-block;
        margin-right: 0.5rem;
        margin-bottom: 0.5rem;
    }
    .dose-button:hover {
        background-color: var(--hover-background-color); /* Use variable */
        color: var(--hover-text-color); /* Use variable */
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
    tab1, tab2, tab3 = st.tabs(["🔍 ძიება", "🧮 დღიური ნორმის კალკულატორი", "📈 ნუტრიენტების მონაცემები"])
    
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
                                <h4 style="margin: 0 0 0.5rem 0; color: var(--primary-text-color);">{row['პროდუქტი']}</h4>
                                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.25rem; font-size: 12px; color: var(--secondary-text-color);">
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
        st.write("აქ შეგიძლიათ აირჩიოთ პროდუქტები და მათი რაოდენობა, რათა გამოთვალოთ დღიური ნუტრიენტების ჯამი.")

        # სქესის არჩევა
        gender = st.radio("აირჩიეთ სქესი:", ("მამაკაცი", "ქალი"))
        
        # პროდუქტის დამატება
        product_options = sorted(df['პროდუქტი'].unique().tolist())
        col1_add, col2_add, col3_add = st.columns([4, 2, 1])

        with col1_add:
            selected_product_to_add = st.selectbox("აირჩიეთ პროდუქტი:", product_options, key="select_product_calc")
        with col2_add:
            amount_to_add = st.number_input("რაოდენობა (გრამი):", min_value=1, value=100, step=10, key="amount_calc")
        with col3_add:
            st.markdown("<br>", unsafe_allow_html=True) # Space for alignment
            if st.button("➕ დამატება", key="add_product_calc"):
                if selected_product_to_add:
                    st.session_state.selected_products.append({
                        'პროდუქტი': selected_product_to_add,
                        'რაოდენობა': amount_to_add
                    })
                    st.success(f"დაემატა: {amount_to_add}გ {selected_product_to_add}")
                else:
                    st.warning("გთხოვთ აირჩიოთ პროდუქტი.")
        
        st.markdown("---")
        st.subheader("🛒 თქვენი არჩეული პროდუქტები:")
        
        if st.session_state.selected_products:
            for i, item in enumerate(st.session_state.selected_products):
                col_item, col_remove = st.columns([5, 1])
                with col_item:
                    st.write(f"- **{item['პროდუქტი']}**: {item['რაოდენობა']} გრამი")
                with col_remove:
                    if st.button("❌ წაშლა", key=f"remove_{i}"):
                        st.session_state.selected_products.pop(i)
                        st.experimental_rerun() # Rerun to update the list immediately
            
            st.markdown("---")
            total_nutrition = calculate_daily_nutrition(st.session_state.selected_products, df)
            
            if total_nutrition:
                st.subheader("📊 დღიური ნუტრიენტების ჯამი:")
                recommended_doses = get_recommended_doses(gender)
                display_nutrition_analysis(total_nutrition, recommended_doses)
        else:
            st.info("არჩეული პროდუქტები არ არის.")
        
        if st.session_state.selected_products:
            if st.button("🗑️ ყველა პროდუქტის გასუფთავება", key="clear_all_selected_products_calc"):
                st.session_state.selected_products = []
                st.experimental_rerun()


    with tab3:
        st.header("📈 ნუტრიენტების მონაცემები")
        st.write("აქ შეგიძლიათ დაათვალიეროთ ნუტრიენტების მონაცემები პროდუქტების მიხედვით.")

        # ნუტრიენტების მულტისელექტი
        all_nutrients = [col for col in df.columns if col not in ['პროდუქტი', 'კატეგორია']]
        selected_nutrients_tab3 = st.multiselect(
            "აირჩიეთ ნუტრიენტები საჩვენებლად:",
            all_nutrients,
            default=st.session_state.nutrients_multiselect_tab3,
            key="nutrients_multiselect_tab3"
        )
        
        # გასუფთავების ღილაკი
        st.button("🗑️ არჩეული ნუტრიენტების გასუფთავება", on_click=clear_nutrients_multiselect_tab3)


        if not selected_nutrients_tab3:
            st.info("გთხოვთ აირჩიოთ მინიმუმ ერთი ნუტრიენტი მონაცემების სანახავად.")
        else:
            display_columns = ['პროდუქტი', 'კატეგორია'] + selected_nutrients_tab3
            st.dataframe(df[display_columns].set_index('პროდუქტი'))

# აპლიკაციის გაშვება
if __name__ == "__main__":
    main()
