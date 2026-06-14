from flask import Flask, render_template, request
import speech_recognition as sr
import requests

app = Flask(__name__)

# 🎤 Speech to Text function
def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak something...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said:", text)
        return text
    except:
        return "Could not understand audio"


# 🎨 MonsterAPI Image Generation
def generate_image(prompt):
    API_KEY = "YOUR_MONSTERAPI_KEY"

    url = "https://api.monsterapi.ai/v1/generate"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "prompt": prompt,
        "style": "realistic"
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        return response.json()["data"]["image_url"]
    else:
        return None


@app.route("/", methods=["GET", "POST"])
def home():
    text = ""
    image_url = None

    if request.method == "POST":
        text = speech_to_text()
        image_url = generate_image(text)

    return render_template("index.html", text=text, image_url=image_url)


if __name__ == "__main__":
    app.run(debug=True)