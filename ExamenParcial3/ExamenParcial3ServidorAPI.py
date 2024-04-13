import platform, sys, subprocess, json
from flask import Flask, jsonify

app = Flask(__name__) 

file_name = "data.json"
sistemaop = sys.platform
sistema = platform.system()
version = platform.win32_ver()
hostname = platform.node()
# print("Estamos en {}".format(sistema), " en version: {}".format(version))
# print ("Tipo SO: {}".format(sistemaop))
if sistema == 'Windows':
    local = subprocess.getoutput("""for /f "tokens=2 delims=[]" %a in ('ping -n 1 -4 "%computername%"') do @echo %a""")
print(hostname)
print(local)

maquina = [    
{"hostname":hostname, 
 "ip":local, 
 "SO":sistemaop}
]

@app.route('/', methods=['GET'])
def get_tasks():
    return jsonify (maquina)

if __name__ == '__main__':
    app.run(debug=True)