from db_config import create_app, redirect

app = create_app()
@app.route('/')
def index():
 return redirect('/apidocs/#')

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))  # Obtem a porta fornecida pelo Render
    app.run(host='0.0.0.0', port=port, debug=True)
