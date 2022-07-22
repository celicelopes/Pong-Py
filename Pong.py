#importa a biblioteca
import pygame, sys, random


#  setup
pygame.init()
clock = pygame.time.Clock()

#define uma função
def inicia_bola():
        global bola_velocidade_x, bola_velocidade_y, bola_move, score_time
        
        bola.center = (largura_tela/2,altura_tela/2)

        current_time = pygame.time.get_ticks()

        if current_time - score_time < 700:
                number_three=contagem_font.render("3",False,vermelho)
                screen.blit(number_three,(largura_tela/2-35,altura_tela/2-60))

        if 700<current_time - score_time<1400:
                number_two=contagem_font.render("2",False,vermelho)
                screen.blit(number_two,(largura_tela/2-35,altura_tela/2-60))
                
        if 1400<current_time - score_time<2100:        
                number_one=contagem_font.render("1",False,vermelho)
                screen.blit(number_one,(largura_tela/2-35,altura_tela/2-60))
                
        if current_time - score_time<2100:
                bola_velocidade_x,bola_velocidade_y = 0,0
        else:
                bola_velocidade_x = 7 * random.choice((1,-1))
                bola_velocidade_y = 7 * random.choice((1,-1))
                score_time = None
        
        
# configuracao de janela 
largura_tela = 860
altura_tela = 640
screen = pygame.display.set_mode((largura_tela,altura_tela))
pygame.display.set_caption('Pong')

# cores

light_grey = (200,200,200)
bg_color = pygame.Color('grey12')
vermelho = pygame.Color9=('firebrick2')

# objetos
bola = pygame.Rect(largura_tela / 2 - 15, altura_tela / 2 - 15, 30, 30)
jogador = pygame.Rect(largura_tela - 20, altura_tela / 2 - 70, 10,140)
inimigo = pygame.Rect(10, altura_tela / 2 - 70, 10,140)

# variaveis
bola_velocidade_x = 7 * random.choice((1,-1))
bola_velocidade_y = 7 * random.choice((1,-1))
jogador_velocidade = 0
inimigo_velocidade = 10
jogador_pontuacao = 0
inimigo_pontuacao = 0
basic_font = pygame.font.Font('freesansbold.ttf',32)
contagem_font = pygame.font.Font ('freesansbold.ttf',120)
bola_move =False
score_time = True


while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                                jogador_velocidade -= 7
                        if event.key == pygame.K_DOWN:
                                jogador_velocidade += 7
                if event.type == pygame.KEYUP:
                        if event.key == pygame.K_UP:
                                jogador_velocidade += 7
                        if event.key == pygame.K_DOWN:
                                jogador_velocidade -= 7
       
    #faz jogador andar pela tela
        jogador.y += jogador_velocidade        
        
    #faz bola andar pela tela
        bola.x += bola_velocidade_x
        bola.y += bola_velocidade_y

    #quando bate no topo muda a direção
        if bola.top <= 0 or bola.bottom >= altura_tela:
                bola_velocidade_y *= -1
        
        #reinicia e registra a pontuacao 
        if bola.left <= 0:
                score_time = pygame.time.get_ticks()
                jogador_pontuacao += 1
        if bola.right >= largura_tela:
                score_time = pygame.time.get_ticks()
                inimigo_pontuacao += 1
        
        #Rebate a bola quando bate nos personagens      
        if bola.colliderect(jogador) or bola.colliderect(inimigo):
                bola_velocidade_x *= -1

    #nao deixa o jogador passar para fora da tela
        if jogador.top <= 0:
                jogador.top = 0
        if jogador.bottom >= altura_tela:
                jogador.bottom = altura_tela
    
    #faz o inimigo caminhar em direcao a bola
        if inimigo.top < bola.y:
                inimigo.top += inimigo_velocidade
        if inimigo.bottom > bola.y:
                inimigo.bottom -= inimigo_velocidade
        
    #nao deixa o inimigo passar para fora da tela
        if inimigo.top <= 0:
                inimigo.top = 0
        if inimigo.bottom >= altura_tela:
                inimigo.bottom = altura_tela
                           

        # desenhando a tela
        screen.fill(bg_color)
        pygame.draw.rect(screen, light_grey, jogador)
        pygame.draw.rect(screen, light_grey, inimigo)
        pygame.draw.ellipse(screen, light_grey, bola)
        pygame.draw.aaline(screen, light_grey,(largura_tela/2,0),(largura_tela/2,altura_tela))

        #inicia a bola
        if score_time:
                inicia_bola()

    #escrevendo a tela
        jogador_text = basic_font.render(f'{jogador_pontuacao}', False, light_grey)
        screen.blit(jogador_text,(440,20))
        inimigo_text = basic_font.render(f'{inimigo_pontuacao}', False, light_grey)
        screen.blit(inimigo_text,(400,20))


        pygame.display.flip()
        clock.tick(60)
