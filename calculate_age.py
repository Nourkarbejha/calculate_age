import datetime

def calculate_age(birthdate):

    today = datetime.datetime.now()

    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

    return age




def main():
    people=[]
    while True:

        names=input('Enter the name plz type"done" for stop:')

        if names.lower()=="done":

            break
        ages=(input("Enter the birtday(YYYY-MM-DD)"))
        try:
            birthdate = datetime.datetime.strptime(ages, "%Y-%m-%d")
    
            people.append(birthdate)
        except ValueError:

            print("Eroor404")

    if not people :

        print("Sorry, no date was entered")

        return

    current_date = datetime.datetime.now()

    oldest_person = min(people)

    youngest_person = max(people)

    print((calculate_age(oldest_person)) )

    print( (calculate_age(youngest_person)) )

    print(len(people))

main()