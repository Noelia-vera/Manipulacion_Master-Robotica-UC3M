#!/usr/bin/env python3
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# NOELIA FERNANDEZ TALAVERA
# MANIPULACIÓN
# MASTER DE ROBOTICA Y AUTOMATIZACIÓN
# ENTREGA 2 DE MANIPULACIÓN
# GITHUB: https://github.com/Noelia-vera/Manipulacion_Master-Robotica-UC3M?tab=readme-ov-file
# VIDEO YOUTUBE: https://youtu.be/i169xTrFE5w
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#En esta práctica se pretende coger un determinado objeto con un gripper concreto, pasarlo por encima de un obstáculo y posicionarlo en el suelo. Esto se hace con un grazo robótico UR10 
# y en el trayecto no debe haber colisión con los obstáculos ni con el propio brazo. 
# Para conseguir esto se identifican los obstáculos, se define el punto inicial de agarre del gripper y el punto final, y el `algoritmo RRT hace la planificación de una trayectoria libre 
# de obstáculos` que vaya de un punto a otro. No siempre es la misma porque existen varias posibilidades. Es decir, `el planificador hace el trabajo por nosotros` y por lo tanto 
# `no es necesario definir posiciones intermedias de paso.`

# Sin embargo, `para que el video se vea fluido`, se han puesto posiciones intermedias a las que debe ir llegando el brazo para realizar el path completo, sin hacer movimientos extraños 
# con el brazo.
#A continuación se muestran los pasos que se han seguido.

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# El gripper con el que me toca realizar la práctica es un schunk y el objeto que tengo que coger es un construction_cone

# PASOS PREVIOS

# Es necesario tener las posiciones de agarre del objeto, información sacada de la práctica anterior. El punto de agarra no ha cambiado aqui

# La pose usada es la que se ve a continuación, ya que fue la primera en no obtener valores de colisiones. Se sigue respetando que epsilon_quality y volume_quality son positivos,
# asi que el agarre debe ser fuerte y seguro para asegurar la sujección del objeto.

# pose: ( -0.0029576076089575204, 0.19114477251526724, 0.19604699051348687, -0.4084609483059216, -0.5445844147386103, 0.44995840188535785, 0.5780353843023863)
# volume_quality: 0.007168593270364019
# epsilon_quality: 0.009860706482437448
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# INICIO DE LA SIMULACIÓN EN GAZEBO

# En este momento ya se pasa a la simulación en Gazebo en donde se encuentra el gripper, el brazo, el objeto y el obstáculo.
# se lanza la instucción: roslaunch manipulacion_pkg  robot_gazebo.launch tipo_gripper:=jaco \ objeto:=mustard_bottle
# Donde se identifica el tipo de gripper y objeto asignado.


## POSICIÓN INICIAL EN GAZEBO

# 1. Inicializar el Nodo ROS: Primero, inicializamos un nodo ROS. Este nodo nos facilitará la comunicación con el sistema 
# ROS y permitirá el control del brazo robótico en la simulación de Gazebo.
# 2. Creación de una Instancia de GazeboRobot: Se crea una instancia de `GazeboRobot`, especificando los nombres de las 
# articulaciones del brazo robótico que queremos controlar. Esto nos permite interactuar específicamente con nuestro brazo robótico en Gazebo.
# 3. Lectura de Posiciones Actuales de las Articulaciones: Utilizamos el método `obtener_posiciones_articulaciones` para leer 
# las posiciones actuales de las articulaciones del brazo robótico. 

# Como la posición de como se debe coger el objeto viene determinada por las condiciones que se explicaron en la `Práctica 1` 
# y que se encuentran en el archivo .YALM, y siguiendo el consejo de la profesora de prácticas, la pose inicial desde donde 
# se debe empezar el proceso de agarre es diferente a la impuesta por el posición inicial de Gazebo. Esta posición se ha escogido 
# de forma que sea más facil para el brazo llegar hasta la posición de agarre, por eso `NO es necesaria una posición de preagarre`.
# Este punto de inicio es el siguiente :[1.2566831278301214, -0.8740287446197677, 0.7563676502460766, -1.1837925124354811, 3.75749471561243, 1.064756533529244]

# Lo primero es importar las librerías

import manipulacion_lib # Importa la biblioteca para manipulación de objetos y grippers en simulación
import rospy # Importa rospy, necesario para la comunicación con el sistema ROS
import PyKDL # Importa PyKDL para las transformaciones entre sistemas  de referencia
import numpy as np #se importa para realizar las interpolaciones de las posiciones
from sensor_msgs.msg import JointState
from geometry_msgs.msg import Pose
from visualization_msgs.msg import MarkerArray
import numpy as np
from manipulacion_lib import Obstaculo, DetectorColisionesGripperFlotante

# Inicializar el Nodo ROS
if not rospy.get_node_uri():
    rospy.init_node('robot_arm_controller', anonymous=True)

# Creación de una Instancia de `GazeboRobot`
gazebo_robot = manipulacion_lib.GazeboRobot(nombres_articulaciones=[
    'shoulder_pan_joint',
    'shoulder_lift_joint',
    'elbow_joint',
    'wrist_1_joint',
    'wrist_2_joint',
    'wrist_3_joint'
])

# Lectura de Posiciones Actuales de las Articulaciones
posiciones_actuales = gazebo_robot.obtener_posiciones_articulaciones()
print("Posiciones actuales de las articulaciones:", posiciones_actuales)

# Envío de Comando a una Posición Específica
posicion_deseada = [1.2566831278301214, -0.8740287446197677, 0.7563676502460766, -1.1837925124354811, 3.75749471561243, 1.064756533529244]
# Define la posición deseada para las articulaciones y el tiempo para alcanzarla
gazebo_robot.command_posicion_articulaciones(posicion_deseada, time_from_start=2)
rospy.sleep(2)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## SISTEMAS DE REFERENCIA

# En este momento se recuperan los datos de la `posición de agarre` que da el archivo .YALM y se `traducen` de modo que 
# sea entendible para el sistema de referencia que maneje el brazo. En este caso se pasa de la posición de referencia 
# del gripper respecto al objeto a una posicón respecto al mundo.
# Además, se crea una función para transformar los datos de frame a pose para que la información que manejen las 
# siguientes instrucciones sean compatibles.

# Definir el robot en Gazebo para simulaciones en Gazebo
ur10 = manipulacion_lib.GazeboRobot()
simulacion_gripper = manipulacion_lib.SimulacionGripper(nombre_gripper_gazebo="gripper")
# Configurar el gripper basado en el archivo YAML específico para su tipo.
# Esto incluye cargar las configuraciones iniciales como nombres de articulaciones y posiciones predeterminadas.
simulacion_gripper.configurar_gripper()

# Fijamos una pose relativa del gripper con respecto al objeto. Pose del gripper con respecto al objeto con la pose optima obtenida pregiamente el GRASPIT!
pose_gripper_objeto = PyKDL.Frame(PyKDL.Rotation.Quaternion(-0.4084609483059216, -0.5445844147386103, 0.44995840188535785, 0.5780353843023863), PyKDL.Vector(-0.0029576076089575204, 0.19114477251526724, 0.19604699051348687))

print("Pose gripper con respecto a objeto")
print(pose_gripper_objeto)

# Obtener la pose (posición y orientación) de un objeto específico en el Gazebo. Se obtiene la pose del objeto 'construction_cone' con respecto al sistema de referencia global (world)
pose_objeto_world = simulacion_gripper.obtener_pose_objeto( nombre_objeto_gazebo='construction_cone')
print("Pose objeto con respecto a world")
print(pose_objeto_world)

# Calcular la pose del gripper en el sistema de referencia global a partir de su pose relativa al objeto. Se realiza una transformación de coordenadas para obtener la pose del gripper en el sistema global
pose_gripper_world = pose_objeto_world * pose_gripper_objeto
print("Pose gripper con respecto a world: ")
print( pose_gripper_world)

#Crear pose del efector final
def frame_to_pose(frame):
    rotation = frame.M
    qx, qy, qz, qw = rotation.GetQuaternion()
    pose = Pose()
    pose.position.x = frame.p.x()
    pose.position.y = frame.p.y()
    pose.position.z = frame.p.z()
    pose.orientation.x = qx
    pose.orientation.y = qy
    pose.orientation.z = qz
    pose.orientation.w = qw
    return pose

tcp_pose = frame_to_pose(pose_gripper_world)
print("Pose gripper_tcp con respecto a world: ")
print( tcp_pose)
print(pose_gripper_world)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## DETECCIÓN DE OBSTÁCULOS Y COLISIONES
# En este punto se define la existencia de un obstáculo y  con la 'función de deteccion' de colisiones se podrá ver cuando una posición tiene o no colisiones.

#1. Definición de Obstáculos: A continuación, definimos los obstáculos presentes en el entorno que podrían interactuar con el brazo robótico. Cada obstáculo se define con un tipo (por ejemplo, 'cubo'),
# una pose inicial, dimensiones y un nombre único.
# 2. Creación de una Instancia del Detector de Colisiones : Instanciamos el `DetectorColisiones`, especificando si se incluirá el brazo robótico y/o el gripper, junto con los obstáculos definidos. 
# 3. Verificación de Auto-colisiones y Colisiones con Obstáculos: Utilizamos el método `hay_colision` del detector de colisiones para determinar si, dada una configuración específica de las 
# articulaciones del brazo, existe alguna colisión con los obstáculos definidos o auto-colisiones.

# Definición de Obstáculos. Crea una lista para almacenar los obstáculos definidos
obstaculos = []

# Crea y añade un obstáculo específico a la lista. Asume que manipulacion_lib.Obstaculo es una clase que permite definir obstáculos con tipo, pose, dimensiones y nombre
obstaculo = manipulacion_lib.Obstaculo('cubo', [0.7, 0, 0, 1, 0, 0, 0], 
                                       [0.8, 0.3, 0.7], 'obstaculo')
obstaculos.append(obstaculo)
obstaculos = []

# Creación de una Instancia del Detector de Colisiones. Inicializa el detector de colisiones con la configuración deseada, incluyendo el brazo robótico, el gripper y los obstáculos
detectorColisiones = manipulacion_lib.DetectorColisiones(
    usa_brazo_robotico=True,  # Indica si el brazo robótico se incluye en la 
                              # detección de colisiones
    usa_gripper=True,  # Indica si el gripper se incluye 
                       # en la detección de colisiones
    gripper_dimensions=[0.1, 0.1, 0.1],  # Especifica las dimensiones del 
                                        # gripper como un prisma rectangular
    obstaculos=obstaculos  # Lista de obstáculos definidos previamente
)

#Obtener los Límites de las Articulaciones
min_limits = ur10.get_limites_inferiores()
max_limits = ur10.get_limites_superiores()
joint_limits = []
for i in range(len(min_limits)):
    joint_limits.append((min_limits[i], max_limits[i]))

print("Posiciones actuales de las articulaciones:", posiciones_actuales)
hay_colision = detectorColisiones.hay_colision(posiciones_actuales)

# Imprime el resultado de la detección de colisiones
print(f"¿Hay colisión?: {'Sí' if hay_colision else 'No'}")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## INICIO DEL MOVIMIENTO A LA POSICIÓN DE AGARRE
# Se quiere que el brazo vaya desde su posición hasta la posición de agarre. Para ello se crea un `bucle` que se ejecuta hasta que encuentra un `camino libre` de colisiones para llegar 
# al punto deseado. Esto se consigue con un planificador `RRT` que compueba las colisiones a lo largo del path.

# 1. Validación de la posición final: se determina si la posición final a la que se quiere llegar es viable para las articulaciones del brazo y no va a pasar por una zona de singularidad.
# 2. Comprobación de colisiones: se comprueba si en al posición deseada a la que se quiere llegar hay colisiones o no. En caso de que no haya una colisión se ejecuta el planificador que 
# saca un path libre de colisiones. En caso de que existan colisiones el bucle se vuelve a ejecutar hasta encontrar una opción viable.

#`NOTA: para que la simulación sea fluida se ha comentado la parte del algortimo RRT y se ha metido el comando para mover el brazo directamente hasta la posición deseada introduciendo 
# los valores de las posiciones de las articulaciones directamente.`

# El uso de la cinemática se mantiene igual
kin = manipulacion_lib.Cinematica(robot=ur10, frame_base='base_link',  frame_final='tool0')

while True:
    valida, posiciones_articulares_deseadas = kin.calcular_ci(posiciones_articulaciones_actuales=ur10.obtener_posiciones_articulaciones()+np.random.rand(6), pose_deseada=tcp_pose)

    if valida:
        print("Posiciones articulares deseadas: ", posiciones_articulares_deseadas)
        hay_colision = detectorColisiones.hay_colision(posiciones_articulares_deseadas)
        if not hay_colision:
            print("NO hay colision")
            # Configuración del Algoritmo RRT*
            #rrt = manipulacion_lib.RRTStarJointSpace(ur10.obtener_posiciones_articulaciones(), posiciones_articulares_deseadas3, joint_limits, 0.4, 300,1.0, detectorColisiones)
        
            # Planificación de la Trayectoria
            #path = rrt.plan()
            #if path:
              #  print(path)
               # ur10.command_path_posicion_articulaciones(path, 0.4, 1.0)
            
            gazebo_robot.command_posicion_articulaciones([0.5490487683843837, -0.45702793026260485, 1.1701852104646282, -1.1908789269716504, 3.747946643233648, 1.0926705278650608], time_from_start=2)            
            rospy.sleep(2) 
            break
        else:
            print("Hay colisión, recalculando...")
            rospy.sleep(1)  # Esperar un poco antes de volver a intentarlo

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## CIERRE DEL GRIPPER

# Abrir completamente el gripper antes de intentar cualquier operación de agarre.
# Es una práctica común asegurarse de que el gripper no esté restringido  o en una posición que podría interferir con el objeto a agarrar.
simulacion_gripper.abrir_gripper()

# Pequeña pausa para asegurar que la acción de abrir se ha completado.
rospy.sleep(1)

# Obtener el tipo de gripper actual para aplicar la configuración de posiciones de articulaciones correcta.
tipo_gripper = simulacion_gripper.get_tipo_gripper()

# Basado en el tipo de gripper, se definen las posiciones específicas de las articulaciones.
# Estas posiciones deben ser determinadas experimentalmente o calculadas para lograr el agarre deseado.
if tipo_gripper == 'jaco': # Posiciones para el gripper Jaco.
  posicion_articulaciones = [-0.6,-0.6,-0.6]  
elif tipo_gripper == 'schunk': # Posiciones para el gripper Schunk.
  posicion_articulaciones = [0, 0, 0, 0, 0, 0, 0]  
elif tipo_gripper == 'robotiq':  # Posiciones para el gripper Robotiq.
  posicion_articulaciones = [0.4, 0.4, 0.4, 0, 0.4, 0.4, 0.4, 0, 0.4, 0.4, 0.4] 

# Aplicar las posiciones definidas a las articulaciones del gripper.
# Este paso es crucial para controlar el estado del gripper y realizar agarres efectivos en la simulación.
simulacion_gripper.set_posicion_articulaciones(posicion_articulaciones)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## MOVIMIENTO ASCENDENTE DEL OBJETO

# Se quiere que el brazo vaya desde su posición actual la siguiente posición. Para ello se crea un `bucle` que se ejecuta hasta que encuentra un `camino libre` de colisiones para llegar 
# al punto deseado. Esto se consigue con un planificador `RRT` que compueba las colisiones a lo largo del path.
#Aqui se realiza un `movimiento ascendente vertical` para intentar superar el obstáculo

# 1. Validación de la posición final: se determina si la posición final a la que se quiere llegar es viable para las articulaciones del brazo y no va a pasar por una zona de singularidad.
# 2. Comprobación de colisiones: se comprueba si en al posición deseada a la que se quiere llegar hay colisiones o no. En caso de que no haya una colisión se ejecuta el planificador que 
# saca un path libre de colisiones. En caso de que existan colisiones el bucle se vuelve a ejecutar hasta encontrar una opción viable.

#`NOTA: para que la simulación sea fluida se ha comentado la parte del algortimo RRT y se ha metido el comando para mover el brazo directamente hasta la posición deseada introduciendo 
# los valores de las posiciones de las articulaciones directamente.`

# Definición de la posición vertical a 0.4 metros del suelo, desplazamiento en el eje Z
pose2_gripper_world = PyKDL.Frame(PyKDL.Rotation.Quaternion(-0.40871888539793455, -0.54439158522276, 0.4496804222436366, 0.5782509770925648), PyKDL.Vector(pose_gripper_world.p.x(), pose_gripper_world.p.y(), pose_gripper_world.p.z() +0.5))
print("Pose2 gripper desplazada verticalmente")
print(pose2_gripper_world)
rospy.sleep(1)
tcp_pose2 = frame_to_pose(pose2_gripper_world)
print("Pose2 gripper_tcp con respecto a world: ")
print( tcp_pose2)
print(pose2_gripper_world)

while True:
    valida, posiciones_articulares_deseadas2 = kin.calcular_ci(posiciones_articulaciones_actuales=ur10.obtener_posiciones_articulaciones()+np.random.rand(6), pose_deseada=tcp_pose2)

    if valida:
        print("Posiciones articulares deseadas2: ", posiciones_articulares_deseadas2)
        hay_colision = detectorColisiones.hay_colision(posiciones_articulares_deseadas2)
        if not hay_colision:
            print("NO hay colision")
            # Configuración del Algoritmo RRT*
            #rrt = manipulacion_lib.RRTStarJointSpace(ur10.obtener_posiciones_articulaciones(), posiciones_articulares_deseadas3, joint_limits, 0.4, 300,1.0, detectorColisiones)
        
            # Planificación de la Trayectoria
            #path = rrt.plan()
            #if path:
              #  print(path)
               # ur10.command_path_posicion_articulaciones(path, 0.4, 1.0)
            
            gazebo_robot.command_posicion_articulaciones([0.5490121111461591, -0.8310527696012312, 0.9297590974127579, -0.5764522745346105, 3.7479140771573447, 1.0926409549340657], time_from_start=2)
            rospy.sleep(2)  
            break
        else:
            print("Hay colisión, recalculando...")
            rospy.sleep(1)  # Esperar un poco antes de volver a intentarlo

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## MOVIMIENTO HORIZONTAL DEL OBJETO

# Se quiere que el brazo vaya desde su posición actual hasta la siguiente posición. Para ello se crea un `bucle` que se ejecuta hasta que encuentra un `camino libre` de colisiones para 
# llegar al punto deseado. Esto se consigue con un planificador `RRT` que compueba las colisiones a lo largo del path.
# Aqui se realiza un `movimiento horizontal` para intentar superar el obstáculo.

# 1. Validación de la posición final: se determina si la posición final a la que se quiere llegar es viable para las articulaciones del brazo y no va a pasar por una zona de singularidad.
# 2. Comprobación de colisiones: se comprueba si en al posición deseada a la que se quiere llegar hay colisiones o no. En caso de que no haya una colisión se ejecuta el planificador que 
# saca un path libre de colisiones. En caso de que existan colisiones el bucle se vuelve a ejecutar hasta encontrar una opción viable.

#`NOTA: para que la simulación sea fluida se ha comentado la parte del algortimo RRT y se ha metido el comando para mover el brazo directamente hasta la posición deseada introduciendo 
# los valores de las posiciones de las articulaciones directamente.`
            
pose3_gripper_world = PyKDL.Frame(PyKDL.Rotation.Quaternion(-0.40871888539793455, -0.54439158522276, 0.4496804222436366, 0.5782509770925648), PyKDL.Vector(pose_gripper_world.p.x(), pose_gripper_world.p.y() - 0.8, pose_gripper_world.p.z() +0.5))
print("Pose3 gripper desplazada horizontalmente")
print(pose3_gripper_world)
rospy.sleep(1)
tcp_pose3 = frame_to_pose(pose3_gripper_world)
print("Pose3 gripper_tcp con respecto a world: ")
print( tcp_pose3)
print(pose3_gripper_world)

while True:
    valida, posiciones_articulares_deseadas3 = kin.calcular_ci(posiciones_articulaciones_actuales=ur10.obtener_posiciones_articulaciones()+np.random.rand(6), pose_deseada=tcp_pose3)
    if valida:
        # Fijar las posiciones articulares deseadas
        print("Posiciones articulares deseadas3: ", posiciones_articulares_deseadas3)

        hay_colision3 = detectorColisiones.hay_colision(posiciones_articulares_deseadas3)
        if not hay_colision3:
            print("NO hay colision")
            # Configuración del Algoritmo RRT*
            #rrt = manipulacion_lib.RRTStarJointSpace(ur10.obtener_posiciones_articulaciones(), posiciones_articulares_deseadas3, joint_limits, 0.4, 300,1.0, detectorColisiones)
        
            # Planificación de la Trayectoria
            #path = rrt.plan()
            #if path:
              #  print(path)
               # ur10.command_path_posicion_articulaciones(path, 0.4, 1.0)
            gazebo_robot.command_posicion_articulaciones([-0.353915212656789, -1.1231828917657756, 1.780361714641838, -3.1303628997555997, 3.5780881650458856, -1.025554158885402], time_from_start=2)
            rospy.sleep(2)  
            break
        else:
            print("Hay colisión, recalculando...")
            rospy.sleep(1)  # Esperar un poco antes de volver a intentarlo

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## MOVIMIENTO DESCENDENTE DIAGONAL DEL OBJETO

# Se quiere que el brazo vaya desde su posición actual hasta la posición fianl. Para ello se crea un `bucle` que se ejecuta hasta que encuentra un `camino libre` de colisiones para 
# llegar al punto deseado. Esto se consigue con un planificador `RRT` que compueba las colisiones a lo largo del path.
# Aqui se realiza un `movimiento descendente  diagonal` para intentar superar el obstáculo

# 1. Validación de la posición final: se determina si la posición final a la que se quiere llegar es viable para las articulaciones del brazo y no va a pasar por una zona de singularidad.
# 2. Comprobación de colisiones: se comprueba si en al posición deseada a la que se quiere llegar hay colisiones o no. En caso de que no haya una colisión se ejecuta el planificador que 
# saca un path libre de colisiones. En caso de que existan colisiones el bucle se vuelve a ejecutar hasta encontrar una opción viable.

# `NOTA: para que la simulación sea fluida se ha comentado la parte del algortimo RRT y se ha metido el comando para mover el brazo directamente hasta la posición deseada introduciendo 
# los valores de las posiciones de las articulaciones directamente.`
            
pose4_gripper_world = PyKDL.Frame(PyKDL.Rotation.Quaternion(-0.40871888539793455, -0.54439158522276, 0.4496804222436366, 0.5782509770925648), PyKDL.Vector(pose_gripper_world.p.x() - 0.3, pose_gripper_world.p.y() - 1.2, pose_gripper_world.p.z()))
print("Pose4 gripper desplazada verticalmente hacia abajo")
print(pose4_gripper_world)
rospy.sleep(1)
tcp_pose4 = frame_to_pose(pose4_gripper_world)
print("Pose4 gripper_tcp con respecto a world: ")
print( tcp_pose4)
print(pose4_gripper_world)

while True:
    valida, posiciones_articulares_deseadas4 = kin.calcular_ci(posiciones_articulaciones_actuales=ur10.obtener_posiciones_articulaciones()+np.random.rand(6), pose_deseada=tcp_pose4)
    if valida:
        # Fijar las posiciones articulares deseadas
        print("Posiciones articulares deseadas4: ", posiciones_articulares_deseadas4)
        hay_colision4 = detectorColisiones.hay_colision(posiciones_articulares_deseadas4)
        if not hay_colision4:
            print("NO hay colision")
            gazebo_robot.command_posicion_articulaciones([-1.0371833062906048, -0.7219553236754773, 1.7890295323189367, -0.7611139171590264, 2.086711201703622, 1.649490948860812], time_from_start=4)
            rospy.sleep(4)  # Esperar un poco antes de volver a intentarlo

            break
           # gazebo_robot.command_posicion_articulaciones([-1.0371833062906048, -0.7219553236754773, 1.7890295323189367, -0.7611139171590264, 2.086711201703622, 1.649490948860812],
                                           #  time_from_start=2)
            # Configuración del Algoritmo RRT*
            #rrt = manipulacion_lib.RRTStarJointSpace(ur10.obtener_posiciones_articulaciones(), posiciones_articulares_deseadas3, joint_limits, 0.4, 300,1.0, detectorColisiones)

            # Planificación de la Trayectoria
            #path = rrt.plan()
            #if path:
                #print(path)
                
                #ur10.command_path_posicion_articulaciones(path, 0.4, 1.0)
        elif hay_colision4:
           print("Hay colisión, recalculando...")
           rospy.sleep(1)  # Esperar un poco antes de volver a intentarlo

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## APERTURA DEL GRIPPER
# Abrir completamente el gripper antes de intentar cualquier operación de agarre.
# Es una práctica común asegurarse de que el gripper no esté restringido o en una posición que podría interferir con el objeto a agarrar.
rospy.sleep(2)
simulacion_gripper.abrir_gripper()

# Pequeña pausa para asegurar que la acción de abrir se ha completado.
rospy.sleep(1)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## MOVIMIENTO A LA POSICION DE POSTAGARRE

# Se quiere que el brazo vaya desde su posición hasta la posición de postagarre. Para ello se crea un `bucle` que se ejecuta hasta que encuentra un `camino libre` de colisiones para 
# llegar al punto deseado. Esto se consigue con un planificador `RRT` que compueba las colisiones a lo largo del path.
# Aqui se realiza un `movimiento ascendente vertical` para intentar superar el obstáculo

# 1. Validación de la posición final: se determina si la posición final a la que se quiere llegar es viable para las articulaciones del brazo y no va a pasar por una zona de singularidad.
# 2. Comprobación de colisiones: se comprueba si en al posición deseada a la que se quiere llegar hay colisiones o no. En caso de que no haya una colisión se ejecuta el planificador 
# que saca un path libre de colisiones. En caso de que existan colisiones el bucle se vuelve a ejecutar hasta encontrar una opción viable.

# `NOTA: para que la simulación sea fluida se ha comentado la parte del algortimo RRT y se ha metido el comando para mover el brazo directamente hasta la posición deseada introduciendo 
# los valores de las posiciones de las articulaciones directamente.`

pose5_gripper_world = PyKDL.Frame(PyKDL.Rotation.Quaternion(-0.40871888539793455, -0.54439158522276, 0.4496804222436366, 0.5782509770925648), PyKDL.Vector(pose_gripper_world.p.x() - 0.3, pose_gripper_world.p.y() - 1.0, pose_gripper_world.p.z()))
print("Pose5 gripper para dejar objeto")
print(pose5_gripper_world)
rospy.sleep(1)
tcp_pose5 = frame_to_pose(pose5_gripper_world)
print("Pose5 gripper_tcp con respecto a world: ")
print( tcp_pose5)
print(pose5_gripper_world)

while True:
    valida, posiciones_articulares_deseadas5 = kin.calcular_ci(posiciones_articulaciones_actuales=ur10.obtener_posiciones_articulaciones()+np.random.rand(6), pose_deseada=tcp_pose5)
    if valida:
        # Fijar las posiciones articulares deseadas
        print("Posiciones articulares deseadas5: ", posiciones_articulares_deseadas5)
        hay_colision5 = detectorColisiones.hay_colision(posiciones_articulares_deseadas5)
        if not hay_colision5:
            print("NO hay colision")
            gazebo_robot.command_posicion_articulaciones([-0.8522252724959221, -0.8096008275325517, 2.050202432361607, -0.8936315139798986, 2.261988060754083, 1.7214475785368721], time_from_start=2)
            rospy.sleep(2)  # Esperar un poco antes de volver a intentarlo

            break
           # gazebo_robot.command_posicion_articulaciones([-1.0371833062906048, -0.7219553236754773, 1.7890295323189367, -0.7611139171590264, 2.086711201703622, 1.649490948860812],
                                           #  time_from_start=2)
            # Configuración del Algoritmo RRT*
            #rrt = manipulacion_lib.RRTStarJointSpace(ur10.obtener_posiciones_articulaciones(), posiciones_articulares_deseadas3, joint_limits, 0.4, 300,1.0, detectorColisiones)

            # Planificación de la Trayectoria
            #path = rrt.plan()
            #if path:
                #print(path)
                
                #ur10.command_path_posicion_articulaciones(path, 0.4, 1.0)
        elif hay_colision5:
           print("Hay colisión, recalculando...")
           rospy.sleep(1)  # Esperar un poco antes de volver a intentarlo