class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def calcular_salario(self):
        salario_base = self.salario
        return salario_base


class Programador(Empleado):
    def __init__(self, nombre, salario, lineas_programadas):
        super().__init__(nombre, salario)
        self.lineas_programadas = lineas_programadas

    def calcular_salario(self):
        salario_bonus = 0.01 * self.lineas_programadas
        salario_final = self.salario + salario_bonus
        return salario_final


class GestorProyectos(Empleado):
    def __init__(self, nombre, salario, proyectos_gestionados):
        super().__init__(nombre, salario)
        self.proyectos_gestionados = proyectos_gestionados

    def calcular_salario(self):
        salario_bonus = 50 * self.proyectos_gestionados
        salario_final = self.salario + salario_bonus
        return salario_final


programador1 = Programador('Samuel', 1600, 32450)

gestor1 = GestorProyectos('Andrea', 1800, 3)

print(f"El programador {programador1.nombre} tiene un salario total de: {programador1.calcular_salario()}€")
print('')
print(f"El gestor de proyectos {gestor1.nombre} tiene un salario total de: {gestor1.calcular_salario()}€")
