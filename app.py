from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)


def generate_password(length=12, use_special=True, use_digits=True, phrase=""):
    # Base character set: letters
    chars = string.ascii_letters

    if use_digits:
        chars += string.digits
    if use_special:
        chars += "!@#$%^&*()-_=+[]{};:,.<>/?"

    # Ensure we have some characters to choose from
    if not chars:
        chars = string.ascii_letters

    # Clean up phrase (optional) and make sure total length works
    phrase = phrase.strip()
    base_len = max(0, length - len(phrase))

    random_part = "".join(random.choice(chars) for _ in range(base_len))

    # Insert phrase at a random position if provided
    if phrase:
        insert_pos = random.randint(0, len(random_part))
        password = random_part[:insert_pos] + phrase + random_part[insert_pos:]
    else:
        password = random_part

    return password


@app.route("/", methods=["GET", "POST"])
def index():
    generated_password = None

    if request.method == "POST":
        try:
            length = int(request.form.get("length", 12))
        except ValueError:
            length = 12

        length = max(4, min(length, 64))  # Clamp between 4 and 64

        use_special = request.form.get("use_special") == "on"
        use_digits = request.form.get("use_digits") == "on"
        phrase = request.form.get("phrase", "")

        generated_password = generate_password(
            length=length,
            use_special=use_special,
            use_digits=use_digits,
            phrase=phrase,
        )

    return render_template("index.html", password=generated_password)


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=False)
