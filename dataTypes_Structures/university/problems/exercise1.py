from enum import Enum
from dataclasses import dataclass, field


class Level_studied(Enum):
    TECNICO = "TECNICO"
    PROFESIONAL = "PROFESIONAL"
    MAESTRIA = "MAESTRIA"


@dataclass
class Candidato:
    edad: int
    experiencias_years: int
    nivel_estudios: Level_studied
    puntaje_prueba: float


class Estado(Enum):
    CONTRATADO = "CONTRATADO"
    LISTA_ESPERA = "LISTA_ESPERA"
    RECHAZADO = "RECHAZADO"


@dataclass
class Builder:
    lista_espera: list[Candidato] = field(default_factory=list)
    cantidatos: list[Candidato] = field(default_factory=list)

    def contractado(self, candidato: Candidato) -> Estado:
        match candidato.puntaje_prueba:
            case p if p < 60:
                return Estado.RECHAZADO
            case _:
                match candidato.nivel_estudios:
                    case Level_studied.MAESTRIA:
                        match candidato.experiencias_years:
                            case y if y >= 2:
                                return Estado.CONTRATADO
                            case _:
                                self.lista_espera.append(candidato)
                                return Estado.LISTA_ESPERA
                    case Level_studied.PROFESIONAL:
                        match candidato.experiencias_years:
                            case y if y > 3:
                                match candidato.edad:
                                    case e if e <= 35:
                                        return Estado.CONTRATADO
                                    case _:
                                        self.lista_espera.append(candidato)
                                        return Estado.LISTA_ESPERA
                            case y if 1 <= y <= 3:
                                self.lista_espera.append(candidato)
                                return Estado.LISTA_ESPERA
                            case _:
                                return Estado.CONTRATADO
                    case Level_studied.TECNICO:
                        match candidato.edad:
                            case e if e <= 30:
                                match candidato.experiencias_years:
                                    case y if y >= 2:
                                        self.lista_espera.append(candidato)
                                        return Estado.LISTA_ESPERA
                                    case _:
                                        return Estado.RECHAZADO
                            case _:
                                return Estado.RECHAZADO
                    case _:
                        return Estado.RECHAZADO

    def enter_data(self):
        print("-----Welcome to the choose employee program-----")
        action = int(
            input(
                "Enter the action you want to do\n 1. Enter possibles employees \n 2. Leave \nEnter data: "
            )
        )

        try:
            match action:
                case 1:
                    count = int(input("Enter the number of possibles employee: "))
                    i = 0
                    while i < count:
                        edad = int(input("Enter age: "))
                        experiencias_years = int(
                            input("Enter the years of experience: ")
                        )

                        # validamos que la informacion de su nivel de estudios corresponda con el enum
                        valid_values = {level.value for level in Level_studied}

                        while True:
                            user_profession = (
                                input(f"Enter level studied {valid_values}: ")
                                .strip()
                                .upper()
                            )

                            if user_profession in valid_values:
                                nivel_estudios = Level_studied(user_profession)
                                break
                            else:
                                print("Invalid level. Try again")

                        puntaje_prueba = float(input("Enter the employee' score: "))

                        candidato = Candidato(
                            edad=edad,
                            experiencias_years=experiencias_years,
                            nivel_estudios=nivel_estudios,
                            puntaje_prueba=puntaje_prueba,
                        )

                        self.cantidatos.append(candidato)
                        i += 1
                case 2:
                    print("Thank for use the program")

                case _:
                    print("Something else were wrong")
        except Exception as e:
            print(f"Type Error: {type(e)}")


if __name__ == "__main__":
    build = Builder()
    build.enter_data()

    print("\n---Results---")
    for canditato in build.cantidatos:
        estado = build.contractado(candidato=canditato)
        print(
            f"Candidato {canditato.nivel_estudios} |"
            f"Edad: {canditato.edad} |"
            f"Estado: {estado.value}"
        )

    print("\n----waiting list----")
    for c in build.lista_espera:
        print(c)
