from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>DevOps App</title>

        <!-- Google Font -->
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap" rel="stylesheet">

        <style>
            *{
                margin:0;
                padding:0;
                box-sizing:border-box;
                font-family:'Poppins',sans-serif;
            }

            body{
                height:100vh;
                display:flex;
                justify-content:center;
                align-items:center;
                background:linear-gradient(135deg,#4facfe,#00f2fe);
            }

            .card{
                background:white;
                padding:40px;
                width:420px;
                border-radius:20px;
                text-align:center;
                box-shadow:0 15px 35px rgba(0,0,0,0.2);
                animation:fadeIn 1s ease;
            }

            .logo{
                width:90px;
                height:90px;
                margin:auto;
                border-radius:50%;
                background:linear-gradient(45deg,#4facfe,#00f2fe);
                display:flex;
                justify-content:center;
                align-items:center;
                color:white;
                font-size:40px;
                font-weight:bold;
                box-shadow:0 8px 20px rgba(0,0,0,0.2);
            }

            h1{
                margin-top:20px;
                color:#333;
                font-size:32px;
            }

            p{
                color:#666;
                margin:15px 0 30px;
                font-size:16px;
                line-height:1.6;
            }

            .btn{
                display:inline-block;
                text-decoration:none;
                padding:12px 28px;
                background:#4facfe;
                color:white;
                border-radius:30px;
                font-weight:600;
                transition:.3s;
            }

            .btn:hover{
                background:#008cff;
                transform:translateY(-3px);
            }

            @keyframes fadeIn{
                from{
                    opacity:0;
                    transform:translateY(30px);
                }
                to{
                    opacity:1;
                    transform:translateY(0);
                }
            }

            footer{
                margin-top:25px;
                color:#999;
                font-size:13px;
            }
        </style>
    </head>

    <body>

        <div class="card">

            <div class="logo">⚙️</div>

            <h1>DevOps Dashboard</h1>

            <p>
                🚀 Flask application is successfully deployed and running.
                Welcome to your modern DevOps demo application.
            </p>

            <a href="#" class="btn">Explore</a>

            <footer>
                Built with ❤️ using Flask & Python
            </footer>

        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
