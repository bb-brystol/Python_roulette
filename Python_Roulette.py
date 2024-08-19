import tkinter as tk
from tkinter import Toplevel
import random

root = tk.Tk()
root.title("Roulette")
label = tk.Label(root, text="Welcome in Roulette")
label.pack(pady=20)
root.configure(bg='#0D865D') 
window_width = 1920
window_height = 1080
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

position_x = int((screen_width / 2) - (window_width / 2))
position_y = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

bg_image = tk.PhotoImage(file="C:/Users/bartek/Desktop/ruleta/roulette_photo.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=1, y=1, relwidth=1, relheight=1)

      
#Start
def on_button_click():
    start_window = Toplevel(root)
    start_window.title("Give me your money")
    #start_window.attributes('-fullscreen', True)
    start_window.state('zoomed')
    start_window.configure(bg="#0D865D")
    #root.withdraw()   
    # Kwota zakładu
    balance = 1000  # Początkowy balans gracza
    bet = tk.IntVar(value=5)  # Wartość zakładu
    chosen_number = tk.IntVar(value=-1)
    chosen_bet = tk.IntVar(value=0)
    # Aktualizacja informacji o balancie
    balance_label = tk.Label(start_window, text=f"Balance: ${balance}", font=("Arial", 20), bg="#0D865D", fg="white")
    balance_label.place(x=10, y=10)

    # Funkcja obstawiania
    def place_bet(amount):
        bet.set(amount)
        chosen_bet.set(amount)
        selected_bet_label.config(text=f"Selected Bet: {chosen_bet.get()}$")  # Aktualizacja etykiety
        print(f"Zakład: {bet.get()}$")

    # Przycisk obstawiania 5$
    button_5 = tk.Button(start_window, text="BET 5$", command=lambda: place_bet(5), width=15, height=2)
    button_5.place(x=100, y=60)

    # Przycisk obstawiania 50$
    button_50 = tk.Button(start_window, text="BET 50$", command=lambda: place_bet(50), width=15, height=2)
    button_50.place(x=600, y=60)

    # Przycisk obstawiania 100$
    button_100 = tk.Button(start_window, text="BET 100$", command=lambda: place_bet(100), width=15, height=2)
    button_100.place(x=1100, y=60)

    # Przycisk obstawiania 500$
    button_500 = tk.Button(start_window, text="BET 500$", command=lambda: place_bet(500), width=15, height=2)
    button_500.place(x=1600, y=60)

    def choose_number(num):
        chosen_number.set(num)
        selected_number_label.config(text=f"Selected Number: {chosen_number.get()}")  

    def choose_bet(num):
        chosen_bet.set(num)
        selected_bet_label.config(text=f"Selected Bet: {chosen_bet.get()}")

    for i in range(37):
        btn = tk.Button(start_window, text=str(i), width=4, height=2, command=lambda n=i: choose_number(n))
        btn.pack(side='left', padx=7)
         
    selected_number_label = tk.Label(start_window, text="Selected Number: None", font=("Arial", 20), bg="#0D865D", fg="white")
    selected_number_label.place(x=900, y=850)

    selected_bet_label = tk.Label(start_window, text="Selected Bet: None", font=("Arial", 20), bg="#0D865D", fg="white")
    selected_bet_label.place(x=900, y=950)
    # Funkcja spinowania koła ruletki
    def spin_wheel():
        nonlocal balance
        numbers = list(range(37))
        result = random.choice(numbers)

        result_label.config(text=f"Result: {result}")

        if result == chosen_number.get():
            balance += bet.get() * 35  # Wygrana
            show_win_message()
        else:
            balance -= bet.get()  # Przegrana

        balance_label.config(text=f"Balance: ${balance}")
    def show_win_message():
        win_window = Toplevel(start_window)
        win_window.title("Gratulacje!")
        win_window.geometry("600x300")
        win_label = tk.Label(win_window, text=f"You won! Your balance is now: {balance}", font=("Arial", 20), fg="green")
        win_label.pack(expand=True)
       
        
        # Zamknięcie okna po 3 sekundach
        win_window.after(3000, win_window.destroy)
    # Przycisk "Spin Wheel"
    spin_button = tk.Button(start_window, text="Start rolling", command=spin_wheel, width=15, height=2)
    spin_button.place(x=900, y=150)

    # Wynik
    result_label = tk.Label(start_window, text="Result: ", font=("Arial", 20), bg="#0D865D", fg="white")
    result_label.place(x=900, y=250)


    def end_game():
        start_window.destroy()
    button = tk.Button(start_window, text="Close game", command=end_game, width=20, height=5)
    button.place(x = 1720, y = 920)
    
#Help
def on_help_click():
    help = tk.Toplevel()
    help.title("Instructions")
    help.geometry("450x600")
    label = tk.Label(help, bg='#1FA956', text="Wybierz Wysokość Zakładu:\n Przed zawarciem zakładu wybierz kwotę, którą chcesz postawić. W kasynach online minimalny zakład w ruletce zazwyczaj wynosi od 0,10 do 1 USD, podczas gdy maksymalny zakład może znacząco się różnić, sięgając kilku tysięcy dolarów lub więcej, w zależności od limitów stołu i polityki konkretnego kasyna. \n \nWybierz Rodzaj Zakładu:\n \n Zdecyduj, na jaki rodzaj zakładu chcesz postawić. W ruletce istnieją różne rodzaje zakładów, w tym: Zakłady wewnętrzne: Zakładanie na konkretne numery lub małe grupy numerów. Zakłady zewnętrzne: Zakładanie na większe grupy numerów, takie jak czerwone lub czarne, parzyste lub nieparzyste, lub kolumny. \n \nOgłoszone zakłady:\n \n Niektóre gry ruletki online oferują specjalne zakłady, takie jak Neighbours, Voisins, Orphelins i inne. Różne zakłady dają różne wypłaty w zależności od swoich odpowiednich szans. Na przykład, zakład na pojedynczy numer (link do /zakłady/Pojedynczy numer) wypłaca 35:1, a zakładparzysty/nieparzystywypłaca 1:1.\n \n Umieść Żetony: \n \nGdy już wybrałeś rodzaj i wysokość zakładu, musisz umieścić swoje żetony na wirtualnym stole ruletki. W ruletce online zazwyczaj robisz to, klikając na odpowiednie miejsce w układzie zakładów.", wraplength=280)
    label.pack(fill='both', expand=True)
    def on_OK_thanks_click():
        help.destroy()
    button = tk.Button(help, text="OK, Thanks", command=on_OK_thanks_click)
    button.pack(pady=10)
#End
def on_end_click():
    root.destroy()


button = tk.Button(root, text="Start", command=on_button_click,width=15, height=4, bg="#1FA956")
button.pack(pady=20)
button = tk.Button(root, text="Help", command=on_help_click, width=15, height=4, bg="#1FA956")
button.pack(pady=20)
button = tk.Button(root, text="End Game", command=on_end_click, width=15, height=4, bg="#1FA956")
button.pack(pady=20)


root.mainloop()
