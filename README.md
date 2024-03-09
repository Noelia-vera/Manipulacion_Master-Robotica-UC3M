# MANIPULACIÓN
## _Master de Robótica y Automatización, Universidad Carlos 3 de Madrid_
### PRÁCTICA 1 
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
* **video:** video de demostracion 
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
* **scripts:** archivos .py para ejecutar la práctica
* **urdf**
***
#### FINALIDAD DE LA PRÁCTICA
En esta práctica se prentende coger un objeto con un determinado gripper, pasarlo por encima de un obstáculo y depositarlo sobre el suelo. Para ello se va a usar GRSAPIT! y Gazebo

***
#### SELECCIÓN DEL OBJETO Y GARRA
En este caso, se va a realizar la práctica es un schunk y un construction_cone

#### PASOS PREVIOS:
Se lanza GRASPIT!

```bash
roslaunch graspit_interface graspit_interface.launch
```

Lo primero que se hace es planificar los posibles agarres que existen para coger el objeto. En mi caso existen 10 pisibles agarres. Dentro de estas opciones, se obtiene el dofs, la pose, epsilon_quality y volume_quality. Para estos dos últimos parámetros, lo mejor para un agarre fuerte y estable es coger los valores más altos. Con esto se obtiene un archivo .yalm con las distintas poses.
Al principio seleccioné la pose que presentaba mayor valor de epsilon_quality y volume_quality. Sin embargo, al realizar la comprobación de colisiones, el cubo que rodea la garra colisionaba. De esa forma fui escogiendo las siguientes poses en orden decreciente de los valores epsilon_quality y volume_quality. La pruebas que se realizaron son las siguientes:

* **pose:** (0.13091874575145673, 0.15573131231692333, 0.12734620859499166, 0.285769154875614, 0.10400013105463027, 0.39602433974889534, 0.86642061678422020)
* **pose:** ( 0.12507508031653083, 0.14549317803960687, 0.09618141709293977, 0.31936521271438256, 0.2365114984285554, 0.31126564789996025, 0.8632391722207667)
* **pose:**(0.16812477177687862, 0.09951479719804965, 0.2714068675810464, 0.48756757910535264, -0.07758475734294457, 0.3126084284817816, 0.811501344222875)
* **pose:**(0.18320125978245017, 0.08981563704179489, 0.17899188659282822,  0.4575796090712538, 0.05907773090282281, 0.23821152157432185, 0.8546262306194555)
* **pose:** (0.1293616869390618, 0.15703835296646632, 0.20648472159145423, 0.3453248222827963, 0.13312190540115681, 0.4020669205251057, 0.8374792635266732)
* **pose:**(0.1374528881405734, 0.1189021949427939, 0.12084095474250842, 0.529238682307343. 0.3086495437439036, 0.23447792118444918, 0.7547595516277266)

Finalmente, la pose usada es la que se ve a continuación, ya que fue la primera en no obtener valores de colisiones. Se sigue respetando que epsilon_quality y volume_quality son positivos, asi que el agarre debe ser fuerte y seguro para asegurar la sujección del objeto.

* **pose:** ( -0.0029576076089575204, 0.19114477251526724, 0.19604699051348687, -0.4084609483059216, -0.5445844147386103, 0.44995840188535785, 0.5780353843023863)
* **dofs:**( 0.2580143213213457,-0.5817693566886498, 1.2474314470597565, -0.4986443566886497, 1.3305564470597564, -0.4767693566886497, 1.3524314470597565)
* **volume_quality:** 0.007168593270364019
* **epsilon_quality:** 0.009860706482437448
***

#### INICIO DE LA SIMULACIÓN DE GAZEBO:
 En este momento ya se pasa a la simulación en Gazebo en donde se encuentra el gripper, el objeto y la mesa. Aqui se identifica el tipo de garra y objeto asignado.
 
```bash
roslaunch manipulacion_pkg gripper_gazebo.launch tipo_gripper:=schunk \objeto:=construction_cone
```
En otra terminal se lanza el archivo .py que ejecuta la simulación.

```bash
python3 my_gripper_cone.py
```

***
### COMENTARIOS DEL ARCHOVO python3 my_gripper_cone.py
El proceso que se usa para la simulación es:
1. Se posiciona el gripper a 0.2 metro del objeto con el misma posición y orientación que la pose calculada en la parte previa de GRASPIT!
2. Se coloca el gripper en la pose optima para coger el objeto.
3. Se comprueban las colisiones.
4. Se coge el objeto.
5. El gripper se desplaza a distintos puntos para conseguir llevar el objeto al otro lado del obstáculo.


* **Para realizar esta parte, se han decidido crear 3 puntos en el espacio. Entre ellos se ha generado una función de interpolación con 150 frames (modificable) para que el desplazamiento se vea fluido. Como se quería comprobar la eficacia de agarre, se han planteado 3 tipos de trayectoria, una vertical (movimiento en el eje Z), una horizontal (movimiento en el eje X) y una en diagonal (movimiento en los ejes  X, Z)**

6. Una vez el objeto esta en el suelo, el gripper se abre soltando el objeto.
7. EL gripper se separa a 0.2 metros del objeto.

### RESULTADOS
### [VIDEO DE DEMOSTRACIÓN](https://www.youtube.com/watch?v=36naFUwaNik)

