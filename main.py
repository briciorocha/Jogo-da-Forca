import pygame
import time
from pygame.locals import *
from sys import exit

import palavras

pygame.init()
pygame.font.init()

largura = 640
altura = 480

qtd_jogador = 1
jogador01_responde = True
erros = 0
acertos = 0
acertou_palavra = False
nivel_jogo = 1

pontos_jogador01 = 0
pontos_jogador02 = 0


fonte_titulos = pygame.font.Font(None, 50)
fonte_textos = pygame.font.Font(None, 30)
fonte_nivel = pygame.font.Font(None, 20)
fonte_info = pygame.font.Font(None, 25)
fonte_letras = pygame.font.Font(None, 40)
fonte_placar = pygame.font.Font(None, 50)

fonte_venceu_perdeu = pygame.font.Font(None, 100)

texto_deve_ditar_palavra = ''

fundo_img = pygame.image.load("assets/fundo.jpg")
fundo = fundo_img.get_rect()

fundo_menu_img = pygame.image.load("assets/fundo_menu.jpg")
fundo_menu = fundo_menu_img.get_rect()

forca_status_img =  pygame.image.load("assets/forca_erro_0.png")
forca_status = forca_status_img.get_rect(right=620, top=100)

placar_img = pygame.image.load("assets/placar.png")
placar = placar_img.get_rect(right=620, top=10)


jogador01_img = pygame.image.load("assets/jogador01.png")
jogador01 = jogador01_img.get_rect(left=(390), top=30)

jogador02_img = pygame.image.load("assets/jogador_maquina.png")
jogador02 = jogador02_img.get_rect(right=610, top=30)


jogador01_digita_palavra_img = pygame.image.load("assets/img_jogador01_digita_palavra.png")
jogador01_digita_palavra = jogador01_digita_palavra_img.get_rect(left=(100), top=80)

jogador02_digita_palavra_img = pygame.image.load("assets/img_jogador02_digita_palavra.png")
jogador02_digita_palavra = jogador02_digita_palavra_img.get_rect(left=(100), top=80)


tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo da Forca')

msg_resultado_img = pygame.image.load("assets/img_ganhou.png")
msg_resultado = msg_resultado_img.get_rect(center=[largura/2-30, altura/2-50])

msg_indica_jogador_img = pygame.image.load("assets/img_indica_jogador01.png")
msg_indica_jogador = msg_indica_jogador_img.get_rect(center=[largura/2-100, altura/2-100])

btn_iniciar_img = pygame.image.load("assets/btn_iniciar.png")
btn_iniciar = btn_iniciar_img.get_rect(center=[largura/2, altura/2+10])

btn_config_img = pygame.image.load("assets/btn_config.png")
btn_config = btn_config_img.get_rect(center=[largura/2, (altura/2)+70])

btn_home_img = pygame.image.load("assets/btn_home_40x40.png")
btn_home = btn_home_img.get_rect(right=70, top=420)

btn_reiniciar_img =  pygame.image.load("assets/btn_reiniciar_40x40.png")
btn_reiniciar = btn_reiniciar_img.get_rect(right=120, top=420)

btn_info_img =  pygame.image.load("assets/btn_info_40x40.png")
btn_info = btn_info_img.get_rect(right=620, top=420)

btn_menu_img = pygame.image.load("assets/btn_menu.png")
btn_menu = btn_menu_img.get_rect(center=[largura/2, (altura/2)+190])

btn_proxima_img = pygame.image.load("assets/btn_proxima.png")
btn_proxima = btn_proxima_img.get_rect(center=[largura/2, (altura/2)+130])

btn_home_fim_jogo = pygame.Rect((largura / 2) - 70, 360, 140, 40)
btn_reiniciar_fim_jogo = pygame.Rect((largura / 2) - 70, 410, 140, 40)

btn_jogador_vs_maquina_img = pygame.image.load("assets/btn_jogador_vs_maquina.png")
btn_jogador_vs_maquina = btn_jogador_vs_maquina_img.get_rect(left=50, top=130)

btn_jogador_vs_jogador_img = pygame.image.load("assets/btn_jogador_vs_jogador.png")
btn_jogador_vs_jogador = btn_jogador_vs_jogador_img.get_rect(left=350, top=130)

btn_continuar_img = pygame.image.load("assets/btn_continuar.png")
btn_continuar = btn_continuar_img.get_rect(center=[largura/2, (altura/2)+130])

btn_gravar_img = pygame.image.load("assets/btn_gravar.png")
btn_gravar = btn_gravar_img.get_rect(left=40, top=400)

fade_img = pygame.Surface((largura, altura)).convert_alpha()
fade = fade_img.get_rect()
fade_img.fill((0,0,0))
fade_alpha = 255


def carrega_palavra():
    if qtd_jogador == 1:
        ifem = '-'
        global palavra_selecionada
        global nivel_jogo
        global pontos_jogador01
        global estado_atual_enigma
        global qtd_ifens_na_palavra
        if palavra_selecionada == '':      
            if pontos_jogador01 < 4:
                nivel_jogo = 1
            elif pontos_jogador01 < 7:
                nivel_jogo = 2
            else:
                nivel_jogo = 3

            palavra_selecionada = palavras.seleciona_palavra(nivel_jogo)
            estado_atual_enigma = ["_"] * len(palavra_selecionada)
                    
            if ifem in palavra_selecionada:
                for i in range(len(palavra_selecionada)):
                    if ifem == palavra_selecionada[i]:
                        estado_atual_enigma[i] = ifem
                        qtd_ifens_na_palavra +=1

def limpar_variaveis():
    global erros
    global acertos
    global letras_digitadas
    global palavra_selecionada
    global qtd_ifens_na_palavra
    global lancar_ponto_jog01
    global lancar_ponto_jog02
    erros = 0
    acertos = 0
    letras_digitadas = ''
    palavra_selecionada = ''
    lancar_ponto_jog01 = True
    lancar_ponto_jog02 = True
    qtd_ifens_na_palavra =0 

def click_menu():
    audio = pygame.mixer.Sound("assets/audios/menu-click.wav")
    audio.set_volume(0.2)
    audio.play()

audio_acertou = pygame.mixer.Sound("assets/audios/acertou.wav")
audio_errou = pygame.mixer.Sound("assets/audios/errou.wav")

def audio_venceu():
    audio = pygame.mixer.Sound("assets/audios/fim_venceu.mp3")
    audio.set_volume(0.3)
    audio.play()

def audio_perdeu():
    audio = pygame.mixer.Sound("assets/audios/fim_perdeu.wav")
    audio.set_volume(0.3)
    audio.play()



text = ''
 
font = pygame.font.SysFont(None, 50)
 
img = font.render(text, True, (255, 200, 0))
 
rect = img.get_rect()
rect.topleft = (100, 240)
cursor = pygame.Rect(rect.topright, (3, rect.height))

palavra_selecionada = ''

palavra_enigma = ''
letras_digitadas = ''

letra_ja_digitada = False
lancar_ponto_jog01 = True
lancar_ponto_jog02 = True

qtd_ifens_na_palavra = 0

cena = "menu"
fps = pygame.time.Clock()


trilha = pygame.mixer.Sound("assets/audios/trilha.mp3")
trilha.set_volume(0.5)
trilha.play(-1)



while True:


    if cena == "jogo":    

        carrega_palavra()

        trilha.set_volume(0.5)

        if erros < 1:
            forca_status_img =  pygame.image.load("assets/forca_erro_0.png")
   
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
                                    
            if event.type == pygame.KEYDOWN:
                letra = event.unicode.upper()

                if letra in letras_digitadas:
                   letra_ja_digitada = True
                else:    
                    letras_digitadas += f'{letra} '
                    letra_ja_digitada = False              
                    if letra in palavra_selecionada:
                        for i in range(len(palavra_selecionada)):
                            if letra == palavra_selecionada[i]:
                                estado_atual_enigma[i] = letra
                                acertos +=1
                    else:
                        erros+=1
                        if erros == 1:
                            forca_status_img =  pygame.image.load("assets/erro_1.png")
                        elif erros == 2:
                            forca_status_img =  pygame.image.load("assets/erro_2.png")
                        elif erros == 3:
                            forca_status_img =  pygame.image.load("assets/erro_3.png")
                        elif erros == 4:
                            forca_status_img =  pygame.image.load("assets/erro_4.png")
                        elif erros == 5:
                            forca_status_img =  pygame.image.load("assets/erro_5.png")
                        elif erros == 6:
                            forca_status_img =  pygame.image.load("assets/erro_6.png")

            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_home.collidepoint(event.pos):
                    fade_alpha = 255
                    click_menu()
                    erros = 0
                    acertos = 0
                    estado_atual_enigma = ["_"] * len(palavra_selecionada)
                    letras_digitadas = ''
                    palavra_selecionada = ''
                    qtd_ifens_na_palavra =0  
                    cena = "menu"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_reiniciar.collidepoint(event.pos):
                    fade_alpha = 255
                    click_menu()
                    limpar_variaveis()
                    carrega_palavra()
                    cena = "jogo"

            if erros >= 6:
                if lancar_ponto_jog02:
                    if qtd_jogador == 1:
                        pontos_jogador02 +=1
                    elif qtd_jogador == 2:
                        if jogador01_responde:
                            pontos_jogador02 +=1
                        else:
                            pontos_jogador01 +=1

                lancar_ponto_jog02 = False
                acertou_palavra = False
                fade_alpha = 255
                if qtd_jogador == 1:
                    if pontos_jogador02 < 10:
                        cena = "fim_partida"
                    else:
                        cena = "fim_jogo"
                else:
                   
                    if pontos_jogador01 == 10 or pontos_jogador01 == 10:
                        cena = "fim_jogo"
                    else:
                        cena = "fim_partida"
                

            if acertos == (len(palavra_selecionada)-qtd_ifens_na_palavra) and palavra_selecionada != '':
                if lancar_ponto_jog01:
                    if qtd_jogador == 1:
                        pontos_jogador01 +=1
                    elif qtd_jogador == 2:
                        if jogador01_responde:
                            pontos_jogador01 +=1
                            msg_indica_jogador_img = pygame.image.load("assets/img_indica_jogador01.png")
                        else:
                            pontos_jogador02 +=1
                            msg_indica_jogador_img = pygame.image.load("assets/img_indica_jogador02.png")


                lancar_ponto_jog01 = False
                acertou_palavra = True                        
                fade_alpha = 255   
                if qtd_jogador == 1:
                    
                    if pontos_jogador01 < 10:
                        cena = "fim_partida"
                    else:
                        cena = "fim_jogo"
                else:
                  
                    if pontos_jogador01 == 10 or pontos_jogador01 == 10:
                        cena = "fim_jogo"
                    else:
                        cena = "fim_partida"

        if fade_alpha > 0:
            fade_alpha -= 15
            fade_img.set_alpha(fade_alpha)       

        tela.fill((255,200,0))

        tela.blit(fundo_img, fundo)
        
        if jogador01_responde:
            tela.blit(jogador01_digita_palavra_img, jogador01_digita_palavra)
        else:
            tela.blit(jogador02_digita_palavra_img, jogador02_digita_palavra)


        txt_orientacao = fonte_textos.render("DESCUBRA A PALAVRA:", True, (255,200,0))
        tela.blit(txt_orientacao, (70, 220))

        txt_orientacao = fonte_nivel.render("NÍVEL: "+str(nivel_jogo), True, (255,200,0))
        tela.blit(txt_orientacao, (470, 73))

        palavra_enigma = ''
        for item in estado_atual_enigma:
             palavra_enigma += f'{item} '

        tela.blit(forca_status_img, forca_status)

        txt_palavra_escondida = fonte_letras.render(palavra_enigma, True, (255,255,255))
        tela.blit(txt_palavra_escondida, (50, 250))

        
        txt_letras_digitadas = fonte_textos.render(letras_digitadas, True, (255,255,255))
        tela.blit(txt_letras_digitadas, (70, 400))

        if letra_ja_digitada:
            txt_alerta = fonte_textos.render("Essa letra já foi digitada", True, (255,200,0))
            tela.blit(txt_alerta, (70, 300))

        tela.blit(placar_img, placar)
        
        tela.blit(jogador01_img, jogador01)
        txt_placar_jogador01 = fonte_placar.render(str(pontos_jogador01), True, (255,255,255))
        tela.blit(txt_placar_jogador01, (440, 35))
        
        tela.blit(jogador02_img, jogador02)
        txt_placar_jogador02 = fonte_placar.render(str(pontos_jogador02), True, (255,255,255))
        tela.blit(txt_placar_jogador02, (550, 35))
        
        tela.blit(btn_home_img, btn_home)
        tela.blit(btn_reiniciar_img, btn_reiniciar) 
        tela.blit(fade_img, fade)
   
    elif cena == "jogador_informa_palavra":
        trilha.set_volume(0.5)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_menu.collidepoint(event.pos):
                    click_menu()
                    fade_alpha = 255
                    erros = 0
                    acertos = 0

                    estado_atual_enigma = ["_"] * len(palavra_selecionada)
                    letras_digitadas = '' 
                    cena = "menu"  
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_continuar.collidepoint(event.pos):
                    if text != "":
                        click_menu()
                        fade_alpha = 255
                        erros = 0
                        acertos = 0
                        palavra_selecionada = text
                        estado_atual_enigma = ["_"] * len(palavra_selecionada)
                        letras_digitadas = '' 
                        lancar_ponto_jog01 = True
                        lancar_ponto_jog02 = True
                        qtd_ifens_na_palavra =0  
                        cena = "jogo"
                        
                    else:
                        
                        texto_deve_ditar_palavra = "VOCÊ PRECISA DIGITAR UMA PALAVRA!"
                               
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if len(text) > 0:
                        
                       
                        text = text[:-1]
                else:
                    text += event.unicode.upper()
                    texto_deve_ditar_palavra = ''
                    
                img = font.render(text, True, (255, 200, 0))
                rect.size = img.get_size()
                cursor.topleft = rect.topright

        if fade_alpha > 0:
            fade_alpha -= 15
            fade_img.set_alpha(fade_alpha)                    

        tela.fill((40,10,50))
        tela.blit(fundo_img, fundo)

        tela.blit(btn_continuar_img, btn_continuar)
        tela.blit(btn_menu_img, btn_menu)


        tela.blit(placar_img, placar)
        if not jogador01_responde:
            tela.blit(jogador01_digita_palavra_img, jogador01_digita_palavra)
        elif jogador01_responde:
            tela.blit(jogador02_digita_palavra_img, jogador02_digita_palavra)

        
        tela.blit(jogador01_img, jogador01)
        txt_placar_jogador01 = fonte_placar.render(str(pontos_jogador01), True, (255,255,255))
        tela.blit(txt_placar_jogador01, (440, 35))
        
        tela.blit(jogador02_img, jogador02)
        txt_placar_jogador02 = fonte_placar.render(str(pontos_jogador02), True, (255,255,255))
        tela.blit(txt_placar_jogador02, (550, 35))
        
        txt_alerta_digite_palavra = fonte_textos.render(texto_deve_ditar_palavra, True, (255,200,0))
        tela.blit(txt_alerta_digite_palavra, (70, 250))

        txt_orientacao = fonte_textos.render("Digite a palavra:", True, (255,200,0))
        tela.blit(txt_orientacao, (70, 200))
        tela.blit(img, rect)
        if time.time() % 1 > 0.5:
            pygame.draw.rect(tela, (255, 0, 0), cursor)
        
        tela.blit(fade_img, fade)
         
       

    elif cena == "fim_jogo":

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if btn_menu.collidepoint(event.pos):
                click_menu()
                fade_alpha = 255
                limpar_variaveis()
                cena = "menu"

        if fade_alpha > 0:
            fade_alpha -= 15
            fade_img.set_alpha(fade_alpha)   

       

        tela.fill((40,10,50))
        tela.blit(fundo_img, fundo)
        
        trilha.set_volume(0.2)

        if qtd_jogador == 1:
            if pontos_jogador01 == 10:
                msg_resultado_img = pygame.image.load("assets/img_ganhou.png")
                audio_venceu()

            elif pontos_jogador02 == 10:
                trilha.stop()
                audio_perdeu()
                msg_resultado_img = pygame.image.load("assets/img_perdeu.png")
        else:
            if pontos_jogador01 == 10:
                audio_venceu()
                msg_resultado_img = pygame.image.load("assets/img_ganhou.png")
                msg_indica_jogador_img = pygame.image.load("assets/img_indica_jogador01.png")

            elif pontos_jogador02 == 10:
                audio_venceu()
                msg_resultado_img = pygame.image.load("assets/img_ganhou.png")
                msg_indica_jogador_img = pygame.image.load("assets/img_indica_jogador02.png")



        tela.blit(msg_resultado_img, msg_resultado)
        tela.blit(msg_indica_jogador_img, msg_indica_jogador)
        tela.blit(btn_menu_img, btn_menu)
        tela.blit(fade_img, fade)
      

    elif cena == "fim_partida":
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if btn_menu.collidepoint(event.pos):
                audio_acertou.stop()
                click_menu()
                fade_alpha = 255
                limpar_variaveis()
                cena = "menu"

        if event.type == pygame.MOUSEBUTTONDOWN:
            if btn_proxima.collidepoint(event.pos):
                click_menu()
                audio_acertou.stop()
                audio_errou.stop()
                if qtd_jogador == 1:
                    fade_alpha = 255
                    limpar_variaveis() 
                    cena = "jogo"
                else:
                    fade_alpha = 255
                    text = ''
                    img = font.render(text, True, (255, 200, 0))
                    rect.size = img.get_size()
                    cursor.topleft = rect.topright      
                    jogador01_responde = not jogador01_responde
                    cena = "jogador_informa_palavra"
        if fade_alpha > 0:
            fade_alpha -= 15
            fade_img.set_alpha(fade_alpha)     

        tela.fill((51,51,51))
        tela.blit(fundo_img, fundo)
        txt_palavra = fonte_textos.render("A PALAVRA É: "+palavra_selecionada, True, (255,255,255))
        tela.blit(txt_palavra, ((largura/2)-(txt_palavra.get_width()/2), 300))   

        trilha.set_volume(0.2)
                    
        if acertou_palavra:
            audio_acertou.play()
            audio_acertou.set_volume(0.5)
            msg_resultado_img = pygame.image.load("assets/img_acertou.png")        
        else:
            audio_errou.play()
            audio_errou.set_volume(0.5)
            msg_resultado_img = pygame.image.load("assets/img_errou.png")
            
        
        tela.blit(msg_resultado_img, msg_resultado)

        if qtd_jogador == 2:
            if jogador01_responde:
                 msg_indica_jogador_img = pygame.image.load("assets/img_indica_jogador01.png")
            else:
                 msg_indica_jogador_img = pygame.image.load("assets/img_indica_jogador02.png")
            tela.blit(msg_indica_jogador_img, msg_indica_jogador)

        tela.blit(btn_menu_img, btn_menu)
        tela.blit(btn_proxima_img, btn_proxima)
        tela.blit(fade_img, fade)

    
    
    elif cena == "config":
        if qtd_jogador == 1:
            btn_jogador_vs_maquina_img = pygame.image.load("assets/btn_jogador_vs_maquina_selecionado.png")
            btn_jogador_vs_jogador_img = pygame.image.load("assets/btn_jogador_vs_jogador.png")
            
        else:
            btn_jogador_vs_maquina_img = pygame.image.load("assets/btn_jogador_vs_maquina.png")
            btn_jogador_vs_jogador_img = pygame.image.load("assets/btn_jogador_vs_jogador_selecionado.png")  

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if btn_gravar.collidepoint(event.pos):
                click_menu()
                fade_alpha = 255
                limpar_variaveis() 
                cena = "menu"

        if event.type == pygame.MOUSEBUTTONDOWN:
            if btn_jogador_vs_maquina.collidepoint(event.pos):
                click_menu()
                qtd_jogador = 1
                btn_jogador_vs_maquina_img = pygame.image.load("assets/btn_jogador_vs_maquina_selecionado.png")
                btn_jogador_vs_jogador_img = pygame.image.load("assets/btn_jogador_vs_jogador.png")

        if event.type == pygame.MOUSEBUTTONDOWN:
            if btn_jogador_vs_jogador.collidepoint(event.pos):
                click_menu()
                qtd_jogador = 2
                btn_jogador_vs_maquina_img = pygame.image.load("assets/btn_jogador_vs_maquina.png")
                btn_jogador_vs_jogador_img = pygame.image.load("assets/btn_jogador_vs_jogador_selecionado.png")
                jogador02_img = pygame.image.load("assets/jogador02.png")
        
        if fade_alpha > 0:
            fade_alpha -= 15
            fade_img.set_alpha(fade_alpha)

        tela.fill((0,0,0))

        tela.blit(fundo_img, fundo)
        
        txt_titulo_config = fonte_titulos.render("Configurações", True, (255,255,255))
        tela.blit(txt_titulo_config, ((largura/2)-(txt_titulo_config.get_width()/2), 40))

        txt_quant_jogadores = fonte_textos.render("Quantos jogadores?", True, (255,255,255))
        tela.blit(txt_quant_jogadores, (50, 100))

        tela.blit(btn_jogador_vs_maquina_img, btn_jogador_vs_maquina)
        tela.blit(btn_jogador_vs_jogador_img, btn_jogador_vs_jogador)

        tela.blit(btn_gravar_img, btn_gravar)
        tela.blit(fade_img, fade)

    elif cena == "info":

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if btn_menu.collidepoint(event.pos):
                click_menu()
                fade_alpha = 255  
                limpar_variaveis()
                cena = "menu"
           
        if fade_alpha > 200:
            fade_alpha -= 10
            fade_img.set_alpha(fade_alpha)

        tela.fill((40,10,50))
        tela.blit(fundo_menu_img, fundo_menu)
        tela.blit(fade_img, fade)
     

        txt_palavra = fonte_textos.render("Desenvolvido por:", True, (255,255,255))
        tela.blit(txt_palavra, ((largura/2)-(txt_palavra.get_width()/2), 170))
        
        txt_palavra = fonte_textos.render("JOSÉ BRÍCIO NEGRÃO DA ROCHA", True, (255,255,255))
        tela.blit(txt_palavra, ((largura/2)-(txt_palavra.get_width()/2), 220))
        txt_palavra = fonte_info.render("Como requisito avaliativo da disciplina Logica de Programação," , True, (255,255,255))
        tela.blit(txt_palavra, ((largura/2)-(txt_palavra.get_width()/2), 250))
        txt_palavra = fonte_info.render("do curso de Pós-Graduação em Desenvolvimento de Sistemas com JAVA" , True, (255,255,255))
        tela.blit(txt_palavra, ((largura/2)-(txt_palavra.get_width()/2), 270))
        txt_palavra = fonte_info.render("da UNICESUMAR" , True, (255,255,255))
        tela.blit(txt_palavra, ((largura/2)-(txt_palavra.get_width()/2), 290))

        btn_menu = btn_menu_img.get_rect(center=[largura/2, (altura/2)+130])
        tela.blit(btn_menu_img, btn_menu)

        
    elif cena == "menu":
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if btn_iniciar.collidepoint(event.pos):
                click_menu()
                limpar_variaveis()
                pontos_jogador01 = 0
                pontos_jogador02 = 0
                palavras.palavas_selecionadas = []
                fade_alpha = 255  
                if qtd_jogador == 1:
                    cena = "jogo"
                else:
                    cena = "jogador_informa_palavra"

        if event.type == pygame.MOUSEBUTTONDOWN:
            if btn_config.collidepoint(event.pos):
                click_menu()
                fade_alpha = 255
                cena = "config"

        if event.type == pygame.MOUSEBUTTONDOWN:
            if btn_info.collidepoint(event.pos):
                click_menu()
                fade_alpha = 255  
                cena = "info"                   
            
        if fade_alpha > 0:
            fade_alpha -= 15
            fade_img.set_alpha(fade_alpha)
        
        tela.fill((0,0,0))
        tela.blit(fundo_menu_img, fundo_menu)       
        tela.blit(btn_iniciar_img, btn_iniciar)
        tela.blit(btn_config_img, btn_config)
        tela.blit(btn_info_img, btn_info)
        tela.blit(fade_img, fade)

    fps.tick(25)
    pygame.display.flip()

 