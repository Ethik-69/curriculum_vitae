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
        self.function_switcher = {
            "--help": self.help,
            "--competencies": self.competencies,
            "--experience": self.experience,
            "--education": self.education,
            "--civilstatus": self.info,
            "--contact": self.contact,
            "--clear": self.clear,
            "--nature": self.nature,
            "--links": self.link,
            "--exit": self.exit,
        }

        self.links = [
            "https://github.com/TheSystem-69",
            "https://www.linkedin.com/in/ethan-chamik-387175106?trk=hp-identity-name",
            "https://www.codingame.com/profile/2c08ee8ef061b39916ae4def1f2854d9647379",
            "http://simplon.co/",
        ]

        self.intro()
        self.input()

    def intro(self):
        print("*" * 43)
        print("** CV-PY Version 0.2 - 2020 Ethan CHAMIK **")
        print("*" * 43)
        print("\n\n\nType 'help' (no quotes) to display some available commands.")

    def help(self):
        print(
            "AVAILABLE COMMANDS :\n"
            "\t-h,   --help\n"
            "\t-com, --competencies\n"
            "\t-ci,  --civilstatus\n"
            "\t-ex,  --experiences\n"
            "\t-na,  --nature\n"
            "\t-ed,  --education\n"
            "\t-con, --contact\n"
            "\t-li,  --links\n"
            "\t--exit"
        )

    def input(self):
        user_input = input("%s@ethik's_CV:~$ " % self.username)
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
        print(f"{'*' * 20} COMPETENCIES {'*' * 20}\n")

        print(
            "SPOKEN LANGUAGES :\n"
            "\tFRENCH : NATIVE SPEAKER\n"
            "\tENGLISH : TECHNICAL++\n"
        )

        print(
            "WORKING ENVIRONMENT :\n"
            "\tGNU/Linux (ArchLinux/Ubuntu/Debian)\n"
            "\tWINDOWS (Sadly)\n"
        )

        print(
            "CODE :\n"
            "\tPython (multiprocessing, Flask, BS4, boto3, Kivy...)\n"
            "\tRethinkDB, Javascript, HTML/CSS, MySQL (But i hate it.)\n"
        )

        print("TECHNO :\n" "\tAWS, CDK, Docker\n")

        print("BASIC USE KNOWLEDGE :\n" "\tKubernetes\n")

        print(
            "SOFTWARE USED :\n"
            "\tJenkins\n"
            "\tPycharm, Atom, VSCode\n"
            "\tGit, GitHub\n"
            "\tSlack, Discord, Google suite\n"
        )

        print("OTHER :\n" "\tScrum, TDD...\n" "\tHardware, 3D printing...")

    def experience(self):
        print(f"{'*' * 20} EXPERIENCES {'*' * 20} \n")
        print("\t     2018 - Today\n" "Consultant Cloud DevOps ++\n" "Airbus - Toulouse\n")

        print("\t     2018 - 31 Dec 2022\n" "Consultant Cloud DevOps\n" "Gekko - Toulouse\n")

        print("\t\t2016\n" "Assistant Teacher\n" "Simplon.VE - Le Cheylard\n")

        print(
            "\n\t     2013 - 2015\n"
            "Computer Support & Web Technician\n"
            "Departement de l'ardeche - Privas\n"
        )

        print("\n\t\t2011\n" "Computer Technician\n" "EDF - CNPE Cruas/Meysse")

    def education(self):
        print(f"{'*' * 20} EDUCATION {'*' * 20} \n")
        print(
            "--> 2018 : Formation - Cloud DevOps (AWS)\n"
            "--> 2016 : Professional Title - Software Developer\n"
            "--> 2016 : Simplon.co - Formation web developer\n"
            "--> 2014 : BAC Pro - Electronic and Digital System\n"
            "--> 2010 : BEP - Electronic and Digital System"
        )

    def info(self):
        print(f"{'*' * 20} CIVIL STATUS {'*' * 20} \n")
        print(
            "LAST NAME : CHAMIK\n"
            "FIRST NAME : ETHAN\n"
            "JOB : DEVOPS\n"
            "AGE : 31 YEARS OLD\n"
            "FRENCH"
        )

    def link(self):
        """Link to github, linkedin, codeingame..."""
        print(f"{'*' * 20} LINKS {'*' * 20} \n")
        print(
            "0 - GitHub : TheSystem-69\n"
            "1 - LinkedIn : Ethan Chamik\n"
            "2 - CodeInGame : Ethik\n"
            "3 - Simplon.co\n"
        )
        print("If you want, I can open any of this link for you.")
        print("Which one do you want ? [0/1/2/3] or [A/a]ll or [N/n]othing ?")
        user_choice = input()

        try:
            if user_choice in "Aa":
                for i in range(len(self.links)):
                    webbrowser.open(self.links[i])

            elif user_choice in "Nn":
                pass

            elif user_choice in "1234":
                webbrowser.open(self.links[int(user_choice)])

        except:
            print("Unknown link")

    def contact(self):
        print(f"{'*' * 20} CONTACT {'*' * 20} \n")
        print("E-MAIL : ethancmk[at]hotmail[dot]com")

    def nature(self):
        print(f"{'*' * 20} NATURE {'*' * 20} \n")
        print(
            "Active listening\n"
            "Picky - Astute\n"
            "Caring - Careful\n"
            "Openness - sensitive\n"
            "Thoughtful - Pugnacious\n"
            "Autodidact - Passionate\n"
            "headstrong - Adaptability"
        )

    def clear(self):
        os.system("clear")
        self.intro()


if __name__ == "__main__":
    cv = Curiculum()
