import pygame as pg
def cobrinha(pos_x, pos_y, tamanho, cor):
    pg.draw.rect(Tela, cor, (pos_x, pos_y, tamanho, tamanho))
def borda(larguraborda):
    pg.draw.rect(Tela, (255, 0, 0), (larguraborda, larguraborda, largura - (larguraborda * 2), altura - (larguraborda * 2)), tamanho)
pg.init()
resolucao = largura, altura = 640, 480
fonte = pg.font.SysFont('Ubuntu', 30)
titulo = fonte.render('Jogo da Cobrinha', True, (0, 255, 0))
Tela = pg.display.set_mode(resolucao)
pg.display.set_caption('Jogo da Cobrinha')
cx = largura / 2
cy = altura / 2
tamanho = 10
vx = tamanho
vy = 0
fps = 5
rodando = True
while rodando:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            rodando = False
        if evento.type == pg.KEYDOWN:
            if evento.key == pg.K_ESCAPE:
                rodando = False
            if evento.key == pg.K_UP and vy != tamanho:
                vx = 0
                vy = -tamanho
            if evento.key == pg.K_DOWN and vy != -tamanho:
                vx = 0
                vy = tamanho
            if evento.key == pg.K_LEFT and vx != tamanho:
                vy = 0
                vx = -tamanho
            if evento.key == pg.K_RIGHT and vx != -tamanho:
                vy = 0
                vx = tamanho
    if cx > 570:
        cx = 40
    if cy > 410:
        cy = 40
    if cx < 40:
        cx = 570
    if cy < 40:
        cy = 410
    cx += vx
    cy += vy
    Tela.fill((0, 0, 0))
    borda(40)
    cobrinha(cx, cy, 10, (255, 255, 255))
    Tela.blit(titulo, (200, 0))
    pg.time.Clock().tick(fps)
    pg.display.update()
pg.quit()