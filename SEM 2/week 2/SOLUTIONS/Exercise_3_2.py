class Competition:
    def __init__(self, description):
        self.__description = description
        self.__competitor_dict = {}

    def get_competitor_dict(self):
        return self.__competitor_dict

    def set_competitor_dict(self, competitor_dict):
        self.__competitor_dict = competitor_dict

class Competitor:
    def __init__(self, registration_no, name, score=0):
        self.registration_no = registration_no
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
        if score.isdigit():
            if 0 <= int(score) <= 100:
                self.__score = score
            else:
                return "Invalid input, score must be between 0 and 100 (inclusive)."
        else:
            return "Invalid input, score must be digits only."
        return True

    def show_competitor_info(self):
        return f"Reg No: {self.registration_no}, Name: {self.__name}, Score: {self.__score}"

comp = Competition("Annual Coding Challenge")
comp_dict = comp.get_competitor_dict()

while True:
    print("\n=== Competition Menu ===")
    print("1. Create Competitor")
    print("2. Retrieve Competitors")
    print("3. Update Competitor")
    print("4. Quit")
    choice = input("Enter choice: ")

    if choice == "1":
        reg_no = input("Enter Registration Number: ")
        name = input("Enter Name: ")
        competitor = Competitor(reg_no, name)
        comp_dict[len(comp_dict) + 1] = competitor
        print(f"Competitor added successfully.")
    elif choice == "2":
        print("--- Competitors List ---")
        for serial_no, competitor in comp_dict.items():
            print(f"Serial No: {serial_no}, {competitor.show_competitor_info()}")
    elif choice == "3":
        serial_no = int(input("Enter Serial No to update: "))
        if serial_no in comp_dict:
            competitor = comp_dict[serial_no]
            new_name = input("Enter new Name: ")
            competitor.set_name(new_name)

            while True:
                new_score = input("Enter new Score: ")
                val_score = competitor.set_score(new_score)
                if val_score is True:
                    break
                else:
                    print(val_score)
        else:
            print("Serial no doesn’t exist.")
        print("Student updated successfully.")
    else:
        print("Exiting program. Goodbye!")
        break
