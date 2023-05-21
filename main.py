from flask import Flask, render_template, request
import openai
import dotenv
import re
import markdown

config = dotenv.dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST' and request.form:
        code = request.form.get("text")
        out = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"{code}"},
                {
                    "role": "user",
                    "content": """Can you point out the mistakes I made in the above code snippet, 
                    and tease me in a comedic manner for each mistake I made. Return only the comments.""",
                },
            ],
        )
        output = out["choices"][0]["message"]["content"]
        pattern = r"\d+\."
        split_out = re.split(pattern, output)
        
        return render_template("index.html", output=split_out)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5005)
