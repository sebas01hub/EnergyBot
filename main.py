import random
import requests
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix="/", intents=intents)

TOKEN = "Insertar token"


# Inicio del bot
@bot.event
async def on_ready():
    print(f'Se ha conectado el bot como: {bot.user}')


@bot.command()
async def consejos(ctx):
    consejos = [
        "Apaga las luces cuando no estés utilizando una habitación.",
        "Desconecta los aparatos que no estés utilizando.",
        "Aprovecha la luz natural durante el día.",
        "Apaga la televisión y otros dispositivos cuando no los necesites.",
        "Utiliza la lavadora y el lavavajillas con cargas completas.",
        "Regula la temperatura del aire acondicionado para ahorrar energia.",
        "Utiliza bombillas LED para reducir el consumo energético.",
        "Reduce el tiempo de uso de agua caliente.",
        "Evita dejar los cargadores conectados cuando no los utilices.",
        "Recuerda que ahorrar energía también ayuda a cuidar el planeta."
    ]

    consejo = random.choice(consejos)

    await ctx.send(
        f"**Consejo para ahorrar energía:**\n\n{consejo}"
    )

electrodomesticos = {
    "aire acondicionado": {
        "funcionamiento": (
            "Extrae el calor del interior y lo expulsa "
            "al exterior."
        ),
        "consumo": "Entre 900 y 2.500 W.",
        "ahorro": (
            "Mantener la temperatura entre 24 y 26 °C, "
            "limpiar los filtros y cerrar puertas y ventanas."
        )
    },
    "refrigerador": {
        "funcionamiento": (
            "Mantiene los alimentos fríos mediante "
            "un sistema de refrigeración."
        ),
        "consumo": (
            "Entre 100 y 400 W mientras funciona "
            "el compresor."
        ),
        "ahorro": (
            "Evitar abrir la puerta constantemente "
            "y no introducir alimentos calientes."
        )
    },
    "lavadora": {
        "funcionamiento": (
            "Utiliza agua, detergente y un motor "
            "para lavar la ropa."
        ),
        "consumo": "Entre 400 y 2.000 W.",
        "ahorro": (
            "Lavar con cargas completas, utilizar "
            "programas ECO y preferir ciclos con agua fría."
        )
    },
    "microondas": {
        "funcionamiento": (
            "Calienta los alimentos mediante "
            "ondas electromagnéticas."
        ),
        "consumo": "Entre 700 y 1.500 W.",
        "ahorro": (
            "Utilizar recipientes adecuados y calentar "
            "únicamente la cantidad necesaria."
        )
    },
    "televisor": {
        "funcionamiento": (
            "Transforma la energía eléctrica en "
            "imágenes y sonido."
        ),
        "consumo": "Entre 30 y 200 W.",
        "ahorro": (
            "Reducir el brillo y apagarlo "
            "cuando no se utilice."
        )
    },
    "ventiladores": {
        "funcionamiento": (
            "Utilizan un motor eléctrico para mover "
            "el aire mediante sus aspas."
        ),
        "consumo": "Entre 20 y 100 W.",
        "ahorro": (
            "Utilizar velocidades bajas y apagarlos "
            "cuando no sean necesarios."
        )
    },
    "bombillas": {
        "funcionamiento": (
            "Transforman la energía eléctrica en luz."
        ),
        "consumo": (
            "Una bombilla LED consume entre 5 y 15 W."
        ),
        "ahorro": (
            "Utilizar bombillas LED y aprovechar "
            "la luz natural."
        )
    }
}


@bot.command()
async def electrodomestico(ctx, *, aparato=None):

    if aparato is None:
        return await ctx.send(
            "Escribe el nombre de un electrodoméstico.\n\n"
            "Ejemplo: /electrodomestico lavadora\n\n"
            "Disponibles:\n" +
            "\n".join(f"- {nombre.title()}" for nombre in electrodomesticos)
        )

    aparato = aparato.lower().strip()

    if aparato not in electrodomesticos:
        return await ctx.send("Ese electrodoméstico no está disponible.")

    datos = electrodomesticos[aparato]

    await ctx.send(
        f"**{aparato.title()}**\n\n"
        f"**Funcionamiento:**\n{datos['funcionamiento']}\n\n"
        f"**Consumo energético:**\n{datos['consumo']}\n\n"
        f"**Consejos para ahorrar energía:**\n{datos['ahorro']}"
    )


@bot.command()
async def temperatura(ctx, *, clima=None):

    if clima is None:
        return await ctx.send(
            "Escribe el tipo de clima para recibir una recomendación.\n\n"
            "Ejemplos:\n"
            "`/temperatura calor`\n"
            "`/temperatura frio`"
        )

    clima = clima.lower().strip()

    if clima == "calor":

        recomendaciones = [
            "Aprovecha la ventilación natural para refrescar tu hogar.",
            "Cierra las cortinas para evitar que entre demasiado calor.",
            "Abre las ventanas cuando afuera haga menos calor.",
            "Utiliza ropa más ligera y fresca para mantenerte cómodo."
        ]

        recomendacion = random.choice(recomendaciones)

        await ctx.send(
            f"**Recomendación para combatir el calor:**\n\n{recomendacion}"
        )

    elif clima == "frio" or clima == "frío":

        recomendaciones = [
            "Aprovecha la luz solar para calentar las habitaciones.",
            "Utiliza cortinas para conservar el calor dentro de casa.",
            "Evita las corrientes de aire cerrando bien puertas y ventanas.",
            "Utiliza ropa más abrigada para mantener tu cuerpo caliente."
        ]

        recomendacion = random.choice(recomendaciones)

        await ctx.send(
            f"**Recomendación para combatir el frío:**\n\n{recomendacion}"
        )

    else:
        await ctx.send(
            "Tipo de clima no válido. Escribe `calor` o `frio`."
        )


def get_clima(ciudad):
    url = f"https://wttr.in/{ciudad}?format=3"
    resp = requests.get(url)

    if resp.status_code == 200:
        return resp.text.strip()

    return None


@bot.command()
async def clima(ctx, *, ciudad=None):

    if ciudad is None:
        return await ctx.send(
            "Escribe una ciudad para consultar el clima.\n\n"
            "Ejemplo: `/clima Madrid`"
        )

    clima_actual = get_clima(ciudad)

    if clima_actual is None:
        return await ctx.send(
            f"No se pudo obtener el clima de {ciudad}."
        )

    if ":" in clima_actual:
        clima_actual = clima_actual.split(":", 1)[1].strip()

    if "sunny" in clima_actual.lower() or "hot" in clima_actual.lower():
        recomendaciones = [
            "Utiliza el aire acondicionado entre 24 y 26 °C para "
            "ahorrar electricidad.",

            "Cierra las cortinas para evitar que entre demasiado calor.",

            "Si no tienes aire acondicionado, aprovecha la "
            "ventilación natural.",

            "Mantén las puertas y ventanas cerradas mientras utilizas el aire "
            "acondicionado."
        ]

    elif "cold" in clima_actual.lower() or "snow" in clima_actual.lower():
        recomendaciones = [
            "Aprovecha la luz solar para calentar las habitaciones.",
            "Cierra las cortinas para conservar el calor.",
            "Evita las corrientes de aire cerrando puertas y ventanas.",
            "Utiliza ropa más abrigada para mantenerte caliente."
        ]

    else:
        recomendaciones = [
            "Aprovecha las ventanas abiertas para ventilar tu hogar.",

            "Utiliza la ventilación natural para mantener una temperatura "
            "agradable.",

            "Apaga el aire acondicionado si no es necesario.",

            "Aprovecha la temperatura exterior para ahorrar electricidad."
        ]

    recomendacion = random.choice(recomendaciones)

    await ctx.send(
        f"**Clima en {ciudad.title()}:**\n\n"
        f"{clima_actual}\n\n"
        f"**Recomendación para ahorrar energía:**\n"
        f"{recomendacion}"
    )


@bot.command()
async def consumo(ctx, aparato=None, potencia=None, horas=None):

    if aparato is None or potencia is None or horas is None:
        return await ctx.send(
            "Introduce el nombre del aparato, su potencia "
            "en vatios y las horas de uso.\n\n"
            "Ejemplo: /consumo microondas 1500 5"
        )

    try:
        potencia = float(potencia)
        horas = float(horas)

    except ValueError:
        return await ctx.send(
            "La potencia y las horas deben ser numeros para poder calcularlos."
        )

    if potencia <= 0 or horas <= 0:
        return await ctx.send(
            "La potencia y las horas deben ser mayores que cero."
        )

    consumo = (potencia * horas) / 1000

    await ctx.send(
        f"**Consumo eléctrico de {aparato.title()}**\n\n"
        f"**Potencia:** {potencia:g} W\n"
        f"**Horas de uso:** {horas:g}\n\n"
        f"**Consumo energético:** {consumo:.2f} kWh"
    )

bot.run(TOKEN)
