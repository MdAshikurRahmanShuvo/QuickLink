from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>QuickLinks</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background: #f0f2f5;
                    margin: 0;
                    padding: 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    min-height: 100vh;
                }

                .container {
                    background: white;
                    width: 400px;
                    padding: 30px;
                    border-radius: 12px;
                    box-shadow: 0px 4px 20px rgba(0,0,0,0.1);
                    text-align: center;
                }

                h1 {
                    color: #333;
                    margin-bottom: 20px;
                }

                ul {
                    list-style: none;
                    padding: 0;
                }

                ul li {
                    margin: 12px 0;
                }

                a {
                    display: block;
                    padding: 12px;
                    background: #2563eb;
                    color: white;
                    border-radius: 8px;
                    text-decoration: none;
                    font-size: 18px;
                    transition: 0.25s;
                }

                a:hover {
                    background: #1e40af;
                    transform: translateY(-3px);
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>QuickLinks</h1>
                <ul>
                    <li><a href="https://www.google.com" target="_blank">Google</a></li>
                    <li><a href="https://www.github.com" target="_blank">GitHub</a></li>
                    <li><a href="https://www.stackoverflow.com" target="_blank">Stack Overflow</a></li>
                    <li><a href="https://www.reddit.com" target="_blank">Reddit</a></li>
                    <li><a href="https://www.wikipedia.org" target="_blank">Wikipedia</a></li>
                </ul>
            </div>
        </body>
        </html>
    """)
#but it is not good practise . good practise is to use templates