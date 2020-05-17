class Notebook:
    notebook_id = 0

    def __init__(self, clockRateCpuInGhz=4.2, capacityOfRam=32, manufacturerName="Lenovo", clockRateGpuInGhz=1.7,
                 capacityOfHdd=1500,
                 screenDiagonal=17):
        self._clock_rate_cpu_in_ghz = clockRateCpuInGhz
        self._capacity_of_ram = capacityOfRam
        self._manufacturer_name = manufacturerName
        self._clock_rate_gpu_in_ghz = clockRateGpuInGhz
        self._capacity_of_hdd = capacityOfHdd
        self._screen_diagonal = screenDiagonal
        Notebook.notebook_id += 1

    def __del__(self):
        print("Notebook deleted.")

    def __str__(self):
        return str(self._clock_rate_cpu_in_ghz) + ', ' + str(
            self._capacity_of_ram) + ', ' + self._manufacturer_name + ', ' + str(
            self._clock_rate_gpu_in_ghz) + ', ' + str(self._capacity_of_hdd) + ', ' + str(self._screen_diagonal)

    @staticmethod
    def get_notebook_id():
        return Notebook.notebook_id


if __name__ == '__main__':
    first_notebook = Notebook(3.5, 8, "Hp", 1.6, 1000, 15)
    second_notebook = Notebook(4.1, 16, "Dell", 1.7, 2000, 15)
    third_notebook = Notebook()

    print('First notebook: ', first_notebook)
    print('Second notebook: ', second_notebook)
    print('Third notebook: ', third_notebook)
    print('\nNotebook ID: ', Notebook.get_notebook_id(), '\n')
    