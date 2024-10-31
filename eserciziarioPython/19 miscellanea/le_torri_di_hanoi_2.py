import tkinter as tk
import time


class HanoiGame:
    def __init__(self, root, num_disks):
        self.root = root
        self.num_disks = num_disks
        self.towers = [[], [], []]
        self.canvas = tk.Canvas(root, width=600, height=400)
        self.canvas.pack()

        # Create the base for the towers
        self.canvas.create_rectangle(50, 350, 550, 370, fill='black')

        # Create the three towers (vertical lines)
        self.tower_positions = [150, 300, 450]
        for x in self.tower_positions:
            self.canvas.create_rectangle(x - 10, 150, x + 10, 350, fill='black')

        # Add disks to the first tower
        self.disks = []
        self.disk_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
        for i in range(num_disks):
            width = 120 - i * 15
            disk = self.canvas.create_rectangle(
                150 - width // 2, 320 - i * 20,
                150 + width // 2, 340 - i * 20,
                fill=self.disk_colors[i % len(self.disk_colors)]
            )
            self.towers[0].append(disk)
            self.disks.append(disk)

        # Start solving after drawing the initial state
        self.root.after(1000, self.solve_hanoi, num_disks, 0, 2, 1)

    def move_disk(self, from_tower, to_tower):
        if not self.towers[from_tower]:
            return
        disk = self.towers[from_tower].pop()
        self.towers[to_tower].append(disk)

        # Get the position of the destination tower
        x = self.tower_positions[to_tower]
        y = 340 - len(self.towers[to_tower]) * 20

        # Move the disk graphically
        self.canvas.coords(disk, x - (self.canvas.coords(disk)[2] - self.canvas.coords(disk)[0]) // 2, y - 20,
                           x + (self.canvas.coords(disk)[2] - self.canvas.coords(disk)[0]) // 2, y)

        # Update the canvas
        self.root.update()
        time.sleep(0.5)

    def solve_hanoi(self, n, from_tower, to_tower, aux_tower):
        if n == 1:
            self.move_disk(from_tower, to_tower)
        else:
            self.solve_hanoi(n - 1, from_tower, aux_tower, to_tower)
            self.move_disk(from_tower, to_tower)
            self.solve_hanoi(n - 1, aux_tower, to_tower, from_tower)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Torri di Hanoi")

    num_disks = 6  # Numero di dischi
    game = HanoiGame(root, num_disks)

    root.mainloop()
