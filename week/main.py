from ticket import create_ticket
from display import display_ticket

def main():

    ticket = create_ticket()

    display_ticket(
        ticket[0],
        ticket[1],
        ticket[2],
        ticket[3],
        ticket[4],
        ticket[5]
    )


if __name__ == "__main__":
    main()