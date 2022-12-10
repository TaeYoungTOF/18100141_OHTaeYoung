
import random as rm
import pygame
import sys

pygame.init()

WHITE = (255, 255, 255)

size = [800, 600]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Black Jack")

done = False
clock = pygame.time.Clock()

while not done:
    clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    screen.fill(WHITE)
    
    pygame.display.flip()
    
pygame.quit()


print('A is 11')

faces = 13*['♠']+13*['◇']+13*['♡']+13*['♣']
numbers=4*(['A']+[str(i) for i in range(2,11)]+['J','Q','K'])
deck = [ f+n for f,n in zip(faces,numbers)]

player=[];dealer=[]
playerPT,dealerPT=0,0

for x in range(2):
    t=rm.choice(deck)
    player.append(t)
    deck.remove(t)
print(f"player : {player}")

for x in range(2):
    t=rm.choice(deck)
    dealer.append(t)
    deck.remove(t)
print(f"dealer : ['{dealer[0]}', ?]")

for x in range(len(player)):
    PT=player[x][1:]
    if PT=='A':
        playerPT+=11
    elif PT=='2':
        playerPT+=2
    elif PT=='3':
        playerPT+=3
    elif PT=='4':
        playerPT+=4
    elif PT=='5':
        playerPT+=5
    elif PT=='6':
        playerPT+=6
    elif PT=='7':
        playerPT+=7
    elif PT=='8':
        playerPT+=8
    elif PT=='9':
        playerPT+=9
    else :
        playerPT+=10
if playerPT==21:
    print('Black Jack! you WIN :)')
    sys.exit()

for x in range(len(dealer)):
    PT=dealer[x][1:]
    if PT=='A':
        dealerPT+=11
    elif PT=='2':
        dealerPT+=2
    elif PT=='3':
        dealerPT+=3
    elif PT=='4':
        dealerPT+=4
    elif PT=='5':
        dealerPT+=5
    elif PT=='6':
        dealerPT+=6
    elif PT=='7':
        dealerPT+=7
    elif PT=='8':
        dealerPT+=8
    elif PT=='9':
        dealerPT+=9
    else :
        dealerPT+=10
if dealerPT==21:
    print('Dealer\'s Black Jack! you LOSE :(')
    sys.exit()


while 1:
    answer=input('Go or Stop ? : ')
    if answer.lower()!='go' and answer.lower()!='stop':
        continue
    if answer.lower()=='go':
        t=rm.choice(deck)
        player.append(t)
        deck.remove(t)
        playerPT=0
        print(f'you : {t}')
        for x in range(len(player)):
            PT=player[x][1:]
            if PT=='A':
                playerPT+=11
            elif PT=='2':
                playerPT+=2
            elif PT=='3':
                playerPT+=3
            elif PT=='4':
                playerPT+=4
            elif PT=='5':
                playerPT+=5
            elif PT=='6':
                playerPT+=6
            elif PT=='7':
                playerPT+=7
            elif PT=='8':
                playerPT+=8
            elif PT=='9':
                playerPT+=9
            else :
                playerPT+=10
        if playerPT==21:
            print('Black Jack! you WIN :)')
            sys.exit()
        elif playerPT>21:
            print('Burst! you LOSE :(')
            sys.exit()
        if dealerPT<17:
            t=rm.choice(deck)
            dealer.append(t)
            deck.remove(t)
            print(f'dealer : {t}')
            for x in range(len(dealer)):
                PT=dealer[x][1:]
                if PT=='A':
                    dealerPT+=11
                elif PT=='2':
                    dealerPT+=2
                elif PT=='3':
                    dealerPT+=3
                elif PT=='4':
                    dealerPT+=4
                elif PT=='5':
                    dealerPT+=5
                elif PT=='6':
                    dealerPT+=6
                elif PT=='7':
                    dealerPT+=7
                elif PT=='8':
                    dealerPT+=8
                elif PT=='9':
                    dealerPT+=9
                else :
                    dealerPT+=10
            if dealerPT==21:
                print('Dealer\'s Black Jack! you LOSE :(')
                sys.exit()
            elif dealerPT>21:
                print('Dealer\'s Burst! you WIN :)')
                sys.exit()
        continue            
    while dealerPT<17:
        t=rm.choice(deck)
        dealer.append(t)
        deck.remove(t)
        print(f'dealer : {t}')
        for x in range(len(dealer)):
            PT=dealer[x][1:]
            if PT=='A':
                dealerPT+=11
            elif PT=='2':
                dealerPT+=2
            elif PT=='3':
                dealerPT+=3
            elif PT=='4':
                dealerPT+=4
            elif PT=='5':
                dealerPT+=5
            elif PT=='6':
                dealerPT+=6
            elif PT=='7':
                dealerPT+=7
            elif PT=='8':
                dealerPT+=8
            elif PT=='9':
                dealerPT+=9
            else :
                dealerPT+=10
        if dealerPT==21:
            print('Dealer\'s Black Jack! you LOSE :(')
            sys.exit()
        elif dealerPT>21:
            print('Dealer\'s Burst! you WIN :)')
            sys.exit()
    if playerPT>dealerPT:
        print(f'you:{playerPT}, dealer:{dealerPT}! you WIN :)')
        sys.exit()
    elif playerPT<dealerPT:
        print(f'you:{playerPT}, dealer:{dealerPT}! you LOSE :(')
        sys.exit()
    else :
        print(f'you:{playerPT}, dealer:{dealerPT}! DRAW XD')
        sys.exit()
