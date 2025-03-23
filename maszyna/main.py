import matplotlib
matplotlib.use("TkAgg")  # Zmiana backendu na TkAgg
import csv_reader as cr
import sqlite_handler as sh
import matplotlib.pyplot as plt

def main():
    # data = cr.read_csv()
    # sh.create_table(headers=data[0])
    # sh.insert_data(headers=data[0],data=data[1])
    headers, data = sh.read_data('dane')
    #print(headers)
    naglowki = [naglowek[1] for naglowek in headers]
    wartosci = [data[0][i] for i in range(1,9)]
    print(wartosci)
    plt.figure(figsize=(10,5))
    plt.bar(naglowki[1:len(wartosci) + 1], wartosci)
    plt.xlabel('Kolumny')
    plt.ylabel('Wartości')
    plt.title('Wykres słupkowy')
    plt.grid(True,axis='y',color='b',linestyle='--',linewidth=0.5)
    plt.show()
    
    
if __name__ == '__main__':
    main()