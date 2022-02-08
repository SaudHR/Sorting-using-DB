import tkinter as tk
import mysql.connector
from functools import partial
from tkinter import *

def popupmsg(Msg):
    popup = tk.Toplevel()
    popup.title("!")
    label = tk.Label(popup, text=Msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()

def submitact():
    user = Username.get()
    passw = password.get()

    print(f"The name entered by you is {user} {passw}")

    logintodb(user, passw)

#•	Add a new tournament "Admin"


#•	Add a team to a tournament "Admin"
def Newteam(db):
    NewteamW = tk.Toplevel()
    NewteamW.geometry("600x600")
    NewteamW.title("Add New team")
    NewTournamentLabel = tk.Label(NewteamW, text="Add New team", )
    NewTournamentLabel.place(x=300, y=20)
    #team_id
    team_id = tk.Entry(NewteamW, width=35)
    team_id.place(x=230, y=160, width=100)

    lblsecrow = tk.Label(NewteamW, text="team_id")
    lblsecrow.place(x=150, y=160)
    #tr_id
    tr_id = tk.Entry(NewteamW, width=35)
    tr_id.place(x=230, y=180, width=100)

    lblsecrow = tk.Label(NewteamW, text="tr_id")
    lblsecrow.place(x=150, y=180)

    #team_group
    team_group = tk.Entry(NewteamW, width=35)
    team_group.place(x=230, y=200, width=100)

    lblsecrow = tk.Label(NewteamW, text="team_group")
    lblsecrow.place(x=150, y=200)

    #won
    won = tk.Entry(NewteamW, width=35)
    won.place(x=230, y=220, width=100)

    lblsecrow = tk.Label(NewteamW, text="won")
    lblsecrow.place(x=150, y=220)

    #draw
    draw = tk.Entry(NewteamW, width=35)
    draw.place(x=230, y=240, width=100)


    lblsecrow = tk.Label(NewteamW, text="draw")
    lblsecrow.place(x=150, y=240)

    # lost
    lost = tk.Entry(NewteamW, width=35)
    lost.place(x=230, y=260, width=100)

    lblsecrow = tk.Label(NewteamW, text="lost")
    lblsecrow.place(x=150, y=260)

    # goal_for
    goal_for = tk.Entry(NewteamW, width=35)
    goal_for.place(x=230, y=280, width=100)

    lblsecrow = tk.Label(NewteamW, text="goal_for")
    lblsecrow.place(x=150, y=280)

    # goal_against
    goal_against = tk.Entry(NewteamW, width=35)
    goal_against.place(x=230, y=300, width=100)

    lblsecrow = tk.Label(NewteamW, text="goal_against")
    lblsecrow.place(x=150, y=300)

    # goal_diff
    goal_diff = tk.Entry(NewteamW, width=35)
    goal_diff.place(x=230, y=320, width=100)

    lblsecrow = tk.Label(NewteamW, text="goal_diff")
    lblsecrow.place(x=150, y=320)

    # points
    points = tk.Entry(NewteamW, width=35)
    points.place(x=230, y=340, width=100)

    lblsecrow = tk.Label(NewteamW, text="points")
    lblsecrow.place(x=150, y=340)

    # group_position
    group_position = tk.Entry(NewteamW, width=35)
    group_position.place(x=230, y=360, width=100)

    lblsecrow = tk.Label(NewteamW, text="group_position")
    lblsecrow.place(x=130, y=360)

    # match_played
    match_played = tk.Entry(NewteamW, width=35)
    match_played.place(x=230, y=380, width=100)

    lblsecrow = tk.Label(NewteamW, text="match_played")
    lblsecrow.place(x=150, y=380)


    # Insert Button
    xx = partial(NewteamInsert, db,team_id,tr_id,team_group,match_played,won,draw,lost,goal_for,goal_against,goal_diff,points,group_position)
    submitbtn = tk.Button(NewteamW, text="Insert",
                          bg='red', command=xx)
    submitbtn.place(x=50, y=400, width=100)
    exit_button = tk.Button(NewteamW, text="Exit", command=NewteamW.destroy)
    exit_button.place(x=150, y=400, width=50)
def NewteamInsert(db,team_id,tr_id,team_group,match_played,won,draw,lost,goal_for,goal_against,goal_diff,points,group_position):
    cursor = db.cursor()
    teamid= team_id.get()
    trid = tr_id.get()
    teamgroup = team_group.get()
    matchplayed = match_played.get()
    won1 = won.get()
    draw1 = draw.get()
    lost1 = lost.get()
    goalfor = goal_for.get()
    goalagainst = goal_against.get()
    goaldiff = goal_diff.get()
    points1 = points.get()
    groupposition = group_position.get()


    savequery = """INSERT INTO kfupm_team 
     VALUES 
     (%s, %s,%s,%s,%s, %s,%s,%s,%s, %s,%s,%s)"""
    record = (teamid,trid,teamgroup,matchplayed,won1,draw1,lost1,goalfor,goalagainst,goaldiff,points1,groupposition)

    try:
        cursor.execute(savequery,record)
        db.commit()
        myresult = cursor.fetchall()

        # Printing the result of the
        # query
        for x in myresult:
            print(x)
        popupmsg("Query Excecuted successfully")
    except:
        db.rollback()
        popupmsg("Error occured")

#•	Select a captain for a team "Admin"
def captain(db):
    captainW = tk.Toplevel()
    captainW.geometry("600x600")
    captainW.title("Select a captain for a team")
    captainWLabel = tk.Label(captainW, text="Select a captain for a team", )
    captainWLabel.place(x=300, y=20)
    #match_no
    match_no = tk.Entry(captainW, width=35)
    match_no.place(x=230, y=160, width=100)

    lblsecrow = tk.Label(captainW, text="match_no")
    lblsecrow.place(x=150, y=160)

    #team_id
    team_id = tk.Entry(captainW, width=35)
    team_id.place(x=230, y=180, width=100)

    lblsecrow = tk.Label(captainW, text="team_id")
    lblsecrow.place(x=150, y=180)

    #player_captain
    player_captain = tk.Entry(captainW, width=35)
    player_captain.place(x=230, y=200, width=100)

    lblsecrow = tk.Label(captainW, text="player_captain")
    lblsecrow.place(x=150, y=200)

    # Insert Button
    xx = partial(captainInsert, db,match_no,team_id,player_captain)
    submitbtn = tk.Button(captainW, text="Insert",
                          bg='red', command=xx)
    submitbtn.place(x=50, y=220, width=100)
    exit_button = tk.Button(captainW, text="Exit", command=captainW.destroy)
    exit_button.place(x=150, y=220, width=50)
def captainInsert(db,match_no,team_id,player_captain):
    cursor = db.cursor()
    matchno = match_no.get()
    teamid= team_id.get()
    playercaptain = player_captain.get()


    savequery = """INSERT INTO match_captain 
     VALUES 
     (%s, %s,%s)"""
    record = (matchno,teamid,playercaptain)

    try:
        cursor.execute(savequery,record)
        db.commit()
        myresult = cursor.fetchall()

        # Printing the result of the
        # query
        for x in myresult:
            print(x)
        popupmsg("Query Excecuted successfully")
    except:
        db.rollback()
        popupmsg("Error occured")

#•	Approve a player to join a team "Admin"
def Approve(db):
    playerW = tk.Toplevel()
    playerW.geometry("600x600")
    playerW.title("Approve a player to join a team")
    NewTournamentLabel = tk.Label(playerW, text="Approve a player to join a team", )
    NewTournamentLabel.place(x=300, y=20)
    # player_id
    player_id = tk.Entry(playerW, width=35)
    player_id.place(x=230, y=160, width=100)

    lblsecrow = tk.Label(playerW, text="player_id")
    lblsecrow.place(x=150, y=160)
    #Team_id
    Team_id = tk.Entry(playerW, width=35)
    Team_id.place(x=230, y=180, width=100)

    lblsecrow = tk.Label(playerW, text="Team_id")
    lblsecrow.place(x=150, y=180)

    # Jersey_no
    Jersey_no = tk.Entry(playerW, width=35)
    Jersey_no.place(x=230, y=200, width=100)

    lblsecrow = tk.Label(playerW, text="Jersey_no")
    lblsecrow.place(x=150, y=200)

    # Player_name
    Player_name = tk.Entry(playerW, width=35)
    Player_name.place(x=230, y=220, width=100)

    lblsecrow = tk.Label(playerW, text="Player_name ")
    lblsecrow.place(x=150, y=220)

    # Position_to_play
    Position_to_play = tk.Entry(playerW, width=35)
    Position_to_play.place(x=230, y=240, width=100)

    lblsecrow = tk.Label(playerW, text="Position_to_play")
    lblsecrow.place(x=130, y=240)

    # Dt_of_bir
    Dt_of_bir = tk.Entry(playerW, width=35)
    Dt_of_bir.place(x=230, y=260, width=100)

    lblsecrow = tk.Label(playerW, text="Dt_of_bir")
    lblsecrow.place(x=150, y=260)


    # Insert Button
    xx = partial(ApproveInsert, db,player_id,Team_id,Jersey_no,Player_name,Position_to_play,Dt_of_bir)
    submitbtn = tk.Button(playerW, text="Insert",
                          bg='red', command=xx)
    submitbtn.place(x=50, y=280, width=100)
    exit_button = tk.Button(playerW, text="Exit", command=playerW.destroy)
    exit_button.place(x=150, y=280, width=50)
def ApproveInsert(db,player_id,Team_id,Jersey_no,Player_name,Position_to_play,Dt_of_bir):
    cursor = db.cursor()
    playerid = player_id.get()
    Teamid = Team_id.get()
    Jerseyno = Jersey_no.get()
    Playername = Player_name.get()
    Positiontoplay = Position_to_play.get()
    Dtofbir = Dt_of_bir.get()


    savequery = """INSERT INTO player 
     VALUES 
     (%s, %s,%s,%s, %s,%s)"""
    record = (playerid,Teamid,Jerseyno,Playername,Positiontoplay,Dtofbir)

    try:
        cursor.execute(savequery,record)
        db.commit()
        myresult = cursor.fetchall()

        # Printing the result of the
        # query
        for x in myresult:
            print(x)
        popupmsg("Query Excecuted successfully")
    except:
        db.rollback()
        popupmsg("Error occured")

#•	Browse all results of a tournament with dates "Guest"
def results_Of_Tournament(db):
    results_Of_TournamentW = tk.Toplevel()
    results_Of_TournamentW.geometry("600x600")
    results_Of_TournamentW.title("Enter the Tr_ID to shot the results")
    results_Of_TournamentWL = tk.Label(results_Of_TournamentW, text="Enter the Tr_ID to shot the results" )
    results_Of_TournamentWL.place(x=300, y=20)
    #tr_id
    tr_id = tk.Entry(results_Of_TournamentW, width=35)
    tr_id.place(x=230, y=160, width=100)

    lblsecrow = tk.Label(results_Of_TournamentW, text="tr_id")
    lblsecrow.place(x=150, y=160)

    # Insert Button
    xx = partial(results_Of_TournamentInsert, db,tr_id)
    submitbtn = tk.Button(results_Of_TournamentW, text="Insert",
                          bg='red', command=xx)
    submitbtn.place(x=50, y=300, width=100)
    Back_button = tk.Button(results_Of_TournamentW, text="Back", command=results_Of_TournamentW.destroy)
    Back_button.place(x=150, y=300, width=50)
def results_Of_TournamentInsert(db,tr_id):
    cursor = db.cursor()
    trid = tr_id.get()
    results_Of_TournamentWW = tk.Toplevel()
    results_Of_TournamentWW.geometry("600x600")
    results_Of_TournamentWW.title("Browse all results of a tournament with dates")

    savequery = """SELECT match_no,results,play_date from match_played where match_no in(SELECT match_no from match_details where team_id in (SELECT team_id from kfupm_team where tr_id = %s))""" % (trid)
    print(savequery)
    try:
        cursor.execute(savequery)
        myresult = cursor.fetchall()
        # Printing the result of the
        # query
        e = Label(results_Of_TournamentWW, width=10, text="match_no", borderwidth=2, relief='ridge', anchor="w",
                  bg="yellow")
        e.grid(row=0, column=0)
        e = Label(results_Of_TournamentWW, width=10, text="results", borderwidth=2, relief='ridge', anchor="w",
                  bg="yellow")
        e.grid(row=0, column=1)
        e = Label(results_Of_TournamentWW, width=10, text="play_date", borderwidth=2, relief='ridge', anchor="w",
                  bg="yellow")
        e.grid(row=0, column=2)
        i = 1
        for x in myresult:
            for j in range(len(x)):
                e = Label(results_Of_TournamentWW, width=10, text=x[j], borderwidth=2, relief='ridge', anchor="w")
                e.grid(row=i, column=j)
            i = i + 1
        print(myresult[0][0])
        for x in myresult:
            print(x)
    except:
        db.rollback()
        popupmsg("Error occured")

    back_button = tk.Button(results_Of_TournamentWW, text="back", command=results_Of_TournamentWW.destroy)
    back_button.grid(row = i,column = 0)

#•	Browse the player with the highest goal score for each team "Guest"
def Player_highest_goal(db):
    Player_highest_goalW = tk.Toplevel()
    Player_highest_goalW.geometry("600x600")
    Player_highest_goalW.title("Browse all results of a tournament with dates")
    cursor = db.cursor()

    savequery = """SELECT a.goal,a.team_id,a.player_id FROM   (Select Count(goal_id) as goal ,team_id , player_id FROM  goal_details 
    Group by player_id,team_id) a JOIN  (Select max(T2) as goal ,team_id From (Select Count(goal_id) as T2,team_id,player_id FROM goal_details
      Group by player_id,team_id) as T1 Group by team_id) b on a.goal=b.goal and a.team_id = b.team_id"""

    try:
        cursor.execute(savequery)
        myresult = cursor.fetchall()
        # Printing the result of the
        # query
        e = Label(Player_highest_goalW, width=10, text="Goals" ,borderwidth=2,relief='ridge', anchor="w" , bg="yellow")
        e.grid(row=0, column=0)
        e = Label(Player_highest_goalW, width=10, text="Team_ID",borderwidth=2,relief='ridge', anchor="w", bg="yellow")
        e.grid(row=0, column=1)
        e = Label(Player_highest_goalW, width=10, text="Player_ID",borderwidth=2,relief='ridge', anchor="w", bg="yellow")
        e.grid(row=0, column=2)
        i=1
        for x in myresult:
            for j in range(len(x)):
                e = Label(Player_highest_goalW,width=10, text=x[j],borderwidth=2,relief='ridge', anchor="w")
                e.grid(row=i, column=j)
            i = i + 1
        print(myresult[0][0])
        for x in myresult:
            print(x)
    except:
        db.rollback()
        popupmsg("Error occured")

    back_button = tk.Button(Player_highest_goalW, text="back", command=Player_highest_goalW.destroy)
    back_button.grid(row = i,column = 0)

#•	Browse the players who did not get any cards in each team "Guest"
def players_not_get_any_cards(db):
    players_not_get_any_cardsW = tk.Toplevel()
    players_not_get_any_cardsW.geometry("600x600")
    players_not_get_any_cardsW.title("Browse the players who did not get any cards in each team")
    cursor = db.cursor()

    savequery = """SELECT player_name,player_id,team_id from player where player_id not in (SELECT player_id from player_booked)
order by team_id"""

    try:
        cursor.execute(savequery)
        myresult = cursor.fetchall()
        # Printing the result of the
        # query
        e = Label(players_not_get_any_cardsW, width=10, text="Player_name" ,borderwidth=2,relief='ridge', anchor="w" , bg="yellow")
        e.grid(row=0, column=0)
        e = Label(players_not_get_any_cardsW, width=10, text="Player_id",borderwidth=2,relief='ridge', anchor="w", bg="yellow")
        e.grid(row=0, column=1)
        e = Label(players_not_get_any_cardsW, width=10, text="Team_id",borderwidth=2,relief='ridge', anchor="w", bg="yellow")
        e.grid(row=0, column=2)
        i=1
        for x in myresult:
            for j in range(len(x)):
                e = Label(players_not_get_any_cardsW,width=10, text=x[j],borderwidth=2,relief='ridge', anchor="w")
                e.grid(row=i, column=j)
            i = i + 1
        print(myresult[0][0])
        for x in myresult:
            print(x)
    except:
        db.rollback()
        popupmsg("Error occured")

    back_button = tk.Button(players_not_get_any_cardsW, text="back", command=players_not_get_any_cardsW.destroy)
    back_button.grid(row = i,column = 0)


def logintodb(user, passw):
    db = mysql.connector.connect(host="localhost",
                                 user=user,
                                 password=passw,
                                 db="new_schema")
    cursor = db.cursor()
    try:
        cursor.execute("""CREATE TABLE x(
      s numeric NOT NULL, 
PRIMARY KEY (s))""")
        cursor.execute("""DROP TABLE x""")
        db.commit()
        myresult = cursor.fetchall()
        db.rollback()
        # If he have access to CREATE TABLE then he is "ADMIN" and then we rollback the DB
    except:
        db.rollback()
        passw =""
        # If he have doesn't access to CREATE TABLE then he is "Guest" and then we rollback the DB
    if passw:
        adminwindow = tk.Toplevel(root)
        adminwindow.geometry("600x600")
        adminwindow.title("Admin Window Login Page")
        Adminlogninss = tk.Label(adminwindow, text="Admin Login screen" )
        Adminlogninss.place(x=300, y=20)
        #Add a new tournament
        xxxxx = partial(NewTournament , db)
        submitbtn1 = tk.Button(adminwindow, text="Add a new tournament",
                              bg='pink', command=xxxxx)
        submitbtn1.place(x=170, y=50, width=300)
        #Add a team to a tournament
        xxxx = partial(Newteam , db)
        submitbtn2 = tk.Button(adminwindow, text="Add a team to a tournament",
                              bg='pink', command=xxxx)
        submitbtn2.place(x=170, y=90, width=300)
        # captain
        xxx = partial(captain , db)
        submitbtn3 = tk.Button(adminwindow, text="Select a captain for a team",
                              bg='pink', command=xxx)
        submitbtn3.place(x=170, y=130, width=300)
        #Approve a player to join a team
        xx = partial(Approve , db)
        submitbtn4 = tk.Button(adminwindow, text="Approve a player to join a team",
                              bg='pink', command=xx)
        submitbtn4.place(x=170, y=170, width=300)
        Logout_button = tk.Button(adminwindow, text="Logout",bg='red', command=adminwindow.destroy)
        Logout_button.place(x=170, y=230, width=50)
    # If no password is enetered by the
    # user
    else:
        GuestW = tk.Toplevel(root)
        GuestW.geometry("600x600")
        GuestW.title("Guest Window Login Page")
        Guestlogninss = tk.Label(GuestW, text="Guest Login screen")
        Guestlogninss.place(x=300, y=20)
        # Browse all results of a tournament with dates-
        xxxxx = partial(results_Of_Tournament, db)
        submitbtn1G = tk.Button(GuestW, text="Browse all results of a tournament with dates-",
                               bg='red', command=xxxxx)
        submitbtn1G.place(x=170, y=50, width=300)
        # Browse the player with the highest goal score for each team.
        xxxx = partial(Player_highest_goal, db)
        submitbtn2G = tk.Button(GuestW, text="Browse the player with the highest goal score for each team.",
                               bg='red', command=xxxx)
        submitbtn2G.place(x=170, y=90, width=300)
        # Browse the players who did not get any cards in each team.
        xxx = partial(players_not_get_any_cards, db)
        submitbtn3G = tk.Button(GuestW, text="Browse the players who did not get any cards in each team. ",
                               bg='red', command=xxx)
        submitbtn3G.place(x=170, y=130, width=300)

        Logout_button = tk.Button(GuestW, text="Logout", bg='red', command=GuestW.destroy)
        Logout_button.place(x=170, y=230, width=50)





root = tk.Tk()
root.geometry("300x300")
root.title("DBMS Login Page")

# Definging the first row
lblfrstrow = tk.Label(root, text="Username ", )
lblfrstrow.place(x=50, y=20)

Username = tk.Entry(root, width=35)
Username.place(x=150, y=20, width=100)

lblsecrow = tk.Label(root, text="Password ")
lblsecrow.place(x=50, y=50)

password = tk.Entry(root, width=35,show = '*')
password.place(x=150, y=50, width=100)

submitbtn = tk.Button(root, text="Login",
                      bg='blue', command=submitact)
submitbtn.place(x=150, y=135, width=55)
#exit button done by ME "Saud" Not "Sattam"
exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.place(x=205, y=135, width=50)
root.mainloop()
