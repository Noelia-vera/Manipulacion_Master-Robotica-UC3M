#!/usr/bin/env python3
# NOELIA FERNANDEZ TALAVERA
# MANIPULACIÓN
# MASTER DE ROBOTICA Y AUTOMATIZACIÓN
# ENTREGA 1 DE MANIPULACIÓN
#---------------------------------------------------------------------------------------------------------------------
#En esta práctica se pretende coger un objeto con un gripper, pasarlo por encima de un obstáculo y depositarlo en el suelo
#Para ello, se ha usado GRASPIT! para calcular las mejores posiciones de agarre, guardadas en un .yaml
#Ahora se programa la forma en que el gripper se acerca al objeto, lo coge y lo deposita en otra posición salvando un obstáculo.

import manipulacion_lib # Importa la biblioteca para manipulación de objetos y 
                        # grippers en simulación
import rospy # Importa rospy, necesario para la comunicación con el sistema ROS
import PyKDL # Importa PyKDL para las transformaciones entre sistemas 
             # de referencia

# Inicializar el nodo de ROS si aún no se ha inicializado
if not rospy.get_node_uri():
    rospy.init_node('gripper_flotante_gazebo', anonymous=True, 
                    log_level=rospy.WARN)

# Creación de una instancia para controlar un gripper flotante en Gazebo
simulacion_gripper_flotante = manipulacion_lib.SimulacionGripperFlotante(
                                nombre_gripper_gazebo="gripper")
# Esta instancia permite interactuar con un gripper en la simulación de Gazebo,
# especificando su nombre
# Independientemente del gripper asignado para la práctica, se utiliza el 
# nombre "gripper" para referenciarlo en la simulación de Gazebo.


# Obtener la pose (posición y orientación) de un objeto específico en el Gazebo
# Se obtiene la pose del objeto 'mustard_bottle' con respecto al sistema de 
# referencia global (world)
pose_objeto_world = simulacion_gripper_flotante.obtener_pose_objeto(
                    nombre_objeto_gazebo='construction_cone')

print("Pose objeto con respecto a world")
print(pose_objeto_world)

# Fijamos una pose relativa del gripper con respecto al objeto
# Pose del gripper con respecto al objeto, especificando una
# traslación de 0.2m en X y 0.1m en Z
pose_gripper_objeto = PyKDL.Frame(PyKDL.Rotation.Quaternion(0.13091874575145673, 0.15573131231692333, 0.12734620859499166, 0.285769154875614), 
                                  PyKDL.Vector(0.10400013105463027, 0.39602433974889534, 0.8664206167842202))

print("Pose gripper con respecto a objeto")
print(pose_gripper_objeto)

# Calcular la pose del gripper en el sistema de referencia global a partir 
# de su pose relativa al objeto
# Se realiza una transformación de coordenadas para obtener la pose del 
# gripper en el sistema global
pose_gripper_world = pose_objeto_world * pose_gripper_objeto
print("Pose gripper con respecto a world: ")
print( pose_gripper_world)
# Fijar la pose del gripper en la simulación de Gazebo
simulacion_gripper_flotante.fijar_pose_gripper(
                    pose_gripper_world=pose_gripper_world)
# Actualiza la posición y orientación del gripper en Gazebo según la pose calculada


#DETECCIÓN DE COLISIONES
from manipulacion_lib import Obstaculo, DetectorColisionesGripperFlotante
obstaculo_rojo = Obstaculo('cubo', [0.75,0,0,1,0,0,0], [0.3,1,0.6], 'obstaculo')
suelo = Obstaculo('cubo', [0,0,0,1,0,0,0], [4,4,0.1], 'suelo')
obstaculos = [obstaculo_rojo, suelo]

detector_colisiones = DetectorColisionesGripperFlotante('robotiq', obstaculos)

# Obtener la matriz de rotación del frame
rotation = pose_gripper_world.M

# Convertir la matriz de rotación a cuaternión
qx, qy, qz, qw = rotation.GetQuaternion()
pose_gripper = [pose_gripper_world.p.x(), pose_gripper_world.p.y(),
                pose_gripper_world.p.z(),
                qx, qy, qz, qw]
print("Colisiona en la pose actual:", detector_colisiones.hay_colision(pose_gripper))

#COGER EL OBJETO
# Configurar el gripper basado en el archivo YAML específico para su tipo.
# Esto incluye cargar las configuraciones iniciales como nombres de articulaciones y posiciones predeterminadas.
simulacion_gripper_flotante.configurar_gripper()

# Abrir completamente el gripper antes de intentar cualquier operación de agarre.
# Es una práctica común asegurarse de que el gripper no esté restringido o en una posición que podría interferir con el objeto a agarrar.
simulacion_gripper_flotante.abrir_gripper()

# Pequeña pausa para asegurar que la acción de abrir se ha completado.
rospy.sleep(1)

# Obtener el tipo de gripper actual para aplicar la configuración de posiciones de articulaciones correcta.
tipo_gripper = simulacion_gripper_flotante.get_tipo_gripper()

# Basado en el tipo de gripper, se definen las posiciones específicas de las articulaciones.
# Estas posiciones deben ser determinadas experimentalmente o calculadas para lograr el agarre deseado.
# Se van a incluir los valores dofs calculados en la primera parte de esta practica donde los valores de 
# epsilon_quality= 0.0765408310704458 y  volume_quality= 0.0184058161009409 son los mayores, proporcionando el mejor agarre.
# dofs: (0.8960347466344013, -0.49437156869790566, 0.6086936514224696, -0.3081215686979055, 0.7949436514224697, -0.47062156869790567, 0.6324436514224696)
# pose: (0.13091874575145673, 0.15573131231692333, 0.12734620859499166, 0.285769154875614, 0.10400013105463027, 0.39602433974889534, 0.8664206167842202)
if tipo_gripper == 'jaco':
  posicion_articulaciones = [-0.6,-0.6,-0.6]  # Posiciones para el gripper Jaco.
elif tipo_gripper == 'schunk':
  # posicion_articulaciones = [0, 0, 0, 0, 0, 0, 0]  # Posiciones para el gripper Schunk.
  posicion_articulaciones = [0.8960347466344013, -0.49437156869790566, 0.6086936514224696, -0.3081215686979055, 0.7949436514224697, -0.47062156869790567, 0.6324436514224696]  # Posiciones para el gripper Schunk.
elif tipo_gripper == 'robotiq':
  posicion_articulaciones = [0.4, 0.4, 0.4, 0, 0.4, 0.4, 0.4, 0, 0.4, 0.4, 0.4]  # Posiciones para el gripper Robotiq.

# Aplicar las posiciones definidas a las articulaciones del gripper.
# Este paso es crucial para controlar el estado del gripper y realizar agarres efectivos en la simulación.
simulacion_gripper_flotante.set_posicion_articulaciones(posicion_articulaciones)