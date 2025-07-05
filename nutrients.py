from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# --- ნუტრიენტების მონაცემები (მაგალითი) ---
# ეს არის გამარტივებული მაგალითი. რეალურ აპლიკაციაში, ეს მონაცემები ბაზიდან ან გარე ფაილიდან უნდა მოდიოდეს.
NUTRIENT_DATA = {
    "ვაშლი": {"ვიტამინი C": 10, "ბოჭკო": 4, "კალორია": 95},
    "ბანანი": {"კალიუმი": 400, "ვიტამინი B6": 0.4, "კალორია": 105},
    "ქათმის მკერდი": {"ცილა": 30, "რკინა": 0.5, "კალორია": 165},
    "ისპანახი": {"ვიტამინი K": 145, "რკინა": 2.7, "კალორია": 23},
    "რძე": {"კალციუმი": 300, "ვიტამინი D": 2, "ცილა": 8},
    "კვერცხი": {"ცილა": 6, "ვიტამინი B12": 0.5, "კალორია": 70},
}

# დღიური ნორმები სქესის მიხედვით (მაგალითი)
DAILY_REQUIREMENTS = {
    "ქალი": {
        "ვიტამინი C": {"min": 75, "max": 2000},
        "ბოჭკო": {"min": 25, "max": 35},
        "კალიუმი": {"min": 2600, "max": 4700},
        "ვიტამინი B6": {"min": 1.3, "max": 100},
        "ცილა": {"min": 46, "max": 100},
        "რკინა": {"min": 18, "max": 45},
        "ვიტამინი K": {"min": 90, "max": 1000},
        "კალციუმი": {"min": 1000, "max": 2500},
        "ვიტამინი D": {"min": 15, "max": 100},
    },
    "კაცი": {
        "ვიტამინი C": {"min": 90, "max": 2000},
        "ბოჭკო": {"min": 38, "max": 45},
        "კალიუმი": {"min": 3400, "max": 4700},
        "ვიტამინი B6": {"min": 1.3, "max": 100},
        "ცილა": {"min": 56, "max": 100},
        "რკინა": {"min": 8, "max": 45},
        "ვიტამინი K": {"min": 120, "max": 1000},
        "კალციუმი": {"min": 1000, "max": 2500},
        "ვიტამინი D": {"min": 15, "max": 100},
    },
}

def calculate_random_products(gender):
    """
    ითვლის პროდუქტების შემთხვევით რაოდენობას,
    რომელიც სქესის მიხედვით ნუტრიენტების დღიურ ნორმას შეავსებს.
    """
    required_nutrients = DAILY_REQUIREMENTS.get(gender)
    if not required_nutrients:
        return {"შეცდომა": "არასწორი სქესი"}

    # აქ შეგვიძლია უფრო კომპლექსური ლოგიკა დავამატოთ
    # მაგალითად, რომ არჩეული პროდუქტების კომბინაცია ნამდვილად აკმაყოფილებდეს ნორმას.
    # ამ გამარტივებულ მაგალითში, უბრალოდ შემთხვევით რაოდენობებს ვაგენერირებთ
    # თითოეული პროდუქტისთვის, რაც დაგვეხმარება ვიზუალურად.

    recommended_products = {}
    for product, nutrients in NUTRIENT_DATA.items():
        # შემთხვევითი რაოდენობა 1-დან 5-მდე პორციამდე
        recommended_products[product] = random.randint(1, 5)

    return recommended_products

def setup_browser():
    """ბრაუზერის ინიციალიზაცია"""
    options = webdriver.ChromeOptions()
    # შეგიძლიათ დაამატოთ headless რეჟიმი თუ არ გსურთ ბრაუზერის ვიზუალურად გახსნა
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver

def main():
    driver = setup_browser()
    original_window = driver.current_window_handle # მთავარი ფანჯრის handle

    try:
        # პირველი ტაბი
        driver.get("https://www.google.com")
        print(f"Tab 1 Title: {driver.title}")
        time.sleep(1)

        # მეორე ტაბი
        driver.execute_script("window.open('');") # ხსნის ახალ ცარიელ ტაბს
        driver.switch_to.window(driver.window_handles[1]) # გადადის ახალ ტაბზე
        driver.get("https://www.youtube.com")
        print(f"Tab 2 Title: {driver.title}")
        time.sleep(1)

        # მესამე ტაბი
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[2])
        driver.get("https://www.amazon.com")
        print(f"Tab 3 Title: {driver.title}")
        time.sleep(1)

        # --- მეოთხე ტაბი: ნუტრიენტების გენერატორი ---
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[3])
        driver.get("data:text/html,<body><h1>ნუტრიენტების რეკომენდატორი</h1><div id='gender-selection'><label for='gender'>აირჩიეთ სქესი:</label><select id='gender'><option value='ქალი'>ქალი</option><option value='კაცი'>კაცი</option></select><button id='generate-btn'>გენერირება</button></div><div id='results'></div><script>document.getElementById('generate-btn').onclick = function() {let gender = document.getElementById('gender').value; let resultsDiv = document.getElementById('results'); resultsDiv.innerHTML = 'იტვირთება...'; fetch('http://localhost:5000/generate_nutrients?gender=' + gender).then(response => response.json()).then(data => {resultsDiv.innerHTML = '<h2>რეკომენდებული პროდუქტები (' + gender + '):</h2><ul>'; for (const [product, quantity] of Object.entries(data)) {resultsDiv.innerHTML += '<li>' + product + ': ' + quantity + ' ერთეული</li>';} resultsDiv.innerHTML += '</ul>';}).catch(error => {resultsDiv.innerHTML = 'შეცდომა: ' + error; console.error('Error:', error);});};</script></body>")
        print(f"Tab 4 Title: {driver.title}")
        time.sleep(2)

        # სქესის არჩევა და ღილაკზე დაჭერა
        # ჩვენ Selenium-ით ვუკავშირდებით HTML გვერდზე არსებულ ელემენტებს
        # და სიმულირებთ მომხმარებლის ინტერაქციას.
        
        # დაელოდე სქესის ამორჩევის ელემენტს
        gender_dropdown = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "gender"))
        )
        
        # სქესის არჩევა (მაგალითად, "კაცი")
        gender_to_select = "კაცი" # ან "ქალი"
        gender_dropdown.send_keys(gender_to_select)
        time.sleep(1)

        # ღილაკზე დაჭერა
        generate_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "generate-btn"))
        )
        generate_button.click()
        time.sleep(3) # დაელოდე შედეგების გამოჩენას

        # შედეგების წაკითხვა (სურვილისამებრ)
        results_div = driver.find_element(By.ID, "results")
        print(f"\nTab 4 Results for {gender_to_select}:")
        print(results_div.text)


        # შეგიძლიათ დაუბრუნდეთ ორიგინალ ტაბს
        # driver.switch_to.window(original_window)
        # print(f"Switched back to original tab. Title: {driver.title}")

        input("\nდააჭირეთ Enter-ს ბრაუზერის დასახურად...")

    except Exception as e:
        print(f"მოხდა შეცდომა: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    # შენიშვნა: "data:text/html" მიდგომა არის მარტივი გზა
    # პატარა HTML კონტენტის ბრაუზერში პირდაპირ ჩასატვირთად.
    # უფრო კომპლექსური UI-სთვის, დაგჭირდებათ
    # Flask/Django ან მსგავსი ვებ ფრეიმვორკი, რომელზეც გაეშვება ეს HTML.
    # ასევე, "fetch" ფუნქცია HTML-ში საჭიროებს backend-ს (მაგალითად, Flask),
    # რომელზეც გაეშვება calculate_random_products ფუნქცია.

    # ქვემოთ მოცემულია Flask-ის მინიმალური მაგალითი,
    # რომელიც საჭირო იქნება HTML-ში fetch ფუნქციის სწორად მუშაობისთვის.
    # გაუშვით ეს Flask აპლიკაცია ცალკე ტერმინალში.
    
    # from flask import Flask, request, jsonify
    # from threading import Thread

    # app = Flask(__name__)

    # @app.route('/generate_nutrients', methods=['GET'])
    # def generate_nutrients():
    #     gender = request.args.get('gender')
    #     if not gender:
    #         return jsonify({"error": "Gender parameter is missing"}), 400
    #     
    #     products = calculate_random_products(gender)
    #     return jsonify(products)

    # def run_flask_app():
    #     app.run(port=5000)

    # # Flask აპლიკაციის გაშვება ცალკე Thread-ში
    # flask_thread = Thread(target=run_flask_app)
    # flask_thread.daemon = True # საშუალებას აძლევს Flask-ს დაიხუროს მთავარ პროგრამასთან ერთად
    # flask_thread.start()

    main()
