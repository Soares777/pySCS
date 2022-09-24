import telepot   
import requests 
import time
import requests as GET 
import threading        
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
import socket, ssl
from time import sleep 
import random
import datetime
from random import randint
import subprocess 
import json 
from bs4 import BeautifulSoup  
from bs4 import BeautifulSoup as bs 
import requests   
from bs4 import BeautifulSoup  
from bs4 import BeautifulSoup as bs 
import requests as GET           
bot = telepot.Bot("5499532499:AAGN1dPqTlDhrur5huJiTqWBgpyy0NW-li4")

mydono = [2010161918, 1564259658]
grupo = [-]

def vizinhos(cpf):
	envia = requests.get(f"https://tudosobretodos.info/{cpf}", headers={'Host': 'tudosobretodos.info', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'save-data': 'on', 'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-A107M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'cross-site', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7', 'cookie': '__cfduid=dc3ac236c5f39888dbd7f585eedf6feb11596724421', 'cookie': '_ga=GA1.2.971515152.1596724424', 'cookie': '_gid=GA1.2.109978583.1596724424'}).text

#soup = BeautifulSoup(envia.text, 'html.parser')
	if "itemMoradores" in envia:
		viz1 = envia.split("<div class='itemMoradores'>")[1].split("<")[0][3:40]

		if "itemMoradores" in envia:
			try:
				viz25 = envia.split("<div class='itemMoradores'>")[2].split("</div>")[0][3:40]
				viz444 = f"2: {viz25}"
			except:
				viz444 = ""
		if "itemMoradores" in envia:
			try:
				viz3 = envia.split("<div class='itemMoradores'>")[3].split("</div>")[0][3:40]
				viz44 = f"3: {viz3}"
			except:
				viz44 = ""

		if "itemMoradores" in envia:
			try:
				viz = envia.split("<div class='itemMoradores'>")[4].split("</div>")[0][3:40]
				viz4 = f"4: {viz}"
			except:
				viz4 = ""
		
		if "itemMoradores" in envia:
			try:
				vizz = envia.split("<div class='itemMoradores'>")[5].split("</div>")[0][3:40]
				viz5 = f"5: {vizz}"
			except:
				viz5 = ""	
		manda = f"<b>VIZINHOS:</b>\n   <code>1: {viz1}{viz444}{viz44}{viz4}{viz5}</code>"
		return manda
	else:
		return " "

def auxilio(cpf):
	envia = requests.get(f"http://www.portaltransparencia.gov.br/busca/resultado?termo={cpf}&pagina=1&tamanhoPagina=10", headers={'Host': 'www.portaltransparencia.gov.br', 'Connection': 'keep-alive', 'Accept': '*/*', 'X-Requested-With': 'XMLHttpRequest', 'Save-Data': 'on', 'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SM-A107M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36', 'Referer': 'http://www.portaltransparencia.gov.br/busca?termo=073.048.496-30', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7', 'Cookie': '_ga=GA1.3.69009689.1596719777; _gid=GA1.3.532974999.1596719777; JSESSIONID=f02wMy61gbWQzzhJfNBg76lg9ZuyrYE0L-vS3qwo.idc-jboss2-ap8-p'})

	js = envia.json()
	total = js["totalRegistros"]
	if "1" in str(total):
		if "Beneficiário do Programa Auxílio Emergencial" in envia.text:
			aux = "Beneficiário do Programa Auxílio Emergencial"
			ben = f"<code>Sim</code>\n<b>AVISO</b>: <code>{aux}</code>"
		else:
			ben = "<code>Não</code>"
	else:
		ben = "<code>Não encontrado.</code>"
	return ben		
def cadsus(cpf, nasc):
    session = requests.Session()
    t = session.get("http://cnesadm.datasus.gov.br/cnesadm/publico/usuarios/cadastro", headers={
        "User-Agent": "Mozilla/5.0 (Linux; Android 9; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Referer": "http://cnesadm.datasus.gov.br/cnesadm/publico/usuarios/cadastro"
    }).text
    soup = bs(t, "html.parser")
    csrf = soup.find("input", {"name": "_csrf"}).get("value")
    post = session.post("http://cnesadm.datasus.gov.br/cnesadm/publico/usuarios/cadastro", data={
        "cpf": cpf,
        "dataNascimento": nasc,
        "_csrf": csrf
    }).text
    soup = bs(post, "html.parser")
    if "CNS" in post:
        cns = soup.find("input", {"name": "cns"}).get("value")
    else:
    	cns = "Não encontrado"
    return cns
    
def consulta_cpf2(cpf):

	consulta = requests.post("http://www.juventudeweb.mte.gov.br/pnpepesquisas.asp", headers={
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Linux; Android 9; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
	            }, data={"acao": "consultar cpf",
    "cpf": cpf
	                }).text.upper().replace('"', '')
	                
	if "PESSOAFISICA" in consulta:
		
		nome = consulta.split("NOPESSOAFISICA=")[1].split("DTNASCIMENTO")[0]	         
		nasc = consulta.split("DTNASCIMENTO=")[1].split("NOLOGRADOURO")[0]	      
		nascns = f"""{nasc[0:2]}{nasc[2:5]}{nasc[5:10]}"""		
		mae = consulta.split("NOMAE=")[1].split("/>")[0]	      
		lgd = consulta.split("NOLOGRADOURO=")[1].split("NRLOGRADOURO")[0]	              
		logradouro = consulta.split("NRLOGRADOURO=")[1].split("DSCOMPLEMENTO")[0]
		cep = consulta.split("NRCEP=")[1].split(" ")[0]
		bairro = consulta.split("NOBAIRRO=")[1].split("NRCEP")[0]
		muni = consulta.split("NOMUNICIPIO=")[1].split("SGUF")[0]
		cp = consulta.split("DSCOMPLEMENTO=")[1].split("NOBAIRRO")[0]  
		uf = consulta.split("SGUF=")[1].split(" ")[0]
		session = requests.Session()
		t = session.get("http://cnesadm.datasus.gov.br/cnesadm/publico/usuarios/cadastro", headers={
        "User-Agent": "Mozilla/5.0 (Linux; Android 9; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Referer": "http://cnesadm.datasus.gov.br/cnesadm/publico/usuarios/cadastro"
    }).text
		soup = bs(t, "html.parser")
		csrf = soup.find("input", {"name": "_csrf"}).get("value")
		post = session.post("http://cnesadm.datasus.gov.br/cnesadm/publico/usuarios/cadastro", data={
        "cpf": cpf,
        "dataNascimento": nascns,
        "_csrf": csrf
    }).text
		soup = bs(post, "html.parser")
		if "CNS" in post:
			cns = soup.find("input", {"name": "cns"}).get("value")
		else:
			cns = "Não encontrado"
		id = nasc[6:10]
		idade = 2020 - int(id)
		manda = vizinhos(cpf)
		dados = f"""<b>DADOS DO CPF [{cpf}] ENCONTRADOS:</b>\n\n<b>CPF:</b> <code>{cpf}</code>\n<b>CNS:</b> <code>{cns}</code>\n<b>NOME:</b> <code>{nome}</code>\n<b>NASCIMENTO:</b> <code>{nasc}</code>\n<b>MÃE:</b> <code>{mae}</code>\n<b>IDADE:</b> <code>{idade}</code>\n
{vizinhos(cpf)}
<b>ENDEREÇO:</b> <pre>{lgd}</pre>\n<b>COMPLEMENTO:</b> <pre>{cp}</pre>\n<b>NÚMERO:</b> <pre>{logradouro}</pre>\n<b>BAIRRO:</b> <pre>{bairro}</pre>\n<b>MUNICÍPIO:</b> <pre>{muni}</pre>\n<b>CEP:</b> <pre>{cep}</pre>\n<b>ESTADO:</b> <pre>{uf}</pre>\n

<b>OBS:</b> <code>Está consulta se apagará em 2 minutos.</code>\n\n<b>OBS:</b> <code>Compre acesso a meu privado com:</code> @EUTHEUZIN"""		
	else:
		dados = f"<b>CPF [{cpf}] INVALIDO!</b>"   

	return dados
	

def main_thread(*args, **kwargs):
	t = threading.Thread(target=main, args=args, kwargs=kwargs)
	t.daemon = True
	t.start()

def on_callback_query(msg):
	c_id = msg["message"]["chat"]["id"]
	m_id = msg["message"]["message_id"]
	data = msg["data"]
	if(data=="delete"):
		if(not msg["from"]["id"] == msg["message"]["reply_to_message"]["from"]["id"]):
			bot.answerCallbackQuery(msg["id"], '⚠️ Você não tem permissão para apagar esta mensagem!', show_alert=True)
		else:
			bot.deleteMessage((c_id, m_id))
			bot.deleteMessage((c_id, msg["message"]["reply_to_message"]["message_id"]))
			
def main(msg):
	botao = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=f"🗑 Apagar 🗑", callback_data="delete")]])
	
	if("text" in msg):
		text = msg["text"]
	else:
		text = ""
	chat = msg["chat"]["id"]
	name = msg["from"]["first_name"]
	id = msg["from"]["id"]

	if(text.upper() == "/ID"):
		bot.sendMessage(chat, f"ID: {chat}")

	permissao = json.load(open("legits.json"))
	if(str(msg["chat"]["id"])) in permissao:	
		if(text.upper() == "/START"):
			bot.sendMessage(chat, f"""<b>Consulte cpf assim:</b>
<code>/cpf 00000000000</code>

  """, reply_to_message_id=msg["message_id"], parse_mode="html")
	
		if(text.split()[0].upper() == "/CPF" and text.split()[1]):
			cpf = text.split()[1]
			sent = bot.sendMessage(msg["chat"]["id"], f"{name},<b>Coletando informações do CPF [{cpf}]...</b>", "html", reply_to_message_id=msg["message_id"])			
			dados = consulta_cpf2(cpf)
			bot.editMessageText((msg["chat"]["id"], sent["message_id"]), dados, "html", reply_markup=botao) 
			time.sleep(120)
			bot.deleteMessage((sent['chat']['id'], sent['message_id']))
			c_id = msg["chat"]["id"]
			m_id = msg["message_id"]
			bot.deleteMessage((c_id, m_id))

	if(msg["from"]["id"] in mydono):
		if("text" in msg):
			text = msg["text"]
		else:
			text = ""

		if(text.upper() == "/LISTA"):
			usuarios = []
			for i in permissao:
				data = datetime.datetime.fromtimestamp(permissao[i]['permitido_desde'])
				usuarios.append(f"""{permissao[i]['nome']} - <code>{i}</code>
Desde: {data.day}/{data.month}/{data.year}""")
			bot.sendMessage(msg["chat"]["id"], """<b>Usuários cadastrados:</b>

{}""".format('\n\n'.join(usuarios)), parse_mode="HTML")

		if(text.split()[0].upper() == "/ADD" and text.split()[1]):
			try:
				user = text.split()[1]
				usr = bot.getChat(user)
				try:
					name = usr["first_name"]
				except KeyError:
					name = usr["title"]
				permissao[user] = dict(nome=name, permitido_desde=int(time.time()))
				with open("legits.json", "w") as file:
					file.write(json.dumps(permissao))
				bot.sendMessage(msg["chat"]["id"], f"<b>O chat {name} ({user}) foi adicionado com sucesso.</b>", parse_mode="HTML")
			except Exception as e:
				bot.sendMessage(msg["chat"]["id"], "<b>Ocorreu um erro, provavelmente o usuário não iniciou o bot.</b>", parse_mode="HTML")
				raise

		if(text.split()[0].upper() == "/REMOVE" and text.split()[1]):
			try:
				user = text.split()[1]
				name = permissao[user]["nome"]
				del permissao[user]
				with open("legits.json", "w") as file:
					file.write(json.dumps(permissao))
				bot.sendMessage(msg["chat"]["id"], f"<b>O chat {name} ({user}) foi removido com sucesso da db.</b>", parse_mode="HTML")
			except:
				bot.sendMessage(msg["chat"]["id"], "<b>Ocorreu um erro, provavelmente o usuário não existe na db.</b>", parse_mode="HTML")
 
MessageLoop(bot, {
    'chat': main_thread,
    'callback_query': on_callback_query}).run_as_thread()

while True:
 pass
 
