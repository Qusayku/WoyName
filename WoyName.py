from pyfiglet import Figlet

def generate_cool_text(text):
    custom_fig = Figlet(font='slant')
    return custom_fig.renderText(text)

name = "ByKEY"
cool_name = generate_cool_text(name)
print(cool_name)

def main():
    name = input("Write Your Name here ! :")
    cool_name = generate_cool_text(name)
    print(cool_name)

if __name__ == "__main__":
    main()