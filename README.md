# MANIPULACIÓN
## _Master de Robótica y Automatización, Universidad Carlos 3 de Madrid_
### PRÁCTICA 2 
</p>

***
#### [ENLACE AL REPOSITORIO GITHUB ](https://github.com/Noelia-vera/Manipulacion_Master-Robotica-UC3M)

</p>


***
#### ORGANIZACIÓN DE CARPETAS:
* **build** 
* **devel**  
* **logs**  
* **src:** archivos de ejecucion  
* **video:** videos de demostracion 
***

#### ORGANIZACIÓN DE SRC:
* **gazebo_pkgs** 
* **graspit_commander**  
* **graspit_interface**  
* **manipulacion_pkg:** archivos de la práctica  

***
#### ORGANIZACIÓN DE MANIPULACION_PKG:
* **config** 
* **graspit_grippers:**  tres tipos de grippers
* **images**  
* **launch:** archivos de manzamiento del entorno  
* **objets_models:** diferentes modelos de obtetos a manipular  
* **rviz:** archivos de manzamiento del entorno  
* **scripts:** archivos .py y .ipynb para ejecutar la práctica
* **urdf**
***
#### FINALIDAD DE LA PRÁCTICA
En esta práctica se pretende coger un determinado objeto con un gripper concreto, pasarlo por encima de un obstáculo y posicionarlo en el suelo. Esto se hace con un grazo robótico UR10 y en el trayecto no debe haber colisión con los obstáculos ni con el propio brazo. 

Para conseguir esto se identifican los obstáculos, se define el punto inicial de agarre del gripper y el punto final, y el **algoritmo RRT hace la planificación de una trayectoria libre de obstáculos** que vaya de un punto a otro. No siempre es la misma porque existen varias posibilidades. Es decir, **el planificador hace el trabajo por nosotros** y por lo tanto **no es necesario definir posiciones intermedias de paso.**

Sin embargo, **para que el video se vea fluido**, se han puesto posiciones intermedias a las que debe ir llegando el brazo para realizar el path completo, sin hacer movimientos extraños con el brazo.
A continuación se muestran los pasos que se han seguido

***
#### SELECCIÓN DEL OBJETO Y GARRA
En este caso, se va a realizar la práctica es un schunk y un construction_cone.

#### PASOS PREVIOS:
Se lanza GAZEBO

```bash
roslaunch manipulacion_pkg  robot_gazebo.launch tipo_gripper:=jaco \ objeto:=mustard_bottle
```
Es necesario tener las posiciones de agarre del objeto, información sacada de la práctica anterior. El punto de agarra no ha cambiado aqui

La pose usada es la que se ve a continuación, ya que fue la primera en no obtener valores de colisiones. Se sigue respetando que epsilon_quality y volume_quality son positivos, asi que el agarre debe ser fuerte y seguro para asegurar la sujección del objeto.

* **pose:** ( -0.0029576076089575204, 0.19114477251526724, 0.19604699051348687, -0.4084609483059216, -0.5445844147386103, 0.44995840188535785, 0.5780353843023863)
* **dofs:**( 0.2580143213213457,-0.5817693566886498, 1.2474314470597565, -0.4986443566886497, 1.3305564470597564, -0.4767693566886497, 1.3524314470597565)
* **volume_quality:** 0.007168593270364019
* **epsilon_quality:** 0.009860706482437448
***


***
### COMENTARIOS PARA PROBAR LA SIMULACIÓN
Se puede ejecutar tanto el notebook jupiter **practica_2.ipynb** como el archivo **robot_cone_arm.py**

El proceso que se usa para la simulación es:
1. Se posiciona el gripper a una posición inicial cómoda para la configuración de las articulaciones del brazo, no hace falta preagarre.
2. Se coloca el gripper en la pose optima para coger el objeto.
3. Se comprueban las colisiones.
4. Se coge el objeto.
5. El gripper se desplaza a distintos puntos para conseguir llevar el objeto al otro lado del obstáculo.


* **Para realizar esta parte, se han decidido crear 2 puntos en el espacio, de modo que el brazo sube de manera vertical por encima dle obstáculo, y luego de manera horizontal, posicionando el objeto con un movimiento diagonal descendente en el suelo.** *

6. Una vez el objeto esta en el suelo, el gripper se abre soltando el objeto.
7. El gripper se separa a 0.2 metros del objeto.

### COMENTARIOS IMPORTANTES

En esta práctica se una un algoritmo llamado **RRT** que permite **planificar trayectorias** de un punto a otro del espacio evitando las colisiones. Por lo tanto, solo es necesario indicar el punto inicial y final, e identificar el obstáculo. El resto lo hace el planificador.
Sin embargo, **para que el video se vea fluido**, se han puesto posiciones intermedias a las que debe ir llegando el brazo para realizar el path completo, sin hacer movimientos extraños con el brazo.

### RESULTADOS
### [VIDEO DE DEMOSTRACIÓN](https://youtu.be/09xbjR7l4c0)

