from flask import Flask, request, send_file
import subprocess

app = Flask(__name__)

@app.route('/executar-python', methods=['POST'])
def executar_python():
    try:
        # Executa o script de amostragem
        subprocess.run(['python3', 'amostragem.py'], check=True)
        return {'mensagem': 'Script executado com sucesso!'}
    except subprocess.CalledProcessError as e:
        return {'erro': f'Erro ao executar o script: {e}'}, 500

@app.route('/download', methods=['GET'])
def download_file():
    return send_file('coordenadas.txt', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
