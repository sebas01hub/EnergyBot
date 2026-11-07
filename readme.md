## EnergyBot - Bot de Discord sobre el consumo energético
De qué trata el proyecto?
La idea de este proyecto es crear un bot de Discord utilizando Python que ayude a las personas a entender un poco mejor el consumo energético en sus hogares y edificios.

Quiero que el bot no solamente proporcione información sobre el tema, sino que también pueda ofrecer consejos y herramientas útiles para que las personas aprendan a ahorrar electricidad y a reducir su impacto en el medioambiente.

Todo esto ya que muchas veces utilizamos aparatos eléctricos sin pensar realmente en cuánta energía consumen o en cómo podríamos utilizarlos de una manera más eficiente. Por eso, me gustaría que este bot sirviera como una pequeña ayuda para cambiar algunos de esos hábitos.

## Ideas de comandos para el bot

Estas son algunas de las ideas que tengo pensadas para las funciones que podría tener el bot. Puede que algunas cambien o que termine añadiendo otras conforme avance con el proyecto.

1. /consejos - Consejos para ahorrar energía

Me gustaría añadir un comando que proporcione consejos sobre cómo ahorrar electricidad y reducir el consumo energético en casa.

Por ejemplo:
Apagar las luces cuando no las estemos utilizando.
Desconectar aparatos que no necesitemos.
Aprovechar la luz natural durante el día.
Evitar dejar dispositivos encendidos innecesariamente.
Utilizar los electrodomésticos de una manera más eficiente.

2. /electrodomesticos - Información sobre aparatos eléctricos

Otra idea sería crear un comando que permita elegir entre diferentes aparatos que normalmente utilizamos en casa.

Una vez seleccionado uno, el bot mostraría información sobre cómo funciona, cuánta energía puede llegar a consumir y qué podemos hacer para utilizarlo de una manera más eficiente.

Algunos ejemplos serían:
Aire acondicionado.
Refrigerador.
Lavadora.
Microondas.
Televisor.
Ventiladores.
Bombillas.

Creo que seria interesante porque muchas veces utilizamos estos aparatos sin conocer realmente su consumo o las formas de ahorrar energía al utilizarlos.

3. /temperatura - Cómo lidiar con el calor o el frío sin gastar electricidad

Este comando estaría pensado para ofrecer alternativas que nos ayuden a mantener una temperatura agradable en casa sin tener que depender tanto de aparatos eléctricos.

Para temperaturas altas:
Aprovechar la ventilación natural.
Cerrar las cortinas para evitar que entre demasiado calor.
Abrir las ventanas cuando la temperatura exterior sea más agradable.
Utilizar ropa más ligera.

Para temperaturas bajas:
Aprovechar la luz solar para calentar las habitaciones.
Utilizar cortinas para conservar el calor.
Evitar las corrientes de aire cerrando bien puertas y ventanas.
Utilizar ropa más abrigada.

La intención es mostrar que existen pequeños trucos que podemos aprovechar antes de recurrir a la electricidad.

4. /clima - Consejos dependiendo del clima de tu ubicación

Esta idea me gustaría desarrollarla utilizando una herramienta de consulta del clima que hemos trabajado anteriormente en clase.

El comando permitiría introducir una ubicación y obtener información sobre el clima de ese lugar. A partir de esos datos, el bot podría ofrecer recomendaciones para ahorrar energía dependiendo de la temperatura.

Por ejemplo:
Si hace mucho calor, recomendar cómo utilizar el aire acondicionado sin consumir tanta electricidad.
Si la temperatura es agradable, sugerir aprovechar las ventanas y la ventilación natural.
Si la persona no tiene aire acondicionado, ofrecer otras alternativas para refrescar su hogar.
Si hace frío, recomendar formas de conservar el calor dentro de casa.

5. /consumo - Calculadora de consumo eléctrico

Por último, me gustaría implementar una calculadora que permita conocer aproximadamente cuánta energía consume un aparato electrónico.

Para utilizarla, el usuario tendría que introducir algunos datos:

Nombre del aparato.
Potencia del aparato en vatios (W).
Cantidad de horas que lo utiliza.

Con esos datos, el bot calcularía el consumo energético utilizando esta fórmula:

Consumo (kWh) = (Potencia (W) × Horas de uso) / 1000

Por ejemplo, si tenemos un aparato de 1500 W y lo utilizamos durante 5 horas:

python
consumo = (1500 * 5) / 1000

Resultado: 7.5 kWh

De esta manera, cualquier persona podría hacerse una idea de cuánta electricidad está utilizando y entender mejor qué aparatos pueden estar aumentando su consumo energético.

## Esto es lo utilizado en el proyecto

Python
Discord.py
Visual Studio Code
API meteorológica
JSON: Posiblemente lo utilizaré para guardar algunos datos, como las estadísticas o los puntos de los usuarios.

## Lo que quiero conseguir

El objetivo de EnergyBot es ayudar a las personas a ser más conscientes de su consumo energético, ofreciendo consejos y herramientas para reducir el gasto eléctrico y su impacto en el medioambiente.