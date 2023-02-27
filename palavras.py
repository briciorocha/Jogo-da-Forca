import random



palavras_nivel_1 = ["anta","alce","asno", "atum","boi","boto","bode","dodô","égua","ema","foca","gato","galo","gnu","jacu","leão","lobo","mula","naja","onça","orca","osga","pato","preá","rato","rã","rena","sapo","siri","tatu","urso","vaca","yak","zebu"]


palavras_nivel_2 = ["abelha","aranha","arara","águia","abutre","ácaro","antílope","anaconda","avestruz","albatroz","alpaca","arraia","baleia","burro","barata","búfalo","besouro","bisonte",
"cachorro","cavalo","canguru","camelo","coala","chita","capivara","cutia","castor","cobra","camaleão","coelho","carneiro","cabra","cabrito",
"cascavel","cisne","coruja","cegonha","corvo ","doninha","dourada","elefante","esquilo","enguia","flamingo","formiga","falcão","furão","faisão",
"flautim","figuinha","gaivota","galinha","ganso","gambá","gavião","girafa","golfinho","gorila","girino","gazela","garça","guará","guará","grilo","hiena","hamster","iguana","impala","irara","itapema","jacaré","jumento","jegue","jiboia","javali","joaninha","jararaca","jaguar","jabuti",
"jabiru","jamanta","krill","leopardo","lagarto","lagarta","lacraia","lebre","lêmure","lhama","lontra","lesma","macaco","morcego","mosca","mosquito",
"minhoca","mangangá","morsa","mariposa","moreia","mexilhão","marreco","marmota","marmota","mamute","medusa","narceja","ovelha","ostra","ouriço","papagaio",
"pavão","pantera","preguiça","pônei","porco","pica-pau","pinguim","pulga","piolho","piranha","quati","quelea ","ratazana","raposa","rouxinol","rolinha",
"robalo","rabudo","sabiá","sagui","saúva","sardinha","sucuri","suricate","surucucu","salmão","seriema","tigre","tubarão","touro","tamanduá",
"tucano","toupeira","texugo","tainha","truta","urubu","vespa","veado","víbora","ynambu","zebra","zangão"]



palavras_nivel_3 = ["borboleta", "beija-flor","bem-te-vi","bicho-preguiça","bicho-da-seda","bacalhau","chimpanzé","cachalote","crocodilo","dromedário","dinossauro","escorpião","escaravelho","elefante-marinho","estrela-do-mar","gafanhoto","guaxinim","hipopótamo","joão-de-barro","lagartixa","libélula","marimbondo","mastodonte","noivinha","orangotango","ornitorrinco","porco-espinho","porquinho-da-índia","quatipuru","rinoceronte","surucucurana","sanguessuga","salamandra","tartaruga","tarântula","tentilhão","tico-tico","urso-panda","unicórnio","vagalume","viúva-negra","vira-bosta"]

palavas_selecionadas = []


def seleciona_palavra(nivel):
    palavra_ja_selecionada = False
    palavra = ''
    palavra_tmp = ''
    if nivel == 1:
        while not palavra_ja_selecionada:
            palavra_tmp = random.choice(palavras_nivel_1).upper()
            if palavra_tmp not in palavas_selecionadas:
                palavra = palavra_tmp
                palavas_selecionadas.append(palavra)
                palavra_ja_selecionada = True
                palavra_tmp =''
            
    if nivel == 2:
        while not palavra_ja_selecionada:
            palavra_tmp = random.choice(palavras_nivel_2).upper()
            if palavra_tmp not in palavas_selecionadas:
                palavra = palavra_tmp
                palavas_selecionadas.append(palavra)
                palavra_ja_selecionada = True
                palavra_tmp =''               

    if nivel == 3:
        while not palavra_ja_selecionada:
            palavra_tmp = random.choice(palavras_nivel_3).upper()
            if palavra_tmp not in palavas_selecionadas:
                palavra = palavra_tmp
                palavas_selecionadas.append(palavra)
                palavra_ja_selecionada = True
                palavra_tmp =''
            

    return palavra