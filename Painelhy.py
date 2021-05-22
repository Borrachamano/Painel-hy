import requests
import hashlib
import pytube
import os
import time

# Cores
a = '\033[33m' # Amarelo
v = '\033[31m' # Vermelho
az = '\033[36m' # Azul
vr = '\033[32m' # Verde
r = '\033[35m' # roxo
b = '\033[m' # Sem cor

while True:
	print(f'{vr}-{b}'*40)
	print(f'{a}{"PAINEL-HY":^40}{b}')
	print(f'{vr}-{b}'*40)
	print(f'''\
{a}({b} 1 {a}){b} - {vr}Consulta CEP{b}
{a}({b} 2 {a}){b} - {vr}Consulta IP{b}
{a}({b} 3 {a}){b} - {vr}Consulta IPWHOIS{b}
{a}({b} 4 {a}){b} - {vr}Consulta placa{b}
{a}({b} 5 {a}){b} - {vr}Informacoes do covid{b}
{a}({b} 6 {a}){b} - {vr}Consulta codigo bancario{b}
{a}({b} 7 {a}){b} - {vr}Conversor de md5{b}
{a}({b} 8 {a}){b} - {vr}Conversor de md4{b}
{a}({b} 9 {a}){b} - {vr}Download de videos yt{b}
{a}({b} 0 {a}){b} - {vr}sair{b} ''')
	print(f'{vr}-{b}'*40)
	menu = str(input(f'{r}>>>{b} '))
	time.sleep(1.5)
	
	
	# Consulta cep
	if menu == '1':
		os.system('clear')
		print(f'{vr}-{b}'*40)
		print(f'{a}{"CONSULTA CEP":^40}{b}')
		print(f'{vr}-{b}'*40)
		print(f'{az}Informe o CEP que deseja consultar: {b}')
		cep = input(f'{r}>>>{b} ')
		while len(cep) != 8:
			print(f'{v}Por favor, Digite um cep valido.{b}')
			cep = input(f'{r}>>>{b} ')
		request = requests.get(f'https://viacep.com.br/ws/{cep}/json/').json()
		print(f'{vr}={b}'*40)
		# Deu certo
		if 'erro' not in request:
			print(f'CEP: {request["cep"]}')
			print(f'RUA: {request["logradouro"]}')
			print(f'BAIRRO: {request["bairro"]}')
			print(f'LOCALIDADE: {request["localidade"]}')
			print(f'UF: {request["uf"]}')
			print(f'IBGE: {request["ibge"]}')
			print(f'DDD: {request["ddd"]}')
		# Deu errado
		else:
			print(f'{v}Cep não encontrado.{v}')
		print(f'{vr}={b}'*40)
		print(f'{az}Aperte enter para voltar ao menu.{b}')
		enter = input(f'{r}>>>{b} ')
	
	
	
	# Consulta ip
	elif menu == '2':
		os.system('clear')
		print(f'{vr}-{b}'*40)
		print(f'{a}{"CONSULTA IP":^40}{b}')
		print(f'{vr}-{b}'*40)
		print(f'{az}Informe o IP que deseja consultar: {b}')
		ip = input(f'{r}>>>{b} ')
		ip_api = requests.get(f'http://ip-api.com/json/{ip}').json()
		print(f'{a}={b}'*40)
		if ip_api['status'] == 'success':
			print(f'IP ADRESS: {ip_api["query"]}')
			print(f'PAIS: {ip_api["country"]}')
			print(f'CODIGO DO PAIS: {ip_api["countryCode"]}')
			print(f'REGIAO: {ip_api["region"]}')
			print(f'NOME DA REGIAO: {ip_api["regionName"]}')
			print(f'CIDADE: {ip_api["city"]}')
			print(f'LATITUDE: {ip_api["lat"]}')
			print(f'LONGITUDE: {ip_api["lon"]}')
			print(f'FUSSO HORARIO: {ip_api["timezone"]}')
			print(f'ISP: {ip_api["isp"]}')
			print(f'ORG: {ip_api["org"]}')
		else:
			print(f'{v}IP não encontrado.{b}')
		print(f'{a}={b}'*40)
		print(f'{az}Aperte enter para voltar ao menu.{b}')
		enter = input(f'{r}>>>{b} ')
	
	
	
	
	# Consulta ip atualizado
	elif menu == '3':
		os.system('clear')
		print(f'{vr}-{b}'*40)
		print(f'{a}{"CONSULTA IPWHOIS":^40}{b}')
		print(f'{vr}-{b}'*40)
		print(f'{az}Informe o IP que deseja consultar:{b} ')
		ipwhois = input(f'{r}>>>{b} ')
		ipwhois_api = requests.get(f'http://ipwhois.app/json/{ipwhois}').json()
		print(f'{vr}={b}'*40)
		if ipwhois_api['success'] == True:
			print(f'IP ADRESS: {ipwhois_api["ip"]}')
			print(f'TIPO: {ipwhois_api["type"]}')
			print(f'CONTINENTE: {ipwhois_api["continent"]}')
			print(f'CODIGO DO CONTINENTE: {ipwhois_api["continent_code"]}')
			print(f'PAIS: {ipwhois_api["country"]}')
			print(f'CODIGO DO PAIS: {ipwhois_api["country_code"]}')
			print(f'CAPITAO DO PAIS: {ipwhois_api["country_capital"]}')
			print(f'TELEFONE DO PAIS: {ipwhois_api["country_phone"]}')
			print(f'REGIAO: {ipwhois_api["region"]}')
			print(f'CIDADE: {ipwhois_api["city"]}')
			print(f'LATITUDE: {ipwhois_api["latitude"]}')
			print(f'LONGITUDE: {ipwhois_api["longitude"]}')
			print(f'ASN: {ipwhois_api["asn"]}')
			print(f'ORG: {ipwhois_api["org"]}')
			print(f'ISP: {ipwhois_api["isp"]}')
			print(f'FUSSO HARARIO: {ipwhois_api["timezone"]}')
			print(f'MOEDA: {ipwhois_api["currency"]}')
			print(f'SIMBOLO DA MOEDA: {ipwhois_api["currency_symbol"]}')
		else:
			print(f'{v}Esse IP não foi encontrado.{b}')
		print(f'{vr}={b}'*40)
		print(f'{az}Aperte enter para voltar ao menu.{b}')
		enter = input(f'{r}>>>{b} ')
	
	
	

	# Consulta placa
	elif menu == '4':
		os.system('clear')
		print(f'{vr}-{b}'*40)
		print(f'{a}{"Consulta PLACA":^40}{b}')
		print(f'{vr}-{b}'*40)
		print(f'{az}Informe a placa que deseja consultar:{b} ')
		placa = input(f'{r}>>>{b} ')
		req = requests.get(f'https://apicarros.com/v1/consulta/{placa}/json', verify=False).json()
		os.system('clear')
		if 'codigoRetorno' in req and req['codigoRetorno'] == '0':
			print(f'{vr}-{b}'*40)
			print(f'{a}{"Informacoes da Placa":^40}{b}')
			print(f'{vr}-{b}'*40)
			print(f'Ano: {req["ano"]}')
			print(f'Data: {req["data"]}')
			print(f'Modelo: {req["modelo"]}')
			print(f'Ano do modelo: {req["anoModelo"]}')
			print(f'Cor: {req["cor"]}')
			print(f'Marca: {req["marca"]}')
			print(f'Roubo/Furto: {req["dataAtualizacaoRouboFurto"]}')
			print(f'Situacao: {req["situacao"]}')
			print(f'Placa: {req["placa"]}')
			print(f'UF: {req["uf"]}')
			print(f'Municipio: {req["municipio"]}')
			print(f'Modificada em: {req["dataAtualizacaoCaracteristicasVeiculo"]}')
			print(f'Alarme atualizado: {req["dataAtualizacaoAlarme"]}')
			print(f'Mensagem de retorno: {req["mensagemRetorno"]}')
			print(f'Codigo de retorno: {req["codigoRetorno"]}')
			print(f'{vr}={b}'*40)
		else:
			print(f'{vr}-{b}'*40)
			print(f'{v}{"Placa não encontrada":^40}{b}')
			print(f'{vr}-{b}'*40)
		print(f'{az}Aperte enter para voltar ao menu.{b}')
		enter = input(f'{r}>>>{b} ')
	
	
	
	
	# Informacoes do covid
	elif menu == '5':
		os.system('clear')
		print(f'{vr}-{b}'*40)
		print(f'{a}{"Informacoes do covid 19":^40}{b}')
		print(f'{vr}-{b}'*40)
		print(f'{az}Informe o UF, exemplo: mt, sp, pa.{b}')
		uf = input(f'{r}>>>{b} ')
		req = requests.get(f'https://covid19-brazil-api.vercel.app/api/report/v1/brazil/uf/{uf}')
		info = req.json()
		print(f'{a}={b}'*51)
		if 'error' not in info and 'data' not in info:
			print(f'DATE E HORARIO LOCAL: {info["datetime"]}')
			print(f'UF: {info["uf"]}')
			print(f'UID: {info["uid"]}')
			print(f'ESTADO: {info["state"]}')
			print(f'CASOS: {info["cases"]}')
			print(f'MORTES: {info["deaths"]}')
			print(f'Suspeitos: {info["suspects"]}')
			print(f'RECUSADOS: {info["refuses"]}')
		else:
			print(f'{v}UF invalido. Tente novamente.{b}')
		print(f'{a}={b}'*51)
		print(f'{az}Aperter enter para voltar ao menu.{b}')
		enter = input(f'{r}>>>{b} ')
		
	
	
	
	# Consulta banco
	elif menu == '6':
		os.system('clear')
		print(f'{vr}-{b}'*40)
		print(f'{a}{"Consulta codigo bancario":^40}{b}')
		print(f'{vr}-{b}'*40)
		print(f'{az}Informe o codigo bancario para fazer a consulta:{b} ')
		banco = input(f'{r}>>>{b} ')
		banc_api = requests.get(f'https://brasilapi.com.br/api/banks/v1/{banco}').json()
		print(f'{vr}={b}'*40)
		if 'message' not in banc_api:
			print(f'Nome: {banc_api["name"]}')
			print(f'Nome Completo: {banc_api["fullName"]}')
			print(f'ISPB: {banc_api["ispb"]}')
		else:
			print(f'{v}Codigo bancario invalido. Tente novamente.{b}')
		print(f'{vr}={b}'*40)
		print(f'{az}Aperte enter para voltar ao menu.{b}')
		enter = input(f'{r}>>>{b} ')
	
	
	
	
	# Conversor de md4
	elif menu == '7':
		os.system('clear')
		print(f'{vr}-{b}'*40)
		print(f'{a}{"Conversor de md5":^40}{b}')
		print(f'{vr}-{b}'*40)
		print(f'{az}Digite a string para fazer o hash:{b} ')
		string = input(f'{r}>>>{b} ')
		md5 = hashlib.md5(string.encode())
		print(f'{vr}-{b}'*40)
		print(f'{a}Hash:{b} {md5.hexdigest()}')
		print(f'{vr}-{b}'*40)
		print(f'{az}Aperter enter para voltar ao menu.{b}')
		enter = input(f'{r}>>>{b} ')
	
	
	
	# Conversor de md4
	elif menu == '8':
		os.system('clear')
		print(f'{vr}-{b}'*40)
		print(f'{a}{"Conversor de md4":^40}{b}')
		print(f'{vr}-{b}'*40)
		print(f'{az}Digite a string para fazer o hash:{b} ')
		str = input(f'{r}>>>{b} ')
		md4 = hashlib.new('md4', str.encode())
		print(f'{vr}-{b}'*40)
		print(f'{a}Hash:{b} {md4.hexdigest()}')
		print(f'{vr}-{b}'*40)
		print(f'{az}Aperte enter para voltar ao menu.{b}')
		enter = input(f'{r}>>>{b} ')
	
	
	# Download videos 
	elif menu == '9':
		os.system('clear')
		print(f'{vr}-{b}'*40)
		print(f'{a}{"Download de videos":^40}{b}')
		print(f'{vr}-{b}'*40)
		print(f'{a}Digite a url do video que deseha baixa:{b} ')
		url = input(f'{r}>>>{b} ')
		video = pytube.YouTube(url).streams.first()
		print(f'{vr}-{b}'*34)
		print(f'{a}Fazendo download...Tenha calma!{b}')
		video.download(output_path='downloads')
		print(f'{a}Dowload Feito!{b}')
		print(f'{vr}-{b}'*34)
		print(f'{az}Aperte enter para voltar ao menu.{b}')
		enter = input(f'{r}>>>{b} ')
	
	
	elif menu == '0':
		break
	
	
	else:
		print(f'{v}Opção invalida. Tente novamente.{b}')
		print(f'{a}-{b}'*40)
		print(f'{az}Aperter enter para voltar ao menu.{b}')
		ent = input(f'{r}>>>{b} ')
	
	os.system('clear')


print(f'{a}Programa finalizado. Volte sempre!{b}')
