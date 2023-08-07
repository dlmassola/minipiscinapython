import requests, json, dewiki, sys

def searchWiki(searchfor):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "parse",
        "page": searchfor,
        "prop": "wikitext",
        "format": "json",
        "redirects": "true"
    }

    try:
        response = requests.get(url=url, params=params)
    except Exception as e:
        print(f'Erro na chamada da API Wikipedia: {e}.')
        return
    
    try:
        data = json.loads(response.text)
    except Exception as e:
        print(f'Erro no json.loads: {e}.')
        return
    
    if data.get("error") is not None:
        print(f'Retorno da API Wikipedia com Erro: {data["error"]["info"]}')
        return
    
    content = dewiki.from_string(data["parse"]["wikitext"]["*"])
    
    try:
        f = open("{}.wiki".format(sys.argv[1].replace(" ", "_")), "w") # nome do arquivo como o de busca
        f.write(content)
        f.close
    except Exception as e:
        print(f'Erro ao criar o arquivo de saída: {e}')
    
if __name__ == '__main__':
    if len(sys.argv) == 2:
        searchWiki(sys.argv[1])
    else:
        print("Informar apenas um parâmetro.")
        
    