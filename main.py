from pyscript import display, document
def acc_make(s):
    document.getElementById('out').innerHTML= " "
    un=document.getElementById('un').value
    ps=document.getElementById('ps').value
    unlen=len(un)
    pslen=len(ps)
    if unlen>6:
        if pslen>9:
            if not ps.isalpha():
                if ps.isdigit():
                    display(f'Must contain alphabetical characters', target='out' )
                else:
                    display(f'Successfully created', target='out')
            else:
                display(f'Must contain numerical characters', target='out')
        else:
            display(f'Password must be more than 9 characters', target="out")         
    else:
        display(f'Username must be more than 6 characters', target='out')

        


"""subj=["English", "Math", "Science", "SS", "Filpino"]
    for sub in subj:
        display(f'{sub}', target='out')
    o=1
    while co<50:
        display(co)
        co+=2
    while true:
        print("YO", target="out")
    for i in range(1,100,2):
        if i == 9:
            continue
        display(i, target="out")"""
    