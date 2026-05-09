class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.gpu = None

    def __str__(self):
        return f"PC [CPU={self.cpu}, RAM={self.ram}, storage={self.storage}, GPU={self.gpu}]"


class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def add_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def add_ram(self, ram):
        self.computer.ram = ram
        return self

    def add_storage(self, storage):
        self.computer.storage = storage
        return self

    def add_gpu(self, gpu):
        self.computer.gpu = gpu
        return self

    def build_computer(self):
        computer = self.computer
        self.computer = Computer()
        return computer


class Director:
    @staticmethod
    def build_gaming_pc():
        return (ComputerBuilder().add_cpu("Intel i9")
                .add_ram("32GB DDR5")
                .add_storage("1TB NVMe SSD")
                .add_gpu("32GB NVidia GForce RTX 4060")
                .build_computer())

    @staticmethod
    def build_office_pc():
        return (ComputerBuilder().add_cpu("AMD Athlon")
                .add_ram("16GB DDR4")
                .add_storage("200GB HDD")
                .add_gpu("Built-in")
                .build_computer())


if __name__ == "__main__":
    pc = Director.build_gaming_pc()
    print(pc)
