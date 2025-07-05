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
        'პარკოსნები', 'პარკოსნები',
        'ბოსტნეული', 'სოკო', 'ბოსტნეული', 'ბოსტნეული', 'ბოსტნეული',
        'ხილი', 'ხილი', 'ხილი', 'ხილი', 'ხილი',
        'მარცვლეული', 'მარცვლეული', 'მარცვლეული',
        'ბოსტნეული', 'ბოსტნეული', 'ბოსტნეული',
        'რძის პროდუქტები', 'რძის პროდუქტები', 'რძის პროდუქტები', 'რძის პროდუქტები'
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
        0, 0, 0,
        100, 0, 0, 0
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
    if gender == "მამაკაცი":
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
    else:  # ქალი
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
            percentage_for_progress = min((current_amount / recommended), 2.0)
        
        unit = get_unit(nutrient)
        
        col1_detail, col2_detail, col3_detail = st.columns([2, 3, 2])
        
        with col1_detail:
            st.write(f"**{name}**")
        
        with col2_detail:
            st.progress(min(percentage_for_progress, 1.0))
        
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
    if 'nutrients_multiselect_tab3' not in st.session_state:
        st.session_state.nutrients_multiselect_tab3 = []
    if 'generated_ration' not in st.session_state:
        st.session_state.generated_ration = []

    # CSS სტაილი კომპაქტური ვიუსთვის
    st.markdown("""
    <style>
    html, body, .stApp {
        font-size: 14px;
        line-height: 1.5;
    }

    .stTextInput, .stSelectbox, .stNumberInput, .stButton, .stRadio, .stExpander {
        margin-bottom: 0.5rem !important;
        margin-top: 0.25rem !important;
    }

    .element-container {
        margin-bottom: 0.5rem !important;
    }
    .stMarkdown {
        margin-bottom: 0.5rem !important;
        margin-top: 0.25rem !important;
    }
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        font-size:16px;
        margin-bottom: 0px;
    }
    
    .nutrition-card {
        background-color: #f8f9fa; 
        color: #333;
        padding: 0.5rem;
        border-radius: 0.25rem;
        margin-bottom: 0.5rem;
        border-left: 3px solid #007bff;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    @media (prefers-color-scheme: dark) {
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
    .stMetric {
        background-color: #f0f2f6;
        border-radius: 0.5rem;
        padding: 0.5rem;
        margin-bottom: 0.5rem;
        border: 1px solid #e0e2e6;
    }
    @media (prefers-color-scheme: dark) {
        .stMetric {
            background-color: #26272e;
            border: 1px solid #3d404d;
        }
    }
    .stMetric label {
        font-size: 0.9em;
        font-weight: bold;
    }
    .stMetric div[data-testid="stMetricValue"] {
        font-size: 1.1em;
    }
    .stMetric div[data-testid="stMetricDelta"] {
        font-size: 0.8em;
    }

    .stExpander div[data-testid="stExpanderForm"] {
        padding: 0.5rem;
    }
    .stExpander details summary {
        padding: 0.5rem 0.75rem;
        margin-bottom: 0.25rem;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.title("🥗 საკვები პროდუქტების ვიტამინ-მინერალური ძიება")
    st.markdown("---")
    
    # დღიური დოზების ინფორმაცია მთავარ გვერდზე
    st.markdown("**📊 დღიური დოზები (ზრდასრული):**")
    
    col0, col1, col2, col3, col4, col5 = st.columns([2, 3, 3, 3, 3, 1])

    with col0:
        st.button("🔥 **კალორიები:** 2000-3000 კკალ", key="dose_calories", use_container_width=True, on_click=set_search_and_min_amount, args=('კალორიები', 0.0))
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
        st.button("🗑️ გასუფთავება", key="clear_all_search", use_container_width=True, on_click=set_search_and_min_amount, args=('', 0.0))
            
    st.markdown("---")
    
    # ტაბების შექმნა
    tab1, tab2, tab3, tab4 = st.tabs(["🔍 ძიება", "🧮 დღიური ნორმის კალკულატორი", "📈 ნუტრიენტების მონაცემები", "✨ დღიური რაციონის შედგენა"])
    
    with tab1:
        # მხარეს პანელი ფილტრებისთვის
        with st.sidebar:
            st.header("🔍 ძიების პარამეტრები")
            
            categories = ['ყველა'] + sorted(df['კატეგორია'].unique().tolist())
            selected_category = st.selectbox("კატეგორია:", categories)
            
            st.session_state.search_term = st.text_input("მოძებნეთ ნუტრიენტი (მაგ. რკინა, ვიტამინი C, კალორიები):", 
                                                         value=st.session_state.search_term, 
                                                         key="main_search_input_text_field")
            
            if st.session_state.search_term:
                st.session_state.min_amount = st.number_input(f"მინიმალური რაოდენობა ({st.session_state.search_term}):", 
                                                               min_value=0.0, 
                                                               value=st.session_state.min_amount,
                                                               step=0.1,
                                                               key="min_amount_input_field")
        
        # მთავარი კონტენტი (ძიების ტაბი)
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
    
    with tab2:
        st.header("🧮 დღიური ნორმის კალკულატორი")
        st.markdown("დაამატეთ პროდუქტები და მათი რაოდენობა (გრამებში), რათა გამოთვალოთ დღიური ნუტრიენტების ჯამური შემცველობა.")
        
        gender = st.radio("აირჩიეთ სქესი:", ["მამაკაცი", "ქალი"], key="gender_tab2", horizontal=True)
        
        product_options = df['პროდუქტი'].unique().tolist()
        selected_product_name = st.selectbox("აირჩიეთ პროდუქტი:", product_options, key="product_selector_tab2")
        
        amount_g = st.number_input("რაოდენობა (გრამებში):", min_value=1.0, value=100.0, step=10.0, key="amount_input_tab2")
        
        if st.button("➕ პროდუქტის დამატება", key="add_product_button_tab2"):
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
                key="selected_products_editor"
            )
            
            st.session_state.selected_products = edited_df.to_dict('records')
            
            if st.button("❌ სიის გასუფთავება", key="clear_selected_products"):
                st.session_state.selected_products = []
                st.success("პროდუქტების სია გასუფთავებულია.")
                st.rerun()
            
            st.markdown("---")
            
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
        
        nutrient_columns = [col for col in df.columns if col not in ['პროდუქტი', 'კატეგორია']]
        selected_nutrients_to_display = st.multiselect(
            "აირჩიეთ ნუტრიენტები საჩვენებლად:",
            options=nutrient_columns,
            default=st.session_state.nutrients_multiselect_tab3,
            key="nutrients_multiselect_tab3"
        )
        
        categories_for_table = ['ყველა'] + sorted(df['კატეგორია'].unique().tolist())
        selected_category_for_table = st.selectbox("ფილტრი კატეგორიის მიხედვით:", categories_for_table, key="category_filter_tab3")

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
        
        ration_gender = st.radio("აირჩიეთ სქესი რაციონის გენერაციისთვის:", ["მამაკაცი", "ქალი"], key="ration_gender_selector", horizontal=True)
        
        st.markdown("---")

        num_ration_items = st.slider("რამდენი პროდუქტი გქონდეთ რაციონში?", min_value=3, max_value=10, value=6, step=1)
        
        tolerance = st.slider("ნუტრიენტების ნორმიდან გადახრის ტოლერანტობა (%)", min_value=0, max_value=20, value=10, step=1) / 100.0

        if st.button("🛠️ რაციონის გენერაცია", key="generate_ration_button"):
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
            
            if st.button("🗑️ გენერირებული რაციონის გასუფთავება", key="clear_generated_ration"):
                st.session_state.generated_ration = []
                st.success("გენერირებული რაციონი გასუფთავებულია.")
                st.rerun()

        else:
            st.info("დააჭირეთ 'რაციონის გენერაცია' ღილაკს, რათა შექმნათ თქვენი დღიური რაციონი.")

if __name__ == "__main__":
    main()
