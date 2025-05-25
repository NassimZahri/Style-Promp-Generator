from flask import Flask, request, render_template
from azure_uploader import upload_image_to_azure
from groq_client import generate_image_prompt

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "image" not in request.files:
            return "No file part", 400
        file = request.files["image"]
        if file.filename == "":
            return "No selected file", 400
        image_path = f"src/uploads/{file.filename}"
        file.save(image_path)

        image_url = upload_image_to_azure(image_path)
        print(f"Image uploaded to Azure: {image_url}")
        question = "Generate a cinematic, Midjourney-style prompt for this image."
        prompt = generate_image_prompt(image_url, question)

        return render_template("result.html", prompt=prompt)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
