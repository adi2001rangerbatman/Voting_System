import matplotlib.pyplot as plt
import mysql.connector


class Candidate:
    def __init__(self, c_name, nic, age, qualification, province, list_no, ppid):
        self.c_name = c_name
        self.nic = nic
        self.age = age
        self.qualification = qualification
        self.province = province
        self.list_no = list_no
        self.ppid = ppid

    def register(self):
        con = mysql.connector.connect(host="localhost", user="root", password="", database="election system")
        cursor = con.cursor()
        sql = "INSERT INTO candidate(nic, c_name, age, qualification, province,list_no, ppid ) VALUES (%s, %s, %s, " \
              "%s ,%s,%s ,%s) "
        val = (self.nic, self.c_name, self.age, self.qualification, self.province, self.list_no, self.ppid)
        cursor.execute(sql, val)
        con.commit()
        con.close()


class Citizen:
    def __init__(self, name, nic, age, province):
        self.name = name
        self.nic = nic
        self.age = age
        self.province = province

    def register(self):
        con = mysql.connector.connect(host="localhost", user="root", password="", database="election system")
        cursor = con.cursor()
        sql = "INSERT INTO citizen (nic, name, age, province) VALUES (%s, %s, %s, %s)"
        val = (self.nic, self.name, self.age, self.province)
        cursor.execute(sql, val)
        con.commit()
        con.close()


class Parties:
    def __init__(self, ppid, p_name):
        self.ppid = ppid
        self.p_name = p_name

    def register(self):
        con = mysql.connector.connect(host="localhost", user="root", password="", database="election system")
        cursor = con.cursor()
        sql = "INSERT INTO political_parties(ppid , p_name) VALUES (%s, %s)"
        val = (self.ppid, self.p_name)
        cursor.execute(sql, val)
        con.commit()
        con.close()


class Votes:
    c_count = 0


def add_citizen():
    nic = int(input("Enter NIC:"))
    name = input("Name:")
    age = int(input("Enter Age:"))
    if age >= 18:
        print("Eligible for Voting\n")
    else:
        print("Not Eligible for voting!!!!!!")
        print("Registered Unsuccessfully!\n")
        menu()
    province = input("Province:")
    citizen_1 = Citizen(name, nic, age, province)
    citizen_1.register()
    print("Registered Successfully!\n")
    input("\nPress Enter to continue...")
    menu()


def add_candidate():
    global ls
    con = mysql.connector.connect(host="localhost", user="root", password="", database="election system")
    cursor = con.cursor()
    cursor.execute("SELECT nic FROM citizen")
    result = cursor.fetchall()
    for x in result:
        ls = list(x)
    nic = int(input("Enter NIC:"))
    for i in ls:
        if ls[0] == nic:
            c_name = input("Candidate Name:")
            age = int(input("Enter Age:"))
            qualification = input("Enter Qualification:")
            province = input("Province:")
            list_no = int(input("List No:"))
            ppid = int(input("Input PPID: "))
            candidate_1 = Candidate(c_name, nic, age, qualification, province, list_no, ppid)
            candidate_1.register()
        else:
            print("You are not registered as a Citizen!!")
            input("\nPress Enter to continue...")
    menu()


def add_parties():
    global ls
    con = mysql.connector.connect(host="localhost", user="root", password="", database="election system")
    cursor = con.cursor()
    cursor.execute("SELECT ppid FROM political_parties")
    result = cursor.fetchall()
    for x in result:
        ls = list(x)
    ppid = int(input("Input Political Party ID:"))
    for items in range(len(ls)):
        if ls[items] == ppid:
            print("Already registered!!!")
            menu()
        else:
            p_name = input("Input Party Name: ")
            party_1 = Parties(ppid, p_name)
            party_1.register()
            print("Registered Successfully!\n")
            input("\nPress Enter to continue...")
    menu()


def display_parties():
    con = mysql.connector.connect(host="localhost", user="root", password="", database="election system")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM political_parties")
    result = cursor.fetchall()

    for items in result:
        print("PPID:- ", items[0])
        print("Political Party Name:- ", items[1])
    input("\nPress Enter to continue...")
    menu()


def display_candidates():
    con = mysql.connector.connect(host="localhost", user="root", password="", database="election system")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM candidate")
    result = cursor.fetchall()

    for items in result:
        print("NIC:", items[0])
        print("Name:", items[1])
        print("Age:", items[2])
        print("Qualification:", items[3])
        print("Province:", items[4])
        print("PPID:", items[6])
        print("\n")
    input("\nPress Enter to continue...")
    menu()


def display_election_results():
    con = mysql.connector.connect(host="localhost", user="root", password="", database="election system")
    cursor = con.cursor()
    candidate_names = []
    vote_counts = []

    cursor.execute("SELECT c_name, vote_count FROM candidate")
    result = cursor.fetchall()

    for items in result:
        candidate_names.append(items[0])
        vote_counts.append(items[1])

    plt.bar(candidate_names, vote_counts)
    plt.xlabel("Candidates")
    plt.ylabel("Vote Count")
    plt.title("Election Results")
    plt.show()

    cursor.close()
    con.close()
    input("\nPress Enter to continue...")
    menu()


def vote():
    global ls
    global re
    con = mysql.connector.connect(host="localhost", user="root", password="", database="election system")
    cursor = con.cursor()
    id = int(input("Input ID: "))
    cursor.execute("SELECT nic FROM citizen WHERE nic = %s", (id,))
    result = cursor.fetchall()
    if len(result) != 0:
        cursor.execute("SELECT * FROM political_parties")
        result = cursor.fetchall()
        for items in result:
            print("PPID:- ", items[0])
            print("Political Party Name:- ", items[1])

        input("\nPress Enter to continue...")
        pid = int(input("Input Party ID: "))
        cursor.execute("SELECT c.c_name, c.province, c.list_no, pp.ppid FROM candidate c JOIN political_parties pp ON "
                       "c.ppid = pp.ppid WHERE pp.ppid = %s", (pid,))
        result = cursor.fetchall()
        x = result
        if not x:
            print("Already  Not Any Candidate registered in this party")
            input("\nPress Enter to continue...")
            menu()
        else:
            for items in result:
                ls = list(items)
                print("Candidate Name: ", ls[0])
                print("Province: ", ls[1])
                print("List No:", ls[2])
                print("Political Party: ", ls[3])
                print("\n")

            candidate_votes = {}  # Dictionary to store candidate votes

            # Allow the citizen to vote for up to 3 candidates
            for _ in range(3):
                list_no = int(input("List No: "))
                cursor.execute("SELECT nic, province FROM candidate WHERE list_no = %s", (list_no,))
                result = cursor.fetchone()

                if result is None:
                    print("Invalid List No. Please try again.")
                    continue

                nic, province = result
                cursor.execute("SELECT province FROM citizen WHERE nic = %s", (id,))
                result = cursor.fetchone()

                if result is None:
                    print("Invalid ID.")
                    break

                citizen_province = result[0]

                if citizen_province != province:
                    print("You can only vote for candidates from your province.")
                    break

                if nic in candidate_votes:
                    candidate_votes[nic] += 1
                else:
                    candidate_votes[nic] = 1

                Votes.c_count += 1

            # Update the vote count for each candidate in the database
            for nic, vote_count in candidate_votes.items():
                cursor.execute("UPDATE candidate SET vote_count = vote_count + %s WHERE nic = %s", (vote_count, nic))
                con.commit()

            print("Vote cast successfully!")
            cursor.close()
            con.close()
            input("\nPress Enter to continue...")
            menu()

    else:
        print("Invalid ID.")

    cursor.close()
    con.close()
    input("\nPress Enter to continue...")
    menu()

def menu():
    print("\n\n")
    print("\t------------------------------------------------")
    print("\t\t   Welcome To The Vote Calculating System      ")
    print("\t------------------------------------------------\n")
    print("\t\t\t   Main Menu\n")
    print("\tPlease select an option:")
    print("\t1. Citizen Registration")
    print("\t2. Candidate Registration")
    print("\t3. Parties Registration")
    print("\t4. Show Candidates")
    print("\t5. Show Political Parties")
    print("\t6. Show Election Result")
    print("\t7. Vote")
    print("\t8. Exit")
    print("\t------------------------------------------------\n")

    choice = int(input('Select Option: '))
    print("\n")
    match choice:
        case 1:
            add_citizen()
        case 2:
            add_candidate()
        case 3:
            add_parties()
        case 4:
            display_candidates()
        case 5:
            display_parties()
        case 6:
            display_election_results()
        case 7:
            vote()
        case 8:
            select = input("\nAre you sure want to exit(Y/N)...?")
            if select.upper() == 'Y':
                exit()
            elif select.upper() == 'N':
                menu()
            else:
                print("\nInvalid Input!!!")
                menu()


menu()
