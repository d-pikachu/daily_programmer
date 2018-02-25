#https://www.reddit.com/r/dailyprogrammer/comments/7x81yg/20180213_challenge_351_easy_cricket_scoring/

data =input()

on_field = ["p1","p2"]
wickets = 0
ball = 0
extras = 0
score = {}

def player(i):
        return "p"+str(i)
        
for i in range(1,12):
        score[player(i)]=0
        
def change_strike():
        on_field.reverse()

def player_scored(runs):
        score[on_field[0]] += runs

def wicket_down():
        if wickets < 10:
                new_player = player(wickets+2)
                on_field[0] = new_player
                
for d in data:
        if ball == 6:
                ball = 0
                change_strike()
                        
        if d in ".b":
                ball += 1

        if d=='b':
                change_strike()
                        
        if d in "wb":
                extras += 1

        if d >= "1" and d <= "9":
                ball += 1
                runs = int(d)
                player_scored(runs)
                if runs%2==1:
                        change_strike()

        if d=="W":
                ball += 1
                wickets += 1
                wicket_down()



for i in range(1,min(wickets+3,12)):
        p = player(i)
        print(p + ": " + str(score[p]))
print("extras: " + str(extras))



















