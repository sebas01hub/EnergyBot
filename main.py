import random
# import requests
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix="/", intents=intents)

TOKEN = "Mi Token"


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
            "Ejemplo: !consejos lavadora\n\n"
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

bot.run(TOKEN)
