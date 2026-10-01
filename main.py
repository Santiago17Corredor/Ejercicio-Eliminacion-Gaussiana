class SistemaEcuaciones:
    def __init__(self):
        # Las primeras tres columnas son los coeficientes.
        # La última columna contiene los términos independientes.
        self.matriz = [
            [2.0,  1.0, -1.0,   8.0],
            [-3.0, -1.0, -2.0, -11.0],
            [-2.0,  1.0,  2.0,  -3.0]
        ]
        self.n = 3

    def mostrar_matriz(self):
        for fila in self.matriz:
            print(
                f"[{fila[0]:9.4f} {fila[1]:9.4f} "
                f"{fila[2]:9.4f} | {fila[3]:9.4f}]"
            )
        print()

    def eliminacion_gaussiana(self):
        print("Matriz aumentada inicial:")
        self.mostrar_matriz()

        # k indica la fila y columna del pivote.
        for k in range(self.n):
            pivote = self.matriz[k][k]

            # Los pivotes de este sistema son distintos de cero.
            if abs(pivote) < 1e-12:
                raise ValueError(
                    "Se necesita intercambiar filas para continuar."
                )

            print(f"Pivote a{k + 1}{k + 1} = {pivote:.4f}")

            # Eliminar los elementos debajo del pivote.
            for i in range(k + 1, self.n):
                factor = self.matriz[i][k] / pivote

                print(
                    f"M{i + 1}{k + 1} = "
                    f"{self.matriz[i][k]:.4f} / {pivote:.4f} "
                    f"= {factor:.4f}"
                )
                print(
                    f"F{i + 1} = F{i + 1} "
                    f"- ({factor:.4f}) * F{k + 1}"
                )

                # Se actualizan los coeficientes y el término independiente.
                for j in range(k, self.n + 1):
                    self.matriz[i][j] -= factor * self.matriz[k][j]

                self.matriz[i][k] = 0.0

            self.mostrar_matriz()

        print("Matriz triangular superior obtenida.")

    def sustitucion_regresiva(self):
        soluciones = [0.0] * self.n

        # Recorrer las filas desde la última hasta la primera.
        for i in range(self.n - 1, -1, -1):
            suma = 0.0

            for j in range(i + 1, self.n):
                suma += self.matriz[i][j] * soluciones[j]

            soluciones[i] = (
                self.matriz[i][self.n] - suma
            ) / self.matriz[i][i]

        return soluciones

    def resolver(self):
        self.eliminacion_gaussiana()
        x, y, z = self.sustitucion_regresiva()

        print("\nSoluciones:")
        print(f"x = {x:.6f}")
        print(f"y = {y:.6f}")
        print(f"z = {z:.6f}")


# Crear un objeto de la clase y resolver el sistema.
sistema = SistemaEcuaciones()
sistema.resolver()