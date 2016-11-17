#! /usr/bin/python
# -*- coding:utf-8 -*-
import os
import sys
import webbrowser

if sys.version_info.major == 2:
    input = raw_input


class Curiculum:
    def __init__(self):
        self.username = os.getlogin()
        self.function_switcher = {"--help": self.help,
                                  "--competencies": self.competencies,
                                  "--experience": self.experience,
                                  "--diplomas": self.formation,
                                  "--civilstatus": self.info,
                                  "--contact": self.contact,
                                  "--clear": self.clear,
                                  "--nature": self.nature,
                                  "--links": self.link,
                                  "--exit": self.exit
                                  }

        self.links = ["https://github.com/TheSystem-69",
                      "https://www.linkedin.com/in/ethan-chamik-387175106?trk=hp-identity-name",
                      "https://www.codingame.com/profile/2c08ee8ef061b39916ae4def1f2854d9647379",
                      "http://simplon.co/"]

        self.intro()
        self.input()

    def intro(self):
        print("*"*43)
        print("** CV-PY Version 0.1 - 2016 Ethan CHAMIK **")
        print("*"*43)
        print("\n\n\nType \'help\' (no quotes) to display some available commands.")

    def help(self):
        print("AVAIABLE COMMANDS :")
        print("-h,   --help")
        print("-com, --competencies")
        print("-ci,  --civilstatus")
        print("-ex,  --experiences")
        print("-na,  --nature")
        print("-di,  --diplomas")
        print("-con, --contact")
        print("-li,  --links")

    def input(self):
        print("%s@ethik's_CV:~$" % self.username),
        user_input = input()
        self.parse_input(user_input)

    def parse_input(self, user_input):
        understand_cmd = False
        if user_input == "":
            print("\nUnknown Command\n")
        else:
            for key in self.function_switcher.keys():
                if user_input in key:
                    understand_cmd = True
                    print("\n")
                    self.function_switcher[key]()
                    print("\n")
                    break
            if not understand_cmd:
                print("\nUnknown Command\n")
        self.input()

    def exit(self):
        sys.exit(0)

    def competencies(self):
        print("SPOKEN LANGUAGES :")
        print("\tFRENCH : NATIVE SPEAKER")
        print("\tENGLISH : TECHNICAL")
        print("\n")
        print("WORKING ENVIRONMENT :")
        print("\tGNU/Linux (ArchLinux/Ubuntu/Debian)")
        print("\n")
        print("CODE :")
        print("\tPython (Threading, Flask, TKinter, GTK, PyGame, BS4, Kivy...)")
        print("\tRethinkDB, Javascript, HTML/CSS, PHP, MySQL")
        print("\n")
        print("LEARNING :")
        print("\tC++ (Qt5)")
        print("\n")
        print("SOFTWARE USED :")
        print("\tPycharm, Atom")
        print("\tGit, GitHub")
        print("\tSlack, Discord, HackPad")
        print("\tSolidWorks, Cura, Pronterface")
        print("\tGimp")
        print("\n")
        print("OTHER :")
        print("\tScrum, TDD...")
        print("\tHardware, 3D printing...")

    def experience(self):
        print("\t\t2016")
        print("Assistant facilitateur (Formateur)")
        print("Simplon.VE - Le Cheylard")

        print("\n\t     2013 - 2015")
        print("Appui informatique & technicien pôle web")
        print("Departement de l'ardeche - Privas")

        print("\n\t\t2011")
        print("Technicien informatique")
        print("EDF - CNPE Cruas/Meysse")

    def formation(self):
        print("   %s EDUCATION %s \n" % ("*"*20, "*"*20))
        print("--> 2016 : Titre Professionnel - Developpeur logiciel")
        print("--> 2016 : Simplon.co - Formation developpeur web")
        print("--> 2014 : BAC Pro - Systemes Electroniques et Numeriques")
        print("--> 2010 : BEP - Systemes Electroniques et Numeriques")

    def info(self):
        print("NOM : CHAMIK\nPRENOM : ETHAN\nPROFESSION : DEVELOPPER\nAGE : 24 YEARS OLD\nFRENCH")

    def link(self):
        """Link to github, linkedin, codeingame..."""
        print("0 - GitHub : TheSystem-69")  # https://github.com/TheSystem-69
        print("1 - LinkedIn : Ethan Chamik")  # https://www.linkedin.com/in/ethan-chamik-387175106?trk=hp-identity-name
        print("2 - CodeInGame : Ethik")  # https://www.codingame.com/profile/2c08ee8ef061b39916ae4def1f2854d9647379
        print("3 - Simplon.co")  # http://simplon.co/
        print("\n")
        print("If you want, I can open any of this link for you.")
        print("Which one do you want ? [0/1/2/3] or [A/a]ll or [N/n]othing ?")
        user_choice = input()
        try:
            if user_choice in "Aa":
                for i in range(len(self.links)):
                    webbrowser.open(self.links[i])
            elif user_choice in "Nn":
                pass
            else:
                webbrowser.open(self.links[int(user_choice)])
        except:
            print("Unknown link")

    def contact(self):
        print("1 CHEMIN D'AURIVES")
        print("07160 LE CHEYLARD")
        print("06 13 56 29 94")
        print("E-MAIL : ethancmk[at]hotmail[dot]com")

    def nature(self):
        print("Active listening")
        print("Picky - Astute")
        print("Caring - Careful")
        print("Openness - sensitive")
        print("Thoughtful - Pugnacious")
        print("Autodidact - Passionate")
        print("headstrong - Adaptability")

    def clear(self):
        os.system("clear")
        self.intro()


if __name__ == "__main__":
    cv = Curiculum()


# TODO: User = real user !!!
