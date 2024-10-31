import matplotlib.pyplot as plt
import matplotlib.patches as patches
import time


# Funzione per disegnare lo stato corrente delle torri
def draw_towers(towers, num_disks):
    plt.clf()  # Pulisci la figura
    fig, ax = plt.subplots()
    ax.set_xlim(0, 9)
    ax.set_ylim(0, num_disks + 2)

    # Disegna le torri
    for i in range(3):
        ax.add_patch(patches.Rectangle((i * 3 + 1.4, 0), 0.2, num_disks + 1, color='brown'))

    # Disegna i dischi
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c2f0c2']

    for i, tower in enumerate(towers):
        for j, disk in enumerate(tower):
            disk_width = disk * 0.5
            ax.add_patch(patches.Rectangle((i * 3 + 1.5 - disk_width / 2, j), disk_width, 0.5,
                                           color=colors[disk % len(colors)]))

    plt.pause(0.5)  # Pausa per visualizzare il disegno
    plt.draw()


# Funzione per risolvere le torri di Hanoi ricorsivamente
def hanoi(n, source, target, auxiliary, towers):
    if n == 1:
        # Sposta il disco dalla torre di origine a quella di destinazione
        disk = towers[source].pop()
        towers[target].append(disk)
        draw_towers(towers, num_disks)
    else:
        # Sposta n-1 dischi dalla torre di origine alla torre ausiliaria
        hanoi(n - 1, source, auxiliary, target, towers)
        # Sposta l'ultimo disco dalla torre di origine alla torre di destinazione
        hanoi(1, source, target, auxiliary, towers)
        # Sposta i n-1 dischi dalla torre ausiliaria alla torre di destinazione
        hanoi(n - 1, auxiliary, target, source, towers)


# Numero di dischi
num_disks = 5

# Inizializza le torri (la prima torre contiene tutti i dischi, le altre due sono vuote)
towers = [list(range(num_disks, 0, -1)), [], []]

# Configura il grafico
plt.ion()  # Modalità interattiva di matplotlib

# Disegna lo stato iniziale
draw_towers(towers, num_disks)

# Esegui l'algoritmo delle torri di Hanoi
hanoi(num_disks, 0, 2, 1, towers)

# Mantieni la finestra aperta alla fine della simulazione
plt.ioff()
plt.show()
