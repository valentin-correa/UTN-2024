import sys

## Definición de registros

ip = 100
memoria = [0] * 65535
xp = 0

def cargarPrograma(): # Cargar programa en memoria
    global ip
    global memoria

    with open(sys.argv[1], "rb") as prog:
            programa = prog.read()
            if len(programa) < 924:
                for byte in programa:
                    memoria[ip] = int(byte, 16)
                    ip+=1
            else:
                raise("El programa no cabe en memoria.")

## Operaciones de SISTEMA
    
def dumpMem(): # Opcode 0xF0
      global memoria

      with open("mem.dump", "wb") as dump:
            memory = [int(x, 16) for x in memoria]
            dump.write(bytes(memory))

def halt(): # Opcode 0xF1
    exit()

def add_d0():
    global memoria
    global ip

    parametro_1 = (memoria[ip+1])
    valor_a = parametro_1>>8
    valor_b = parametro_1&0xFF
    suma = valor_a + valor_b
    if suma > 255:
        suma = (suma >> 0) & 0xFF
    memoria[ip+2] = suma
         
def sub_d1():
    global memoria
    global ip 

    parametro_1 = (memoria[ip+1])
    valor_a = parametro_1>>8
    valor_b = parametro_1&0xFF
    resta = valor_a - valor_b
    memoria[ip+2] = resta

def mod_d2():
    global memoria
    global ip

    parametro_1 = (memoria[ip+1])
    valor_a = parametro_1>>8
    valor_b = parametro_1&0xFF
    modulo = valor_a % valor_b
    memoria[ip+2] = modulo

def inrxp_d3():
    global xp
    xp+=1

def dcrxp_d4():
    global xp
    xp-=1

# Asociaciones

opcodes = {
     # MOV
     0xA0: mov_a0(),
     0xA1: mov_a1(),
     0xA2: mov_a2(),
     0xA3: mov_a3(),
     0xA4: mov_a4(),
     0xA5: mov_a5(),
     0xA6: mov_a6(),
     0xA7: mov_a7(),
     # JUMPS
     0xB0: jmp_b0(),
     0xB1: jmp_b1(),
     # LÓGICAS
     0xC0: log_c0(),
     0xC1: log_c1(),
     0xC2: log_c2(),
     0xC3: log_c3(),
     # ARITMÉTICAS
     0xD0: add_d0(),
     0xD1: sub_d1(),
     0xD2: mod_d2(),
     0xD3: inrxp_d3(),
     0xD4: dcrxp_d4(),
     # SISTEMA
     0xF0: dumpMem(),
     0xF1: halt()
}    
    
if __name__ == "__main__":
      cargarPrograma()
      dumpMem()