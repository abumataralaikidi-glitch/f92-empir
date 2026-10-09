from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI(title="F-92 Sovereign Empire - Android & Web UI Interface")

class TextInteraction(BaseModel):
    commander_input: str

@app.get("/", response_html=True, response_class=HTMLResponse)
def serve_ui():
    html_content = """
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>F-92 Sovereign Empire - لوحة القيادة والكتابة</title>
        <style>
            body {
                background-color: #0d1117;
                color: #c9d1d9;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                margin: 0;
                padding: 20px;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                min-height: 100vh;
            }
            .container {
                background-color: #161b22;
                border: 1px solid #30363d;
                border-radius: 12px;
                padding: 30px;
                width: 100%;
                max-width: 600px;
                box-shadow: 0 8px 24px rgba(0,0,0,0.5);
            }
            h1 {
                color: #58a6ff;
                text-align: center;
                font-size: 24px;
                margin-bottom: 10px;
            }
            .subtitle {
                text-align: center;
                color: #8b949e;
                font-size: 14px;
                margin-bottom: 25px;
            }
            textarea {
                width: 100%;
                height: 120px;
                background-color: #0d1117;
                border: 1px solid #30363d;
                border-radius: 8px;
                color: #ffffff;
                padding: 12px;
                font-size: 16px;
                resize: none;
                box-sizing: border-box;
                margin-bottom: 15px;
            }
            textarea:focus {
                border-color: #58a6ff;
                outline: none;
            }
            button {
                background-color: #238636;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 12px 20px;
                font-size: 16px;
                cursor: pointer;
                width: 100%;
                font-weight: bold;
                transition: background-color 0.2s;
            }
            button:hover {
                background-color: #2ea043;
            }
            .output-box {
                margin-top: 20px;
                background-color: #0d1117;
                border: 1px solid #30363d;
                border-radius: 8px;
                padding: 15px;
                min-height: 80px;
                color: #7ee787;
                white-space: pre-wrap;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>إمبراطورية F-92 السيادية</h1>
            <div class="subtitle">لوحة الكتابة والتحكم المباشر - العراب: صلاح الدين سامي</div>
            
            <label for="userInput">أدخل الأوامر أو النصوص هنا:</label>
            <textarea id="userInput" placeholder="اكتب هنا ما تشاء لتنفيذه عبر إمبراطورية F-92..."></textarea>
            
            <button onclick="sendData()">إرسال وتجهيز الأمر</button>
            
            <div class="output-box" id="outputResult">استجابة الإمبراطورية ستظهر هنا...</div>
        </div>

        <script>
            async function sendData() {
                const text = document.getElementById('userInput').value;
                const outputDiv = document.getElementById('outputResult');
                
                if (!text.trim()) {
                    outputDiv.innerText = "برجاء كتابة نص أو أمر أولاً يا عراب.";
                    return;
                }

                outputDiv.innerText = "جاري المعالجة بواسطة العصب المركزي للإمبراطورية...";

                try {
                    const response = await fetch('/api/ui/process', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ commander_input: text })
                    });
                    const data = await response.json();
                    outputDiv.innerText = "الرد السيادي:\\n" + JSON.stringify(data, null, 2);
                } catch (error) {
                    outputDiv.innerText = "حدث خطأ في الاتصال بالسيرفر السيادي.";
                }
            }
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.post("/api/ui/process")
def process_ui_input(data: TextInteraction):
    return {
        "status": "Success",
        "commander": "صلاح الدين سامي (العراب)",
        "received_text": data.commander_input,
        "action_executed": "تم استقبال النص وعرضه في واجهة الكتابة بنجاح.",
        "system_status": "All systems operating at peak sovereign capacity."
    }
