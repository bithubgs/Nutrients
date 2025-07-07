import streamlit as st
import pandas as pd
import random
from pulp import *

# საკვები პროდუქტების მონაცემები (გაფართოებული კალორიულობით და მეტი პროდუქტით)
products_data = {
    'პროდუქტი': [
        'საქონლის ხორცი (მჭლე)', 'ღორის ღვიძლი', 'ქათმის მკერდი', 'ქათმის ღვიძლი', 'ინდაურის ხორცი', 'ცხვრის ხორცი', 'ხბოს ხორცი',
        'ორაგული (ველური)', 'თინუსი (დაკონსერვებული, წყალში)', 'სარდინი (ზეთში, ძვლებით)', 'კრევეტები', 'მიდიები', 'ზღვის კალმახი', 'ვირთევზა', 'სკუმბრია',
        'ისპანახი', 'ბროკოლი', 'სტაფილო', 'ტკბილი კარტოფილი', 'კომბოსტო', 'წითელი ბულგარული წიწაკა', 'წითელი კომბოსტო', 'კალე', 'ბრიუსელის კომბოსტო', 'პორტობელო სოკო', 'ბარდა', 'კამა', 'ოხრახუში', 'ნიორი', 'ჯანჯაფილი', 'მწვანე ლობიო',
        'ავოკადო', 'ბანანი', 'ფორთოხალი', 'კივი', 'მარწყვი', 'მოცვი', 'ვაშლი', 'ლიმონი', 'გრეიპფრუტი', 'ხმელი გარგარი',
        'კარაქი', 'რძე (მთლიანი)', 'იოგურტი (ბერძნული)', 'ყველი (ჩედარი)', 'კვერცხი', 'ხაჭო', 'ძროხის რძე (D ვიტამინით გამდიდრებული)',
        'შავი ლობიო', 'ოსპი', 'წიწიბურა', 'ყავისფერი ბრინჯი', 'კინოა', 'შვრია', 'თეთრი ლობიო',
        'ნუში', 'ნიგოზი', 'ჩიას თესლი', 'მზესუმზირის თესლი', 'გოგრის თესლი', 'კეშიუ', 'ფისტა', 'ბრაზილიური კაკალი', 'ფიჭვის კაკალი',
        'სპირულინა', 'ქლორელა', 'სოიოს რძე (გამაგრებული)', 'ტოფუ', 'შავი შოკოლადი (70%+ კაკაო)', 'საფუარის ექსტრაქტი', 'ქატო', 'მიწისთხილის კარაქი', 'ქოქოსის რძე', 'თევზის ქონი (კოდის)', 'შამპინიონი (D ვიტამინით გამდიდრებული)',
        # ახალი პროდუქტები და კატეგორიები
        'მთლიანი ხორბლის პური', 'შვრიის ფანტელი', 'ყავისფერი ბრინჯის მაკარონი', 'ტკბილი სიმინდი',
        'ზეითუნის ზეთი', 'ქოქოსის ზეთი', 'სელის თესლის ზეთი',
        'ქათმის ბარკალი', 'საქონლის ღვიძლი', 'ინდაურის ღვიძლი',
        'კვერცხის გული', 'კვერცხის ცილა',
        'წითელი ოსპი', 'წიწილა (Chickpeas)',
        'ბროკოლი (მოხარშული)', 'სოკო (თეთრი)', 'პომიდორი', 'კიტრი', 'ბადრიჯანი',
        'მაყვალი', 'ჟოლო', 'ატამი', 'ქლიავი', 'ალუბალი',
        'ფეტვი', 'ქერი', 'ამარანტი',
        'მდოგვის მწვანილი', 'ტურნიპის მწვანილი', 'რუკოლა',
        'რძე (ნახევრად უცხიმო)', 'რიკოტა ყველი', 'პარმეზანი', 'თხის ყველი'
    ],
    'კატეგორია': [
        'ხორცი', 'ღვიძლი', 'ხორცი', 'ღვიძლი', 'ხორცი', 'ხორცი', 'ხორცი',
        'თევზი', 'თევზი', 'თევზი', 'ზღვის პროდუქტები', 'ზღვის პროდუქტები', 'თევზი', 'თევზი', 'თევზი',
        'ბოსტნეული', 'ბოსტნეული', 'ბოსტნეული', 'ბოსტნეული', 'ბოსტნეული', 'ბოსტნეული', 'ბოსტნეული', 'ბოსტნეული', 'ბოსტნეული', 'სოკო', 'პარკოსნები', 'ბოსტნეული', 'ბოსტნეული', 'ბოსტნეული', 'ბოსტნეული', 'პარკოსნები',
        'ხილი', 'ხილი', 'ხილი', 'ხილი', 'ხილი', 'ხილი', 'ხილი', 'ხილი', 'ხილი', 'ხილი',
        'რძის პროდუქტები', 'რძის პროდუქტები', 'რძის პროდუქტები', 'რძის პროდუქტები', 'კვერცხი', 'რძის პროდუქტები', 'რძის პროდუქტები',
        'პარკოსნები', 'პარკოსნები', 'მარცვლეული', 'მარცვლეული', 'მარცვლეული', 'მარცვლეული', 'პარკოსნები',
        'კაკალი და თესლი', 'კაკალი და თესლი', 'კაკალი და თესლი', 'კაკალი და თესლი', 'კაკალი და თესლი', 'კაკალი და თესლი', 'კაკალი და თესლი', 'კაკალი და თესლი', 'კაკალი და თესლი',
        'სუპერფუდი', 'სუპერფუდი', 'მცენარეული რძე', 'სოიოს პროდუქტები', 'საკონდიტრო ნაწარმი', 'სუპერფუდი', 'მარცვლეული', 'პარკოსნები', 'მცენარეული რძე', 'თევზის პროდუქტები', 'სოკო',
        # ახალი კატეგორიები
        'პური და მარცვლეული', 'პური და მარცვლეული', 'პური და მარცვლეული', 'ბოსტნეული',
        'ცხიმები და ზეთები', 'ცხიმები და ზეთები', 'ცხიმები და ზეთები',
        'ხორცი', 'ღვიძლი', 'ღვიძლი',
        'კვერცხი', 'კვერცხი',
        'წითელი ოსპი', 'წიწილა (Chickpeas)',
        'ბროკოლი (მოხარშული)', 'სოკო (თეთრი)', 'პომიდორი', 'კიტრი', 'ბადრიჯანი',
        'მაყვალი', 'ჟოლო', 'ატამი', 'ქლიავი', 'ალუბალი',
        'ფეტვი', 'ქერი', 'ამარანტი',
        'მდოგვის მწვანილი', 'ტურნიპის მწვანილი', 'რუკოლა',
        'რძე (ნახევრად უცხიმო)', 'რიკოტა ყველი', 'პარმეზანი', 'თხის ყველი'
    ],
    'კალორიები_კკალ': [ # Calories per 100g
        131, 135, 165, 135, 104, 294, 137, # Meat
        208, 116, 208, 85, 86, 200, 82, 205, # Fish/Seafood
        23, 34, 41, 86, 25, 31, 31, 49, 43, 22, 81, 43, 36, 149, 80, 31, # Vegetables
        160, 89, 47, 61, 32, 57, 52, 29, 42, 241, # Fruits
        717, 61, 59, 404, 155, 103, 64, # Dairy/Eggs
        347, 116, 343, 111, 378, 389, 116, # Legumes/Grains
        579, 654, 486, 584, 574, 553, 567, 659, 629, # Nuts/Seeds
        290, 420, 54, 76, 598, 200, 275, 590, 354, 900, 22, # Superfoods/Misc
        # New products calories (approximate values)
        265, 389, 158, 86, # Bread/Grains
        884, 862, 884, # Fats/Oils
        210, 140, 110, # More Meat/Liver
        160, 50, # Eggs parts
        116, 164, # More legumes
        35, 28, 18, 16, 25, # More vegetables
        50, 52, 49, 46, 50, # More fruits
        378, 322, 371, # More grains
        30, 32, 25, # More greens
        47, 300, 390, 320 # More dairy
    ],
    'რკინა_მგ': [
        3.3, 30.5, 0.9, 13.0, 2.5, 2.1, 3.5,
        0.8, 1.3, 2.9, 1.8, 6.7, 90.0, 1.0, 1.6,
        2.7, 0.7, 0.3, 0.7, 0.5, 0.5, 0.5, 1.5, 0.5, 0.5, 1.5, 1.0, 2.0, 1.7, 0.6, 1.0,
        0.6, 0.3, 0.1, 0.3, 0.3, 0.2, 0.2, 0.2, 0.2, 1.5,
        0.2, 0.03, 0.1, 0.4, 1.2, 0.4, 0.1,
        6.2, 7.5, 2.2, 0.8, 4.6, 4.0, 6.0,
        2.9, 2.7, 7.7, 5.2, 3.3, 4.0, 3.9, 2.5, 5.0,
        28.5, 58.0, 0.5, 2.0, 3.0, 1.5, 10.0, 1.5, 0.5, 0.1, 0.2,
        # New products
        2.5, 3.0, 1.5, 0.5,
        0.1, 0.1, 0.1,
        2.8, 7.0, 3.0,
        1.5, 0.0,
        2.0, 2.5,
        0.7, 0.5, 0.3, 0.2, 0.2,
        0.2, 0.2, 0.2, 0.1, 0.1,
        2.0, 1.5, 2.5,
        1.0, 1.2, 0.8,
        0.05, 0.1, 0.2, 0.1
    ],
    'B12_მკგ': [
        2.6, 83.1, 0.3, 16.6, 0.4, 2.1, 3.0,
        4.9, 4.3, 8.9, 1.1, 24.0, 1.5, 5.4, 19.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        0.2, 0.4, 0.5, 0.8, 0.6, 0.4, 1.2,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        175.0, 65.0, 2.4, 0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 100.0, 0.0,
        # New products
        0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0,
        1.5, 50.0, 15.0,
        0.8, 0.0,
        0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0,
        0.0, 0.0, 0.0,
        0.4, 0.0, 0.0, 0.0
    ],
    'ფოლატი_მკგ': [
        4, 290, 3, 588, 4, 7, 5,
        26, 5, 10, 3, 76, 180, 12, 2,
        194, 63, 3, 40, 107, 24, 30, 140, 60, 17, 30, 150, 170, 15, 10, 33,
        81, 20, 30, 25, 20, 6, 3, 30, 20, 200,
        3, 5, 7, 27, 47, 24, 5,
        394, 181, 30, 8, 184, 56, 200,
        28, 45, 49, 227, 15, 60, 70, 10, 80,
        94, 23, 50, 29, 30, 50, 160, 60, 15, 0, 17,
        # New products
        40, 56, 10, 50,
        0, 0, 0,
        5, 300, 60,
        40, 0,
        180, 168,
        60, 20, 20, 15, 10,
        10, 15, 10, 8, 10,
        30, 20, 40,
        180, 200, 120,
        7, 10, 5, 10
    ],
    'C_ვიტამინი_მგ': [
        0, 1, 0, 17, 0, 0, 0,
        0, 0, 0, 2, 8, 3, 0, 0,
        28, 89, 6, 20, 36, 128, 60, 120, 110, 2, 10, 85, 133, 5, 5, 5,
        10, 9, 53, 93, 59, 10, 4, 53, 40, 1,
        0, 0, 0, 0, 0, 0, 1,
        2, 5, 0, 0, 0, 0, 0,
        1, 1, 0, 1, 0, 0, 0, 0, 0,
        10, 9, 0, 0, 0, 0, 0, 0, 0, 0, 2,
        # New products
        0, 0, 0, 10,
        0, 0, 0,
        0, 1, 15,
        0, 0,
        2, 2,
        90, 5, 13, 7, 2,
        5, 5, 5, 4, 10,
        0, 0, 0,
        30, 20, 10,
        0, 0, 0, 0
    ],
    'D_ვიტამინი_IU': [
        3, 15, 0, 44, 6, 53, 7,
        360, 154, 164, 5, 76, 0, 388, 388,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 375, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        142, 115, 5, 24, 82, 0, 100,
        0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 100, 0, 0, 0, 0, 0, 0, 1360, 1000,
        # New products
        0, 0, 0, 0,
        0, 0, 0,
        10, 20, 5,
        40, 0,
        0, 0,
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        0, 0, 0,
        100, 0, 0, 0,
        0, 0, 0 # Added one more zero to match length 109
    ],
    'კალციუმი_მგ': [
        12, 5, 8, 8, 10, 7, 12,
        12, 4, 382, 70, 26, 1170, 20, 12,
        99, 47, 6, 30, 40, 10, 40, 150, 60, 3, 30, 200, 170, 20, 10, 50,
        12, 5, 40, 34, 13, 8, 7, 30, 20, 5,
        24, 113, 110, 721, 50, 83, 120,
        113, 35, 20, 23, 47, 52, 150,
        37, 28, 177, 78, 50, 60, 100, 160, 10,
        120, 74, 300, 350, 100, 20, 200, 20, 10, 10, 5,
        # New products
        30, 40, 10, 10,
        0, 0, 0,
        15, 8, 10,
        50, 5,
        120, 100,
        50, 10, 10, 8, 10,
        20, 25, 20, 15, 20,
        30, 20, 40,
        200, 180, 150,
        110, 800, 1000, 300
    ],
    'მაგნიუმი_მგ': [
        20, 18, 29, 19, 25, 17, 25,
        29, 64, 39, 39, 34, 560, 27, 97,
        79, 21, 12, 25, 12, 10, 15, 30, 20, 9, 40, 50, 30, 25, 18, 20,
        29, 27, 10, 15, 10, 12, 5, 10, 12, 150,
        2, 10, 11, 28, 10, 8, 12,
        140, 36, 112, 143, 197, 138, 150,
        158, 183, 335, 325, 262, 292, 121, 197, 251,
        195, 315, 25, 50, 100, 15, 50, 150, 15, 5, 10,
        # New products
        40, 50, 20, 25,
        0, 0, 0,
        30, 20, 15,
        10, 0,
        30, 25,
        25, 15, 10, 8, 12,
        15, 18, 12, 10, 15,
        40, 35, 50,
        80, 90, 70,
        10, 10, 15, 18
    ],
    'კალიუმი_მგ': [
        350, 320, 300, 290, 300, 320, 380,
        363, 290, 397, 259, 290, 990, 290, 360,
        558, 316, 300, 337, 250, 211, 250, 350, 280, 260, 450, 500, 450, 400, 415, 200,
        487, 358, 180, 200, 150, 150, 100, 100, 150, 600,
        24, 150, 170, 90, 138, 150, 150,
        644, 900, 380, 220, 170, 429, 600,
        705, 440, 407, 894, 500, 600, 700, 600, 700,
        800, 700, 150, 120, 100, 50, 250, 350, 150, 0, 200,
        # New products
        150, 200, 100, 270,
        0, 0, 0,
        320, 280, 250,
        130, 0,
        600, 500,
        300, 250, 200, 180, 150,
        160, 180, 190, 170, 180,
        300, 280, 320,
        350, 380, 300,
        150, 120, 100, 160
    ],
    'თუთია_მგ': [
        4.0, 7.0, 0.4, 2.7, 2.0, 2.5, 4.5,
        0.6, 0.8, 1.3, 0.6, 1.3, 4.0, 0.5, 1.2,
        0.1, 0.2, 0.1, 0.2, 0.2, 0.1, 0.1, 0.2, 0.2, 0.5, 0.5, 0.5, 0.5, 0.3, 0.3, 0.3,
        0.4, 0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.5,
        0.1, 0.4, 0.5, 3.0, 1.1, 0.5, 0.4,
        3.0, 1.3, 1.3, 0.8, 2.0, 2.0, 2.0,
        0.9, 0.9, 3.5, 5.0, 2.0, 1.5, 1.5, 2.0, 1.0,
        0.7, 0.5, 0.8, 0.8, 1.0, 0.5, 2.0, 0.5, 0.1, 0.1, 0.5,
        # New products
        0.8, 1.0, 0.5, 0.4,
        0.0, 0.0, 0.0,
        1.5, 3.0, 1.0,
        1.0, 0.0,
        1.0, 1.2,
        0.2, 0.1, 0.1, 0.1, 0.1,
        0.1, 0.1, 0.1, 0.1, 0.1,
        1.5, 1.0, 1.8,
        0.5, 0.6, 0.4,
        0.5, 1.0, 1.5, 0.8
    ],
    'A_ვიტამინი_მკგ_RAE': [
        1, 1000, 10, 800, 5, 5, 10,
        20, 20, 10, 10, 10, 5, 10, 30,
        469, 31, 835, 709, 5, 47, 50, 500, 250, 0, 10, 50, 100, 10, 0, 10,
        7, 3, 22, 23, 30, 10, 5, 10, 15, 0,
        100, 50, 10, 100, 50, 20, 60,
        1, 1, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        300, 200, 50, 0, 0, 0, 0, 0, 0, 5, 0,
        # New products
        0, 0, 0, 30,
        0, 0, 0,
        10, 800, 200,
        200, 0,
        1, 5,
        40, 10, 5, 3, 20,
        10, 12, 8, 5, 7,
        0, 0, 0,
        600, 700, 300,
        80, 50, 100, 60
    ],
    'E_ვიტამინი_მგ_ATE': [
        0.5, 0.5, 0.2, 0.3, 0.1, 0.1, 0.2,
        0.8, 0.2, 0.2, 0.1, 0.1, 0.1, 0.1, 0.5,
        0.3, 0.8, 0.7, 0.3, 0.1, 1.6, 0.2, 0.5, 0.3, 0.1, 0.2, 0.5, 0.2, 0.1, 0.1, 0.1,
        2.1, 0.4, 0.2, 0.1, 0.4, 0.2, 0.1, 0.1, 0.2, 0.0,
        0.8, 0.1, 0.1, 0.1, 0.5, 0.1, 0.1,
        0.0, 0.1, 0.1, 0.0, 0.0, 0.1, 0.0,
        7.7, 2.7, 0.5, 35.0, 0.1, 2.0, 2.9, 0.5, 1.0,
        0.1, 0.1, 0.1, 0.0, 0.5, 0.0, 0.5, 0.0, 0.1, 0.1, 0.1,
        # New products
        0.1, 0.5, 0.2, 0.1,
        14.0, 8.0, 20.0,
        0.5, 0.8, 0.3,
        0.5, 0.0,
        0.1, 0.2,
        0.8, 0.5, 0.3, 0.2, 0.1,
        0.2, 0.2, 0.2, 0.1, 0.2,
        0.1, 0.1, 0.1,
        0.5, 0.6, 0.4,
        0.1, 0.1, 0.1, 0.1
    ],
    'K_ვიტამინი_მკგ': [
        1, 3, 0, 5, 0, 0, 0,
        5, 0, 0, 0, 0, 0, 0, 0,
        483, 102, 19, 21, 109, 14, 80, 681, 177, 0, 3, 160, 200, 0, 0, 0,
        21, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        7, 0, 0, 0, 0, 0, 0,
        4, 4, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        # New products
        0, 0, 0, 10,
        0, 0, 0,
        1, 2, 8,
        0, 0,
        5, 4,
        100, 15, 8, 5, 10,
        0, 0, 0, 0, 0,
        0, 0, 0,
        250, 300, 180,
        0, 0, 0, 0
    ],
    'სელენი_მკგ': [
        35, 50, 20, 50, 20, 25, 40,
        40, 90, 55, 30, 20, 150, 100, 80,
        1, 1, 0.2, 0.6, 0.3, 0.1, 0.3, 0.5, 0.4, 0.5, 0.5, 1, 1, 0.6, 0.2, 1,
        0.4, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 1,
        1, 2, 2, 10, 15, 2, 5,
        0.6, 0.6, 0.3, 10, 5, 10, 1,
        0.2, 0.1, 0.4, 0.4, 10, 1, 10, 544, 1,
        4, 2, 10, 10, 5, 20, 50, 5, 1, 80, 5,
        # New products
        5, 6, 3, 0.5,
        0, 0, 0,
        25, 30, 10,
        15, 0,
        0.5, 1.0,
        0.8, 0.5, 0.3, 0.2, 0.1,
        0.1, 0.1, 0.1, 0.1, 0.1,
        1.5, 1.0, 2.0,
        20, 25, 15,
        2, 1, 3, 1
    ]
}

# Verify all lists in products_data have the same length before creating DataFrame
first_key = list(products_data.keys())[0]
expected_length = len(products_data[first_key])
for key, value in products_data.items():
    if len(value) != expected_length:
        st.error(f"Error: List '{key}' has length {len(value)}, but expected {expected_length}. Please check your data for consistency.")
        st.stop() # Stop the app execution if there's an inconsistency

# DataFrame-ის შექმნა
df = pd.DataFrame(products_data)

# Callback ფუნქცია გასუფთავებისთვის
def clear_nutrients_multiselect_tab4():
    st.session_state.nutrients_multiselect_tab4 = []

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
    
    nutrient_mapping = {
        'რკინა': 'რკინა_მგ', 'iron': 'რკინა_მგ', 'fe': 'რკინა_მგ',
        'b12': 'B12_მკგ', 'ვიტამინი b12': 'B12_მკგ', 'vitamin b12': 'B12_მკგ', 'კობალამინი': 'B12_მკგ',
        'ფოლატი': 'ფოლატი_მკგ', 'folate': 'ფოლატი_მკგ', 'ფოლიუმის მჟავა': 'ფოლატი_მკგ',
        'c': 'C_ვიტამინი_მგ', 'ვიტამინი c': 'C_ვიტამინი_მგ', 'vitamin c': 'C_ვიტამინი_მგ', 'c ვიტამინი': 'C_ვიტამინი_მგ', 'ასკორბინის მჟავა': 'C_ვიტამინი_მგ',
        'd': 'D_ვიტამინი_IU', 'ვიტამინი d': 'D_ვიტამინი_IU', 'vitamin d': 'D_ვიტამინი_IU', 'd ვიტამინი': 'D_ვიტამინი_IU', 'კალციფეროლი': 'D_ვიტამინი_IU',
        'კალციუმი': 'კალციუმი_მგ', 'calcium': 'კალციუმი_მგ', 'ca': 'კალციუმი_მგ',
        'მაგნიუმი': 'მაგნიუმი_მგ', 'magnesium': 'მაგნიუმი_მგ', 'mg': 'მაგნიუმი_მგ',
        'კალიუმი': 'კალიუმი_მგ', 'potassium': 'კალიუმი_მგ', 'k (კალიუმი)': 'კალიუმი_მგ',
        'თუთია': 'თუთია_მგ', 'zinc': 'თუთია_მგ', 'zn': 'თუთია_მგ',
        'a': 'A_ვიტამინი_მკგ_RAE', 'ვიტამინი a': 'A_ვიტამინი_მკგ_RAE', 'a ვიტამინი': 'A_ვიტამინი_მკგ_RAE', 'vitamin a': 'A_ვიტამინი_მკგ_RAE', 'რეტინოლი': 'A_ვიტამინი_მკგ_RAE',
        'e': 'E_ვიტამინი_მგ_ATE', 'ვიტამინი e': 'E_ვიტამინი_მგ_ATE', 'e ვიტამინი': 'E_ვიტამინი_მგ_ATE', 'vitamin e': 'E_ვიტამინი_მგ_ATE', 'ტოკოფეროლი': 'E_ვიტამინი_მგ_ATE',
        'k': 'K_ვიტამინი_მკგ', 'ვიტამინი k': 'K_ვიტამინი_მკგ', 'k ვიტამინი': 'K_ვიტამინი_მკგ', 'vitamin k': 'K_ვიტამინი_მკგ', 'ფილოქვინონი': 'K_ვიტამინი_მკგ',
        'სელენი': 'სელენი_მკგ', 'selenium': 'სელენი_მკგ', 'se': 'სელენი_მკგ',
        'კალორიები': 'კალორიები_კკალ', 'calories': 'კალორიები_კკალ', 'ენერგია': 'კალორიები_კკალ'
    }
    
    if search_lower in nutrient_mapping:
        return nutrient_mapping[search_lower]
        
    for col in df.columns:
        if col not in ['პროდუქტი', 'კატეგორია']:
            if search_lower in col.lower():
                return col
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
    elif 'კკალ' in column_name:
        return 'კკალ'
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
        "სელენი": "55 მკგ",
        "კალორიები": "2000-2500 კკალ (ქალები), 2500-3000 კკალ (მამაკაცები)"
    }
    
    for key, dose in daily_doses.items():
        if key.lower() in nutrient_name.lower():
            return dose
    return None

def calculate_daily_nutrition(selected_products, df):
    """გამოთვლის სულ დღიურ ნუტრიენტებს არჩეული პროდუქტებიდან"""
    if not selected_products:
        return None
    
    total_nutrition = {
        'კალორიები_კკალ': 0, # Add calories here
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
        product_data = df[df['პროდუქტი'] == item['პროდუქტი']]
        
        if not product_data.empty:
            multiplier = item['რაოდენობა'] / 100.0
            
            for nutrient in total_nutrition.keys():
                # Ensure the nutrient column exists before accessing it
                if nutrient in product_data.columns:
                    total_nutrition[nutrient] += product_data.iloc[0][nutrient] * multiplier
    
    return total_nutrition

def get_recommended_doses(gender):
    """რეკომენდებული დღიური დოზები სქესის მიხედვით, კალორიების ჩათვლით"""
    if gender == "მამრობითი":
        return {
            'კალორიები_კკალ': 2750, # Average for men
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
    else:  # მდედრობითი
        return {
            'კალორიები_კკალ': 2250, # Average for women
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
        'კალორიები_კკალ': '🔥 კალორიები', # Added calories
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

                current_amount = total_nutrition.get(nutrient_key, 0) # Use .get() for safety
                recommended = recommended_doses.get(nutrient_key, 1) # Use .get() for safety, avoid div by zero

                percentage = (current_amount / recommended) * 100 if recommended > 0 else 0
                
                with cols[i]:
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
        current_amount = total_nutrition.get(nutrient, 0)
        recommended = recommended_doses.get(nutrient, 1)
        
        percentage_for_progress = 0
        if recommended > 0:
            percentage_for_progress = min((current_amount / recommended), 1.0) # Cap at 100% for progress bar
        
        unit = get_unit(nutrient)
        
        col1_detail, col2_detail, col3_detail = st.columns([2, 3, 2])
        
        with col1_detail:
            st.write(f"**{name}**")
        
        with col2_detail:
            st.progress(percentage_for_progress)
        
        with col3_detail:
            st.write(f"{current_amount:.1f}/{recommended} {unit}")
    
    # რეკომენდაციები
    st.markdown("---")
    st.subheader("💡 რეკომენდაციები:")
    
    recommendations = []
    
    for nutrient, name in nutrient_names.items():
        current_amount = total_nutrition.get(nutrient, 0)
        recommended = recommended_doses.get(nutrient, 1)
        
        percentage = (current_amount / recommended) * 100 if recommended > 0 else 0
        
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
    nutrient_col = find_nutrient_column(search_term)    
    
    if not nutrient_col:
        return pd.DataFrame()
    
    if min_amount == 0.0:
        results = df[df[nutrient_col] > 0].copy()
    else:
        results = df[df[nutrient_col] >= min_amount].copy()
    
    results = results.sort_values(nutrient_col, ascending=False)
    
    return results

def generate_random_ration(df, num_items=5):
    """
    გენერირებს შემთხვევით დღიურ რაციონს პროდუქტების სიიდან.
    ცდილობს მრავალფეროვნების დაცვას კატეგორიების მიხედვით.
    """
    all_products = df['პროდუქტი'].unique().tolist()
    all_categories = df['კატეგორია'].unique().tolist()
    
    selected_ration_products_names = []
    
    random.shuffle(all_categories) 
    for category in all_categories:
        if len(selected_ration_products_names) >= num_items:
            break
        category_products = df[df['კატეგორია'] == category]['პროდუქტი'].tolist()
        if category_products:
            chosen_product = random.choice(category_products)
            if chosen_product not in selected_ration_products_names:
                selected_ration_products_names.append(chosen_product)

    while len(selected_ration_products_names) < num_items:
        chosen_product = random.choice(all_products)
        if chosen_product not in selected_ration_products_names:
            selected_ration_products_names.append(chosen_product)
            
    return selected_ration_products_names

def optimize_ration(selected_product_names, df, recommended_doses, nutrient_keys, tolerance_percent=0.1):
    """
    ოპტიმიზირებს პროდუქტების რაოდენობას (გრამებში) შერჩეული ნუტრიენტების
    რეკომენდებულ დოზებთან მიახლოების მიზნით.
    """
    
    prob = LpProblem("Optimize Daily Ration", LpMinimize)
    
    product_vars = LpVariable.dicts("Product", selected_product_names, 5, 500, LpContinuous)

    over_supply = LpVariable.dicts("Over", nutrient_keys, 0)
    under_supply = LpVariable.dicts("Under", nutrient_keys, 0)

    prob += lpSum([over_supply[n] + under_supply[n] for n in nutrient_keys]), "Total Deviation from Recommended Doses"
    
    for nutrient in nutrient_keys:
        total_nutrient_expr = lpSum([
            (df[df['პროდუქტი'] == p].iloc[0][nutrient] / 100) * product_vars[p]
            for p in selected_product_names if nutrient in df.columns # Ensure column exists
        ])
        
        rec_dose = recommended_doses[nutrient]

        # Ensure rec_dose is not zero for percentage calculations, especially for calories
        min_bound = rec_dose * (1 - tolerance_percent) if rec_dose > 0 else 0
        max_bound = rec_dose * (1 + tolerance_percent) if rec_dose > 0 else float('inf') # Use infinity if rec_dose is zero for upper bound

        prob += total_nutrient_expr + under_supply[nutrient] >= min_bound, f"Min {nutrient}"
        prob += total_nutrient_expr - over_supply[nutrient] <= max_bound, f"Max {nutrient}"

    # Solve the problem
    prob.solve(PULP_CBC_CMD(msg=0))

    optimized_ration = []
    if LpStatus[prob.status] == "Optimal":
        for product_name in selected_product_names:
            amount = product_vars[product_name].varValue
            if amount is not None and amount > 5:
                optimized_ration.append({'პროდუქტი': product_name, 'რაოდენობა': round(amount, 1)})
        return optimized_ration
    else:
        st.warning(f"PuLP Solver Status: {LpStatus[prob.status]}. ვერ მოხერხდა ოპტიმალური რაციონის გენერირება.")
        return []

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

# --- Streamlit აპლიკაცია ---
def main():
    st.set_page_config(
        page_title="🍏 თქვენი პირადი ნუტრიციოლოგი",
        layout="wide",
        initial_sidebar_state="auto",
        menu_items={
            'About': "ეს აპლიკაცია შექმნილია თქვენი პირადი კვებითი რეკომენდაციების მოსაწოდებლად. გთხოვთ, გაითვალისწინოთ, რომ ეს არ არის პროფესიონალური სამედიცინო რჩევა."
        }
    )
    
    # session state-ის ინიციალიზაცია
    if 'search_term' not in st.session_state:
        st.session_state.search_term = ''
    if 'min_amount' not in st.session_state:
        st.session_state.min_amount = 0.0
    if 'selected_products' not in st.session_state:
        st.session_state.selected_products = []
    if 'nutrients_multiselect_tab4' not in st.session_state:
        st.session_state.nutrients_multiselect_tab4 = []
    if 'generated_ration' not in st.session_state:
        st.session_state.generated_ration = []
    if 'current_page' not in st.session_state:
        st.session_state.current_page = "👨‍⚕️ პირადი ნუტრიციოლოგი" # Default page

    # CSS სტაილი კომპაქტური ვიუსთვის და DARK MODE-ის ადაპტაციისთვის
    st.markdown("""
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

    /* Sidebar Radio Button Styling - START */
    /* Target the container of the radio buttons in the sidebar */
    .st-emotion-cache-1r6dm7m > div[data-baseweb="radio"] { /* This targets the div that contains the radio labels */
        padding: 0; /* Remove default padding */
    }

    /* Target individual radio labels to make them look like buttons */
    .st-emotion-cache-1r6dm7m > div[data-baseweb="radio"] > label {
        display: block;
        padding: 12px 15px;
        margin: 5px 0; /* Space between "buttons" */
        border-radius: 8px;
        background-color: #f0f0f0; /* Light background for unselected */
        color: #333; /* Dark text for unselected */
        cursor: pointer;
        transition: all 0.2s ease-in-out;
        font-size: 1.1em;
        font-weight: 500;
        border: 1px solid #e0e0e0;
        text-align: left; /* Align text to the left */
    }

    /* Hide the actual radio circle */
    .st-emotion-cache-1r6dm7m > div[data-baseweb="radio"] input[type="radio"] {
        display: none;
    }

    /* Style for the text part of the radio button */
    .st-emotion-cache-1r6dm7m > div[data-baseweb="radio"] label > div:nth-child(2) {
        flex: 1; /* Make the text div take full width */
    }

    /* Hover effect */
    .st-emotion-cache-1r6dm7m > div[data-baseweb="radio"] label:hover {
        background-color: #e6e6e6; /* Slightly darker on hover */
        transform: translateY(-1px);
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    /* Selected state */
    .st-emotion-cache-1r6dm7m > div[data-baseweb="radio"] label.st-emotion-cache-1r6dm7m:has(input:checked) {
        background-color: #4CAF50; /* Green for selected */
        color: white;
        border-color: #4CAF50;
        font-weight: bold;
        box-shadow: 0 3px 8px rgba(0,128,0,0.2);
    }
    /* Sidebar Radio Button Styling - END */


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

        /* Specific styles for nutrition cards in dark mode */
        .nutrition-card {
            background-color: #333333;
            color: #f8f9fa;
            border-left: 3px solid #66b3ff;
            box-shadow: 0 2px 4px rgba(0,0,0,0.3);
        }
        .nutrition-card h4 {
            color: #f8f9fa !important;
        }
        .nutrition-value {
            color: #99ccff !important;
        }
        .stMarkdown, .stText, .stLabel {
            color: #f8f9fa;
        }
        .stMetric {
            background-color: #26272e;
            border: 1px solid #3d404d;
        }

        /* Sidebar Radio Button Styling - DARK MODE */
        .st-emotion-cache-1r6dm7m > div[data-baseweb="radio"] > label {
            background-color: #3a3a3a;
            color: #e0e0e0;
            border-color: #555;
        }
        .st-emotion-cache-1r6dm7m > div[data-baseweb="radio"] > label:hover {
            background-color: #4a4a4a;
        }
        .st-emotion-cache-1r6dm7m > div[data-baseweb="radio"] > label.st-emotion-cache-1r6dm7m:has(input:checked) {
            background-color: #66bb6a; /* Lighter green for dark mode selected */
            color: white;
            border-color: #66bb6a;
            box-shadow: 0 3px 8px rgba(0,200,0,0.2);
        }
    }
    </style>
    """, unsafe_allow_html=True)


    # Sidebar Navigation
    with st.sidebar:
        st.header("ნავიგაცია")
        if st.button("👨‍⚕️ **პირადი ნუტრიციოლოგი**", key="btn_nutr"):
            st.session_state.current_page = "👨‍⚕️ პირადი ნუტრიციოლოგი"
        if st.button("🔍 **პროდუქტების ძიება**", key="btn_search"):
            st.session_state.current_page = "🔍 პროდუქტების ძიება"
        if st.button("🧮 **დღიური ნორმის კალკულატორი**", key="btn_calc"):
            st.session_state.current_page = "🧮 დღიური ნორმის კალკულატორი"
        if st.button("📈 **ნუტრიენტების მონაცემები**", key="btn_data"):
            st.session_state.current_page = "📈 ნუტრიენტების მონაცემები"
        if st.button("✨ **დღიური რაციონის შედგენა**", key="btn_ration"):
            st.session_state.current_page = "✨ დღიური რაციონის შედგენა"
        # page_options = [
        #     "👨‍⚕️ პირადი ნუტრიციოლოგი",
        #     "🔍 პროდუქტების ძიება",
        #     "🧮 დღიური ნორმის კალკულატორი",
        #     "📈 ნუტრიენტების მონაცემები",
        #     "✨ დღიური რაციონის შედგენა"
        # ]
        # st.session_state.current_page = st.radio(
        #     "აირჩიეთ გვერდი:",
        #     page_options,
        #     key="sidebar_navigation_radio" # Unique key for sidebar radio
        # )

    # Main Content Area based on selected page
    if st.session_state.current_page == "👨‍⚕️ პირადი ნუტრიციოლოგი":
        st.header("👨‍⚕️🍏 თქვენი პირადი ნუტრიციოლოგი")
        
        st.write("📝შეიყვანეთ თქვენი მონაცემები და მიიღეთ დეტალური კვებითი რეკომენდაციები თქვენი ინდივიდუალური საჭიროებების გათვალისწინებით.")

        # --- User data input ---
        gender_personal = st.radio("🧍 **სქესი:**", ("მამრობითი", "მდედრობითი"), key="gender_personal_page", horizontal=True)
        weight = st.number_input("⚖️ **წონა (კგ):**", min_value=1.0, max_value=300.0, value=70.0, step=0.1, key="weight_personal_page")
        height = st.number_input("📏 **სიმაღლე (სმ):**", min_value=50.0, max_value=250.0, value=170.0, step=0.1, key="height_personal_page")
        age = st.number_input("🎂 **ასაკი (წელი):**", min_value=1, max_value=120, value=30, key="age_personal_page")

        activity_level = st.selectbox(
            "🏃 **ფიზიკური აქტივობა:**",
            (
                "მინიმალური (მჯდომარე ცხოვრება)",
                "მსუბუქი (კვირაში 1-3-ჯერ ვარჯიში)",
                "ზომიერი (კვირაში 3-5-ჯერ ვარჯიში)",
                "მაღალი (კვირაში 6-7-ჯერ ვარჯიში)",
                "ძალიან მაღალი (ყოველდღიური, ინტენსიური ვარჯიში)"
            ), key="activity_personal_page"
        )

        meal_frequency = st.number_input("🍽️ **ჭამის სიხშირე (დღეში):**", min_value=2, max_value=6, value=3, key="meal_freq_personal_page")

        body_type = st.selectbox(
            "🧍 **აღნაგობა:**",
            ("გამხდარი", "საშუალო", "მსუქანი"), key="body_type_personal_page"
        )

        goal = st.selectbox(
            "🎯 **კვებითი მიზანი:**",
            ("წონის დაკლება", "წონის შენარჩუნება", "წონის მომატება"), key="goal_personal_page"
        )

        # --- Blood type selection with both international and Georgian designations ---
        st.markdown("---")
        st.subheader("🩸 სისხლის ჯგუფი")
        blood_abo_options = [
            "არ ვიცი",
            "0 (I ჯგუფი)",
            "A (II ჯგუფი)",
            "B (III ჯგუფი)",
            "AB (IV ჯგუფი)"
        ]
        blood_abo_selection = st.selectbox(
            "**ABO სისტემა / ქართული სტანდარტი:**",
            blood_abo_options, key="blood_abo_personal_page"
        )

        blood_rh = st.selectbox(
            "**Rh ფაქტორი:**",
            ("არ ვიცი", "+ (დადებითი)", "- (უარყოფითი)"), key="blood_rh_personal_page"
        )

        # Extracting the ABO part for internal logic if needed
        blood_abo = blood_abo_selection.split(' ')[0] if blood_abo_selection != "არ ვიცი" else "არ ვიცი"
        standard_blood_group = blood_abo_selection if blood_abo_selection != "არ ვიცი" else "უცნობი"

        st.markdown("---")
        calculate_button = st.button("✨ მიიღე რეკომენდაციები", key="calculate_personal_page")

        if calculate_button:
            bmr_val = calculate_bmr(weight, height, age, gender_personal)
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
                * **� ვახშამი:**
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

    elif st.session_state.current_page == "🔍 პროდუქტების ძიება":
        st.header("🔍 პროდუქტების ძიება")
        st.markdown("აქ შეგიძლიათ მოძებნოთ პროდუქტები კონკრეტული ნუტრიენტების შემცველობის მიხედვით და იხილოთ მათი დეტალური ინფორმაცია.")

        # "დღიური დოზები (ზრდასრული)" განყოფილება
        st.markdown("**📊 დღიური დოზები (ზრდასრული):**")
        
        col0, col1, col2, col3, col4, col5 = st.columns([2, 3, 3, 3, 3, 1])

        with col0:
            st.button("🔥 **კალორიები:** 2000-3000 კკალ", key="dose_calories_search_page", use_container_width=True, on_click=set_search_and_min_amount, args=('კალორიები', 0.0))
        with col1:
            st.button("🔶 **რკინა:** 18 მგ (ქალები), 8 მგ (მამაკაცები)", key="dose_iron_search_page", use_container_width=True, on_click=set_search_and_min_amount, args=('რკინა', 0.0))
            st.button("🔷 **B12:** 2.4 მკგ", key="dose_b12_search_page", use_container_width=True, on_click=set_search_and_min_amount, args=('B12', 0.0))
            st.button("🟢 **ფოლატი:** 400 მკგ", key="dose_folate_search_page", use_container_width=True, on_click=set_search_and_min_amount, args=('ფოლატი', 0.0))
        with col2:
            st.button("🟡 **C ვიტამინი:** 90 მგ (მამაკაცები), 75 მგ (ქალები)", key="dose_c_search_page", use_container_width=True, on_click=set_search_and_min_amount, args=('C ვიტამინი', 0.0))
            st.button("🟠 **D ვიტამინი:** 600-800 IU", key="dose_d_search_page", use_container_width=True, on_click=set_search_and_min_amount, args=('D ვიტამინი', 0.0))
            st.button("⚪ **კალციუმი:** 1000-1200 მგ", key="dose_calcium_search_page", use_container_width=True, on_click=set_search_and_min_amount, args=('კალციუმი', 0.0))
        with col3:
            st.button("🟣 **მაგნიუმი:** 400-420 მგ (მამაკაცები), 310-320 მგ (ქალები)", key="dose_magnesium_search_page", use_container_width=True, on_click=set_search_and_min_amount, args=('მაგნიუმი', 0.0))
            st.button("🔵 **კალიუმი:** 3500-4700 მგ", key="dose_potassium_search_page", use_container_width=True, on_click=set_search_and_min_amount, args=('კალიუმი', 0.0))
            st.button("⚫ **თუთია:** 11 მგ (მამაკაცები), 8 მგ (ქალები)", key="dose_zinc_search_page", use_container_width=True, on_click=set_search_and_min_amount, args=('თუთია', 0.0))
        with col4:
            st.button("⚪ **A ვიტამინი:** 700-900 მკგ RAE", key="dose_a_search_page", use_container_width=True, on_click=set_search_and_min_amount, args=('A ვიტამინი', 0.0))
            st.button("🟤 **E ვიტამინი:** 15 მგ", key="dose_e_search_page", use_container_width=True, on_click=set_search_and_min_amount, args=('E ვიტამინი', 0.0))
            st.button("⚫ **K ვიტამინი:** 90-120 მკგ", key="dose_k_search_page", use_container_width=True, on_click=set_search_and_min_amount, args=('K ვიტამინი', 0.0))
            st.button("⚪ **სელენი:** 55 მკგ", key="dose_selenium_search_page", use_container_width=True, on_click=set_search_and_min_amount, args=('სელენი', 0.0))
        with col5:
            st.button("🗑️ გასუფთავება", key="clear_all_search_page", use_container_width=True, on_click=set_search_and_min_amount, args=('', 0.0))
                
        st.markdown("---")
        
        # ძიების პარამეტრები 
        categories = ['ყველა'] + sorted(df['კატეგორია'].unique().tolist())
        selected_category = st.selectbox("კატეგორია:", categories, key="category_filter_search_page")
        
        st.session_state.search_term = st.text_input("მოძებნეთ ნუტრიენტი (მაგ. რკინა, ვიტამინი C, კალორიები):", 
                                                     value=st.session_state.search_term, 
                                                     key="main_search_input_text_field_search_page")
        
        if st.session_state.search_term:
            st.session_state.min_amount = st.number_input(f"მინიმალური რაოდენობა ({st.session_state.search_term}):", 
                                                           min_value=0.0, 
                                                           value=st.session_state.min_amount,
                                                           step=0.1,
                                                           key="min_amount_input_field_search_page")
        
        filtered_df = df.copy()
        
        if selected_category != 'ყველა':
            filtered_df = filtered_df[filtered_df['კატეგორია'] == selected_category]
        
        if st.session_state.search_term:
            search_results = search_by_nutrient(filtered_df, st.session_state.search_term, 
                                                st.session_state.min_amount)
            
            if not search_results.empty:
                st.subheader(f"🎯 ძიების შედეგები: '{st.session_state.search_term}'")
                
                daily_dose = get_daily_dose(st.session_state.search_term)
                if daily_dose:
                    st.info(f"📊 **დღიური რეკომენდებული დოზა:** {daily_dose}")
                
                categories_found = search_results['კატეგორია'].unique()
                
                for category in sorted(categories_found):
                    with st.expander(f"📂 {category}", expanded=True):
                        category_data = search_results[search_results['კატეგორია'] == category]
                        
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
                                    if value > 0:
                                        st.write(f"`{value} {unit}`")
                                    else:
                                        st.write("`0`")
            else:
                st.warning(f"არ მოიძებნა პროდუქტები '{st.session_state.search_term}'-ით ამ კრიტერიუმებით.")
        
        else:
            st.subheader("📋 ყველა პროდუქტი კატეგორიების მიხედვით")
            
            categories_to_show = filtered_df['კატეგორია'].unique()
            
            for category in sorted(categories_to_show):
                with st.expander(f"📂 {category}", expanded=False):
                    category_data = filtered_df[filtered_df['კატეგორია'] == category]
                    
                    cols_grid = st.columns(3)  
                    
                    for idx, (_, row) in enumerate(category_data.iterrows()):
                        with cols_grid[idx % 3]:
                            # Ensure all nutrient columns exist before accessing them in the markdown
                            # Add calories to the displayed card
                            nutrition_info = f"""
                            <div class="nutrition-card">
                                <h4 style="margin: 0 0 0.25rem 0; font-size: 1.1em;">{row['პროდუქტი']}</h4>
                                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.15rem; font-size: 0.85em;"> 
                                    <div>🔥 კალორიები: <span class="nutrition-value">{row.get('კალორიები_კკალ', 0)} კკალ</span></div>
                                    <div>🔶 რკინა: <span class="nutrition-value">{row.get('რკინა_მგ', 0)} მგ</span></div>
                                    <div>🔷 B12: <span class="nutrition-value">{row.get('B12_მკგ', 0)} მკგ</span></div>
                                    <div>🟢 ფოლატი: <span class="nutrition-value">{row.get('ფოლატი_მკგ', 0)} მკგ</span></div>
                                    <div>🟡 C ვიტ.: <span class="nutrition-value">{row.get('C_ვიტამინი_მგ', 0)} მგ</span></div>
                                    <div>🟠 D ვიტ.: <span class="nutrition-value">{row.get('D_ვიტამინი_IU', 0)} IU</span></div>
                                    <div>⚪ კალციუმი: <span class="nutrition-value">{row.get('კალციუმი_მგ', 0)} მგ</span></div>
                                    <div>🟣 მაგნიუმი: <span class="nutrition-value">{row.get('მაგნიუმი_მგ', 0)} მგ</span></div>
                                    <div>🔵 კალიუმი: <span class="nutrition-value">{row.get('კალიუმი_მგ', 0)} მგ</span></div>
                                    <div>⚫ თუთია: <span class="nutrition-value">{row.get('თუთია_მგ', 0)} მგ</span></div>
                                    <div>⚪ A ვიტ.: <span class="nutrition-value">{row.get('A_ვიტამინი_მკგ_RAE', 0)} მკგ RAE</span></div>
                                    <div>🟤 E ვიტ.: <span class="nutrition-value">{row.get('E_ვიტამინი_მგ_ATE', 0)} მგ ATE</span></div>
                                    <div>⚫ K ვიტ.: <span class="nutrition-value">{row.get('K_ვიტამინი_მკგ', 0)} მკგ</span></div>
                                    <div>⚪ სელენი: <span class="nutrition-value">{row.get('სელენი_მკგ', 0)} მკგ</span></div>
                                </div>
                            </div>
                            """
                            st.markdown(nutrition_info, unsafe_allow_html=True)

    elif st.session_state.current_page == "🧮 დღიური ნორმის კალკულატორი":
        st.header("🧮 დღიური ნორმის კალკულატორი")
        st.markdown("დაამატეთ პროდუქტები და მათი რაოდენობა (გრამებში), რათა გამოთვალოთ დღიური ნუტრიენტების ჯამური შემცველობა.")
        
        gender_calc = st.radio("აირჩიეთ სქესი:", ["მამრობითი", "მდედრობითი"], key="gender_calculator_page", horizontal=True)
        
        product_options = df['პროდუქტი'].unique().tolist()
        selected_product_name = st.selectbox("აირჩიეთ პროდუქტი:", product_options, key="product_selector_calculator_page")
        
        amount_g = st.number_input("რაოდენობა (გრამებში):", min_value=1.0, value=100.0, step=10.0, key="amount_input_calculator_page")
        
        if st.button("➕ პროდუქტის დამატება", key="add_product_button_calculator_page"):
            if selected_product_name and amount_g > 0:
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
                key="selected_products_editor_calculator_page" # Unique key
            )
            
            st.session_state.selected_products = edited_df.to_dict('records')
            
            if st.button("❌ სიის გასუფთავება", key="clear_selected_products_calculator_page"): # Unique key
                st.session_state.selected_products = []
                st.success("პროდუქტების სია გასუფთავებულია.")
                st.rerun()
            
            st.markdown("---")
            
            total_nutrition = calculate_daily_nutrition(st.session_state.selected_products, df)
            
            if total_nutrition:
                st.subheader("📊 დღიური ნუტრიენტების ანალიზი:")
                recommended_doses = get_recommended_doses(gender_calc)
                display_nutrition_analysis(total_nutrition, recommended_doses)
            else:
                st.info("დაამატეთ პროდუქტები დღიური ნორმის სანახავად.")
        else:
            st.info("პროდუქტები არ არის დამატებული.")

    elif st.session_state.current_page == "📈 ნუტრიენტების მონაცემები":
        st.header("📈 ნუტრიენტების სრული მონაცემები")
        st.markdown("იხილეთ ყველა პროდუქტის და ნუტრიენტის დეტალური მონაცემები.")
        
        nutrient_columns = [col for col in df.columns if col not in ['პროდუქტი', 'კატეგორია']]
        selected_nutrients_to_display = st.multiselect(
            "აირჩიეთ ნუტრიენტები საჩვენებლად:",
            options=nutrient_columns,
            default=st.session_state.nutrients_multiselect_tab4,
            key="nutrients_multiselect_data_page" # Unique key
        )
        
        categories_for_table = ['ყველა'] + sorted(df['კატეგორია'].unique().tolist())
        selected_category_for_table = st.selectbox("ფილტრი კატეგორიის მიხედვით:", categories_for_table, key="category_filter_data_page") # Unique key

        st.button("🗑️ არჩეული ნუტრიენტების გასუფთავება", on_click=clear_nutrients_multiselect_tab4, key="clear_multiselect_data_page") # Unique key

        display_columns = ['პროდუქტი', 'კატეგორია'] + selected_nutrients_to_display

        filtered_df_tab4 = df.copy()
        if selected_category_for_table != 'ყველა':
            filtered_df_tab4 = filtered_df_tab4[filtered_df_tab4['კატეგორია'] == selected_category_for_table]

        if not selected_nutrients_to_display:
            st.warning("გთხოვთ აირჩიოთ მინიმუმ ერთი ნუტრიენტი მონაცემების საჩვენებლად.")
        else:
            st.dataframe(filtered_df_tab4[display_columns], use_container_width=True)

    elif st.session_state.current_page == "✨ დღიური რაციონის შედგენა":
        st.header("✨ დღიური რაციონის შედგენა")
        st.markdown("ამ ფუნქციის გამოყენებით შეგიძლიათ გენერირება დღიური რაციონი თქვენი სქესის მიხედვით, რომელიც დააბალანსებს აუცილებელ ნუტრიენტებს.")
        
        ration_gender = st.radio("აირჩიეთ სქესი რაციონის გენერაციისთვის:", ["მამრობითი", "მდედრობითი"], key="ration_gender_selector_ration_page", horizontal=True) # Unique key
        
        st.markdown("---")

        num_ration_items = st.slider("რამდენი პროდუქტი გქონდეთ რაციონში?", min_value=3, max_value=10, value=6, step=1, key="num_ration_items_ration_page") # Unique key
        
        tolerance = st.slider("ნუტრიენტების ნორმიდან გადახრის ტოლერანტობა (%)", min_value=0, max_value=20, value=10, step=1, key="tolerance_ration_page") / 100.0 # Unique key

        if st.button("🛠️ რაციონის გენერაცია", key="generate_ration_button_ration_page"): # Unique key
            initial_product_names = generate_random_ration(df, num_items=num_ration_items)
            
            recommended_doses_for_opt = get_recommended_doses(ration_gender)
            
            # Ensure 'კალორიები_კკალ' is included in nutrient_keys_for_opt
            nutrient_keys_for_opt = [col for col in df.columns if col not in ['პროდუქტი', 'კატეგორია']]

            st.session_state.generated_ration = optimize_ration(
                initial_product_names, 
                df, 
                recommended_doses_for_opt, 
                nutrient_keys_for_opt,
                tolerance_percent=tolerance
            )
            
            if st.session_state.generated_ration:
                st.success("🎉 რაციონი წარმატებით გენერირდა!")
            else:
                st.error("❌ ვერ მოხერხდა ოპტიმალური რაციონის გენერირება მოცემული კრიტერიუმებით. სცადეთ სხვა რაოდენობის პროდუქტები ან შეცვალეთ ტოლერანტობა.")

        if st.session_state.generated_ration:
            st.subheader("📋 გენერირებული დღიური რაციონი:")
            generated_ration_df = pd.DataFrame(st.session_state.generated_ration)
            st.dataframe(generated_ration_df, use_container_width=True)

            total_nutrition_generated = calculate_daily_nutrition(st.session_state.generated_ration, df)
            if total_nutrition_generated:
                st.subheader("📊 გენერირებული რაციონის ნუტრიენტების ანალიზი:")
                recommended_doses_for_ration = get_recommended_doses(ration_gender)
                display_nutrition_analysis(total_nutrition_generated, recommended_doses_for_ration)
            
            if st.button("🗑️ გენერირებული რაციონის გასუფთავება", key="clear_generated_ration_ration_page"): # Unique key
                st.session_state.generated_ration = []
                st.success("გენერირებული რაციონი გასუფთავებულია.")
                st.rerun()

        else:
            st.info("დააჭირეთ 'რაციონის გენერაცია' ღილაკს, რათა შექმნათ თქვენი დღიური რაციონი.")

if __name__ == "__main__":
    main()