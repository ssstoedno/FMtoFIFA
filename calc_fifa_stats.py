import random

def print_stats(fifa_stats:dict)->None:
    for dic in fifa_stats:
        print("------------------------------------------------------------------------")
        print(f"{dic.upper()} :", end=" ")
        for key in fifa_stats[dic]:
            print(f"{key}={fifa_stats[dic][key]};",end=" ")
        print()
    print("------------------------------------------------------------------------")



def calc_fs(player_info:dict,player_stats:dict)->dict:
    res={}
    
    gk=False
    attacking={"crossing":0,"finishing":0,"heading acc":0,"short passing":0,"volleys":0}
    skill={"dribbling":0,"curve":0,"fk acc":0,"long passing":0, "ball control":0}
    movement={"acceleration":0,"sprint speed":0,"agility":0,"reactions":0,"balance":0}
    power={"shot power":0,"jumping":0, "stamina":0,"strength":0,"long shots":0}
    mentality={"aggression":0,"interceptions":0,"positioning":0,"vision":0,"penalties":0,"composure":0,"work rate":""}
    defending={"defensive awareness":0,"slide tackle":0,"stand tackle":0}

    #find fm ratings
    if player_info["Position"]=="GK":
        gk=True
        gk={"gk diving":0,"gk handling":0,"gk kicking":0,"gk positioning":0,"gk reflexes":0}
        dic_copy=gk.keys()
        
        for key in dic_copy:
            if key=="gk diving":
                gk[key]=round(0.4*player_stats["Aerial Reach"]+0.4*player_stats["Command of Area"]+ 0.2*player_stats["Eccentricity"],0)
            elif key=="gk handling":
                gk[key]=player_stats["Handling"]
            elif key=="gk kicking":
                gk[key]=player_stats["Kicking"]
            elif key=="gk positioning":
                gk[key]=player_stats["Positioning"]
            elif key=="gk reflexes":
                gk[key]=player_stats["Reflexes"]

        res["gk"]=gk
    dic_copy=attacking.keys()
    for key in dic_copy:
        if key=="crossing" and not gk:
            attacking[key]=round(0.95*player_stats["Crossing"]+0.05*player_stats["Technique"],0)
        elif key=="finishing" and not gk:
            attacking[key]=round(0.95*player_stats["Finishing"]+0.05*player_stats["Technique"],0)
        elif key=="heading acc" and not gk:
            attacking[key]=player_stats["Heading"]
        elif key=="short passing":
            attacking[key]=round(0.97*player_stats["Passing"]+0.03*player_stats["Technique"],0)
        elif key=="volleys" and not gk:
            attacking[key]=round(0.2*player_stats["Flair"]+0.7*player_stats["Technique"]+0.1*player_stats["First Touch"],0)
    
    res["attacking"]=attacking

    dic_copy=skill.keys()
    for key in dic_copy:
        if key=="dribbling" and not gk:
            skill[key]=round(0.95*player_stats["Dribbling"]+0.05*player_stats["Technique"],0)
        elif key=="curve" and not gk:
            skill[key]=round(0.5*player_stats["Crossing"]+0.5*player_stats["Technique"],0)
        elif key=="fk acc" and not gk:
            skill[key]=round(0.95*player_stats["Free Kick Taking"]+0.05*player_stats["Technique"],0)
        elif key=="long passing":
            skill[key]=round(0.9*player_stats["Passing"]+0.1*player_stats["Technique"],0)
        elif key=="ball control":
            skill[key]=player_stats["Technique"]

    res["skill"]=skill

    dic_copy=movement.keys()
    for key in dic_copy:
        if key=="acceleration":
            movement[key]=player_stats["Acceleration"]
        elif key=="sprint speed":
            movement[key]=player_stats["Pace"]
        elif key=="agility":
            movement[key]=player_stats["Agility"]
        elif key=="reactions":
            movement[key]=player_stats["Anticipation"]
        elif key=="balance":
            movement[key]=player_stats["Balance"]

    res["movement"]=movement

    dic_copy=power.keys()
    for key in dic_copy:
        if key=="shot power" and not gk:
            power[key]=round(0.5*player_stats["Long Shots"]+0.4*player_stats["Finishing"]+0.1*player_stats["Technique"],0)
        elif key=="jumping":
            power[key]=player_stats["Jumping Reach"]
        elif key=="stamina":
            power[key]=player_stats["Stamina"]
        elif key=="strength":
            power[key]=player_stats["Strength"]
        elif key=="long shots" and not gk:
            power[key]=round(0.95*player_stats["Long Shots"]+0.05*player_stats["Technique"],0)

    res["power"]=power
        
    dic_copy=mentality.keys()
    for key in dic_copy:
        if key=="aggression":
            mentality[key]=player_stats["Aggression"]
        elif key=="interceptions" and not gk:
            mentality[key]=round(0.2*player_stats["Positioning"]+0.8*player_stats["Anticipation"],0)
        elif key=="positioning" and not gk:
            mentality[key]=player_stats["Off the Ball"]
        elif key=="vision":
            mentality[key]=player_stats["Vision"]
        elif key=="penalties" and not gk:
            mentality[key]=round(0.9*player_stats["Penalty Taking"]+0.05*player_stats["Technique"]+0.05*player_stats["Finishing"],0)
        elif key=="composure":
            mentality[key]=player_stats["Composure"]
        elif key=="work rate":
            work_rate=""
            if len(player_info["Position"].split())==1 and any(position in player_info["Position"] for position in ["GK", "DC"]):
                if player_stats["Work Rate"]<7:
                    work_rate="low/low"
                elif player_stats["Work Rate"]<14:
                    work_rate="medium/low"
                else:
                    work_rate="high/low"

            elif len(player_info["Position"].split())==1 and "ST" == player_info["Position"]:
                if player_stats["Work Rate"]<7:
                   work_rate="low/low"
                elif player_stats["Work Rate"]<14:
                    work_rate="low/medium"
                else:
                    work_rate="low/high"
            else:
                actions=dict((i,"low/low") for i in range(1,5))
                actions.update(dict((i,random.choice(["low/medium","medium/low"])) for i in range(5,9)))
                actions.update(dict((i,random.choice(["medium/medium","high/low","low/high"])) for i in range(9,13)))
                actions.update(dict((i,random.choice(["medium/high", "high/medium"])) for i in range(13,17)))
                actions.update(dict((i,"high/high") for i in range(17,21)))
                work_rate=actions[player_stats["Work Rate"]]

            mentality["work rate"]=work_rate

    res["mentality"]=mentality

    dic_copy=defending.keys()
    for key in dic_copy:
        if key=="defensive awareness":
            defending[key]=round(0.3*player_stats["Positioning"]+0.5*player_stats["Anticipation"]+0.2*player_stats["Concentration"],0)
        if key=="stand tackle" and not gk:
            defending[key]=player_stats["Tackling"]
        elif key=="slide tackle" and not gk:
            defending[key]=round(0.85*player_stats["Tackling"]+0.15*player_stats["Bravery"],0)

    res["defending"]=defending

    #calc fm->fifa rating

    actions={0:0,1:random.randint(15,19),2:random.randint(20,24),3:random.randint(25,29),4:random.randint(30,34),5:random.randint(35,39),6:random.randint(40,44),7:random.randint(45,49),8:random.randint(50,54),9:random.randint(55,59),
             10:random.randint(60,65),11:random.randint(66,68),12:random.randint(69,72),13:random.randint(73,75),14:random.randint(76,78),15:random.randint(79,83),16:random.randint(84,87),17:random.randint(88,91),
             18:random.randint(92,94),19:random.randint(95,97),20:random.randint(98,99)}
    for dic in res:
        for key in res[dic]:
            if key != "work rate":
                res[dic][key]=actions[res[dic][key]]
            
    return res  




    