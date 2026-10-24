from pyscript import document

def candidate_checker(e):
    club_members=["nathan bernaldez","max calata", "ethan deleon", "yujin kim", "antonio mago"]
    f_name = document.getElementById('first_name').value
    l_name = document.getElementById('last_name').value
    candidate = f_name + ' ' + l_name

    member_check = candidate.lower() in club_members
    messages= (f'Sorry {candidate}, your name is not on the list',
    f'Welcome! {candidate}, you are now in')

    document.getElementById('result').innerHTML = messages[member_check]