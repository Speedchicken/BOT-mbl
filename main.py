import discord
import asyncio
import random


client = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='digite .ajuda'))
    print('-------------------------')
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

    if message.content.lower().startswith('.bomba'):
        await client.send_message(message.channel, '5')
        await client.send_message(message.channel, '4')
        await client.send_message(message.channel, '3')
        await client.send_message(message.channel, '2')
        msg000 = await client.send_message(message.channel, "1")
        await client.add_reaction(message=msg000, emoji="💣")
        embed = discord.Embed(title="", description="", color=0xffffff)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/475391478227664896/476897684788215820/boom.png')
        await client.send_message(message.channel, embed=embed)

    if message.content.lower().startswith('.bomdia'):
        choice = random.randint(1, 10)
        if choice == 1:
            embed = discord.Embed(title="", description='', color=0xffffff)
            embed.set_image(url='https://cdn.discordapp.com/attachments/475391478227664896/476892247304962058/3.jpg')
            await client.send_message(message.channel, embed=embed)
        if choice == 2:
            embed = discord.Embed(title="", description='', color=0xffffff)
            embed.set_image(url='https://cdn.discordapp.com/attachments/475391478227664896/476892249544982528/4.jpg')
            await client.send_message(message.channel, embed=embed)
        if choice == 3:
            embed = discord.Embed(title="", description='', color=0xffffff)
            embed.set_image(url='https://cdn.discordapp.com/attachments/475391478227664896/476892248252874772/5.jpg')
            await client.send_message(message.channel, embed=embed)
        if choice == 4:
            embed = discord.Embed(title="", description='', color=0xffffff)
            embed.set_image(url='https://cdn.discordapp.com/attachments/475391478227664896/476892257232879616/1.jpg')
            await client.send_message(message.channel, embed=embed)
        if choice == 5:
            embed = discord.Embed(title="", description='', color=0xffffff)
            embed.set_image(url='https://cdn.discordapp.com/attachments/475391478227664896/476892260655693824/2.jpg')
            await client.send_message(message.channel, embed=embed)
        if choice == 6:
            embed = discord.Embed(title="", description='', color=0xffffff)
            embed.set_image(url='https://cdn.discordapp.com/attachments/475391478227664896/476893153765359646/6.jpg')
            await client.send_message(message.channel, embed=embed)
        if choice == 7:
            embed = discord.Embed(title="", description='', color=0xffffff)
            embed.set_image(url='https://cdn.discordapp.com/attachments/475391478227664896/476893178767736832/8.jpg')
            await client.send_message(message.channel, embed=embed)
        if choice == 8:
            embed = discord.Embed(title="", description='', color=0xffffff)
            embed.set_image(url='https://cdn.discordapp.com/attachments/475391478227664896/476893184476053512/9.jpg')
            await client.send_message(message.channel, embed=embed)


    if message.content.lower().startswith('.sorteio1a4'):
        choice = random.randint(1, 4)
        if choice == 1:
            embed = discord.Embed(title="", description='', color=0xffffff)
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/475391478227664896/476503504895082498/1.png')
            await client.send_message(message.channel, embed=embed)
        if choice == 2:
            embed = discord.Embed(title="", description='', color=0xffffff)
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/475391478227664896/476503503175548929/2.png')
            await client.send_message(message.channel, embed=embed)
        if choice == 3:
            embed = discord.Embed(title="", description='', color=0xffffff)
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/475391478227664896/476503866414727178/3.png')
            await client.send_message(message.channel, embed=embed)
        if choice == 4:
            embed = discord.Embed(title="", description='', color=0xffffff)
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/475391478227664896/476506465293565985/4.png')
            await client.send_message(message.channel, embed=embed)

    if message.content.lower().startswith('.sorteio1a3'):
        choice = random.randint(1, 3)
        if choice == 1:
            embed = discord.Embed(title="", description='', color=0xffffff)
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/475391478227664896/476503504895082498/1.png')
            await client.send_message(message.channel, embed=embed)
        if choice == 2:
            embed = discord.Embed(title="", description='', color=0xffffff)
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/475391478227664896/476503503175548929/2.png')
            await client.send_message(message.channel, embed=embed)
        if choice == 3:
            embed = discord.Embed(title="", description='', color=0xffffff)
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/475391478227664896/476503866414727178/3.png')
            await client.send_message(message.channel, embed=embed)

    if message.content.lower().startswith('.sorteio1a2'):
        choice = random.randint(1, 2)
        if choice == 1:
            embed = discord.Embed(title="", description='', color=0xffffff)
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/475391478227664896/476503504895082498/1.png')
            await client.send_message(message.channel, embed=embed)
        if choice == 2:
            embed = discord.Embed(title="", description='', color=0xffffff)
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/475391478227664896/476503503175548929/2.png')
            await client.send_message(message.channel, embed=embed)

    if message.content.lower().startswith('.totinha'):
        choice = random.randint(1, 14)
        if choice == 1:
            embed = discord.Embed(title='', description='', color=0xffffff)
            embed.add_field(name='O totinha é ...', value='O rei soberano de todos os reinos das trevas \n com suas enormes asas demoniacas voa por ai ...', inline=False)
            embed.set_image(url='https://cdn.discordapp.com/attachments/475391478227664896/480176013792247818/o-mundo-das-trevas-logo.png')
            embed.set_footer(text='reality show das trevas')
            await client.send_message(message.channel, embed=embed)
        if choice == 2:
            embed = discord.Embed(title='', description='', color=0xffffff)
            embed.add_field(name='O totinha é ...', value='O Lorde das TREVAS \n o grande pregador do satanismo', inline=False)
            embed.set_image(url='https://cdn.discordapp.com/attachments/475391478227664896/480176013792247818/o-mundo-das-trevas-logo.png')
            embed.set_footer(text='reality show das trevas')
            await client.send_message(message.channel, embed=embed)
        if choice == 3:
            embed = discord.Embed(title='', description='', color=0xffffff)
            embed.add_field(name='O totinha gosta ...', value='De louvar o capeta \n e abraçar santos', inline=False)
            embed.set_image(url='https://cdn.discordapp.com/attachments/475391478227664896/480176013792247818/o-mundo-das-trevas-logo.png')
            embed.set_footer(text='reality show das trevas')
            await client.send_message(message.channel, embed=embed)
        if choice == 4:
            embed = discord.Embed(title='', description='', color=0xffffff)
            embed.add_field(name='O totinha é ...', value='Um demonio disfarçado de ser humano com uma missão em nosso planeta \n SALVE O LORDE DAS TREVAS', inline=False)
            embed.set_image(url='https://cdn.discordapp.com/attachments/475391478227664896/480176013792247818/o-mundo-das-trevas-logo.png')
            embed.set_footer(text='reality show das trevas')
            await client.send_message(message.channel, embed=embed)
        if choice == 5:
            embed = discord.Embed(title='', description='', color=0xffffff)
            embed.add_field(name='O totinha é ...', value='É ruim em todos os jogos eletronicos existentes no planeta Terra\n ou seja lixinho', inline=False)
            embed.set_image(url='https://cdn.discordapp.com/attachments/475391478227664896/480176013792247818/o-mundo-das-trevas-logo.png')
            embed.set_footer(text='reality show das trevas')
            await client.send_message(message.channel, embed=embed)
        if choice == 6:
            embed = discord.Embed(title='', description='', color=0xffffff)
            embed.add_field(name='O totinha gosta ...', value='O nosso Lorde das Trevas tem uma grande CRUSH, Mirelle \n mas ele a chama de Majestade das Trevas ', inline=False)
            embed.set_image(url='https://cdn.discordapp.com/attachments/475391478227664896/480176013792247818/o-mundo-das-trevas-logo.png')
            embed.set_footer(text='reality show das trevas')
            await client.send_message(message.channel, embed=embed)
        if choice == 7:
            embed = discord.Embed(title='', description='', color=0xffffff)
            embed.add_field(name='O totinha é ...', value='Apenas um garoto que sofre por um amor não correspondido\n MIRELLE não o nota', inline=False)
            embed.set_image(url='https://cdn.discordapp.com/attachments/475391478227664896/480176013792247818/o-mundo-das-trevas-logo.png')
            embed.set_footer(text='reality show das trevas')
            await client.send_message(message.channel, embed=embed)
        if choice == 8:
            embed = discord.Embed(title='', description='', color=0xffffff)
            embed.add_field(name='O totinha é ...', value='Um jovem aprendiz de feitiçaria nordica\n onde invoca capetas e demonios da 20ª camada da DEEP WEB', inline=False)
            embed.set_image(url='https://cdn.discordapp.com/attachments/475391478227664896/480176013792247818/o-mundo-das-trevas-logo.png')
            embed.set_footer(text='reality show das trevas')
            await client.send_message(message.channel, embed=embed)
        if choice == 9:
            embed = discord.Embed(title='', description='', color=0xffffff)
            embed.add_field(name='O totinha é ...', value='Um grande player carregado por seus colegas do discord \n ele passa 24h em um PC para ser ruim em todo jogo mb', inline=False)
            embed.set_image(url='https://cdn.discordapp.com/attachments/475391478227664896/480176013792247818/o-mundo-das-trevas-logo.png')
            embed.set_footer(text='reality show das trevas')
            await client.send_message(message.channel, embed=embed)
        if choice == 10:
            embed = discord.Embed(title='', description='', color=0xffffff)
            embed.add_field(name='MEU NOME NAO É TOTINHA ...', value='MEU NOME É LORDE DAS TREVAS\n COM TODO RESPEITO... AJOELHEM-SE PERANTE A MIM', inline=False)
            embed.set_image(url='https://cdn.discordapp.com/attachments/475391478227664896/480176013792247818/o-mundo-das-trevas-logo.png')
            embed.set_footer(text='reality show das trevas')
            await client.send_message(message.channel, embed=embed)
        if choice == 11:
            embed = discord.Embed(title='', description='', color=0xffffff)
            embed.add_field(name='Curiosidades do totinha ...', value='O totinha tira leite de vaca e em seguida assisti hentai\n ele tambem gosta de porno do Bob Esponja ', inline=False)
            embed.set_image(url='https://cdn.discordapp.com/attachments/475391478227664896/480176013792247818/o-mundo-das-trevas-logo.png')
            embed.set_footer(text='reality show das trevas')
            await client.send_message(message.channel, embed=embed)
        if choice == 12:
            embed = discord.Embed(title='', description='', color=0xffffff)
            embed.add_field(name='Curiosidades do totinha ...', value='Ele é um escravoceta da Mirelle \n e ele tambem tem um colar com M de Mirelle ', inline=False)
            embed.set_image(url='https://cdn.discordapp.com/attachments/475391478227664896/480176013792247818/o-mundo-das-trevas-logo.png')
            embed.set_footer(text='reality show das trevas')
            await client.send_message(message.channel, embed=embed)
        if choice == 13:
            embed = discord.Embed(title='', description='', color=0xffffff)
            embed.add_field(name='Curiosidades do totinha ...', value='Ele tem um colar com um M de Mirelle  \n ou pode ser de MARIA MÃE DE JESUS ... AMEM IRMÃOS ', inline=False)
            embed.set_image(url='https://cdn.discordapp.com/attachments/475391478227664896/480176013792247818/o-mundo-das-trevas-logo.png')
            embed.set_footer(text='reality show das trevas')
            await client.send_message(message.channel, embed=embed)
        if choice == 14:
            embed = discord.Embed(title='', description='', color=0xffffff)
            embed.add_field(name='Curiosidades do totinha ...', value='O Lorde das Trevas tem um irmão gemêo que ninguem sabe ...\n mas agora vou revelar para todos', inline=False)
            embed.set_image(url='https://cdn.discordapp.com/attachments/475391478227664896/480192688465903636/irmaos.png')
            embed.set_footer(text='reality show das trevas')
            await client.send_message(message.channel, embed=embed)

    if message.content.lower().startswith('.moeda'):
        choice = random.randint(1, 2)
        if choice == 1:
            embed = discord.Embed(title="Coroa", description="", color=0xffffff)
            embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/412586257114464259.png?v=1')
            await client.send_message(message.channel, embed=embed)
        if choice == 2:
            embed = discord.Embed(title="Cara", description="", color=0xffffff)
            embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/412586256409559041.png?v=1')
            await client.send_message(message.channel, embed=embed)

    if message.content.lower().startswith('.status'):
        embed = discord.Embed(title="", description="", color=0xffffff)
        embed.set_author(name='Informações - discord ----------------------https://discord.gg/aveuuFS', icon_url='https://cdn.discordapp.com/attachments/475391478227664896/475727223194910720/img.png')
        embed.add_field(name='Status', value='**Hospedado** - ```https://www.heroku.com```\n**BOT** - ```online```\n**Username** - ```MelByLaw```\n**Client ID** - ```39281828************************```\n', inline=False)
        embed.set_footer(text='bot em execução')
        await client.send_message(message.channel, embed=embed)

    if message.content.lower().startswith('.pornhelp'):
        embed = discord.Embed(title="", description="", color=0xffffff)
        embed.set_author(name='Informaçoes', icon_url='https://cdn.discordapp.com/attachments/475391478227664896/475727223194910720/img.png')
        embed.add_field(name='Comandos', value='.pornhelp\n\n.porn hentai\n\n.porn analzin\n\n', inline=False)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/475391478227664896/476487848871198720/18.png')
        embed.set_image(url='https://cdn.discordapp.com/attachments/475391478227664896/476488703431409681/show.png')
        embed.set_footer(text='ta batendo uma neh... vou conta pra mãe')
        await client.send_message(message.channel, embed=embed)

    if message.content.lower().startswith('.porn hentai'):
        choice = random.randint (1, 10)
        if choice == 1:
            embed = discord.Embed(title="punhetero - DEUS TA VENDO", description="", color=0xffffff)
            embed.set_image(url='https://cdn.nekos.life/Random_hentai_gif/Random_hentai_gifNB0139.gif')
            await client.send_message(message.channel, embed=embed)
        if choice == 2:
            embed = discord.Embed(title="punhetero - DEUS TA VENDO", description="", color=0xffffff)
            embed.set_image(url='https://cdn.nekos.life/Random_hentai_gif/Random_hentai_gifNB_1978.gif')
            await client.send_message(message.channel, embed=embed)
        if choice == 3:
            embed = discord.Embed(title="punhetero - DEUS TA VENDO", description="", color=0xffffff)
            embed.set_image(url='https://cdn.nekos.life/Random_hentai_gif/Random_hentai_gifNB_1319.gif')
            await client.send_message(message.channel, embed=embed)
        if choice == 4:
            embed = discord.Embed(title="punhetero - DEUS TA VENDO", description="", color=0xffffff)
            embed.set_image(url='https://cdn.nekos.life/Random_hentai_gif/Random_hentai_gifNB_0642.gif')
            await client.send_message(message.channel, embed=embed)
        if choice == 5:
            embed = discord.Embed(title="punhetero - DEUS TA VENDO", description="", color=0xffffff)
            embed.set_image(url='https://cdn.nekos.life/Random_hentai_gif/Random_hentai_gifNB0853.gif')
            await client.send_message(message.channel, embed=embed)
        if choice == 6:
            embed = discord.Embed(title="punhetero - DEUS TA VENDO", description="", color=0xffffff)
            embed.set_image(url='https://cdn.nekos.life/Random_hentai_gif/Random_hentai_gifNB_1422.gif')
            await client.send_message(message.channel, embed=embed)
        if choice == 7:
            embed = discord.Embed(title="punhetero - DEUS TA VENDO", description="", color=0xffffff)
            embed.set_image(url='https://cdn.nekos.life/Random_hentai_gif/Random_hentai_gifNB_1987.gif')
            await client.send_message(message.channel, embed=embed)
        if choice == 8:
            embed = discord.Embed(title="punhetero - DEUS TA VENDO", description="", color=0xffffff)
            embed.set_image(url='https://cdn.nekos.life/Random_hentai_gif/Random_hentai_gifNB_1001.gif')
            await client.send_message(message.channel, embed=embed)
        if choice == 9:
            embed = discord.Embed(title="punhetero - DEUS TA VENDO", description="", color=0xffffff)
            embed.set_image(url='https://cdn.nekos.life/Random_hentai_gif/Random_hentai_gifNB_1030.gif')
            await client.send_message(message.channel, embed=embed)
        if choice == 10:
            embed = discord.Embed(title="punhetero - DEUS TA VENDO", description="", color=0xffffff)
            embed.set_image(url='https://cdn.nekos.life/Random_hentai_gif/Random_hentai_gifNB0456.gif')
            await client.send_message(message.channel, embed=embed)

    if message.content.lower().startswith('.meupinto'):
        pinto = 'O seu pinto é desse tamanho !\n```8=D```'
        pinto1 = 'O seu pinto é desse tamanho !\n```8==D```'
        pinto2 = 'O seu pinto é desse tamanho !\n```8=====D```'
        pinto3 = 'O seu pinto é desse tamanho !\n```8=========D```'
        pinto4 = 'O seu pinto é desse tamanho !\n```8==================D```'
        pinto5 = 'Você nem tem pinto'
        pinto6 = 'ENORMOÇAURO\n```8================================================================D```'
        pinto7 = 'Seu pintinho é piquininim\n``` é tão pequeno que nao aparece```'
        pinto8 = 'Seu pintinho é finim\n```8--D```'
        choice = random.randint (1, 8)
        if choice == 1:
            await client.send_message(message.channel, pinto1)
        if choice == 2:
            await client.send_message(message.channel, pinto2)
        if choice == 3:
            await client.send_message(message.channel, pinto3)
        if choice == 4:
            await client.send_message(message.channel, pinto4)
        if choice == 5:
            await client.send_message(message.channel, pinto)
        if choice == 6:
            await client.send_message(message.channel, pinto6)
        if choice == 7:
            await client.send_message(message.channel, pinto7)
        if choice == 8:
            await client.send_message(message.channel, pinto8)
        if choice == 9:
            await client.send_message(message.channel, pinto5)

    if message.content.lower().startswith('.porn analzin'):
        choice = random.randint (1, 10)
        if choice == 1:
            embed = discord.Embed(title="punhetero - DEUS TA VENDO", description="", color=0xffffff)
            embed.set_image(url='https://cdn.boob.bot/anal/BC11.jpg')
            await client.send_message(message.channel, embed=embed)
        if choice == 2:
            embed = discord.Embed(title="punhetero - DEUS TA VENDO", description="", color=0xffffff)
            embed.set_image(url='https://cdn.boob.bot/ass/5073.JPG')
            await client.send_message(message.channel, embed=embed)
        if choice == 3:
            embed = discord.Embed(title="punhetero - DEUS TA VENDO", description="", color=0xffffff)
            embed.set_image(url='https://cdn.boob.bot/ass/4E0C.JPG')
            await client.send_message(message.channel, embed=embed)
        if choice == 4:
            embed = discord.Embed(title="punhetero - DEUS TA VENDO", description="", color=0xffffff)
            embed.set_image(url='https://cdn.boob.bot/anal/14A87.jpg')
            await client.send_message(message.channel, embed=embed)
        if choice == 5:
            embed = discord.Embed(title="punhetero - DEUS TA VENDO", description="", color=0xffffff)
            embed.set_image(url='https://cdn.boob.bot/anal/869C.jpg')
            await client.send_message(message.channel, embed=embed)
        if choice == 6:
            embed = discord.Embed(title="punhetero - DEUS TA VENDO", description="", color=0xffffff)
            embed.set_image(url='https://cdn.boob.bot/ass/4C68.JPG')
            await client.send_message(message.channel, embed=embed)
        if choice == 7:
            embed = discord.Embed(title="punhetero - DEUS TA VENDO", description="", color=0xffffff)
            embed.set_image(url='https://cdn.boob.bot/ass/4C92.JPG')
            await client.send_message(message.channel, embed=embed)
        if choice == 8:
            embed = discord.Embed(title="punhetero - DEUS TA VENDO", description="", color=0xffffff)
            embed.set_image(url='https://cdn.boob.bot/ass/4FEC.JPG')
            await client.send_message(message.channel, embed=embed)
        if choice == 9:
            embed = discord.Embed(title="punhetero - DEUS TA VENDO", description="", color=0xffffff)
            embed.set_image(url='https://cdn.boob.bot/anal/DF57.jpg')
            await client.send_message(message.channel, embed=embed)
        if choice == 10:
            embed = discord.Embed(title="punhetero - DEUS TA VENDO", description="", color=0xffffff)
            embed.set_image(url='https://cdn.boob.bot/anal/F1CC.jpg')
            await client.send_message(message.channel, embed=embed)

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
        msg28 = 'Tenho um pau de 30cm :smiling_imp::smiling_imp:'
        msg29 = 'Ja peguuei muita mulher gostosa :speak_no_evil: :speak_no_evil: '
        msg30 = 'Ja perdi a conta do tanto de bundas que ja vi ...'
        msg31 = 'Tenho varios contatinhos :telephone_receiver: :telephone_receiver: '
        msg32 = 'Ja fui passei pela estrada de barro :poop: :poop:'
        msg33 = 'Sou o cafetão do pesqueiro pantanal 😂 😎'
        msg34 = 'Vejo hentai todo dia 😁 😁'
        msg35 = 'Gosto de fazer um ballcat 😈 😋'
        msg36 = 'Amo comer um Lorenzo 😊 😊'
        msg37 = 'Adoro uma Mirellezinha 😉 😉'
        msg38 = 'Prefiro animações de pornô 😋 😋'
        msg39 = 'Eu peso mais que o Matheus e o Léo junto 😂 😂'
        msg40 = 'Ja fui coelinha da playboy 😚 😂'
        msg41 = 'Amo engravidar um Lorenzo 😈 😈'
        choice = random.randint (1,41)
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
        if choice == 28:
            await client.send_message(message.channel, msg28)
        if choice == 29:
            await client.send_message(message.channel, msg29)
        if choice == 30:
            await client.send_message(message.channel, msg30)
        if choice == 31:
            await client.send_message(message.channel, msg31)
        if choice == 32:
            await client.send_message(message.channel, msg32)
        if choice == 33:
            await client.send_message(message.channel, msg33)
        if choice == 34:
            await client.send_message(message.channel, msg34)
        if choice == 35:
            await client.send_message(message.channel, msg35)
        if choice == 36:
            await client.send_message(message.channel, msg36)
        if choice == 37:
            await client.send_message(message.channel, msg37)
        if choice == 38:
            await client.send_message(message.channel, msg38)
        if choice == 39:
            await client.send_message(message.channel, msg39)
        if choice == 40:
            await client.send_message(message.channel, msg40)
        if choice == 41:
            await client.send_message(message.channel, msg41)

    if message.content.lower().startswith('.ajuda'):
        embed = discord.Embed(title="", description="", color=0xffffff)
        embed.set_author(name='Informações BOT MelByLaw', icon_url='https://cdn.discordapp.com/attachments/475391478227664896/475727223194910720/img.png')
        embed.add_field(name='Comandos', value='.meusegredo\n.status\n.info\n.ping\n')
        embed.add_field(name='NSFW', value='.pornhelp\n.porn hentai\n.porn analzin', inline=True)
        embed.add_field(name='Diversão', value='.user (@membro)\n.ship (@membro) (@membro)\n.moeda\n.meupinto', inline=True)
        embed.add_field(name='Sorteio', value='.sorteio1a2\n.sorteio1a3\n.sorteio1a4\n', inline=True)
        embed.add_field(name='Inuteis', value='.totinha\n.bomba\n.bomdia\n', inline=True)
        await client.send_message(message.channel, embed=embed)

client.run('MzkyODE4MjgyMTQ0NTk1OTc4.DkeUQQ.NGoqk9tzBfh0FPKzx37WwC87Fr8')
