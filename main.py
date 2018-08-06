import discord
import asyncio
import random
import io
import time
from discord.ext import commands


client = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='discord.gg/aveuuFS'))
    print('-------------------------')
    print('Logged in...')
    print('BOT - online')
    print('Username: ' + str(client.user.name))
    print('Client ID: ' + str(client.user.id))
    print('---------STATUS----------')

@client.event
async def on_member_join(member):
    regras = client.get_channel("390779854469201931")
    msg = "Bem Vindo {} ao nosso servidor\nLeia nossas regras -> {}\nconvide seus amigos\nhttps://discord.gg/aveuuFS".format(member.mention, regras.mention)
    await client.send_message(member, msg)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    for user in message.mentions:
        member = message.mentions[0]
        if message.content.lower().startswith('.ship {} {}'.format(user.mention, member.mention)):
            member = message.mentions[0]
            msg001 = ':sparkling_heart: Hmmm, será que nós temos um novo casal aqui? :sparkling_heart:\n:heart: Os dois foram feitos um para o outro! :blush:\n\n100% [████████████████████] \n{} + {}'.format(
                user.mention, member.mention)
            msg002 = ':heart: Esse casal é quase perfeito :blush:\n:heart_eyes: Só 10% para a perfeição :kissing_closed_eyes:\n\n90% [███████████████████   ] \n{} + {}'.format(
                user.mention, member.mention)
            msg003 = ':grimacing: Só vou falar uma coisa :upside_down: \n:point_right: Eu SHIPO :sweat_smile: \n\n80% [████████████████            ] \n{} + {}'.format(
                user.mention, member.mention)
            msg004 = ':grin: Ja é mais que 50% :laughing: \n:thumbsup: Acho que vocês dois deveriam ir para um motel :thinking: \n\n70% [█████████████                     ] \n{} + {}'.format(
                user.mention, member.mention)
            msg005 = ':blush: Os opostos se atraem :ok_hand: \n:wave: Entre tapas e beijos :kissing_closed_eyes: :heart_eyes: \n\n50% [██████████                              ]  \n{} + {}'.format(
                user.mention, member.mention)
            msg006 = ':thinking: :thinking: É... acho que nao é uma boa ideia :grin:\n :poop: Talvez não seja a melhor posibilidade :tired_face: :grimacing: \n\n20% [████                                                ]   \n{} + {}'.format(
                user.mention, member.mention)
            msg007 = ':speak_no_evil: Não vou nem opinar :speak_no_evil: \n :thumbsup:  :thumbsup: VAI DAR ERRADO ESSE RELACIONAMENTO :thumbsup: \n\n10% [██                                                      ]  \n{} + {}'.format(
                user.mention, member.mention)
            msg008 = ':thumbsdown: PUTA QUE PARIU CARA:gun: \n:upside_down: VOCÊS É IGUAL MANGA COM LEITE :eggplant: (<-- não tinha manga )\n\n5% [█                                                         ]  \n{} + {}'.format(
                user.mention, member.mention)
            msg009 = ':dizzy_face: NEM FODENDO :dizzy_face:\n:dizzy_face: NEM FODENDO :dizzy_face:\n\n[█████NEM FODENDO████]  \n{} + {}'.format(
                user.mention, member.mention)
            msg010 = ':point_right: :ok_hand: ESSE CASAL É SÓ SEXO :point_right: :ok_hand:\n :point_right: :ok_hand: SÓ SEXO :point_right: :ok_hand:\n\n[███SÓ VAI SER SEXO███] \n{} + {}'.format(
                user.mention, member.mention)
            msg011 = ':ok_hand: ANAL TODO DIA :ok_hand:\n:ok_hand: ORAL TODA NOITE :ok_hand:\n\n [█████100% PUTARIA█████] \n{} + {}'.format(
                user.mention, member.mention)
            msg012 = '[                        error                        ] \n[........error.......] \n[                        error                        ]  \n[........error.......] '.format(
                user.mention, member.mention)
            choice = random.randint(1, 11)
            if choice == 1:
                await client.send_message(message.channel, msg001)
            if choice == 2:
                await client.send_message(message.channel, msg002)
            if choice == 3:
                await client.send_message(message.channel, msg003)
            if choice == 4:
                await client.send_message(message.channel, msg004)
            if choice == 5:
                await client.send_message(message.channel, msg005)
            if choice == 6:
                await client.send_message(message.channel, msg006)
            if choice == 7:
                await client.send_message(message.channel, msg007)
            if choice == 8:
                await client.send_message(message.channel, msg008)
            if choice == 9:
                await client.send_message(message.channel, msg009)
            if choice == 10:
                await client.send_message(message.channel, msg010)
            if choice == 11:
                await client.send_message(message.channel, msg011)
            if choice == 12:
                await client.send_message(message.channel, msg012)

    if message.content.startswith('.user'):
        try:
            user = message.mentions[0]
            userentrou = str(user.joined_at).split('.', 1)[0]
            usercriou = str(user.created_at).split('.', 1)[0]

            userembed = discord.Embed(
                title="Username:",
                description=user.name,
                color=0xe67e22
            )
            userembed.set_author(
                name="Informações do usuario"

            )
            userembed.add_field(
                name="Juntou-se ao servidor em:",
                value=userentrou
            )
            userembed.add_field(
                name="Usuário criado em:",
                value=usercriou
            )
            userembed.add_field(
                name="Série:",
                value=user.discriminator
            )
            userembed.add_field(
                name="ID:",
                value=user.id
            )

            await client.send_message(message.channel, embed=userembed)
        except IndexError:
            await client.send_message(message.channel, "Eu não consegui encontrar o usuário.")
        except:
            await client.send_message(message.channel, "Desculpa, ERROR")
        finally:
            pass

    if message.content.lower().startswith('.ping'):
        await client.send_message(message.channel, ":ping_pong: pong!! xD xD")

    if message.content.lower().startswith('.info'):
        embed = discord.Embed(title="", description="", color=0xffffff)
        embed.add_field(name="Sobre", value="Programado PyCharm\nLinguagem python\ndiscord.py\nDesenvolvido em client\nexe = IDLE python 3.6", inline=True)
        embed.add_field(name="Status", value="Bot - online\nUsername: MelByLaw\nClient ID: 392188------\nBot desenvolvido por : Gabriel Lima", inline=True)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/475391478227664896/475728032422690817/Ponto_de_exclamacao_da_RedeTV.svg.png')
        embed.set_author(name='Informações Bot MelByLaw', icon_url='https://cdn.discordapp.com/attachments/475391478227664896/475727223194910720/img.png')
        await client.send_message(message.channel, embed=embed)

    if message.content.lower().startswith('.meusegredo'):
        msg1 = 'Hoje eu bati 1 punhetinha :pray: :pray: '
        msg2 = 'Amanha vou dar o cu 2 vezes kkk :ok_hand::ok_hand:'
        msg3 = 'Queria comer 3 travecos hue hue :scream_cat:'
        msg4 = 'Comi 4 bucetinhas hoje :clap::clap: '
        msg5 = 'Hoje vou fuder com 5 anões :boy::boy::boy::boy::boy:'
        msg6 = 'Ja fiz a posição 69 com um urso peludo :bear::bear:'
        msg7 = 'Ja tranzei 7 vezes nessa semana :bow: :bow: '
        msg8 = 'Sou viado mesmo e falo pra todo mundo :relaxed: :relaxed: '
        msg9 = 'Hoje enfiei o meu telefone no cu 10 vezes :telephone: :telephone: '
        msg10 = 'Gosto do CAPETA... igual o totinha 😈😈'
        msg11 = '... acho que sou mulher :information_desk_person: :information_desk_person: '
        msg12 = 'A Anna Valeri é mulher do Gabriel só pra deixar claro mesmo :joy::joy:'
        msg13 = 'Ja me comeram de 4, mas não fala para ninguem :zipper_mouth::zipper_mouth:'
        msg14 = 'Gosto de fazer oral em homem ... chupar um penis :zipper_mouth: 8===D'
        msg15 = 'Ja comi a mãe da pessoa acima :joy::joy:'
        msg16 = 'Gosto de zoofilia :racehorse::racehorse: '
        msg17 = 'Ja enfiei o chuveirinho no meu cu :shower::shower:  '
        msg18 = 'Minha mãe faz sexo por dinheiro :moneybag: :money_mouth: :money_with_wings: '
        msg19 = 'Ja fui corno na vida :cow: :cow: '
        msg20 = 'Ja comi cabritinha :goat: :goat: '
        msg21 = 'Eu não do o cu na botinha não :boot: :boot: '
        msg22 = 'Meu piru é piquinininho :turkey: '
        msg23 = 'Odeio quando meus amigos me comem :rolling_eyes: '
        msg24 = 'Ninguem sabe que sou gay :spy: :spy: '
        msg25 = 'Meu penis é enorme :snake: :snake: '
        msg26 = 'Sou feito para casar :heartpulse: :hearts: '
        msg27 = 'Me chama no wpp bb :telephone_receiver: '
        choice = random.randint (1,21)
        if choice == 1:
            await client.send_message(message.channel, msg1)
        if choice == 2:
            await client.send_message(message.channel, msg2)
        if choice == 3:
            await client.send_message(message.channel, msg3)
        if choice == 4:
            await client.send_message(message.channel, msg4)
        if choice == 5:
            await client.send_message(message.channel, msg5)
        if choice == 6:
            await client.send_message(message.channel, msg6)
        if choice == 7:
            await client.send_message(message.channel, msg7)
        if choice == 8:
            await client.send_message(message.channel, msg8)
        if choice == 9:
            await client.send_message(message.channel, msg9)
        if choice == 10:
            await client.send_message(message.channel, msg10)
        if choice == 11:
            await client.send_message(message.channel, msg11)
        if choice == 12:
            await client.send_message(message.channel, msg12)
        if choice == 13:
            await client.send_message(message.channel, msg13)
        if choice == 14:
            await client.send_message(message.channel, msg14)
        if choice == 15:
            await client.send_message(message.channel, msg15)
        if choice == 16:
            await client.send_message(message.channel, msg16)
        if choice == 17:
            await client.send_message(message.channel, msg17)
        if choice == 18:
            await client.send_message(message.channel, msg18)
        if choice == 19:
            await client.send_message(message.channel, msg19)
        if choice == 20:
            await client.send_message(message.channel, msg20)
        if choice == 21:
            await client.send_message(message.channel, msg21)
        if choice == 22:
            await client.send_message(message.channel, msg22)
        if choice == 23:
            await client.send_message(message.channel, msg23)
        if choice == 24:
            await client.send_message(message.channel, msg24)
        if choice == 25:
            await client.send_message(message.channel, msg25)
        if choice == 26:
            await client.send_message(message.channel, msg26)
        if choice == 27:
            await client.send_message(message.channel, msg27)

client.run('MzkyODE4MjgyMTQ0NTk1OTc4.DkeUQQ.NGoqk9tzBfh0FPKzx37WwC87Fr8')