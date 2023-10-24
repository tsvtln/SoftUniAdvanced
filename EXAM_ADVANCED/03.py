def team_lineup(*args):
    players_counties = {}
    final_list = []
    for player, cntry in args:
        if cntry not in players_counties.keys():
            players_counties[cntry] = [player]
        else:
            players_counties[cntry].append(player)
    sorted_dict = dict(sorted(players_counties.items(), key=lambda item: len(item[1]), reverse=True))
    sorted_dc = dict(sorted(sorted_dict.items(), key=lambda xxx: (-len(xxx[1]), xxx[0])))

    for country, players in sorted_dc.items():
        final_list.append(f"{country}:")
        for player_name in players:
            final_list.append(f"  -{player_name}")
    return '\n'.join(final_list)





# print(team_lineup(
#    ("Harry Kane", "England"),
#    ("Manuel Neuer", "Germany"),
#    ("Raheem Sterling", "England"),
#    ("Toni Kroos", "Germany"),
#    ("Cristiano Ronaldo", "Portugal"),
#    ("Thomas Muller", "Germany")))

# print(team_lineup(
#    ("Lionel Messi", "Argentina"),
#    ("Neymar", "Brazil"),
#    ("Cristiano Ronaldo", "Portugal"),
#    ("Harry Kane", "England"),
#    ("Kylian Mbappe", "France"),
#    ("Raheem Sterling", "England")))

# print(team_lineup(
#    ("Harry Kane", "England"),
#    ("Manuel Neuer", "Germany"),
#    ("Raheem Sterling", "England"),
#    ("Toni Kroos", "Germany"),
#    ("Cristiano Ronaldo", "Portugal"),
#    ("Thomas Muller", "Germany"),
#    ("Bruno Fernandes", "Portugal"),
#    ("Bernardo Silva", "Portugal"),
#    ("Harry Maguire", "England")))