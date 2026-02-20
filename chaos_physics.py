from flask import Flask, render_template_string
import random

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Chaos Engine</title>
</head>
<body style="margin:0; background:black;">
<canvas id="canvas"></canvas>
<script>
let canvas = document.getElementById("canvas");
let ctx = canvas.getContext("2d");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

let particles = [];

for (let i = 0; i < 100; i++) {
    particles.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        vx: (Math.random() - 0.5) * 4,
        vy: (Math.random() - 0.5) * 4
    });
}

function update() {
    ctx.fillStyle = "rgba(0,0,0,0.2)";
    ctx.fillRect(0,0,canvas.width,canvas.height);

    ctx.fillStyle = "white";

    particles.forEach(p => {
        p.x += p.vx;
        p.y += p.vy;

        if (p.x < 0 || p.x > canvas.width) p.vx *= -1;
        if (p.y < 0 || p.y > canvas.height) p.vy *= -1;

        ctx.beginPath();
        ctx.arc(p.x, p.y, 2, 0, Math.PI * 2);
        ctx.fill();
    });

    requestAnimationFrame(update);
}

update();
</script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)
