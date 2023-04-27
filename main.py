import find_playername
import find_stats
import calc_fifa_stats

if __name__=='__main__':
    player_ID=input("Enter ID of player: ").strip()
    player_name=find_playername.find_pn(player_ID)
    playerinfo_n_stats=find_stats.find_s(player_ID,player_name)
    fifa_stats=calc_fifa_stats.calc_fs(playerinfo_n_stats[0],playerinfo_n_stats[1])
    calc_fifa_stats.print_stats(fifa_stats)

#ADDNEWLINE

#addedfromworkingbranch
