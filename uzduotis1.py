def mainFunction():
    def dataEntry():
        player1 = input('Player1 shoots: ')
        player2 = input('Player2 shoots: ')
        return player1, player2 
    
    player1, player2 = dataEntry()

    def timeCalculation():
        
        player2ShootingTime = 0
        player1ShootingTime = 0

        for i in player1:
            if i != ' ':
                break
            elif i == ' ':
                player1ShootingTime += 1

        for i in player2:
            if i != ' ':
                    break
            elif i == ' ':
                player2ShootingTime += 1
                
            
        return player1ShootingTime, player2ShootingTime

    player1ShootingTime, player2ShootingTime = timeCalculation()

    def numeriko(player1ShootingTime, player2ShootingTime):
        if player1ShootingTime < player2ShootingTime:
            print('player1 has won')
        else:
            print('player2 has won')
    
    numeriko(player1ShootingTime, player2ShootingTime)

mainFunction()
