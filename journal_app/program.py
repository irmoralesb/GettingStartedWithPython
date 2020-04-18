import journal


def main():
    print_header()
    run_event_loop()


def print_header():
    print("-----------------------")
    print("     JOURNAL APP")
    print("-----------------------")
    print()


def run_event_loop():
    print("What do you want to do with your journal?")
    cmd = None
    cmd_clean = None
    journal_name = "my_journal"
    journal_data = journal.load(journal_name)
    while cmd_clean != "x":
        cmd = input("[L]ist entries, [A]dd entry, E[x]it: ")
        cmd_clean = cmd.lower().strip()
        if cmd_clean == "l":
            list_entries(journal_data)
        elif cmd_clean == "a":
            add_entry(journal_data)
        else:
            print("Invalid option {}".format(cmd))
    journal.save(journal_name, journal_data)
    print("Program exited.")


def list_entries(data):
    print("Your journal entries: ")
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print("* [{}] {}".format(idx + 1, entry))


def add_entry(data):
    text = input("Type your entry, <enter> to exit: ")
    journal.add_entry(text, data)


if __name__ == main:
    main()
