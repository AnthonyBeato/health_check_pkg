Health Check para Sistema entre múltiples Raspberry Pi's.

#### Iniciar nodo de escuchar el heartbeat
- ros2 run health_check_pkg heartbeat_listener_node

#### Iniciar nodo de publicación de heartbeat
- ros2 run health_check_pkg diagnostics_publisher_node 

#### Iniciar nodo de publicación de diagnostico
- ros2 run health_check_pkg diagnostics_publisher_node

#### Escuchar diagnostico publicado
- ros2 topic echo diagnostics
