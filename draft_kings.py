from bs4 import BeautifulSoup
import requests
from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

response = requests.get("https://sportsbook.draftkings.com/leagues/basketball/88670846")
draft_kings_list = response.text

soup = BeautifulSoup(draft_kings_list, "html.parser")
matchup = soup.find_all("div", class_="event-cell__name-text")
# lines = soup.find_all("div", class_="sportsbook-outcome-cell__element")
# for line in lines:
#     print(line.getText())
game_day_matches = []
spreads = []
all_odds = []
for matches in matchup:
    matchups = matches.getText()
    game_day_matches.append(matchups)
spread = soup.find_all("span", class_="sportsbook-outcome-cell__line")
for sp in spread:
    game_day_spreads = sp.getText()
    spreads.append(game_day_spreads)

odds = soup.find_all("span", class_="sportsbook-odds american no-margin default-color")
for odd in odds:
    game_day_odds = odd.getText()
    all_odds.append(game_day_odds)


    # print(game_day_matches)
final_spreads = spreads[::2]
    # print(all_odds)

vals = zip(final_spreads, all_odds)
dictionary = dict(zip(game_day_matches,vals))


data = pd.DataFrame(dictionary)
pd.set_option('display.max_columns', None)
diction = list(data)


#
# print(diction)
# print(data)
team_one_spread = (data['BKN Nets'][0])
team_two_spread = (data['DAL Mavericks'][0])
team_three_spread = (data['NY Knicks'][0])
team_four_spread = (data['SA Spurs'][0])
team_five_spread = (data['BOS Celtics'][0])
team_six_spread = (data['LA Lakers'][0])

team_one_moneyline = (data['BKN Nets'][1])
team_two_moneyline = (data['DAL Mavericks'][1])
team_three_moneyline = (data['NY Knicks'][1])
team_four_moneyline = (data['SA Spurs'][1])
team_five_moneyline = (data['BOS Celtics'][1])
team_six_moneyline = (data['LA Lakers'][1])

    #see if you can complete with the range function for len of teams
# todays_games = [f"{game_day_matches[0]} vs. {game_day_matches[1]}, {game_day_matches[2]} vs. {game_day_matches[3]}, {game_day_matches[4]} vs. {game_day_matches[5]}, {game_day_matches[6]} vs. {game_day_matches[7]}, {game_day_matches[8]} vs. {game_day_matches[9]}, {game_day_matches[10]} vs. {game_day_matches[11]},{game_day_matches[12]} vs. {game_day_matches[13]}, {game_day_matches[14]} vs. {game_day_matches[15]}, {game_day_matches[16]} vs. {game_day_matches[17]}"
#                 for games in game_day_matches]
# print(todays_games)

# UI setup
window = Tk()
window.title("Gamble the odds")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526)
nba_img = PhotoImage(file="nba goats.png")
football_img = PhotoImage(file="nfl goats.png")
img_background = canvas.create_image(400, 263, image=nba_img)
title = canvas.create_text(400, 150, text="Today's Games", font=("Ariel", 20, "italic"))


canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
#
game_1 = Label(text=f"{diction[0]}\n vs. \n{diction[1]}", font=("Arial", 12, "bold"), bg=BACKGROUND_COLOR)
game_1.place(x= 100, y=200)
game_2 = Label(text=f"{diction[2]}\n vs. \n{diction[3]}", font=("Arial", 12, "bold"), bg=BACKGROUND_COLOR)
game_2.place(x = 100, y=270)
game_3 = Label(text=f"{diction[4]}\n vs. \n{diction[5]}", font=("Arial", 12, "bold"), bg=BACKGROUND_COLOR)
game_3.place(x = 100, y=350)

spread_name = Label(text="Spread", font=("Arial", 12, "bold"), bg=BACKGROUND_COLOR)
spread_name.place(x=300, y=180)
moneyline = Label(text="MoneyLine", font=("Arial", 12, "bold"), bg=BACKGROUND_COLOR)
moneyline.place(x=500, y=180)
team_1_spread = Label(text=f"{team_one_spread} ", font=("Arial", 12, "bold"), bg=BACKGROUND_COLOR)
team_1_spread.place(x= 300, y=200)
team_2_spread = Label(text=f"{team_two_spread} ", font=("Arial", 12, "bold"), bg=BACKGROUND_COLOR)
team_2_spread.place(x =300, y=235)
team_3_spread = Label(text=f"{team_three_spread} ", font=("Arial", 12, "bold"), bg=BACKGROUND_COLOR)
team_3_spread.place(x = 300, y=270)
team_4_spread = Label(text=f"{team_four_spread} ", font=("Arial", 12, "bold"), bg=BACKGROUND_COLOR)
team_4_spread.place(x= 300, y=310)
team_5_spread = Label(text=f"{team_five_spread} ", font=("Arial", 12, "bold"),bg=BACKGROUND_COLOR)
team_5_spread.place(x = 300, y=350)
team_6_spread = Label(text=f"{team_six_spread} ", font=("Arial", 12, "bold"), bg=BACKGROUND_COLOR)
team_6_spread.place(x = 300, y=390)

team_1_money = Label(text=f"{team_one_moneyline} ", font=("Arial", 12, "bold"), bg=BACKGROUND_COLOR)
team_1_money.place(x= 500, y=200)
team_2_money = Label(text=f"{team_two_moneyline} ", font=("Arial", 12, "bold"), bg=BACKGROUND_COLOR)
team_2_money.place(x =500, y=230)
team_3_money= Label(text=f"{team_three_moneyline} ", font=("Arial", 12, "bold"), bg=BACKGROUND_COLOR)
team_3_money.place(x = 500, y=270)
team_4_money = Label(text=f"{team_four_moneyline} ", font=("Arial", 12, "bold"), bg=BACKGROUND_COLOR)
team_4_money.place(x= 500, y=310)
team_5_money = Label(text=f"{team_five_moneyline} ", font=("Arial", 12, "bold"), bg=BACKGROUND_COLOR)
team_5_money.place(x = 500, y=350)
team_6_money = Label(text=f"{team_six_moneyline} ", font=("Arial", 12, "bold"), bg=BACKGROUND_COLOR)
team_6_money.place(x = 500, y=390)

def toggle_to_nfl():
    canvas.itemconfig(img_background, image=football_img)

toggle_image = PhotoImage(file="right.png")
known_button = Button(image=toggle_image, highlightthickness=0, command=toggle_to_nfl)
known_button.grid(row=1, column=1)



mainloop()