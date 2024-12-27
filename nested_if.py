has_ticket=False
has_id=True
is_vip=True

if has_ticket:
    if has_id:
        print("watch movie")
    else:
        print("ID is required to watch the show")
  
else:
    if is_vip:
        print("watch movie")
    else:
        print("no vip no ticket")


    print("buy ticket")