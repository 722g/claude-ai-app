from flask import Flask, request
import anthropic

app = Flask(__name__)
client = anthropic.Anthropic(api_key="YOUR_API_KEY_HERE")

@app.route("/", methods=["GET", "POST"])
def index():
    answer = ""
    if request.method == "POST":
        question = request.form["question"]
        message = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            messages=[{"role": "user", "content": question}]
        )
        answer = message.content[0].text
    return f"""<!DOCTYPE html>
    <html>
    <head><title>Gigi AI</title>
    <style>
    body{{font-family:Arial;max-width:800px;margin:50px auto;padding:20px}}
    textarea{{width:100%;height:100px;padding:10px;font-size:16px}}
    button{{background:black;color:white;padding:12px 30px;border:none;font-size:16px;cursor:pointer;margin-top:10px}}
    .answer{{background:#f5f5f5;padding:20px;margin-top:20px;border-radius:8px;white-space:pre-wrap}}
    </style></head>
    <body>
    <h1>Ask Claude Anything</h1>
    <form method="POST">
    <textarea name="question" placeholder="Type your question here..."></textarea>
    <br><button type="submit">Ask Claude</button>
    </form>
    {"<div class='answer'>" + answer + "</div>" if answer else ""}
    </body></html>"""

if __name__ == "__main__":
    app.run(debug=True)
