#!/usr/bin/env python3
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# NOELIA FERNANDEZ TALAVERA
# MANIPULACIÓN
# MASTER DE ROBOTICA Y AUTOMATIZACIÓN
# ENTREGA 1 DE MANIPULACIÓN
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#En esta práctica se pretende coger un objeto con un gripper flotante,  pasarlo por encima de un obstáculo y depositarlo en el suelo
#Para ello, se va a usar GRASPIT! y Gazebo
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# El gripper con el que me toca realizar la práctica es un schunk y el objeto que tengo que coger es un construction_cone

# PASOS PREVIOS

# Lo primero es iniciar GRASPIT mediante la instrucción: roslaunch graspit_interface graspit_interface.launch
# Con GRASPIT! lo que se hace es importar la garra, el objeto a coger y la superficie. Tras esto se planifican los posibles agarres que existen para coger el objeto.
# En mi caso existen 10 pisibles agarres. Dentro de estas opciones, se obtiene el dofs, la pose, epsilon_quality y volume_quality. Para estos dos últimos parámetros, 
# lo mejor para un agarre fuerte y estable es coger los valores más altos.

# Al principio seleccione la pose que presentaba mayor valor de epsilon_quality y volume_quality. Sin embargo, al realizar la comprobación de colisiones, el cubo que rodea la 
# garra colisionaba. De esa forma fui escogiendo las siguientes poses en orden decreciente de los valores epsilon_quality y volume_quality. La pruebas que se realizaron son las siguientes:

# pose: (0.13091874575145673, 0.15573131231692333, 0.12734620859499166, 0.285769154875614, 0.10400013105463027, 0.39602433974889534, 0.86642061678422020)
# pose: ( 0.12507508031653083, 0.14549317803960687, 0.09618141709293977, 0.31936521271438256, 0.2365114984285554, 0.31126564789996025, 0.8632391722207667)
# pose: (0.16812477177687862, 0.09951479719804965, 0.2714068675810464, 0.48756757910535264, -0.07758475734294457, 0.3126084284817816, 0.811501344222875)
# pose: (0.18320125978245017, 0.08981563704179489, 0.17899188659282822,  0.4575796090712538, 0.05907773090282281, 0.23821152157432185, 0.8546262306194555)
# pose: (0.1293616869390618, 0.15703835296646632, 0.20648472159145423, 0.3453248222827963, 0.13312190540115681, 0.4020669205251057, 0.8374792635266732)
# pose: (0.1374528881405734, 0.1189021949427939, 0.12084095474250842, 0.529238682307343. 0.3086495437439036, 0.23447792118444918, 0.7547595516277266)

# Finalmente, la pose usada es la que se ve a continuación, ya que fue la primera en no obtener valores de colisiones. Se sigue respetando que epsilon_quality y volume_quality son positivos,
# asi que el agarre debe ser fuerte y seguro para asegurar la sujección del objeto.

# pose: ( -0.0029576076089575204, 0.19114477251526724, 0.19604699051348687, -0.4084609483059216, -0.5445844147386103, 0.44995840188535785, 0.5780353843023863)
# volume_quality: 0.007168593270364019
# epsilon_quality: 0.009860706482437448
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# INICIO DE LA SIMULACIÓN EN GAZEBO

# En este momento ya se pasa a la simulación en Gazebo en donde se encuentra el gripper, el objeto y la mesa.
# se lanza la instucción: roslaunch manipulacion_pkg gripper_gazebo.launch tipo_gripper:=schunk \objeto:=construction_cone
# Donde se identifica el tipo de garra y objeto asignado.

#Lo primero es importar las librerías

import manipulacion_lib # Importa la biblioteca para manipulación de objetos y grippers en simulación
import rospy # Importa rospy, necesario para la comunicación con el sistema ROS
import PyKDL # Importa PyKDL para las transformaciones entre sistemas  de referencia
import numpy as np #se importa para realizar las interpolaciones de las posiciones

# ahora se van a definir unas funciones de interpolación, es decir, generan unas poses intermedias entre dos poses finales para que la simulación se vea fluida. Estas se usarán posetriormente

# Función 1 para generar una serie de poses intermedias entre dos poses dadas
def generar_trayectoria(pose_gripper_world, pose2_gripper_world, num_frames):
    # Generar una serie de poses intermedias
    poses_intermedias = []
    for i in range(num_frames):
      alpha = i / (num_frames - 1)  # Interpolación lineal entre 0 y 1
     # Interpolación lineal de las posiciones
      posicion_interpolada = pose_gripper_world.p * (1 - alpha) + pose2_gripper_world.p * alpha
     # Crear un nuevo frame con la posición interpolada y la misma orientación que la pose inicial
      pose_interpolada = PyKDL.Frame(pose_gripper_world.M, posicion_interpolada)
      poses_intermedias.append(pose_interpolada)
    return poses_intermedias

# Función 2 para generar una serie de poses intermedias entre dos poses dadas
def generar_trayectoria2(pose2_gripper_world, pose3_gripper_world, num_frames):
    # Generar una serie de poses intermedias
    poses2_intermedias = []
    for i in range(num_frames):
      alpha = i / (num_frames - 1)  # Interpolación lineal entre 0 y 1
     # Interpolación lineal de las posiciones
      posicion2_interpolada = pose2_gripper_world.p * (1 - alpha) + pose3_gripper_world.p * alpha
     # Crear un nuevo frame con la posición interpolada y la misma orientación que la pose inicial
      pose2_interpolada = PyKDL.Frame(pose2_gripper_world.M, posicion2_interpolada)
      poses2_intermedias.append(pose2_interpolada)
    return poses2_intermedias

# Función 3 para generar una serie de poses intermedias entre dos poses dadas
def generar_trayectoria3(pose3_gripper_world, pose4_gripper_world, num_frames):
    # Generar una serie de poses intermedias
    poses3_intermedias = []
    for i in range(num_frames):
      alpha = i / (num_frames - 1)  # Interpolación lineal entre 0 y 1
     # Interpolación lineal de las posiciones
      posicion3_interpolada = pose3_gripper_world.p * (1 - alpha) + pose4_gripper_world.p * alpha
     # Crear un nuevo frame con la posición interpolada y la misma orientación que la pose inicial
      pose3_interpolada = PyKDL.Frame(pose3_gripper_world.M, posicion3_interpolada)
      poses3_intermedias.append(pose3_interpolada)
    return poses3_intermedias


# Inicializar el nodo de ROS si aún no se ha inicializado
if not rospy.get_node_uri():
    rospy.init_node('gripper_flotante_gazebo', anonymous=True, log_level=rospy.WARN)

# Creación de una instancia para controlar un gripper flotante en Gazebo
simulacion_gripper_flotante = manipulacion_lib.SimulacionGripperFlotante( nombre_gripper_gazebo="gripper")
# Esta instancia permite interactuar con un gripper en la simulación de Gazebo, especificando su nombre
# Independientemente del gripper asignado para la práctica, se utiliza el nombre "gripper" para referenciarlo en la simulación de Gazebo.


# Obtener la pose (posición y orientación) de un objeto específico en el Gazebo
# Se obtiene la pose del objeto 'construction_cone' con respecto al sistema de referencia global (world)
pose_objeto_world = simulacion_gripper_flotante.obtener_pose_objeto( nombre_objeto_gazebo='construction_cone')
print("Pose objeto con respecto a world")
print(pose_objeto_world)

# Fijamos una pose relativa del gripper con respecto al objeto. Pose del gripper con respecto al objeto con la pose optima obtenida pregiamente el GRASPIT!
pose_gripper_objeto = PyKDL.Frame(PyKDL.Rotation.Quaternion(-0.4084609483059216, -0.5445844147386103, 0.44995840188535785, 0.5780353843023863), PyKDL.Vector(-0.0029576076089575204, 0.19114477251526724, 0.19604699051348687))

print("Pose gripper con respecto a objeto")
print(pose_gripper_objeto)

# Calcular la pose del gripper en el sistema de referencia global a partir de su pose relativa al objeto
# Se realiza una transformación de coordenadas para obtener la pose del gripper en el sistema global
pose_gripper_world = pose_objeto_world * pose_gripper_objeto
print("Pose gripper con respecto a world: ")
print( pose_gripper_world)

# Hacemos un preagarre de 0.2 metros para acercarnos al objeto y colocar la garra en la posición optima para el agarre
offset = 0.2 # Definimos un offset de 0.2 metros

# Creamos una nueva pose de tipo Frame de PyKDL que no altera la rotación  (identidad) y desplaza el gripper 0.2 metros a lo largo del eje X local. Este valor se puede modificar al gusto del usuario
pose_nueva_gripper = PyKDL.Frame(PyKDL.Rotation(), PyKDL.Vector(offset, 0, 0 ))

# Multiplicamos la pose actual del gripper en el mundo por la transformación que acabamos de crear para obtener la nueva pose en el sistema de coordenadas del mundo.
pose_nueva_world = pose_gripper_world*pose_nueva_gripper

# Fijamos la nueva pose del gripper en la simulación de Gazebo. Actualiza la posición y orientación del gripper en Gazebo según la pose calculada, que se encuentra a 0.2 metros del objeto
simulacion_gripper_flotante.fijar_pose_gripper( pose_gripper_world=pose_nueva_world)
rospy.sleep(1)
# Fijar la pose del gripper en la simulación de Gazebo tocando el objeto
simulacion_gripper_flotante.fijar_pose_gripper( pose_gripper_world=pose_gripper_world)
rospy.sleep(1)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# DETECCION DE COLISIONES
# Se comprueba si el gripper colisiona con el entorno
from manipulacion_lib import Obstaculo, DetectorColisionesGripperFlotante
obstaculo_rojo = Obstaculo('cubo', [0.75,0,0,1,0,0,0], [0.3,1,0.6], 'obstaculo')
suelo = Obstaculo('cubo', [0,0,0,1,0,0,0], [4,4,0.1], 'suelo')
obstaculos = [obstaculo_rojo, suelo]

detector_colisiones = DetectorColisionesGripperFlotante('robotiq', obstaculos)

# Obtener la matriz de rotación del frame
rotation = pose_gripper_world.M

# Convertir la matriz de rotación a cuaternión
qx, qy, qz, qw = rotation.GetQuaternion()
pose_gripper = [pose_gripper_world.p.x(), pose_gripper_world.p.y(), pose_gripper_world.p.z(), qx, qy, qz, qw]
print("Colisiona en la pose actual:", detector_colisiones.hay_colision(pose_gripper))

# Esto incluye cargar las configuraciones iniciales como nombres de articulaciones y posiciones predeterminadas.
simulacion_gripper_flotante.configurar_gripper()
# Abrir completamente el gripper antes de intentar cualquier operación de agarre.
# Es una práctica común asegurarse de que el gripper no esté restringido o en una posición que podría interferir con el objeto a agarrar.
simulacion_gripper_flotante.abrir_gripper()

# Pequeña pausa para asegurar que la acción de abrir se ha completado.
rospy.sleep(1)

# Obtener el tipo de gripper actual para aplicar la configuración de posiciones de articulaciones correcta.
tipo_gripper = simulacion_gripper_flotante.get_tipo_gripper()
# Basado en el tipo de gripper, se definen las posiciones específicas de las articulaciones. Estas posiciones deben ser determinadas experimentalmente o calculadas para lograr el agarre deseado.
# En este punto se sustituyen los valores dofs obtenidos previamente en GRASPIT! para la pose correspondiente.

if tipo_gripper == 'jaco':
  posicion_articulaciones = [-0.6,-0.6,-0.6]  # Posiciones para el gripper Jaco.
elif tipo_gripper == 'schunk':
  # posicion_articulaciones = [0, 0, 0, 0, 0, 0, 0]  # Posiciones para el gripper Schunk.
  posicion_articulaciones = [0.2580143213213457,-0.5817693566886498, 1.2474314470597565, -0.4986443566886497, 1.3305564470597564, -0.4767693566886497, 1.3524314470597565]
    # Posiciones para el gripper Schunk.
elif tipo_gripper == 'robotiq':
  posicion_articulaciones = [0.4, 0.4, 0.4, 0, 0.4, 0.4, 0.4, 0, 0.4, 0.4, 0.4]  # Posiciones para el gripper Robotiq.

# Aplicar las posiciones definidas a las articulaciones del gripper. Este paso es crucial para controlar el estado del gripper y realizar agarres efectivos en la simulación.
simulacion_gripper_flotante.set_posicion_articulaciones(posicion_articulaciones)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# En este punto comienza el proceso de desplazar el gripper a distintas posiciones. Para ello hay que definir las posiciones a donde se quiere desplazar el cono. Para comprobar el agarre
# se ha decidido desplazar de manera vertical el cono hasta una pose2 (desplazamiento en un eje), de manera horizontal hasta una pose3 para pasar por encima del obstáculo (desplazamiento en
# un eje), y depositar el cono en una pose4 (desplazamiento en 2 ejes). De esta forma se compuega la calidad del agarre.

# Definición de la posición vertical a 0.4 metros del suelo, desplazamiento en el eje Z
pose2_gripper_world = PyKDL.Frame(PyKDL.Rotation.Quaternion(qx, qy, qz, qw), PyKDL.Vector(pose_gripper_world.p.x(), pose_gripper_world.p.y(), pose_gripper_world.p.z() + 0.4))
print("Pose2 gripper desplazada verticalmente")
print(pose2_gripper_world)
rospy.sleep(1)

# Se llama a la función de interpolación entre pose y pose2 con 150 frames para generar una trayectoria fluida
trayectoria = generar_trayectoria(pose_gripper_world, pose2_gripper_world, num_frames=150)
for pose_interpolada in trayectoria:
    # Fijar la pose del gripper en la simulación de Gazebo
    simulacion_gripper_flotante.fijar_pose_gripper(pose_gripper_world=pose_interpolada)
    rospy.sleep(0.05)  # Pequeña pausa para suavizar la animación

rospy.sleep(1)


# Definición de la posición horizontal a 0.7 metros metros de la posición 2, movimientoel eje Y
pose3_gripper_world = PyKDL.Frame(PyKDL.Rotation.Quaternion(qx, qy, qz, qw), PyKDL.Vector(pose2_gripper_world.p.x()+ 0.7, pose2_gripper_world.p.y(), pose2_gripper_world.p.z()))
print("Pose3 gripper horizontalmente")
print(pose3_gripper_world)
rospy.sleep(1)

# Se llama a la función de interpolación entre pose2 y pose3 con 150 frames para generar una trayectoria fluida
trayectoria2 = generar_trayectoria(pose2_gripper_world, pose3_gripper_world, num_frames=150)
for pose_interpolada2 in trayectoria2:
    # Fijar la pose del gripper en la simulación de Gazebo
  simulacion_gripper_flotante.fijar_pose_gripper(pose_gripper_world=pose_interpolada2)   
  rospy.sleep(0.05)  # Pequeña pausa para suavizar la animación

rospy.sleep(1)

# Definición de la posición vertical a 0.3 metros en el eje X y -0.4 metros en el eje Z,movimiento diagonal
pose4_gripper_world = PyKDL.Frame(PyKDL.Rotation.Quaternion(qx, qy, qz, qw), PyKDL.Vector(pose3_gripper_world.p.x()+ 0.3, pose3_gripper_world.p.y(), pose3_gripper_world.p.z()-0.4))
print("Pose4 gripper diagonal")
print(pose3_gripper_world)
rospy.sleep(1)

# Se llama a la función de interpolación entre pose3 y pose4 con 150 frames para generar una trayectoria fluida
trayectoria3 = generar_trayectoria(pose3_gripper_world, pose4_gripper_world, num_frames=150)
for pose_interpolada3 in trayectoria3:
    # Fijar la pose del gripper en la simulación de Gazebo
  simulacion_gripper_flotante.fijar_pose_gripper(pose_gripper_world=pose_interpolada3)   
  rospy.sleep(0.05)  # Pequeña pausa para suavizar la animación
  
rospy.sleep(1)

# Apertura del gripper para dejar el objeto
simulacion_gripper_flotante.abrir_gripper()
rospy.sleep(1)

# Creamos una nueva pose de tipo Frame de PyKDL que no altera la rotación (identidad) y desplaza el gripper 0.2 metros a lo largo del eje X local. Posición de separación
pose_nueva_gripper_espera = PyKDL.Frame(PyKDL.Rotation(), PyKDL.Vector(offset, 0, 0 ))

# Multiplicamos la pose actual del gripper en el mundo por la transformación que acabamos de crear para obtener la nueva pose en el sistema de coordenadas del mundo.
pose_nueva_world_espera = pose4_gripper_world*pose_nueva_gripper_espera

# Fijamos la nueva pose del gripper en la simulación de Gazebo.
simulacion_gripper_flotante.fijar_pose_gripper(pose_gripper_world=pose_nueva_world_espera)