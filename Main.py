#Oscar Juarez - 17315
#David Soto - -17551
#Algoritmos y Estructura de Datos - seccion 10
#Fecha: 2/03/18

import simpy
import random

def iniciarRAM(self, env):
    self.capacidad_ram = simpy.Resource(env, capacity = 10)
    self.instrucciones_a_realizar = simpy.Container(env, init=1, capacity=10)
    self.mon_proc = env.process(self.monitorear_memoria(env))

def monitorear_memoria(self, env):
    while True:
        if self.capacidad_ram.level < 10:
            print ("Llamando a la memoria en %s" % env.now)
            env.process(memoria(env, self))
        #yield env.timeout(15)

def memoria(env, ram):
    yield env.timeout(tiempo_solicitado)

    print("Hora de solicitado: %s" % env.now)

    cantidad = ram.instrucciones_a_realizar.capacity - ram.instrucciones_a_realizar.numero_inst

    yield ram.instrucciones_a_realizar.put(cantidad)

def proceso(nombre, env, ram):
    print ('Proceso %s soliticanto memoria en %s' % (name, env.now))
    with ram.capacidad_ram.request() as req:
        yield req
        print ('Ejecutando el proceso %s en %s' % (nombre, env.now))
        #yield ram.instrucciones_a_realizar.get(40)
        #yield env.timeout(5)
        print ('El proceso %s se ha terminado de realizar' % (nombre, env.now))

def generador_instrucciones(env, ram):
    for i in range (25):
        env.process(proceso(i, env, ram))
        #yield env.timeout(25)


#--------PROGRAMA----------

env = simpy.Environment() #ambiente de simulación
CPU = simpy.Resource(env,capacity = 1)
random.seed(10) # fijar el inicio de random

totalProcesos = 0

for i in range(25):
    env.process(RAM('carro %d'%i,env,random.expovariate(1.0/10),CPU))

#env.run(until=50)  #correr la simulación hasta el tiempo = 50

#print ("tiempo promedio por vehículo es: ", totalDia/5.0)
