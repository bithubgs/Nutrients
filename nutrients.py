import streamlit as st
import pandas as pd

# საკვები პროდუქტების მონაცემები
products_data = {
    'პროდუქტი': [
        'ღვინის ღია ხორცი', 'ღორის ღვიძლი', 'მსხვილფეხა რქოსანი', 'ქათმის ღვიძლი',
        'სალმონი', 'ტუნა', 'სარდინი', 'კრევეტები', 'მიდიები',
        'ისპანახი', 'ბროკოლი', 'ავოკადო', 'სტაფილო', 'ბანანი',
        'კარაქი', 'რძე', 'იოგურტი', 'ყველი', 'კვერცხი',
        'ლობიო', 'ნუში', 'თოვლი', 'კუნჟუთი', 'მზესუმზირის თესლი',
        'ზღვის კალმახი', 'სპირულინა', 'კლორელა', 'რუხი ბრინჯი', 'კვინოა',
        'ღია თევზი', 'მაკრელი', 'კაშტნის სოკო', 'წითელი ხორცი', 'ღორის ხორცი'
    ],
    'კატეგორია': [
        'ხორცი', 'ღვიძლი', 'ღია ხორცი', 'ღვიძლი',
        'თევზი', 'თევზი', 'თევზი', 'ზღვის პროდუქტები', 'ზღვის პროდუქტები',
        'ბოსტნეული', 'ბოსტნეული', 'ხილი', 'ხილი', 'ხილი',
        'რძის პროდუქტები', 'რძის პროდუქტები', 'რძის პროდუქტები', 'რძის პროდუქტები', 'კვერცხი',
        'ბურღულეული', 'კაკალი და თესლი', 'კაკალი და თესლი', 'კაკალი და თესლი', 'კაკალი და თესლი',
        'ზღვის პროდუქტები', 'სუპერფუდი', 'სუპერფუდი', 'მარცვლეული', 'მარცვლეული',
        'თევზი', 'თევზი', 'სოკო', 'ხორცი', 'ხორცი'
    ],
    'რკინა_მგ': [
        3.3, 30.5, 2.6, 13.0,
        0.8, 1.3, 2.9, 1.8, 6.7,
        2.7, 0.7, 0.6, 0.1, 0.3,
        0.2, 0.03, 0.1, 0.4, 1.2,
        6.2, 2.9, 3.7, 14.6, 5.2,
        90.0, 28.5, 58.0, 0.8, 4.6,
        1.0, 1.6, 0.5, 2.9, 0.9
    ],
    'B12_მკგ': [
        2.6, 83.1, 2.4, 16.6,
        4.9, 4.3, 8.9, 1.1, 24.0,
        0.0, 0.0, 0.0, 0.0, 0.0,
        0.2, 0.4, 0.5, 0.8, 0.6,
        0.0, 0.0, 0.0, 0.0, 0.0,
        1.5, 175.0, 65.0, 0.0, 0.0,
        5.4, 19.0, 0.0, 2.1, 0.7
    ],
    'ფოლატი_მკგ': [
        4, 290, 6, 588,
        26, 5, 10, 3, 76,
        194, 63, 81, 3, 20,
        3, 5, 7, 27, 47,
        394, 28, 57, 79, 227,
        180, 94, 23, 8, 184,
        12, 2, 17, 7, 3
    ],
    'C_ვიტამინი_მგ': [
        0, 1, 0, 17,
        0, 0, 0, 2, 8,
        28, 89, 10, 4, 9,
        0, 0, 0, 0, 0,
        2, 1, 8, 0, 1,
        3, 10, 9, 0, 0,
        0, 0, 2, 0, 1
    ],
    'D_ვიტამინი_IU': [
        3, 15, 7, 44,
        360, 154, 164, 5, 76,
        0, 0, 0, 0, 0,
        142, 115, 5, 24, 82,
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        388, 388, 375, 6, 53
    ],
    'კალციუმი_მგ': [
        12, 5, 18, 8,
        12, 4, 382, 70, 26,
        99, 47, 12, 6, 5,
        24, 113, 110, 721, 50,
        113, 37, 160, 975, 78,
        1170, 120, 74, 23, 47,
        20, 12, 3, 7, 5
    ],
    'მაგნიუმი_მგ': [
        20, 18, 20, 19,
        29, 64, 39, 39, 34,
        79, 21, 29, 5, 27,
        2, 10, 11, 28, 10,
        140, 158, 168, 351, 325,
        560, 195, 315, 143, 197,
        27, 97, 9, 17, 16
    ]
}

# DataFrame-ის შექმნა
df = pd.DataFrame(products_data)

# სტრიმლიტის აპლიკაცია
def main():
    st.set_page_config(page_title="საკვები პროდუქტების ვიტამინ-მინერალური ძიება", layout="wide")
    
    st.title("🥗 საკვები პროდუქტების ვიტამინ-მინერალური ძიება")
    st.markdown("---")
    
    # მხარეს პანელი ფილტრებისთვის
    with st.sidebar:
        st.header("🔍 ძიება და ფილტრი")
        
        # კატეგორიის ფილტრი
        categories = ['ყველა'] + sorted(df['კატეგორია'].unique().tolist())
        selected_category = st.selectbox("კატეგორია:", categories)
        
        # საძიებო ველი
        search_term = st.text_input("მოძებნე ვიტამინი/მინერალი:", 
                                   placeholder="მაგ: რკინა, B12, ფოლატი")
        
        # მინიმალური რაოდენობის ფილტრი
        if search_term:
            min_amount = st.number_input(f"მინიმალური რაოდენობა:", 
                                       min_value=0.0, value=0.0, step=0.1)
        
        st.markdown("---")
        st.markdown("**ძიების მაგალითები:**")
        st.markdown("• რკინა")
        st.markdown("• B12")
        st.markdown("• ფოლატი")
        st.markdown("• C ვიტამინი")
        st.markdown("• კალციუმი")
        st.markdown("• მაგნიუმი")
    
    # მთავარი კონტენტი
    filtered_df = df.copy()
    
    # კატეგორიის ფილტრი
    if selected_category != 'ყველა':
        filtered_df = filtered_df[filtered_df['კატეგორია'] == selected_category]
    
    # ძიების ფუნქცია
    if search_term:
        search_results = search_by_nutrient(filtered_df, search_term, 
                                          min_amount if 'min_amount' in locals() else 0)
        
        if not search_results.empty:
            st.subheader(f"🎯 ძიების შედეგები: '{search_term}'")
            
            # კატეგორიების მიხედვით ჯგუფირება
            categories_found = search_results['კატეგორია'].unique()
            
            for category in sorted(categories_found):
                with st.expander(f"📂 {category}", expanded=True):
                    category_data = search_results[search_results['კატეგორია'] == category]
                    
                    # ყველაზე მდიდარი პროდუქტების ჩვენება
                    nutrient_col = find_nutrient_column(search_term)
                    if nutrient_col:
                        category_data = category_data.sort_values(nutrient_col, ascending=False)
                        
                        for _, row in category_data.iterrows():
                            col1, col2 = st.columns([3, 1])
                            with col1:
                                st.write(f"**{row['პროდუქტი']}**")
                            with col2:
                                value = row[nutrient_col]
                                unit = get_unit(nutrient_col)
                                if value > 0:
                                    st.write(f"`{value} {unit}`")
                                else:
                                    st.write("`0`")
        else:
            st.warning(f"არ მოიძებნა პროდუქტები '{search_term}'-ით")
    
    else:
        # ყველა პროდუქტის ჩვენება კატეგორიების მიხედვით
        st.subheader("📋 ყველა პროდუქტი კატეგორიების მიხედვით")
        
        categories_to_show = filtered_df['კატეგორია'].unique()
        
        for category in sorted(categories_to_show):
            with st.expander(f"📂 {category}", expanded=False):
                category_data = filtered_df[filtered_df['კატეგორია'] == category]
                
                for _, row in category_data.iterrows():
                    st.write(f"• **{row['პროდუქტი']}**")
    
    # სტატისტიკა
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("სულ პროდუქტები", len(filtered_df))
    
    with col2:
        st.metric("კატეგორიები", len(filtered_df['კატეგორია'].unique()))
    
    with col3:
        if search_term and 'search_results' in locals():
            st.metric("ძიების შედეგები", len(search_results))

def find_nutrient_column(search_term):
    """ვპოულობთ შესაბამის სვეტს ძიების ტერმინის მიხედვით"""
    search_lower = search_term.lower()
    
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
        'd': 'D_ვიტამინი_IU',
        'ვიტამინი d': 'D_ვიტამინი_IU',
        'vitamin d': 'D_ვიტამინი_IU',
        'კალციუმი': 'კალციუმი_მგ',
        'calcium': 'კალციუმი_მგ',
        'მაგნიუმი': 'მაგნიუმი_მგ',
        'magnesium': 'მაგნიუმი_მგ'
    }
    
    return nutrient_mapping.get(search_lower)

def get_unit(column_name):
    """ვაბრუნებთ შესაბამის ზომის ერთეულს"""
    if 'მგ' in column_name:
        return 'მგ'
    elif 'მკგ' in column_name:
        return 'მკგ'
    elif 'IU' in column_name:
        return 'IU'
    return ''

def search_by_nutrient(df, search_term, min_amount=0):
    """ვიძებთ პროდუქტებს კონკრეტული ნუტრიენტის მიხედვით"""
    nutrient_col = find_nutrient_column(search_term)
    
    if not nutrient_col:
        return pd.DataFrame()
    
    # ვფილტრავთ პროდუქტებს, რომლებიც შეიცავენ ამ ნუტრიენტს მინიმალური რაოდენობის ზემოთ
    results = df[df[nutrient_col] > min_amount].copy()
    
    # ვალაგებთ მაღალი შემცველობის მიხედვით
    results = results.sort_values(nutrient_col, ascending=False)
    
    return results

if __name__ == "__main__":
    main()